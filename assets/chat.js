// VantTS — asistente de preguntas guiadas (20 nov 2026).
// Contesta solo con textos del sitio; no usa IA, no guarda nada y no usa cookies.
// Sin JavaScript, el botón flotante sigue abriendo WhatsApp.
(function () {
  var lanzador = document.getElementById("chatLanzador");
  var panel = document.getElementById("chat");
  var datosEl = document.getElementById("chat-datos");
  if (!lanzador || !panel || !datosEl) return;
  var datos;
  try { datos = JSON.parse(datosEl.textContent); } catch (e) { return; }

  var log = document.getElementById("chatLog");
  var opciones = document.getElementById("chatOpciones");
  var cerrar = document.getElementById("chatCerrar");
  var calma = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var ICO_WA = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"/></svg>';
  var iniciado = false;

  lanzador.setAttribute("role", "button");
  lanzador.setAttribute("aria-expanded", "false");
  lanzador.setAttribute("aria-controls", "chat");
  lanzador.removeAttribute("target");

  function burbuja(texto, quien) {
    var b = document.createElement("div");
    b.className = "chat-msg chat-" + quien;
    [].concat(texto).forEach(function (t) {
      var p = document.createElement("p");
      p.textContent = t;
      b.appendChild(p);
    });
    log.appendChild(b);
    // La respuesta se ve desde su primera línea; lo que eliges, al fondo.
    log.scrollTop = quien === "bot" ? Math.max(0, b.offsetTop - 12) : log.scrollHeight;
    return b;
  }

  function mostrar(id) {
    var nodo = datos.nodos[id];
    if (!nodo) return;
    opciones.textContent = "";
    var escribe = document.createElement("div");
    escribe.className = "chat-msg chat-bot chat-escribe";
    escribe.setAttribute("aria-hidden", "true");
    escribe.innerHTML = "<span></span><span></span><span></span>";
    if (!calma) log.appendChild(escribe);
    log.scrollTop = log.scrollHeight;
    setTimeout(function () {
      if (escribe.parentNode) escribe.parentNode.removeChild(escribe);
      var b = burbuja(nodo.texto, "bot");
      pintarOpciones(nodo.opciones || []);
      log.scrollTop = Math.max(0, b.offsetTop - 12);
    }, calma ? 0 : 450);
  }

  function pintarOpciones(lista) {
    lista.forEach(function (o) {
      var el;
      if (o.wa || o.href) {
        el = document.createElement("a");
        el.href = o.wa || o.href;
        if (o.wa) { el.target = "_blank"; el.rel = "noopener"; el.className = "chat-op chat-op-wa"; el.innerHTML = ICO_WA; }
        else { el.className = "chat-op chat-op-ir"; el.addEventListener("click", function () { if (o.href.charAt(0) === "#") abrir(false); }); }
        var s = document.createElement("span"); s.textContent = o.t; el.appendChild(s);
      } else {
        el = document.createElement("button");
        el.type = "button";
        el.className = "chat-op";
        el.textContent = o.t;
        el.addEventListener("click", function () {
          burbuja(o.t, "yo");
          mostrar(o.ir);
        });
      }
      opciones.appendChild(el);
    });
    var primero = opciones.querySelector(".chat-op");
    if (primero && panel.contains(document.activeElement)) primero.focus({ preventScroll: true });
  }

  function abrir(si) {
    panel.hidden = !si;
    lanzador.setAttribute("aria-expanded", si ? "true" : "false");
    lanzador.setAttribute("aria-label", si ? "Cerrar el asistente de VantTS" : "Abrir el asistente de VantTS");
    document.documentElement.classList.toggle("chat-abierto", si);
    if (si) {
      if (!iniciado) { iniciado = true; mostrar(datos.inicio); }
      setTimeout(function () { (opciones.querySelector(".chat-op") || cerrar).focus({ preventScroll: true }); }, calma ? 0 : 480);
    } else {
      lanzador.focus({ preventScroll: true });
    }
  }

  lanzador.addEventListener("click", function (e) { e.preventDefault(); abrir(panel.hidden); });
  cerrar.addEventListener("click", function () { abrir(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !panel.hidden) abrir(false); });
})();
