// VantTS — movimiento del sitio (propuesta del 22 oct 2026, aprobada y publicada ese día).
// Complementa motion.css. Cada bloque revisa su clase m-* en <html> y respeta "reducir movimiento".
(function () {
  const raiz = document.documentElement;
  const quieto = () => window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const activo = (c) => raiz.classList.contains(c) && !quieto();

  // M5 · Índice de cascada: cada tarjeta sabe su lugar dentro de su grupo (--i).
  document.querySelectorAll(".revelar").forEach((el) => {
    const hermanos = Array.from(el.parentElement.children).filter((h) => h.classList.contains("revelar"));
    el.style.setProperty("--i", String(Math.min(hermanos.indexOf(el), 5)));
  });

  // M6 · Línea cobre de los títulos y destello al llegar desde el menú.
  const encabezados = document.querySelectorAll(".encabezado, .encabezado-izq");
  if ("IntersectionObserver" in window) {
    const obs = new IntersectionObserver((ents) => {
      ents.forEach((en) => { if (en.isIntersecting) { en.target.classList.add("titulo-visto"); obs.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -15% 0px" });
    encabezados.forEach((e) => obs.observe(e));
  }
  document.querySelectorAll('a[href^="#"]').forEach((a) => a.addEventListener("click", () => {
    if (!activo("m-titulos")) return;
    const sec = document.querySelector(a.getAttribute("href"));
    const enc = sec && sec.querySelector(".encabezado");
    if (!enc) return;
    setTimeout(() => { enc.classList.remove("titulo-destello"); void enc.offsetWidth; enc.classList.add("titulo-destello"); }, 450);
  }));

  // M7 · Indicador que se desliza entre pestañas + cambio de captura con View Transitions.
  const tabsCaja = document.querySelector(".tabs");
  if (tabsCaja) {
    const tabs = Array.from(tabsCaja.querySelectorAll('[role="tab"]'));
    const ind = document.createElement("span");
    ind.className = "tabs-indicador"; ind.setAttribute("aria-hidden", "true");
    tabsCaja.prepend(ind);
    function unaFila() { return tabs.every((t) => t.offsetTop === tabs[0].offsetTop); }
    function mover() {
      const usar = raiz.classList.contains("m-pestanas") && unaFila();
      tabsCaja.classList.toggle("con-indicador", usar);
      ind.style.display = usar ? "" : "none";
      const sel = tabs.find((t) => t.getAttribute("aria-selected") === "true");
      if (!usar || !sel) return;
      ind.style.width = sel.offsetWidth + "px";
      ind.style.height = sel.offsetHeight + "px";
      ind.style.transform = `translate(${sel.offsetLeft}px, ${sel.offsetTop}px)`;
    }
    // El script del sitio ya cambia de pestaña al hacer clic; aquí envolvemos ese cambio
    // en una View Transition (si el navegador la tiene) y movemos el indicador.
    tabs.forEach((t) => t.addEventListener("click", (e) => {
      if (!activo("m-pestanas") || !document.startViewTransition || t.getAttribute("aria-selected") === "true") { requestAnimationFrame(mover); return; }
      if (t.dataset.mVt === "1") { t.dataset.mVt = ""; requestAnimationFrame(mover); return; }
      e.stopImmediatePropagation();
      document.startViewTransition(() => { t.dataset.mVt = "1"; t.click(); });
      requestAnimationFrame(mover);
    }, true));
    tabsCaja.addEventListener("keydown", () => requestAnimationFrame(mover));
    window.addEventListener("resize", mover);
    raiz.addEventListener("m-cambio", mover);
    mover();
  }

  // M8 · Luz que sigue al cursor en tarjetas.
  document.querySelectorAll(".dolor, .plan").forEach((c) => c.addEventListener("pointermove", (e) => {
    if (!activo("m-tarjetas")) return;
    const r = c.getBoundingClientRect();
    c.style.setProperty("--mx", (e.clientX - r.left) + "px");
    c.style.setProperty("--my", (e.clientY - r.top) + "px");
  }));

  // M11 · WhatsApp: aparece al pasar el inicio y saluda una sola vez por visita.
  const wa = document.querySelector(".wa-flotante");
  const hero = document.getElementById("inicio");
  if (wa && hero) {
    let saludo = false;
    function revisar() {
      if (!activo("m-whatsapp")) { wa.classList.remove("wa-oculto"); return; }
      const paso = hero.getBoundingClientRect().bottom < window.innerHeight * 0.4;
      wa.classList.toggle("wa-oculto", !paso);
      if (paso && !saludo) {
        saludo = true;
        setTimeout(() => {
          wa.classList.add("wa-saluda");
          const g = document.createElement("span");
          g.className = "wa-globo"; g.textContent = "¿Dudas? Escríbenos"; g.setAttribute("aria-hidden", "true");
          wa.parentElement.style.position = "fixed";
          wa.parentElement.appendChild(g);
          setTimeout(() => { g.remove(); wa.classList.remove("wa-saluda"); }, 4300);
        }, 600);
      }
    }
    window.addEventListener("scroll", revisar, { passive: true });
    raiz.addEventListener("m-cambio", revisar);
    revisar();
  }
})();
