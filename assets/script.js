// VantTS — menú lateral desplegable por proximidad al borde izquierdo.
// Se activa al pasar el cursor cerca del lateral izquierdo, o al tocar/hacer
// clic en la pestaña verde (para pantallas táctiles). No oculta el contenido:
// es un panel angosto que se superpone, no un overlay de pantalla completa.
(function () {
  const hoverZone = document.querySelector(".hover-zone");
  const sidebar = document.querySelector(".sidebar");
  const handle = document.querySelector(".sidebar-handle");
  if (!hoverZone || !sidebar || !handle) return;

  let closeTimer = null;
  let abiertoEn = 0;

  function open() {
    clearTimeout(closeTimer);
    if (!sidebar.classList.contains("open")) abiertoEn = Date.now();
    sidebar.classList.add("open");
    handle.classList.add("active");
  }

  function scheduleClose() {
    clearTimeout(closeTimer);
    closeTimer = setTimeout(() => {
      sidebar.classList.remove("open");
      handle.classList.remove("active");
    }, 260);
  }

  [hoverZone, sidebar, handle].forEach((el) => {
    el.addEventListener("mouseenter", open);
    el.addEventListener("mouseleave", scheduleClose);
  });

  // Clic/toque en la pestaña: alterna el menú (para dispositivos sin hover).
  handle.addEventListener("click", (e) => {
    e.preventDefault();
    // Si el menú se acaba de abrir al pasar el cursor, el clic no lo vuelve a cerrar
    if (sidebar.classList.contains("open") && Date.now() - abiertoEn > 400) {
      sidebar.classList.remove("open");
      handle.classList.remove("active");
    } else {
      open();
    }
  });

  // Cerrar si se toca fuera del menú en pantallas táctiles.
  document.addEventListener("click", (e) => {
    if (
      sidebar.classList.contains("open") &&
      !sidebar.contains(e.target) &&
      !handle.contains(e.target)
    ) {
      sidebar.classList.remove("open");
      handle.classList.remove("active");
    }
  });
})();

// Botón "Subir ↑": aparece al bajar en la página y regresa suavemente al inicio.
(function () {
  const subir = document.getElementById("subir");
  if (!subir) return;
  function revisar() {
    subir.classList.toggle("visible", window.scrollY > 400);
  }
  window.addEventListener("scroll", revisar, { passive: true });
  revisar();
  subir.addEventListener("click", (e) => {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
})();

// Página única: los enlaces del menú llevan a su sección, cierran el menú y
// el enlace de la sección visible queda resaltado mientras haces scroll.
(function () {
  const sidebar = document.querySelector(".sidebar");
  const handle = document.querySelector(".sidebar-handle");
  const links = Array.from(document.querySelectorAll(".sidebar nav a[data-seccion]"));
  if (!links.length) return;

  links.forEach((a) => a.addEventListener("click", () => {
    if (sidebar) sidebar.classList.remove("open");
    if (handle) handle.classList.remove("active");
  }));

  function marcar(id) {
    links.forEach((a) => a.classList.toggle("activa", a.dataset.seccion === id));
  }

  const secciones = links.map((a) => document.getElementById(a.dataset.seccion)).filter(Boolean);
  function actualizar() {
    const linea = window.innerHeight * 0.35;
    let actual = secciones[0];
    secciones.forEach((s) => { if (s.getBoundingClientRect().top <= linea) actual = s; });
    // Al llegar al final de la página, la última sección queda marcada
    if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) {
      actual = secciones[secciones.length - 1];
    }
    if (actual) marcar(actual.id);
  }
  window.addEventListener("scroll", actualizar, { passive: true });
  window.addEventListener("resize", actualizar);
  actualizar();
})();
