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

  function open() {
    clearTimeout(closeTimer);
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
    if (sidebar.classList.contains("open")) {
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
