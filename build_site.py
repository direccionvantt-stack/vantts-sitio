#!/usr/bin/env python3
"""
Genera el sitio de VantTS (v4, 1 nov 2026): dos páginas con el mismo diseño.

- index.html           Inicio de VantTS como empresa: software a la medida (sistemas,
                       apps, automatización con IA y sitios web), cómo trabajamos, cómo
                       cobramos (cotización + renta mensual), productos y contacto.
- barber/index.html    Todo lo de VantTS Barber (antes era la página única v3): qué
                       resuelve, cómo funciona, IA, caso Rocker Barber, precios y preguntas.

Decisiones de Luis (1 nov 2026): inicio de empresa + página de Barber; anunciar
sistemas, apps, IA y sitios web; precio de lo hecho a la medida por cotización + renta
mensual; productos que vienen como "Próximamente".

Reglas: solo se dice lo que ya funciona en VantTS Barber (VTS-COM-06); las capturas son
de la cuenta de demostración (datos inventados). Las direcciones anteriores
(solucion.html, precios.html, ...) y los enlaces viejos como /#precios llevan a su sección.
"""
import os
import datetime

OUT_DIR = os.environ.get("VANTTS_SITE_OUT", os.path.dirname(os.path.abspath(__file__)))
ANIO = datetime.date.today().year

WHATSAPP = "https://wa.me/523312506541?text=Hola%2C%20vi%20la%20p%C3%A1gina%20de%20VantTS%20y%20quiero%20saber%20m%C3%A1s"
WA_COTIZAR = "https://wa.me/523312506541?text=Hola%2C%20vi%20la%20p%C3%A1gina%20de%20VantTS%20y%20quiero%20cotizar%20un%20proyecto"
WA_BARBER = "https://wa.me/523312506541?text=Hola%2C%20vi%20la%20p%C3%A1gina%20de%20VantTS%20Barber%20y%20quiero%20saber%20m%C3%A1s"
INSTAGRAM = "https://www.instagram.com/vantts.mx/"
FACEBOOK = "https://www.facebook.com/profile.php?id=61595384815178"
YOUTUBE = "https://www.youtube.com/@vantts_mx"

# Secciones de VantTS Barber que antes vivían en el inicio: los enlaces viejos
# (vantts.com.mx/#precios) se mandan a barber/#precios.
SECCIONES_BARBER = ["solucion", "funciones", "ia", "precios"]
# Páginas anteriores: se conservan como redirección a su sección
PAGINAS_ANTERIORES = {
    "solucion": "/barber/#solucion",
    "precios": "/barber/#precios",
    "casos": "/#casos",
    "nosotros": "/#nosotros",
    "contacto": "/#contacto",
}


def ico(path, cls="ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{path}</svg>'


# Íconos de línea (mismo trazo en todo el sitio)
I_WA = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"/><path d="M9.2 8.6c.2-.5.5-.5.8-.5h.5c.2 0 .4 0 .5.4l.7 1.6c.1.2 0 .4-.1.6l-.5.6c-.1.1-.2.3 0 .5.6 1 1.4 1.8 2.5 2.4.2.1.4.1.5 0l.6-.7c.2-.2.4-.2.6-.1l1.6.8c.2.1.3.2.3.4 0 .9-.6 1.6-1.6 1.7-1 .1-2.6-.3-4.3-1.9S9 11.1 9 10.1c0-.6.1-1.1.2-1.5z"/></svg>'
I_FLECHA = ico('<path d="M5 12h14M13 6l6 6-6 6"/>')
I_CHECK = ico('<path d="M5 12.5l4.2 4.2L19 7"/>')
I_PORCIENTO = ico('<path d="M19 5L5 19"/><circle cx="7" cy="7" r="2.5"/><circle cx="17" cy="17" r="2.5"/>')
I_CALENDARIO = ico('<rect x="3.5" y="5" width="17" height="15" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>')
I_DESCARGA = ico('<path d="M12 4v11M7 10l5 5 5-5"/><path d="M5 20h14"/>')
I_TIENDA = ico('<path d="M4 9l1.5-5h13L20 9"/><path d="M4 9a2.7 2.7 0 0 0 5.3 0 2.7 2.7 0 0 0 5.4 0 2.7 2.7 0 0 0 5.3 0"/><path d="M5.5 11.5V20h13v-8.5"/><path d="M10 20v-5h4v5"/>')
I_CHAT = ico('<path d="M5 18.5V6.5A2.5 2.5 0 0 1 7.5 4h9A2.5 2.5 0 0 1 19 6.5v7a2.5 2.5 0 0 1-2.5 2.5H9z"/><path d="M8.5 9h7M8.5 12h4.5"/>')
I_DINERO = ico('<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5v9M9.3 9.6c0-1.1 1.1-2 2.7-2s2.7.7 2.7 1.8c0 2.4-5.4 1.1-5.4 3.4 0 1.1 1.2 1.8 2.7 1.8s2.7-.9 2.7-2"/>')
I_TIJERA = ico('<circle cx="6.5" cy="7" r="2.5"/><circle cx="6.5" cy="17" r="2.5"/><path d="M8.6 8.4L20 16M8.6 15.6L20 8"/>')
I_ESCUDO = ico('<path d="M12 3l7 3v6c0 4.4-3 7.7-7 9-4-1.3-7-4.6-7-9V6z"/><path d="M9 12l2 2 4-4"/>')
I_CHISPA = ico('<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M18.5 15.5l.8 2.2 2.2.8-2.2.8-.8 2.2-.8-2.2-2.2-.8 2.2-.8z"/>')
I_ARCHIVO = ico('<path d="M14 3.5H7.5a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2V8z"/><path d="M14 3.5V8h4.5M9 13h6M9 16.5h4"/>')
# Íconos del inicio de VantTS (1 nov 2026)
I_TABLERO = ico('<rect x="3.5" y="4.5" width="17" height="15" rx="2.5"/><path d="M3.5 9h17M9 9v10.5"/><path d="M12 13h5M12 16h3"/>')
I_CELULAR = ico('<rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M10.5 18.5h3"/>')
I_GLOBO = ico('<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.4 2.6 2.4 14.4 0 17M12 3.5c-2.4 2.6-2.4 14.4 0 17"/>')
I_FOCO = ico('<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.7.6 1.1 1.3 1.1 2.2h5c0-.9.4-1.6 1.1-2.2A6 6 0 0 0 12 3z"/>')
I_CODIGO = ico('<path d="M8.5 7L3.5 12l5 5M15.5 7l5 5-5 5M13.5 4.5l-3 15"/>')
I_HERRAMIENTA = ico('<path d="M14.5 5.5a4 4 0 0 0-5.2 5.2L4 16v4h4l5.3-5.3a4 4 0 0 0 5.2-5.2l-2.6 2.6-2.6-.6-.6-2.6z"/>')
I_HOJA = ico('<path d="M5 19c0-8 5-13.5 14.5-14.5C18.5 14 13 19 5 19z"/><path d="M5 19l7-7"/>')
I_HUELLA = ico('<circle cx="7" cy="10" r="1.8"/><circle cx="11" cy="6.5" r="1.8"/><circle cx="15.5" cy="7.5" r="1.8"/><circle cx="18" cy="11.5" r="1.8"/><path d="M8.5 17.5c0-2.6 2-5 4.5-5s4 2 4 4c0 1.8-1.4 3-3.2 3-1 0-1.6-.4-2.3-.4s-1.3.4-2 .4c-.6 0-1-.6-1-2z"/>')
I_TROFEO = ico('<path d="M8 4.5h8v5a4 4 0 0 1-8 0z"/><path d="M8 6.5H5a3 3 0 0 0 3 3.5M16 6.5h3a3 3 0 0 1-3 3.5M12 13.5v3.5M8.5 20h7M10 17h4v3h-4z"/>')

# Pie de página
ICO_TEL = ico('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>', "pie-ico")
ICO_MAIL = ico('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>', "pie-ico")
ICO_PIN = ico('<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>', "pie-ico")
ICO_GLOBO = ico('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 2.5 15.3 0 18M12 3c-2.5 2.7-2.5 15.3 0 18"/>', "pie-ico")
ICO_ESCUDO = ico('<path d="M12 3l7 3v6c0 4.4-3 7.7-7 9-4-1.3-7-4.6-7-9V6z"/><path d="M9 12l2 2 4-4"/>', "pie-ico")
ICO_IG = ico('<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="0.6"/>', "pie-ico")
ICO_FB = ico('<path d="M14 8.5h2.5V5H14a3.5 3.5 0 0 0-3.5 3.5V11H8v3.5h2.5V21H14v-6.5h2.5L17 11h-3V9a.5.5 0 0 1 .5-.5z"/>', "pie-ico")
ICO_YT = ico('<rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10 9.2v5.6l4.8-2.8z"/>', "pie-ico")


def btn_wa(texto="Escríbeme por WhatsApp", cls="btn", url=WHATSAPP):
    return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener">{I_WA}<span>{texto}</span></a>'


def telefono(src, alt, cls="telefono", carga="lazy", a=""):
    extra = ' fetchpriority="high"' if carga == "eager" else ""
    return f'<figure class="{cls}"><img src="{a}assets/img/{src}" alt="{alt}" loading="{carga}"{extra} decoding="async" width="600" height="1153"></figure>'


def slug(t):
    return t.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace(" ", "-")


# ===========================================================================
#  PÁGINA 1 · INICIO DE VANTTS (la empresa)
# ===========================================================================

NAV_VANTTS = [
    ("servicios", "Servicios"),
    ("proceso", "Cómo trabajamos"),
    ("productos", "Productos"),
    ("cobro", "Cómo cobramos"),
    ("preguntas", "Preguntas"),
    ("nosotros", "Nosotros"),
]


def v_inicio():
    return f"""
  <section class="hero" id="inicio" aria-label="Inicio">
    <div class="hero-fondo" aria-hidden="true"></div>
    <div class="contenedor hero-grid">
      <div class="hero-texto">
        <a class="pildora" href="#productos"><img src="assets/img/icono.png" alt="" width="22" height="22"><span>Software a la medida + IA · Guadalajara</span>{I_FLECHA}</a>
        <h1>La tecnología que tu negocio necesita, <span class="acento">hecha a tu medida.</span></h1>
        <p class="lead">Sistemas, apps, sitios web y automatizaciones con inteligencia artificial. Nos cuentas cómo trabajas, lo construimos contigo y lo mantenemos funcionando con una renta mensual.</p>
        <div class="cta-fila">
          {btn_wa("Cuéntanos tu idea", url=WA_COTIZAR)}
          <a class="btn btn-sec" href="#servicios"><span>Ver qué hacemos</span></a>
        </div>
        <p class="micro">{I_CHECK}Cotización sin costo <span class="punto">·</span> Trato directo <span class="punto">·</span> Hecho en Guadalajara</p>
      </div>
      <div class="hero-visual hero-visual-vantts" aria-label="Ejemplos de lo que construimos">
        <div class="ventana" aria-hidden="true">
          <div class="ventana-barra"><i></i><i></i><i></i><span></span></div>
          <div class="ventana-cuerpo">
            <div class="ventana-menu"><b></b><span></span><span></span><span></span><span></span></div>
            <div class="ventana-main">
              <div class="ventana-titulo"></div>
              <div class="ventana-kpis"><div><span></span><b></b></div><div><span></span><b></b></div><div><span></span><b></b></div></div>
              <div class="ventana-grafica"><i style="height:38%"></i><i style="height:56%"></i><i style="height:47%"></i><i style="height:72%"></i><i style="height:64%"></i><i style="height:88%"></i><i style="height:79%"></i></div>
            </div>
          </div>
        </div>
        {telefono("agenda.jpg", "Agenda de VantTS Barber, un sistema que construimos", "telefono telefono-frente", "eager")}
        <div class="chip chip-1">{I_CODIGO}<span>Sistemas, apps y sitios hechos para tu negocio</span></div>
        <div class="chip chip-2">{I_CHISPA}<span>IA que trabaja con los datos de tu negocio</span></div>
        <p class="demo-nota">Celular: VantTS Barber, cuenta de demostración · datos inventados</p>
      </div>
    </div>
  </section>

  <section class="confianza" aria-label="Por qué trabajar con nosotros">
    <div class="contenedor confianza-grid">
      <div class="conf">{I_HERRAMIENTA}<p><strong>A tu medida</strong><span>no una plantilla genérica</span></p></div>
      <div class="conf">{I_DINERO}<p><strong>Cotización sin costo</strong><span>sabes cuánto antes de empezar</span></p></div>
      <div class="conf">{I_CALENDARIO}<p><strong>Renta mensual</strong><span>con mantenimiento</span></p></div>
      <div class="conf">{I_TIENDA}<p><strong>Ya funciona</strong><span>en Rocker Barber, Guadalajara</span></p></div>
    </div>
  </section>
"""


def servicio(icono, titulo, texto, ejemplos):
    lis = "".join(f"<li>{I_CHECK}<span>{e}</span></li>" for e in ejemplos)
    return f"""
        <article class="dolor servicio revelar">
          <div class="dolor-ico">{icono}</div>
          <h3>{titulo}</h3>
          <p class="dolor-resp">{texto}</p>
          <ul class="servicio-ej">{lis}</ul>
        </article>"""


def v_servicios():
    return f"""
  <section class="seccion" id="servicios" aria-label="Servicios">
    <div class="contenedor">
      <div class="encabezado">
        <p class="eyebrow">Qué hacemos</p>
        <h2>Si tu negocio lo necesita, lo construimos</h2>
        <p class="lead">No vendemos un solo programa: hacemos la herramienta que tu negocio necesita, con tus procesos y tu forma de trabajar.</p>
      </div>
      <div class="dolores servicios">
{servicio(I_TABLERO, "Sistemas para tu negocio", "Software de gestión hecho con tus procesos, para que dejes el cuaderno y el Excel.", ["Citas, agenda y reservas", "Inventario, compras y proveedores", "Ventas, caja, clientes y reportes"])}
{servicio(I_CELULAR, "Apps web y móviles", "Aplicaciones para tus clientes o para tu equipo, que se usan desde el celular o la computadora.", ["Reservas o pedidos de tus clientes", "Una app interna para tu equipo", "Un portal para tus clientes"])}
{servicio(I_CHISPA, "Automatización con IA", "Lo que hoy se hace a mano, hecho solo; y una IA que responde con los datos de tu negocio.", ["Asistentes que conocen tu negocio", "Reportes y avisos automáticos", "Pasar tus datos de Excel a tu sistema"])}
{servicio(I_GLOBO, "Sitios web", "La página de tu negocio, que se ve bien en el celular y que mantenemos al día.", ["Página de tu negocio o tu marca", "Catálogo, menú o lista de servicios", "Botón para que te escriban por WhatsApp"])}
      </div>
      <div class="otra-idea revelar">
        <div class="otra-idea-ico">{I_FOCO}</div>
        <div>
          <h3>¿Tienes otra idea?</h3>
          <p>Si es tecnología, cuéntanosla. Te decimos con honestidad si podemos hacerla y cómo la haríamos.</p>
        </div>
        {btn_wa("Cuéntanos tu idea", "btn btn-sec", WA_COTIZAR)}
      </div>
    </div>
  </section>
"""


PASOS = [
    ("Nos cuentas", "Por WhatsApp o en persona: qué haces, qué te quita tiempo y qué quieres lograr."),
    ("Te cotizamos sin costo", "Te decimos qué construiríamos, en cuánto tiempo y cuánto cuesta, antes de empezar."),
    ("Lo construimos contigo", "Te enseñamos avances y lo ajustamos con lo que nos dices, como hicimos con los barberos de VantTS Barber."),
    ("Lo mantenemos cada mes", "Con la renta mensual lo mantenemos funcionando y te ayudamos cuando algo no te salga."),
]


def v_proceso():
    pasos = "".join(f"""
        <li class="paso revelar"><span class="paso-num">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p></li>""" for i, (t, d) in enumerate(PASOS))
    return f"""
  <section class="seccion seccion-alt" id="proceso" aria-label="Cómo trabajamos">
    <div class="contenedor">
      <div class="encabezado">
        <p class="eyebrow">Cómo trabajamos</p>
        <h2>De tu idea a algo que ya funciona</h2>
        <p class="lead">Cuatro pasos, sin tecnicismos. Hablas siempre con quien lo construye.</p>
      </div>
      <ol class="pasos">{pasos}
      </ol>
    </div>
  </section>
"""


def producto_chico(icono, nombre, texto, estado):
    return f"""
          <article class="producto producto-pronto revelar">
            <div class="producto-ico">{icono}</div>
            <div>
              <h3>{nombre} <span class="pd-pronto">Próximamente</span></h3>
              <p>{texto}</p>
              <p class="producto-estado">{estado}</p>
            </div>
          </article>"""


def v_productos():
    return f"""
  <section class="seccion" id="productos" aria-label="Productos">
    <div class="contenedor">
      <div class="encabezado">
        <p class="eyebrow">Productos</p>
        <h2>Soluciones listas para tu giro</h2>
        <p class="lead">Además de lo hecho a la medida, tenemos productos propios para giros específicos. Los construimos con negocios reales y solo ofrecemos lo que ya probamos.</p>
      </div>
      <div class="productos">
        <article class="producto producto-dest revelar">
          <div class="producto-dest-texto">
            <span class="producto-marca"><img src="assets/img/vantts-barber-icono.png" alt="" width="40" height="40">VantTS Barber <span class="giro-tag on">Disponible</span></span>
            <h3>Cuánto gana tu barbería, sin adivinar</h3>
            <p>Tu agenda, tus clientes y tus ventas en un solo lugar, para barberías y salones. Tus clientes reservan solos con tu link y tú ves cuánto ganas de verdad.</p>
            <ul class="lista-check">
              <li>{I_CHECK}<span>Plan Básico gratis; Pro $249 y Max $599 al mes, IVA incluido</span></li>
              <li>{I_CHECK}<span>Sin comisión por cita y mes a mes</span></li>
              <li>{I_CHECK}<span>Ya funciona en Rocker Barber, Guadalajara</span></li>
            </ul>
            <div class="cta-fila">
              <a class="btn" href="barber/"><span>Conoce VantTS Barber</span>{I_FLECHA}</a>
              <a class="btn btn-sec" href="barber/#precios"><span>Ver precios</span></a>
            </div>
          </div>
          <div class="producto-dest-visual">{telefono("clientes.jpg", "Clientes en VantTS Barber, con historial y a quién llamar")}</div>
        </article>
        <div class="productos-pronto">
{producto_chico(I_HOJA, "VantTS Salud y Bienestar", "Para masajes y bienestar: citas, clientes y una ficha de bienestar con el consentimiento de tu cliente.", "En desarrollo")}
{producto_chico(I_HUELLA, "VantTS Vet", "Para clínicas veterinarias: pacientes, hospitalización y reportes.", "En planeación")}
{producto_chico(I_TROFEO, "VantTS Life", "Tu agenda personal convertida en juego: tus pendientes son misiones que te dan niveles y recompensas.", "Para personas, no solo negocios")}
        </div>
      </div>
    </div>
  </section>
"""


def v_cobro():
    return f"""
  <section class="seccion seccion-oscura" id="cobro" aria-label="Cómo cobramos">
    <div class="contenedor ia-grid">
      <div class="ia-texto">
        <p class="eyebrow eyebrow-claro">{I_DINERO}Cómo cobramos</p>
        <h2>Una cotización clara y una renta mensual</h2>
        <p class="lead">Cada negocio necesita algo distinto, por eso lo hecho a la medida no tiene un precio fijo: primero entendemos lo que necesitas y después te decimos cuánto cuesta.</p>
        <div class="cta-fila">{btn_wa("Pide tu cotización", "btn btn-claro", WA_COTIZAR)}</div>
        <p class="cobro-nota">¿Tienes barbería o salón? <a href="barber/#precios">VantTS Barber</a> ya tiene precio fijo y un plan gratis.</p>
      </div>
      <div class="cobro-pasos">
        <div class="cobro-paso"><span class="cobro-num">1</span><div><h3>El desarrollo</h3><p>Te lo cotizamos sin costo, según lo que de verdad necesitas.</p></div></div>
        <div class="cobro-paso"><span class="cobro-num">2</span><div><h3>La renta mensual</h3><p>Incluye el mantenimiento, para que tu sistema siga funcionando.</p></div></div>
      </div>
    </div>
  </section>
"""


# Cifras reales de Rocker Barber en VantTS Barber (consulta a la base del
# 4 nov 2026; Zeku aceptó publicarlas). Al actualizarlas, cambiar también
# el periodo.
CASO_CIFRAS = [("91", "citas atendidas"), ("101", "clientes registrados"), ("95", "ventas registradas")]
CASO_PERIODO = "del 15 de septiembre al 4 de noviembre de 2026"
CASO_NOTA = f"Cifras reales de Rocker Barber en VantTS Barber, {CASO_PERIODO}, con 15 días cerrados con su corte de caja."

# Testimonio de Zeku (VTS-COM-09): solo sus palabras, con su autorización
# guardada y la versión final aprobada por él. Mientras sea None no se
# muestra nada. Formato: ("frase", "Zeku, Rocker Barber").
TESTIMONIO = None


def caso_datos_html():
    return "\n".join(f'          <div class="dato"><strong>{n}</strong><span>{t}</span></div>' for n, t in CASO_CIFRAS)


def testimonio_html():
    if not TESTIMONIO:
        return ""
    frase, autor = TESTIMONIO
    return f'          <blockquote class="testimonio"><p>“{frase}”</p><cite>{autor}</cite></blockquote>'


def v_casos():
    return f"""
  <section class="seccion" id="casos" aria-label="Casos">
    <div class="contenedor">
      <div class="caso revelar">
        <div class="caso-texto">
          <p class="eyebrow">Caso real</p>
          <h2>Lo que ya construimos: Rocker Barber</h2>
          <p class="lead">Una barbería de Guadalajara con más de dos años operando lleva su agenda, sus clientes y sus ventas en VantTS Barber, el sistema que construimos con ellos.</p>
{testimonio_html()}
          <p class="caso-nota">{CASO_NOTA}</p>
          <div class="cta-fila"><a class="btn btn-sec" href="barber/"><span>Ver VantTS Barber</span>{I_FLECHA}</a></div>
        </div>
        <div class="caso-datos">
{caso_datos_html()}
        </div>
      </div>
    </div>
  </section>
"""


FAQ_VANTTS = [
    ("¿Qué tipo de proyectos hacen?", "Sistemas de gestión, apps web y móviles, automatizaciones con inteligencia artificial y sitios web. Si tienes otra idea, cuéntanos y te decimos con honestidad si podemos hacerla."),
    ("¿Cuánto cuesta?", "Depende de lo que necesites. Te cotizamos sin costo el desarrollo y una renta mensual que incluye el mantenimiento. Sabes cuánto es antes de empezar."),
    ("¿Cuánto tiempo tarda?", "Depende del tamaño del proyecto. Te lo decimos en la cotización, junto con el precio."),
    ("¿Necesito saber de computación?", "No. Tú nos explicas cómo trabajas y nosotros nos encargamos de la parte técnica. Lo hacemos simple, para que lo use cualquiera en tu negocio."),
    ("¿Usan inteligencia artificial?", "Sí: nos ayuda a construir y, cuando de verdad sirve, va dentro de lo que hacemos. Por ejemplo, el panel de IA de VantTS Barber le contesta al dueño con los números de su propio negocio."),
    ("Tengo una barbería o un salón, ¿qué me conviene?", "VantTS Barber: ya está listo, tiene un plan gratis y precios fijos. Si necesitas algo que no tiene, lo platicamos."),
]


def faq_html(lista):
    return "\n".join(f"""        <details class="faq-item">
          <summary><span>{p}</span><span class="faq-mas" aria-hidden="true"></span></summary>
          <p>{r}</p>
        </details>""" for p, r in lista)


def seccion_preguntas(lista, wa):
    return f"""
  <section class="seccion seccion-alt" id="preguntas" aria-label="Preguntas frecuentes">
    <div class="contenedor faq-grid">
      <div class="encabezado encabezado-izq">
        <p class="eyebrow">Preguntas frecuentes</p>
        <h2>Lo que más nos preguntan</h2>
        <p class="lead">¿Tienes otra duda? Escríbenos y te contestamos nosotros, no un robot.</p>
        {btn_wa("Pregúntanos por WhatsApp", "btn btn-sec", wa)}
      </div>
      <div class="faq">
{faq_html(lista)}
      </div>
    </div>
  </section>
"""


def v_nosotros():
    return """
  <section class="seccion" id="nosotros" aria-label="Nosotros">
    <div class="contenedor nosotros-grid">
      <div>
        <p class="eyebrow">Nosotros</p>
        <h2>Por qué existe VantTS</h2>
        <p class="lead">VantTS nace en Guadalajara con una idea simple: los pequeños negocios merecen tecnología pensada para ellos, no versiones reducidas de software para empresas grandes.</p>
        <p>Detrás de VantTS está Luis P. Reyes, construyendo la empresa desde cero y aprendiendo en el camino, con apoyo de inteligencia artificial para desarrollar cada proyecto. Empezamos con VantTS Barber y hoy construimos para cualquier negocio que lo necesite. Todavía estamos en una etapa temprana: preferimos construir bien antes que construir rápido.</p>
      </div>
      <div class="mision revelar" id="mision">
        <p class="eyebrow">Nuestra misión</p>
        <p class="mision-texto">Ayudar a los pequeños negocios de México a digitalizar su operación y entender su rentabilidad real, empezando por barberías y estéticas en Guadalajara y creciendo giro por giro.</p>
        <ul class="giros">
          <li><span class="giro-tag on">Hoy</span>Barberías y salones</li>
          <li><span class="giro-tag">En desarrollo</span>Masajes y bienestar</li>
          <li><span class="giro-tag">En planeación</span>Veterinarias</li>
          <li><span class="giro-tag">En análisis</span>Abarrotes</li>
        </ul>
      </div>
    </div>
  </section>
"""


def v_contacto():
    return f"""
  <section class="cierre" id="contacto" aria-label="Contacto">
    <div class="contenedor cierre-grid">
      <div>
        <h2>¿Qué quieres construir?</h2>
        <p class="lead">Escríbenos por WhatsApp y cuéntanos tu idea. Te contestamos nosotros y te cotizamos sin costo.</p>
        <div class="cta-fila">{btn_wa("Cuéntanos tu idea", "btn btn-claro", WA_COTIZAR)}</div>
      </div>
{lista_contacto(WA_COTIZAR)}
    </div>
  </section>
"""


def lista_contacto(wa):
    return f"""      <ul class="contacto-lista">
        <li><span class="etiqueta">WhatsApp</span><a href="{wa}" target="_blank" rel="noopener">33 1250 6541</a></li>
        <li><span class="etiqueta">Correo</span><a href="mailto:direccion@vantts.com.mx">direccion@vantts.com.mx</a></li>
        <li><span class="etiqueta">Ubicación</span>Guadalajara, Jalisco</li>
        <li><span class="etiqueta">Redes</span><span><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a> · <a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a> · <a href="{YOUTUBE}" target="_blank" rel="noopener">YouTube</a></span></li>
      </ul>"""


# ===========================================================================
#  PÁGINA 2 · VANTTS BARBER (barber/index.html)
#  Los textos son los mismos de la página única v3; solo cambian las rutas (../).
# ===========================================================================

NAV_BARBER = [
    ("solucion", "Qué resuelve"),
    ("funciones", "Cómo funciona"),
    ("ia", "IA"),
    ("precios", "Precios"),
    ("preguntas", "Preguntas"),
]
A = "../"  # rutas de assets e inicio desde barber/


def b_inicio():
    return f"""
  <section class="hero" id="inicio" aria-label="Inicio">
    <div class="hero-fondo" aria-hidden="true"></div>
    <div class="contenedor hero-grid">
      <div class="hero-texto">
        <a class="pildora" href="{A}#productos"><img src="{A}assets/img/vantts-barber-icono.png" alt="" width="22" height="22"><span>VantTS Barber · un producto de VantTS</span>{I_FLECHA}</a>
        <h1>Cuánto gana tu barbería, <span class="acento">sin adivinar.</span></h1>
        <p class="lead">Tu agenda, tus clientes y tus ventas en un solo lugar, para que sepas cuánto ganas de verdad. Tus clientes siguen siendo tuyos.</p>
        <div class="cta-fila">
          {btn_wa(url=WA_BARBER)}
          <a class="btn btn-sec" href="#funciones"><span>Ver cómo funciona</span></a>
        </div>
        <p class="micro">{I_CHECK}Plan Básico gratis <span class="punto">·</span> IVA incluido <span class="punto">·</span> Mes a mes</p>
      </div>
      <div class="hero-visual" aria-label="Capturas de VantTS Barber">
        {telefono("agenda.jpg", "Agenda de la semana en VantTS Barber, con citas de varios barberos", "telefono telefono-atras", "eager", A)}
        {telefono("metricas.jpg", "Métricas del mes: punto de equilibrio y ventas", "telefono telefono-frente", "eager", A)}
        <div class="chip chip-1">{I_CALENDARIO}<span>Tus clientes reservan solos con tu link</span></div>
        <div class="chip chip-2">{I_DINERO}<span>Ves cuánto te falta para cubrir tus gastos</span></div>
        <p class="demo-nota">Cuenta de demostración · datos inventados</p>
      </div>
    </div>
  </section>

  <section class="confianza" aria-label="Por qué confiar">
    <div class="contenedor confianza-grid">
      <div class="conf">{I_PORCIENTO}<p><strong>Sin comisión</strong><span>ni por cita ni por cliente</span></p></div>
      <div class="conf">{I_CALENDARIO}<p><strong>Mes a mes</strong><span>cancelas cuando quieras</span></p></div>
      <div class="conf">{I_DESCARGA}<p><strong>Tus datos son tuyos</strong><span>30 días para bajarlos si te vas</span></p></div>
      <div class="conf">{I_TIENDA}<p><strong>Ya funciona</strong><span>en Rocker Barber, Guadalajara</span></p></div>
    </div>
  </section>
"""


def dolor(icono, frase, respuesta):
    return f"""
        <article class="dolor revelar">
          <div class="dolor-ico">{icono}</div>
          <p class="dolor-frase">“{frase}”</p>
          <p class="dolor-resp">{respuesta}</p>
        </article>"""


def b_solucion():
    return f"""
  <section class="seccion" id="solucion" aria-label="Qué resuelve">
    <div class="contenedor">
      <div class="encabezado">
        <p class="eyebrow">Qué resuelve</p>
        <h2>¿Te suena alguna?</h2>
        <p class="lead">Lo que nos contaron los barberos que entrevistamos, y lo que VantTS Barber hace con eso.</p>
      </div>
      <div class="dolores">
{dolor(I_DINERO, "No sé cuánto gano ni cuántos clientes atiendo.", "Desde el plan Pro, cada venta queda ligada al cliente y al servicio, y ves cuánto llevas vendido en el mes y cuánto te falta para cubrir tus gastos.")}
{dolor(I_TIJERA, "Le cobro menos a mi cliente de siempre para no perderlo.", "Ves el historial de visitas de cada cliente: el dato para poner tu precio con números, no con miedo. En Max, puntos para premiarlo sin bajar el precio.")}
{dolor(I_CHAT, "Mis citas y mis clientes están en WhatsApp.", "Mandas tu link y tu cliente elige servicio, día y hora. Desde el plan Pro, la cita entra sola a tu agenda.")}
{dolor(I_ESCUDO, "No confío en sistemas de otros.", "No hay directorio que te ponga junto a otras barberías ni comisión por cita. Es mes a mes y, si un día te vas, tienes 30 días para bajar tus datos.")}
      </div>
    </div>
  </section>
"""


PESTANAS = [
    ("reservas", "Reservas", "Desde Básico", "Tu cliente reserva solo, con tu link",
     ["Elige barbero, servicio, día y hora desde tu link o tu código QR.",
      "Solo ve los días que atiendes: tus descansos no salen.",
      "No tiene que descargar ninguna app."],
     "reserva.jpg", "Página de reservas: el cliente elige día y hora"),
    ("agenda", "Agenda", "Desde Básico", "Toda tu agenda, de un vistazo",
     ["Por día, semana o mes; de un barbero o de todos combinados.",
      "Completas, mueves o cancelas cada cita con un toque.",
      "Desde el plan Pro, las reservas en línea entran solas."],
     "agenda.jpg", "Agenda semanal con citas de varios barberos"),
    ("clientes", "Clientes", "Desde Básico", "Cada cliente, con su historial",
     ["Su historial de visitas, aunque solo te dé su apodo.",
      "Te marca a quién toca llamarle (25 días sin venir), quién está en riesgo (45) y a quién ya perdiste (90).",
      "Le llamas o le escribes por WhatsApp con un toque."],
     "clientes.jpg", "Clientes con tarjetas de para llamar, en riesgo y nuevos sin regresar"),
    ("ventas", "Ventas y caja", "Desde Básico", "Tus ventas y tu caja, al día",
     ["Anotas cada venta y su propina en segundos; desde el plan Pro, ligada al cliente y al servicio.",
      "Apuntas tus gastos del día.",
      "Con el cierre del día ves al momento si sobra o falta efectivo."],
     "ventas.jpg", "Formulario para registrar una venta"),
    ("numeros", "Números", "Desde Pro", "Cuánto ganas de verdad",
     ["Cuánto llevas vendido este mes y cuánto te falta para cubrir tus gastos.",
      "Tu ticket promedio, tus gastos fijos y variables y tu margen.",
      "Sin cuaderno ni calculadora."],
     "metricas.jpg", "Métricas del mes con el punto de equilibrio"),
]


def pestanas_html():
    botones, paneles = [], []
    for i, (pid, nombre, plan, titulo, puntos, img, alt) in enumerate(PESTANAS):
        sel = "true" if i == 0 else "false"
        botones.append(f'<button class="tab" role="tab" id="tab-{pid}" aria-controls="panel-{pid}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}"><span class="tab-num">{i + 1:02d}</span>{nombre}</button>')
        lis = "\n".join(f"              <li>{I_CHECK}<span>{p}</span></li>" for p in puntos)
        oculto = "" if i == 0 else " hidden"
        paneles.append(f"""
        <div class="panel" role="tabpanel" id="panel-{pid}" aria-labelledby="tab-{pid}"{oculto}>
          <div class="panel-texto">
            <span class="plan-chip">{plan}</span>
            <h3>{titulo}</h3>
            <ul class="lista-check">
{lis}
            </ul>
          </div>
          <div class="panel-visual">{telefono(img, alt, a=A)}</div>
        </div>""")
    return "\n          ".join(botones), "".join(paneles)


def b_funciones():
    _botones, _paneles = pestanas_html()
    return f"""
  <section class="seccion seccion-alt" id="funciones" aria-label="Cómo funciona">
    <div class="contenedor">
      <div class="encabezado">
        <p class="eyebrow">Cómo funciona</p>
        <h2>De la reserva a tus números, en un solo lugar</h2>
        <p class="lead">Así se ve VantTS Barber en el celular. Capturas de la cuenta de demostración, con datos inventados.</p>
      </div>
      <div class="tabs" role="tablist" aria-label="Partes de VantTS Barber">
          {_botones}
      </div>
      <div class="paneles">{_paneles}
      </div>
    </div>
  </section>
"""


def b_ia():
    return f"""
  <section class="seccion seccion-oscura" id="ia" aria-label="Inteligencia artificial">
    <div class="contenedor ia-grid">
      <div class="ia-texto">
        <p class="eyebrow eyebrow-claro">{I_CHISPA}IA para tu barbería</p>
        <h2>Una IA que solo habla de tu negocio</h2>
        <p class="lead">El panel de IA lee tus ventas, tu agenda, tus clientes y tus metas, y te responde con tus propios números. No es un chat para cualquier cosa: está hecho para que decidas mejor en tu barbería.</p>
        <ul class="lista-check lista-clara">
          <li>{I_CHECK}<span>Te sugiere qué hacer y te dice dónde verlo dentro de la app, como a qué cliente conviene llamarle.</span></li>
          <li>{I_CHECK}<span>Pasa tus clientes, servicios o productos desde un archivo de otro sistema: la IA los acomoda y tú revisas antes de guardar.</span></li>
          <li>{I_CHECK}<span>Desde el plan Max, con 500 créditos al mes; en Ultra, 1,000.</span></li>
        </ul>
      </div>
      <div class="ia-ejemplos" aria-label="Ejemplos de preguntas">
        <p class="ia-etiqueta">Ejemplos de preguntas</p>
        <div class="burbuja">¿Cómo voy este mes contra mis gastos?</div>
        <div class="burbuja">¿A qué clientes me conviene llamar esta semana?</div>
        <div class="burbuja">¿Qué meta de ventas me pongo para diciembre?</div>
        <div class="ia-campo">{I_CHISPA}<span>Pregúntale a tu negocio…</span></div>
      </div>
    </div>
  </section>
"""


def b_casos():
    return f"""
  <section class="seccion" id="casos" aria-label="Casos">
    <div class="contenedor">
      <div class="caso revelar">
        <div class="caso-texto">
          <p class="eyebrow">Caso real</p>
          <h2>Rocker Barber ya trabaja así</h2>
          <p class="lead">Una barbería de Guadalajara con más de dos años operando lleva su agenda, sus clientes y sus ventas en VantTS Barber. Lo construimos con barberos, para barberos.</p>
{testimonio_html()}
          <p class="caso-nota">{CASO_NOTA}</p>
        </div>
        <div class="caso-datos">
{caso_datos_html()}
        </div>
      </div>
    </div>
  </section>
"""


def plan_card(nombre, precio, subtitulo, items, destacado=False, proximo=False):
    cls = "plan destacado" if destacado else ("plan proximo" if proximo else "plan")
    etiqueta = '<div class="plan-etiqueta">Recomendado</div>' if destacado else ('<div class="plan-etiqueta">Próximamente</div>' if proximo else "")
    precio_html = '<div class="plan-precio pronto">Precio por anunciar</div>' if proximo else f'<div class="plan-precio">{precio}<span>/mes</span></div>'
    lis = "\n".join(f"            <li>{I_CHECK}<span>{i}</span></li>" for i in items)
    pid = slug(nombre)
    return f"""
        <div class="{cls}">
          {etiqueta}
          <h3>{nombre}</h3>
          {precio_html}
          <p class="plan-sub">{subtitulo}</p>
          <ul>
{lis}
          </ul>
          <button type="button" class="plan-ver" data-plan="{pid}" aria-haspopup="dialog">Ver todo lo que incluye{I_FLECHA}</button>
        </div>"""


# Lista completa de funciones por plan (fuente: docs del proyecto, revisados el 22 oct 2026;
# planes de las funciones sin plan decididos por Luis el 22 oct 2026).
# Cada plan lista solo lo que AGREGA; la ventana muestra también lo heredado.
# ("texto", "detalle", proximamente)
PLANES_DETALLE = [
    ("basico", "Básico", "$0", "Para empezar a ordenar tu negocio sin riesgo.", "Una cuenta de administrador.", [
        ("Agenda y caja", [
            ("Agenda de citas", "Tú capturas cada cita.", False),
            ("Reserva en línea con tu link", "Tu cliente elige servicio, día y hora desde tu link y tú confirmas la cita con un toque.", False),
            ("Agenda para cada barbero", "Tus barberos aparecen en la agenda y el cliente elige con quién; tú la manejas desde tu cuenta.", False),
            ("Días de trabajo", "Eliges qué días atiendes.", False),
            ("Registro de ventas a mano", "Anotas cada venta y su propina en la app.", False),
            ("Registro de gastos", "Lo que pagas, incluido lo que sale de la caja.", False),
            ("Cierre del día y corte de caja", "El corte cuadra con tus ventas del día, dejas fondo de caja y te queda el PDF.", False),
        ]),
        ("Clientes", [
            ("Clientes con historial", "Aunque solo te den su apodo; de paso o frecuentes.", False),
            ("Niveles por visitas", "Tus clientes suben de nivel según cuántas veces vienen.", False),
            ("Listas de a quién llamar", "Quién lleva días sin venir, quién está en riesgo y quién no ha regresado, con botón de WhatsApp y mensaje listo.", False),
            ("Registro del cliente frecuente", "Le mandas un link y él llena sus datos.", False),
            ("Aviso de privacidad de tu barbería", "Listo para compartir con tus clientes.", False),
            ("Expediente del cliente en PDF", "", False),
            ("Botón “No llegó”", "Lleva la cuenta de las faltas de cada cliente.", False),
        ]),
        ("Tu negocio", [
            ("Catálogo de servicios y precios", "Con la duración de cada servicio.", False),
            ("Bandeja de avisos", "Avisos al celular y un resumen diario a las 8 a.m.: cumpleaños, VIP por vencer, qué toca comprar.", False),
            ("Pídenos mejoras", "Tú o tu equipo nos piden cambios para su sistema.", False),
        ]),
    ]),
    ("pro", "Pro", "$249", "Para saber cuánto ganas de verdad.", "", [
        ("Agenda y equipo", [
            ("Las reservas de tu link entran solas a tu agenda", "Sin que tengas que confirmarlas.", False),
            ("Garantía para asegurar cada reserva", "Un depósito con tarjeta al reservar, que se regresa completo si el cliente cancela con 1 hora o más.", True),
            ("Recordatorios por WhatsApp", "A tu cliente, 1 día antes y 1 hora antes de su cita.", True),
            ("Cuentas para tu equipo", "Cada barbero con su cuenta: +$100 al mes por cada uno después del primero.", False),
            ("Roles y permisos", "Administrador, encargado, barbero o recepción: tú decides qué ve cada quien.", False),
            ("Cambio de días con tu aprobación", "Tus barberos piden cambiar sus días y tú apruebas.", False),
            ("Peticiones de tus clientes", "Cambios o reagendas de citas que apruebas o rechazas.", False),
        ]),
        ("Dinero", [
            ("Ventas ligadas a cada cliente y servicio", "Sabes quién te compró qué, y alimentan tus métricas.", False),
            ("Inventario", "Productos, existencias, aviso de poco stock y qué toca comprar.", False),
            ("Métricas y punto de equilibrio", "Cómo va tu negocio en gráficas y cuánto necesitas vender para no perder.", False),
            ("Contabilidad", "Balance y estado de resultados.", False),
            ("Reportes y resumen ejecutivo", "Movimientos, clientes, ventas por forma de pago, por barbero y por origen, y tus números clave en una pantalla.", False),
        ]),
        ("Marketing", [
            ("Promociones y descuentos", "Promociones con vigencia y descuentos de un solo uso.", False),
            ("Tarjetas de regalo", "Las vendes en caja, se mandan en PDF por WhatsApp, no vencen y el saldo se usa en una o varias visitas.", False),
            ("Metas y estrategia de marketing", "Con ideas listas y guía por tema.", False),
            ("Avance de tus metas", "Línea de tiempo y gráfica de avance.", False),
        ]),
    ]),
    ("max", "Max", "$599", "Para hacer crecer tu negocio y a tus clientes fieles.", "", [
        ("Clientes fieles", [
            ("Puntos por visitas", "Premias a tu cliente de siempre sin bajarle el precio.", False),
            ("Membresía VIP de paga", "Cobras una membresía a tus clientes.", False),
            ("Fiado y por cobrar", "Ventas a crédito, abonos y recordatorio por WhatsApp.", False),
        ]),
        ("Equipo y operación", [
            ("Nómina y comisiones", "Comisión, sueldo más comisión o renta de silla; propinas, adelantos y bonos, con recibo en PDF.", False),
            ("Compras y proveedores", "Te sugiere qué pedir, mandas la orden por WhatsApp o PDF y llevas lo que debes.", False),
            ("Sucursales", "Varias barberías con clientes y catálogo compartidos, traspasos de inventario y totales del grupo.", False),
            ("Bitácora de cambios", "Quién cambió qué y cuándo, guardado 2 años.", False),
        ]),
        ("Redes sociales", [
            ("Calendario de publicaciones", "Te avisa a la hora y comparte con un botón.", False),
            ("Publicación automática en Instagram y Facebook", "", True),
        ]),
        ("Inteligencia artificial", [
            ("Panel de IA con 500 créditos al mes", "Le preguntas por tu negocio y te propone qué hacer.", False),
            ("Importar desde Excel con IA", "Clientes, inventario, servicios y proveedores desde tu archivo (usa créditos). Gratis en cualquier plan durante tus primeros 30 días.", False),
        ]),
        ("Más", [
            ("Solicitudes de factura electrónica", "Guardas tus datos fiscales y lo que te piden tus clientes.", False),
            ("Tutoriales en video", "Técnicas y cortes paso a paso.", False),
        ]),
    ]),
    ("ultra", "Ultra", "", "Para facturar sin salir de VantTS Barber.", "", [
        ("Lo que agrega Ultra", [
            ("Facturas electrónicas timbradas", "Emites tus facturas desde VantTS Barber.", False),
            ("Panel de IA con 1,000 créditos al mes", "El doble que en Max.", False),
        ]),
    ]),
]

TODOS_LOS_PLANES = [
    "Sin comisión por cita",
    "Mes a mes, sin plazo forzoso",
    "IVA incluido en el precio",
    "Respaldo automático diario de tu información",
    "Descargas en PDF o Excel",
    "30 días para bajar tus datos si te vas",
    "Subes de plan cuando quieras; si bajas, aplica al terminar tu mes",
    "Garantía de precio: en los planes de paga, lo que pagas no sube durante 12 meses desde tu primer pago",
    "Importar tus clientes y servicios con IA, gratis en tus primeros 30 días",
]


def _lista_funciones(grupos):
    out = []
    for titulo, items in grupos:
        lis = []
        for texto, detalle, pronto in items:
            tag = '<span class="pd-pronto">Próximamente</span>' if pronto else ""
            det = f'<span class="pd-det">{detalle}</span>' if detalle else ""
            lis.append(f'<li>{I_CHECK}<span><strong>{texto}</strong>{tag}{det}</span></li>')
        out.append(f'<div class="pd-grupo"><h4>{titulo}</h4><ul>{"".join(lis)}</ul></div>')
    return "".join(out)


def plan_dialogo():
    tabs, paneles = [], []
    for i, (pid, nombre, precio, sub, nota, grupos) in enumerate(PLANES_DETALLE):
        tabs.append(f'<button type="button" role="tab" id="pdt-{pid}" aria-controls="pdp-{pid}" aria-selected="false" tabindex="-1" data-plan="{pid}">{nombre}</button>')
        precio_html = '<span class="pd-precio pronto">Próximamente · precio por anunciar</span>' if not precio else f'<span class="pd-precio">{precio}<small>/mes, IVA incluido</small></span>'
        heredado = ""
        if i > 0:
            previos = []
            for pid2, nombre2, _, _, _, grupos2 in PLANES_DETALLE[:i][::-1]:
                n = sum(len(it) for _, it in grupos2)
                previos.append(f'<details class="pd-hereda"><summary>Y todo lo de {nombre2} <span>({n})</span></summary>{_lista_funciones(grupos2)}</details>')
            heredado = "".join(previos)
        titulo_lista = "Incluye" if i == 0 else f"Lo que agrega {nombre}"
        nota_html = f'<p class="pd-nota">{nota}</p>' if nota else ""
        paneles.append(f"""<section class="pd-panel" role="tabpanel" id="pdp-{pid}" aria-labelledby="pdt-{pid}" hidden>
        <header class="pd-cab"><h3>{nombre}</h3>{precio_html}<p>{sub}</p>{nota_html}</header>
        <p class="pd-titulo">{titulo_lista}</p>
        {_lista_funciones(grupos)}
        {heredado}
      </section>""")
    todos = "".join(f"<li>{I_CHECK}<span>{t}</span></li>" for t in TODOS_LOS_PLANES)
    return f"""
  <dialog class="plan-dialogo" id="planDialogo" aria-labelledby="planDialogoTitulo">
    <div class="pd-caja">
      <div class="pd-barra">
        <h2 id="planDialogoTitulo" class="pd-h2">Todo lo que incluye cada plan</h2>
        <button type="button" class="pd-cerrar" data-cerrar aria-label="Cerrar">×</button>
      </div>
      <div class="pd-tabs" role="tablist" aria-label="Planes">{"".join(tabs)}</div>
      <div class="pd-cuerpo">
      {"".join(paneles)}
        <div class="pd-todos"><h4>En todos los planes</h4><ul>{todos}</ul></div>
        <p class="pd-leyenda"><span class="pd-pronto">Próximamente</span> Ya está en camino; te avisamos cuando esté lista para tu negocio.</p>
      </div>
      <div class="pd-pie"><a class="btn" href="{WA_BARBER}" target="_blank" rel="noopener">{I_WA}<span>Pregúntanos por WhatsApp</span></a></div>
    </div>
  </dialog>"""


# Calculadora de "¿cuánto pagarías al mes?" (4 nov 2026). Sin nombrar marcas:
# la comisión de 20 % por la primera cita de cada cliente nuevo es la que
# publica Fresha en fresha.com/pricing.
PRECIO_PRO, PRECIO_MAX, PRECIO_CUENTA_EXTRA, COMISION_REF = 249, 599, 100, 20


def pesos(n):
    return f"${n:,.0f}"


def calculadora_html(barberos=3, nuevos=10, corte=150):
    extra = PRECIO_CUENTA_EXTRA * (barberos - 1)
    comision = nuevos * corte * COMISION_REF / 100
    return f"""
      <div class="calc revelar" id="calculadora" data-pro="{PRECIO_PRO}" data-max="{PRECIO_MAX}" data-extra="{PRECIO_CUENTA_EXTRA}" data-comision="{COMISION_REF}">
        <div class="calc-texto">
          <h3>¿Cuánto pagarías al mes?</h3>
          <p>Con IVA incluido y sin comisiones por cita ni por cliente nuevo.</p>
          <div class="calc-campos">
            <label>Barberos con cuenta propia<input type="number" id="calcBarberos" min="1" max="30" step="1" value="{barberos}" inputmode="numeric"></label>
            <label>Clientes nuevos al mes<input type="number" id="calcNuevos" min="0" max="999" step="1" value="{nuevos}" inputmode="numeric"></label>
            <label>Precio promedio del corte<input type="number" id="calcCorte" min="0" max="9999" step="10" value="{corte}" inputmode="numeric"></label>
          </div>
        </div>
        <div class="calc-resultados" aria-live="polite">
          <div class="calc-plan"><span>Pro</span><strong id="calcPro">{pesos(PRECIO_PRO + extra)}</strong><small>al mes, con IVA</small></div>
          <div class="calc-plan"><span>Max</span><strong id="calcMax">{pesos(PRECIO_MAX + extra)}</strong><small>al mes, con IVA</small></div>
          <div class="calc-plan calc-ahorro"><span>Comisión por clientes nuevos</span><strong>$0</strong><small id="calcComision">Si una app te cobrara {COMISION_REF} % de la primera cita de cada cliente nuevo, se te irían {pesos(comision)} al mes.</small></div>
        </div>
        <p class="calc-nota">Pro y Max incluyen una cuenta; cada barbero con cuenta propia después del primero suma {pesos(PRECIO_CUENTA_EXTRA)} al mes. En Básico (gratis) tus barberos son agendas sin cuenta. Hay apps con directorio de clientes que cobran {COMISION_REF} % de la primera cita de cada cliente nuevo que llega por ahí.</p>
      </div>"""


def b_precios():
    return f"""
  <section class="seccion seccion-alt" id="precios" aria-label="Precios">
    <div class="contenedor">
      <div class="encabezado">
        <p class="eyebrow">Precios</p>
        <h2>Empieza gratis. Paga cuando veas el valor.</h2>
        <p class="lead">Cuatro planes claros, con IVA incluido y sin letras chiquitas, pensados para barberías y salones. Si tu negocio es de otro giro, <a href="{A}#servicios">te construimos algo a tu medida</a>.</p>
      </div>
      <div class="planes">
{plan_card("Básico", "$0", "Para empezar a ordenar tu negocio sin riesgo.", [
    "Agenda: tú capturas tus citas",
    "Reserva en línea con tu link",
    "Clientes con historial, aunque solo te den su apodo",
    "Catálogo de servicios y precios",
    "Ventas y gastos a mano, y corte de caja del día",
    "Una cuenta de administrador",
])}
{plan_card("Pro", "$249", "Para saber cuánto ganas de verdad.", [
    "Todo lo de Básico",
    "Las reservas en línea se acomodan solas en tu agenda",
    "Garantía opcional para asegurar cada reserva (próximamente)",
    "Ventas ligadas a cada cliente y servicio",
    "Métricas y punto de equilibrio",
    "Metas y estrategia de marketing",
    "Cuentas para tu equipo: +$100/mes por barbero después del primero",
], destacado=True)}
{plan_card("Max", "$599", "Para hacer crecer tu negocio y a tus clientes fieles.", [
    "Todo lo de Pro",
    "Fidelidad: puntos por visitas",
    "Membresías VIP de paga para tus clientes",
    "Calendario de contenido para redes",
    "Panel de IA con 500 créditos al mes",
    "Solicitudes de factura electrónica",
    "Cuentas para tu equipo: +$100/mes por barbero después del primero",
])}
{plan_card("Ultra", "", "Para facturar sin salir de VantTS Barber.", [
    "Todo lo de Max",
    "Facturas electrónicas timbradas desde VantTS Barber",
    "Panel de IA con 1,000 créditos al mes",
], proximo=True)}
      </div>
{calculadora_html()}
      <p class="nota">Precios en pesos mexicanos, con IVA incluido. Vigentes para barberías y salones. <strong>Garantía de precio:</strong> lo que pagas por tu plan y por cada cuenta adicional no sube durante 12 meses desde tu primer pago.</p>
    </div>
{plan_dialogo()}
  </section>
"""


FAQ_BARBER = [
    ("¿Los precios incluyen IVA?", "Sí. El precio que ves es el que pagas."),
    ("¿El precio me puede subir?", "En los planes de paga, lo que pagas por tu plan y por cada cuenta adicional no sube durante 12 meses desde tu primer pago."),
    ("Vengo de otra app, ¿puedo pasar mis clientes?", "Sí. Descarga tu lista en Excel desde la app que usas hoy y súbela a VantTS Barber: la IA acomoda las columnas por ti y tú revisas antes de guardar. En tus primeros 30 días es gratis en cualquier plan, para clientes y servicios (y tu inventario desde Pro). Si algo no te sale, nos escribes por WhatsApp."),
    ("¿Y si con el plan Básico me basta?", "Te quedas en Básico, que es gratis, sin presión. Preferimos que pagues cuando de verdad veas el valor."),
    ("¿Mis clientes siguen siendo míos?", "Sí. No hay directorio que te ponga junto a otras barberías y no cobramos comisión por cita ni por cliente. Si un día te vas, tienes 30 días para bajar tus datos."),
    ("¿Necesito saber de computación?", "Si usas WhatsApp, puedes usarlo. Se abre desde tu celular, sin instalar nada; configuramos tu barbería y tus servicios contigo, y si algo no te sale nos escribes por WhatsApp."),
    ("¿Mi cliente tiene que descargar una app?", "No. Reserva desde tu link o tu código QR, en el navegador de su celular."),
    ("¿Sirve si tengo varios barberos?", "Sí. Cada barbero tiene su agenda y tu cliente elige con quién reservar; tú decides qué ve cada quien y ves cuánto vendió cada uno. Las cuentas para tu equipo van desde el plan Pro, con +$100 al mes por barbero después del primero."),
    ("¿Puedo cancelar cuando quiera?", "Sí. Es mes a mes, sin plazo forzoso."),
    ("Mi negocio no es barbería ni salón, ¿me sirve?", f'VantTS Barber está hecho para barberías y salones. Para otro giro, <a href="{A}#servicios">te construimos un sistema a tu medida</a>: escríbenos y te cotizamos sin costo.'),
]


def b_contacto():
    return f"""
  <section class="cierre" id="contacto" aria-label="Contacto">
    <div class="contenedor cierre-grid">
      <div>
        <h2>¿Lo vemos juntos?</h2>
        <p class="lead">Escríbeme por WhatsApp y te enseño VantTS Barber con la cuenta de demostración. Es la forma más rápida de contactarnos.</p>
        <div class="cta-fila">{btn_wa("Escríbeme por WhatsApp", "btn btn-claro", WA_BARBER)}</div>
      </div>
{lista_contacto(WA_BARBER)}
    </div>
  </section>
"""


# ===========================================================================
#  PIEZAS COMUNES: menú, pie de página y esqueleto de la página
# ===========================================================================

def footer(h, b, wa):
    """h: ruta al inicio ("" o "../"); b: ruta a la página de Barber ("barber/" o "")."""
    return f"""<footer class="pie">
  <div class="pie-columnas">
    <div class="pie-marca">
      <span class="pie-logo"><img class="logo-ico" src="{h}assets/img/icono.png" alt="" width="36" height="36"><img src="{h}assets/img/wordmark-claro.png" alt="VantTS" width="150" height="28"></span>
      <p>Software de gestión + IA para negocios.</p>
    </div>
    <div>
      <h4>Servicios</h4>
      <ul>
        <li><a href="{h}#servicios">Sistemas para tu negocio</a></li>
        <li><a href="{h}#servicios">Apps web y móviles</a></li>
        <li><a href="{h}#servicios">Automatización con IA</a></li>
        <li><a href="{h}#servicios">Sitios web</a></li>
      </ul>
    </div>
    <div>
      <h4>Productos</h4>
      <ul>
        <li><a href="{b or './'}">VantTS Barber</a><span class="pie-tag on">Hoy</span></li>
        <li>VantTS Salud y Bienestar<span class="pie-tag">Próximamente</span></li>
        <li>VantTS Vet<span class="pie-tag">Próximamente</span></li>
        <li>VantTS Life<span class="pie-tag">Próximamente</span></li>
      </ul>
    </div>
    <div>
      <h4>Empresa</h4>
      <ul>
        <li><a href="{h}#nosotros">Nosotros</a></li>
        <li><a href="{h}#mision">Nuestra misión</a></li>
        <li><a href="{h}#proceso">Cómo trabajamos</a></li>
        <li><a href="{h}#contacto">Contacto</a></li>
      </ul>
    </div>
    <div>
      <h4>Hablemos</h4>
      <ul>
        <li><a href="{wa}" target="_blank" rel="noopener">{ICO_TEL}33 1250 6541</a></li>
        <li><a href="mailto:direccion@vantts.com.mx">{ICO_MAIL}direccion@vantts.com.mx</a></li>
        <li>{ICO_PIN}Guadalajara, Jalisco</li>
      </ul>
      <h4 class="pie-sub">Síguenos</h4>
      <ul class="pie-redes">
        <li><a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{ICO_IG}</a></li>
        <li><a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook">{ICO_FB}</a></li>
        <li><a href="{YOUTUBE}" target="_blank" rel="noopener" aria-label="YouTube">{ICO_YT}</a></li>
      </ul>
    </div>
  </div>
  <div class="pie-base">
    <div class="pie-base-in">
      <span>{ICO_GLOBO}Español (México)</span>
      <span>{ICO_ESCUDO}Sin cookies de rastreo</span>
      <span class="pie-espacio"></span>
      <span>© {ANIO} VantTS</span>
    </div>
  </div>
</footer>
<div class="flotantes">
  <a class="subir" id="subir" href="#inicio" aria-label="Subir al inicio de la página">↑</a>
  <a class="wa-flotante" href="{wa}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">{I_WA}</a>
</div>"""


def nav_html(items, h, anuncio, wa, wa_texto, extra=""):
    links = "\n".join(f'        <a href="#{sid}" data-seccion="{sid}">{label}</a>' for sid, label in items)
    logo_href = "#inicio" if not h else h
    return f"""<div class="anuncio">
  {anuncio}
</div>
<header class="nav" id="nav">
  <div class="contenedor nav-in">
    <a class="nav-logo" href="{logo_href}" aria-label="VantTS, ir al inicio"><img class="logo-ico" src="{h}assets/img/icono.png" alt="" width="36" height="36"><img class="logo-texto" src="{h}assets/img/wordmark.png" alt="VantTS" width="147" height="28"></a>
    <nav class="nav-links" id="navLinks" aria-label="Secciones">
{links}{extra}
        <a class="nav-wa" href="{wa}" target="_blank" rel="noopener">{I_WA}<span>{wa_texto}</span></a>
    </nav>
    <a class="btn btn-chico nav-cta" href="{wa}" target="_blank" rel="noopener">{I_WA}<span>WhatsApp</span></a>
    <button class="nav-boton" id="navBoton" aria-label="Abrir menú" aria-expanded="false" aria-controls="navLinks"><span></span><span></span><span></span></button>
  </div>
</header>"""


# Movimiento del sitio (aprobado por Luis el 22 oct 2026): cada idea M2-M12 es una clase en <html>.
# Para apagar una, quítala de esta lista. Detalle en Investigación/VantTS_Investigacion_Movimiento_del_sitio.docx.
MOVIMIENTO = "m-progreso m-hero m-parallax m-cascada m-titulos m-pestanas m-tarjetas m-faq m-botones m-whatsapp m-menu"


def pagina(*, h, titulo, descripcion, og_titulo, og_desc, url, saltar, nav, cuerpo, pie, head_extra=""):
    return f"""<!doctype html>
<html lang="es-MX" class="{MOVIMIENTO}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<meta name="theme-color" content="#1F4E3D">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_MX">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{og_titulo}">
<meta property="og:description" content="{og_desc}">
<meta property="og:image" content="https://vantts.com.mx/assets/icono-512.png">
<link rel="canonical" href="{url}">{head_extra}
<link rel="icon" href="{h}assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{h}assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="{h}assets/apple-touch-icon.png">
<link rel="preload" href="{h}assets/fonts/outfit-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{h}assets/style.css">
<link rel="stylesheet" href="{h}assets/motion.css">
</head>
<body>
<a class="saltar" href="#{saltar}">Saltar al contenido</a>
{nav}

<main>
{cuerpo}
</main>

{pie}

<script src="{h}assets/script.js"></script>
<script src="{h}assets/motion.js"></script>
</body>
</html>
"""


# Enlaces viejos como vantts.com.mx/#precios: se mandan a la página de Barber.
REDIRIGE_HASH = f"""
<script>(function(){{var h=location.hash.slice(1);if({SECCIONES_BARBER!r}.indexOf(h)>-1)location.replace("barber/#"+h);}})();</script>"""


def redireccion(destino):
    """Las direcciones anteriores (p. ej. /precios.html) llevan a su sección."""
    return f"""<!doctype html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<title>VantTS</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="https://vantts.com.mx{destino}">
<meta http-equiv="refresh" content="0; url={destino}">
<script>location.replace("{destino}");</script>
</head>
<body><a href="{destino}">Continuar a VantTS</a></body>
</html>
"""


# ---------------------------------------------------------------------------
# Generar
# ---------------------------------------------------------------------------
inicio_html = pagina(
    h="",
    titulo="VantTS · Software a la medida + IA para negocios",
    descripcion="Sistemas, apps, sitios web y automatización con IA hechos a la medida de tu negocio, con cotización sin costo y renta mensual con mantenimiento. Creadores de VantTS Barber. Guadalajara, Jalisco.",
    og_titulo="VantTS · La tecnología que tu negocio necesita, hecha a tu medida",
    og_desc="Sistemas, apps, sitios web y automatización con IA. Te cotizamos sin costo.",
    url="https://vantts.com.mx/",
    saltar="servicios",
    nav=nav_html(NAV_VANTTS, "",
                 f'<a href="barber/"><span class="anuncio-tag">Producto</span>VantTS Barber: agenda, clientes y ventas para tu barbería, desde $0.<span class="anuncio-flecha">{I_FLECHA}</span></a>',
                 WA_COTIZAR, "Cuéntanos tu idea"),
    cuerpo="".join([v_inicio(), v_servicios(), v_proceso(), v_productos(), v_cobro(), v_casos(),
                    seccion_preguntas(FAQ_VANTTS, WA_COTIZAR), v_nosotros(), v_contacto()]),
    pie=footer("", "barber/", WA_COTIZAR),
    head_extra=REDIRIGE_HASH,
)

barber_html = pagina(
    h=A,
    titulo="VantTS Barber · Cuánto gana tu barbería, sin adivinar",
    descripcion="VantTS Barber: tu agenda, tus clientes y tus ventas en un solo lugar, para que sepas cuánto ganas de verdad. Planes Básico gratis, Pro $249 y Max $599 al mes, IVA incluido; Ultra, próximamente.",
    og_titulo="VantTS Barber · Cuánto gana tu barbería, sin adivinar",
    og_desc="Tu agenda, tus clientes y tus ventas en un solo lugar. Plan Básico gratis, IVA incluido, mes a mes.",
    url="https://vantts.com.mx/barber/",
    saltar="solucion",
    nav=nav_html(NAV_BARBER, A,
                 f'<a href="#precios"><span class="anuncio-tag">Nuevo</span>VantTS Barber ya tiene 4 planes, desde $0. Ultra llega pronto con facturación.<span class="anuncio-flecha">{I_FLECHA}</span></a>',
                 WA_BARBER, "Escríbeme por WhatsApp",
                 extra=f'\n        <a class="nav-volver" href="{A}">Más de VantTS</a>'),
    cuerpo="".join([b_inicio(), b_solucion(), b_funciones(), b_ia(), b_casos(), b_precios(),
                    seccion_preguntas(FAQ_BARBER, WA_BARBER), b_contacto()]),
    pie=footer(A, "", WA_BARBER),
)

with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(inicio_html)
print("Generado: index.html (inicio de VantTS, v4)")

os.makedirs(os.path.join(OUT_DIR, "barber"), exist_ok=True)
with open(os.path.join(OUT_DIR, "barber", "index.html"), "w", encoding="utf-8") as f:
    f.write(barber_html)
print("Generado: barber/index.html (VantTS Barber)")

for nombre, destino in PAGINAS_ANTERIORES.items():
    with open(os.path.join(OUT_DIR, f"{nombre}.html"), "w", encoding="utf-8") as f:
        f.write(redireccion(destino))
    print(f"Generado: {nombre}.html -> {destino}")
