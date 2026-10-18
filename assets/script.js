// VantTS — sitio de una sola página (v3, 18 oct 2026)
document.documentElement.classList.add("js");

// Menú superior: botón de menú en celular, borde al bajar y sección activa.
(function () {
  const nav = document.getElementById("nav");
  const boton = document.getElementById("navBoton");
  const links = document.getElementById("navLinks");
  if (!nav || !boton || !links) return;

  function cerrar() {
    links.classList.remove("abierto");
    boton.setAttribute("aria-expanded", "false");
    boton.setAttribute("aria-label", "Abrir menú");
  }
  boton.addEventListener("click", () => {
    const abierto = links.classList.toggle("abierto");
    boton.setAttribute("aria-expanded", String(abierto));
    boton.setAttribute("aria-label", abierto ? "Cerrar menú" : "Abrir menú");
  });
  links.querySelectorAll("a").forEach((a) => a.addEventListener("click", cerrar));
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") cerrar(); });
  document.addEventListener("click", (e) => { if (!nav.contains(e.target)) cerrar(); });

  const enlaces = Array.from(links.querySelectorAll("a[data-seccion]"));
  const secciones = enlaces.map((a) => document.getElementById(a.dataset.seccion)).filter(Boolean);
  function actualizar() {
    nav.classList.toggle("con-borde", window.scrollY > 8);
    const linea = window.innerHeight * 0.35;
    let actual = null;
    secciones.forEach((s) => { if (s.getBoundingClientRect().top <= linea) actual = s; });
    if (secciones.length && secciones[secciones.length - 1].getBoundingClientRect().bottom < linea) actual = null;
    enlaces.forEach((a) => a.classList.toggle("activa", !!actual && a.dataset.seccion === actual.id));
  }
  window.addEventListener("scroll", actualizar, { passive: true });
  window.addEventListener("resize", actualizar);
  actualizar();
})();

// Pestañas de "Cómo funciona" (con flechas del teclado).
(function () {
  const tabs = Array.from(document.querySelectorAll('.tabs [role="tab"]'));
  if (!tabs.length) return;
  function elegir(tab, foco) {
    tabs.forEach((t) => {
      const sel = t === tab;
      t.setAttribute("aria-selected", String(sel));
      t.tabIndex = sel ? 0 : -1;
      const panel = document.getElementById(t.getAttribute("aria-controls"));
      if (!panel) return;
      panel.hidden = !sel;
      if (sel) { panel.classList.remove("entra"); void panel.offsetWidth; panel.classList.add("entra"); }
    });
    if (foco) tab.focus();
    tab.scrollIntoView({ block: "nearest", inline: "center", behavior: "smooth" });
  }
  tabs.forEach((t, i) => {
    t.addEventListener("click", () => elegir(t, false));
    t.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight") { e.preventDefault(); elegir(tabs[(i + 1) % tabs.length], true); }
      if (e.key === "ArrowLeft") { e.preventDefault(); elegir(tabs[(i - 1 + tabs.length) % tabs.length], true); }
    });
  });
})();

// Aparición suave de tarjetas al bajar (se respeta "reducir movimiento").
(function () {
  const items = document.querySelectorAll(".revelar");
  if (!("IntersectionObserver" in window)) { items.forEach((el) => el.classList.add("visto")); return; }
  const obs = new IntersectionObserver((entradas) => {
    entradas.forEach((en) => { if (en.isIntersecting) { en.target.classList.add("visto"); obs.unobserve(en.target); } });
  }, { rootMargin: "0px 0px -8% 0px" });
  items.forEach((el) => obs.observe(el));
})();

// Botón "Subir": aparece al bajar y regresa al inicio.
(function () {
  const subir = document.getElementById("subir");
  if (!subir) return;
  function revisar() { subir.classList.toggle("visible", window.scrollY > 700); }
  window.addEventListener("scroll", revisar, { passive: true });
  revisar();
  subir.addEventListener("click", (e) => { e.preventDefault(); window.scrollTo({ top: 0, behavior: "smooth" }); });
})();
