// VantTS — inicio v5: selector "¿Qué te quita tiempo hoy?".
// Sin JavaScript se ve el primer ejemplo; con él, cada opción muestra su plano.
(function () {
  var lista = document.querySelector(".necs");
  if (!lista) return;
  var tabs = Array.prototype.slice.call(lista.querySelectorAll('[role="tab"]'));
  function elegir(tab, foco) {
    tabs.forEach(function (t) {
      var activo = t === tab;
      t.setAttribute("aria-selected", activo ? "true" : "false");
      t.tabIndex = activo ? 0 : -1;
      var p = document.getElementById(t.getAttribute("aria-controls"));
      if (!p) return;
      p.hidden = !activo;
      p.classList.remove("plano-entra");
      if (activo) { void p.offsetWidth; p.classList.add("plano-entra"); }
    });
    if (foco) tab.focus();
    if (tab.scrollIntoView && lista.scrollWidth > lista.clientWidth) tab.scrollIntoView({ block: "nearest", inline: "center", behavior: "smooth" });
  }
  tabs.forEach(function (t, i) {
    t.addEventListener("click", function () { elegir(t, false); });
    t.addEventListener("keydown", function (e) {
      var d = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[e.key];
      if (e.key === "Home") { e.preventDefault(); elegir(tabs[0], true); }
      else if (e.key === "End") { e.preventDefault(); elegir(tabs[tabs.length - 1], true); }
      else if (d) { e.preventDefault(); elegir(tabs[(i + d + tabs.length) % tabs.length], true); }
    });
  });
})();

// Videos: el grande carga el reproductor de YouTube solo cuando lo tocan;
// los cinco chicos se eligen al azar en cada visita, de los videos públicos más recientes del canal.
(function () {
  var marco = document.querySelector(".video-marco");
  if (marco) {
    marco.addEventListener("click", function () {
      var id = marco.getAttribute("data-video");
      var caja = document.createElement("div");
      caja.className = "video-marco";
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
      f.title = "Video de VantTS";
      f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
      f.allowFullscreen = true;
      caja.appendChild(f);
      marco.parentNode.replaceChild(caja, marco);
    });
  }

  var cont = document.getElementById("cortos");
  if (!cont) return;
  var principal = cont.getAttribute("data-principal");
  var ID_OK = /^[\w-]{11}$/;

  function pintar(lista) {
    var buenos = lista.filter(function (v) { return v && ID_OK.test(v.id) && v.id !== principal; });
    if (buenos.length < 5) return false;
    for (var i = buenos.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1)), t = buenos[i]; buenos[i] = buenos[j]; buenos[j] = t;
    }
    var frag = document.createDocumentFragment();
    buenos.slice(0, 5).forEach(function (v) {
      var a = document.createElement("a");
      a.className = "corto"; a.target = "_blank"; a.rel = "noopener";
      a.href = "https://www.youtube.com/" + (v.corto === false ? "watch?v=" : "shorts/") + v.id;
      var caja = document.createElement("span"); caja.className = "corto-img";
      var img = document.createElement("img");
      img.alt = ""; img.loading = "lazy"; img.width = 270; img.height = 480;
      img.onerror = function () { img.onerror = null; img.src = "https://i.ytimg.com/vi/" + v.id + "/hqdefault.jpg"; };
      img.src = "https://i.ytimg.com/vi/" + v.id + (v.corto === false ? "/hqdefault.jpg" : "/oar2.jpg");
      caja.appendChild(img);
      caja.insertAdjacentHTML("beforeend", '<svg class="ico-play" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>');
      var tit = document.createElement("span"); tit.className = "corto-titulo"; tit.textContent = String(v.titulo || "");
      a.appendChild(caja); a.appendChild(tit); frag.appendChild(a);
    });
    cont.textContent = ""; cont.appendChild(frag);
    return true;
  }

  function respaldo() {
    try { pintar(JSON.parse(document.getElementById("videos-respaldo").textContent)); } catch (e) {}
  }

  if (!window.fetch || location.protocol === "file:") { respaldo(); return; }
  fetch("/api/videos").then(function (r) { if (!r.ok) throw 0; return r.json(); })
    .then(function (lista) { if (!Array.isArray(lista) || !pintar(lista)) respaldo(); })
    .catch(respaldo);
})();
