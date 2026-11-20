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
