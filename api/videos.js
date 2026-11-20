// VantTS — /api/videos: los videos públicos más recientes del canal de YouTube (los últimos 15),
// tomados de la lista automática que YouTube publica por canal. No usa llaves ni guarda datos.
// La respuesta se guarda una hora en Vercel para no consultar a YouTube en cada visita.
const CANAL = "UCMQf89_Ih4nU-i2mO9xJKnw";

function limpio(t) {
  return t.replace(/&amp;/g, "&").replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&lt;/g, "<").replace(/&gt;/g, ">")
    .replace(/\s*#\S+/g, "").trim();
}

module.exports = async (req, res) => {
  try {
    const r = await fetch("https://www.youtube.com/feeds/videos.xml?channel_id=" + CANAL);
    if (!r.ok) throw new Error("YouTube respondió " + r.status);
    const xml = await r.text();
    const videos = xml.split("<entry>").slice(1).map((e) => {
      const id = (e.match(/<yt:videoId>([\w-]{11})</) || [])[1];
      const titulo = (e.match(/<title>([^<]*)</) || [])[1] || "";
      const enlace = (e.match(/<link[^>]+href="([^"]+)"/) || [])[1] || "";
      return id ? { id: id, titulo: limpio(titulo), corto: enlace.indexOf("/shorts/") !== -1 } : null;
    }).filter(Boolean);
    if (!videos.length) throw new Error("Lista vacía");
    res.setHeader("Cache-Control", "public, s-maxage=3600, stale-while-revalidate=86400");
    res.status(200).json(videos);
  } catch (err) {
    res.setHeader("Cache-Control", "no-store");
    res.status(502).json({ error: "No se pudo leer la lista de videos" });
  }
};
