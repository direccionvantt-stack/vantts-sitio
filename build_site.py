#!/usr/bin/env python3
"""
Genera el sitio de VantTS como una sola página (index.html), rediseño v3 (18 oct 2026).

Basado en la revisión de 69 páginas de inicio de empresas grandes de IA y software
(Investigación/VantTS_Investigacion_Rediseno_del_sitio.docx): menú superior fijo,
hero corto con el producto a la vista, franja de confianza, funciones contadas como
resultados en pestañas, IA como función concreta, precios, preguntas frecuentes y
cierre con WhatsApp. Todo en una sola página; las direcciones anteriores
(solucion.html, precios.html, ...) redirigen a su sección.

Reglas: solo se dice lo que ya funciona en VantTS Barber (VTS-COM-06); las capturas
son de la cuenta de demostración (datos inventados).
"""
import os
import datetime

OUT_DIR = os.environ.get("VANTTS_SITE_OUT", os.path.dirname(os.path.abspath(__file__)))
ANIO = datetime.date.today().year

# Menú superior: (id de la sección, texto)
NAV = [
    ("solucion", "Qué resuelve"),
    ("funciones", "Cómo funciona"),
    ("ia", "IA"),
    ("precios", "Precios"),
    ("preguntas", "Preguntas"),
    ("nosotros", "Nosotros"),
]
# Páginas anteriores: se conservan como redirección a su sección
PAGINAS_ANTERIORES = ["solucion", "precios", "casos", "nosotros", "contacto"]

WHATSAPP = "https://wa.me/523312506541?text=Hola%2C%20vi%20la%20p%C3%A1gina%20de%20VantTS%20y%20quiero%20saber%20m%C3%A1s"
INSTAGRAM = "https://www.instagram.com/vantts.mx/"
FACEBOOK = "https://www.facebook.com/profile.php?id=61595384815178"
YOUTUBE = "https://www.youtube.com/@vantts_mx"


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

# Pie de página: mismos íconos que la versión anterior
ICO_TEL = ico('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>', "pie-ico")
ICO_MAIL = ico('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>', "pie-ico")
ICO_PIN = ico('<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>', "pie-ico")
ICO_GLOBO = ico('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 2.5 15.3 0 18M12 3c-2.5 2.7-2.5 15.3 0 18"/>', "pie-ico")
ICO_ESCUDO = ico('<path d="M12 3l7 3v6c0 4.4-3 7.7-7 9-4-1.3-7-4.6-7-9V6z"/><path d="M9 12l2 2 4-4"/>', "pie-ico")
ICO_IG = ico('<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="0.6"/>', "pie-ico")
ICO_FB = ico('<path d="M14 8.5h2.5V5H14a3.5 3.5 0 0 0-3.5 3.5V11H8v3.5h2.5V21H14v-6.5h2.5L17 11h-3V9a.5.5 0 0 1 .5-.5z"/>', "pie-ico")
ICO_YT = ico('<rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10 9.2v5.6l4.8-2.8z"/>', "pie-ico")


def btn_wa(texto="Escríbeme por WhatsApp", cls="btn"):
    return f'<a class="{cls}" href="{WHATSAPP}" target="_blank" rel="noopener">{I_WA}<span>{texto}</span></a>'


def telefono(src, alt, cls="telefono", carga="lazy"):
    extra = ' fetchpriority="high"' if carga == "eager" else ""
    return f'<figure class="{cls}"><img src="assets/img/{src}" alt="{alt}" loading="{carga}"{extra} decoding="async" width="600" height="1153"></figure>'


# ---------------------------------------------------------------------------
# 1. INICIO (hero)
# ---------------------------------------------------------------------------
inicio = f"""
  <section class="hero" id="inicio" aria-label="Inicio">
    <div class="hero-fondo" aria-hidden="true"></div>
    <div class="contenedor hero-grid">
      <div class="hero-texto">
        <a class="pildora" href="#funciones"><img src="assets/img/vantts-barber-icono.png" alt="" width="22" height="22"><span>VantTS Barber · nuestro primer producto</span>{I_FLECHA}</a>
        <h1>Cuánto gana tu barbería, <span class="acento">sin adivinar.</span></h1>
        <p class="lead">Tu agenda, tus clientes y tus ventas en un solo lugar, para que sepas cuánto ganas de verdad. Tus clientes siguen siendo tuyos.</p>
        <div class="cta-fila">
          {btn_wa()}
          <a class="btn btn-sec" href="#funciones"><span>Ver cómo funciona</span></a>
        </div>
        <p class="micro">{I_CHECK}Plan Básico gratis <span class="punto">·</span> IVA incluido <span class="punto">·</span> Mes a mes</p>
      </div>
      <div class="hero-visual" aria-label="Capturas de VantTS Barber">
        {telefono("agenda.jpg", "Agenda de la semana en VantTS Barber, con citas de varios barberos", "telefono telefono-atras", "eager")}
        {telefono("metricas.jpg", "Métricas del mes: punto de equilibrio y ventas", "telefono telefono-frente", "eager")}
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

# ---------------------------------------------------------------------------
# 2. QUÉ RESUELVE (los 4 dolores de VTS-COM-06)
# ---------------------------------------------------------------------------
def dolor(icono, frase, respuesta):
    return f"""
        <article class="dolor revelar">
          <div class="dolor-ico">{icono}</div>
          <p class="dolor-frase">“{frase}”</p>
          <p class="dolor-resp">{respuesta}</p>
        </article>"""

solucion = f"""
  <section class="seccion" id="solucion" aria-label="Qué resuelve">
    <div class="contenedor">
      <div class="encabezado">
        <p class="eyebrow">Qué resuelve</p>
        <h2>¿Te suena alguna?</h2>
        <p class="lead">Lo que nos contaron los barberos que entrevistamos, y lo que VantTS Barber hace con eso.</p>
      </div>
      <div class="dolores">
{dolor(I_DINERO, "No sé cuánto gano ni cuántos clientes atiendo.", "Cada venta queda ligada al cliente y al servicio, y ves cuánto llevas vendido en el mes y cuánto te falta para cubrir tus gastos.")}
{dolor(I_TIJERA, "Le cobro menos a mi cliente de siempre para no perderlo.", "Ves el historial de visitas de cada cliente: el dato para poner tu precio con números, no con miedo. En Max, puntos y niveles para premiarlo sin bajar el precio.")}
{dolor(I_CHAT, "Mis citas y mis clientes están en WhatsApp.", "Mandas tu link y tu cliente elige servicio, día y hora. Desde el plan Pro, la cita entra sola a tu agenda.")}
{dolor(I_ESCUDO, "No confío en sistemas de otros.", "No hay directorio que te ponga junto a otras barberías ni comisión por cita. Es mes a mes y, si un día te vas, tienes 30 días para bajar tus datos.")}
      </div>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# 3. CÓMO FUNCIONA (pestañas con capturas de la cuenta demo)
# ---------------------------------------------------------------------------
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
          <div class="panel-visual">{telefono(img, alt)}</div>
        </div>""")
    return "\n          ".join(botones), "".join(paneles)


_botones, _paneles = pestanas_html()
funciones = f"""
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

# ---------------------------------------------------------------------------
# 4. IA (función concreta, desde Max)
# ---------------------------------------------------------------------------
ia = f"""
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

# ---------------------------------------------------------------------------
# 5. CASO (Rocker Barber)
# ---------------------------------------------------------------------------
casos = f"""
  <section class="seccion" id="casos" aria-label="Casos">
    <div class="contenedor">
      <div class="caso revelar">
        <div class="caso-texto">
          <p class="eyebrow">Caso real</p>
          <h2>Rocker Barber ya trabaja así</h2>
          <p class="lead">Una barbería de Guadalajara con más de dos años operando lleva su agenda, sus clientes y sus ventas en VantTS Barber. Lo construimos con barberos, para barberos.</p>
          <p class="caso-nota">Estamos midiendo resultados con ellos. En cuanto tengamos números, los vas a ver aquí: preferimos enseñar resultados reales, no promesas.</p>
        </div>
        <div class="caso-datos">
          <div class="dato"><strong>+2 años</strong><span>operando en Guadalajara</span></div>
          <div class="dato"><strong>1 sistema</strong><span>agenda, clientes y ventas juntos</span></div>
          <div class="dato"><strong>$0</strong><span>de comisión por cita</span></div>
        </div>
      </div>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# 6. PRECIOS (mismos 4 planes y textos vigentes)
# ---------------------------------------------------------------------------
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


def slug(t):
    return t.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace(" ", "-")


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
            ("Importar desde Excel con IA", "Clientes, inventario, servicios y proveedores desde tu archivo (usa créditos).", False),
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
      <div class="pd-pie"><a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">{I_WA}<span>Pregúntanos por WhatsApp</span></a></div>
    </div>
  </dialog>"""


precios = f"""
  <section class="seccion seccion-alt" id="precios" aria-label="Precios">
    <div class="contenedor">
      <div class="encabezado">
        <p class="eyebrow">Precios</p>
        <h2>Empieza gratis. Paga cuando veas el valor.</h2>
        <p class="lead">Cuatro planes claros, con IVA incluido y sin letras chiquitas. Hoy están pensados para barberías y salones; si tu negocio es de otro giro, te cotizamos según lo que de verdad necesites.</p>
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
    "Fidelidad: puntos y niveles por visitas",
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
      <p class="nota">Precios en pesos mexicanos, con IVA incluido. Vigentes para barberías y salones.</p>
    </div>
{plan_dialogo()}
  </section>
"""

# ---------------------------------------------------------------------------
# 7. PREGUNTAS FRECUENTES
# ---------------------------------------------------------------------------
FAQ = [
    ("¿Los precios incluyen IVA?", "Sí. El precio que ves es el que pagas."),
    ("¿Y si con el plan Básico me basta?", "Te quedas en Básico, que es gratis, sin presión. Preferimos que pagues cuando de verdad veas el valor."),
    ("¿Mis clientes siguen siendo míos?", "Sí. No hay directorio que te ponga junto a otras barberías y no cobramos comisión por cita ni por cliente. Si un día te vas, tienes 30 días para bajar tus datos."),
    ("¿Necesito saber de computación?", "Si usas WhatsApp, puedes usarlo. Se abre desde tu celular, sin instalar nada; configuramos tu barbería y tus servicios contigo, y si algo no te sale nos escribes por WhatsApp."),
    ("¿Mi cliente tiene que descargar una app?", "No. Reserva desde tu link o tu código QR, en el navegador de su celular."),
    ("¿Sirve si tengo varios barberos?", "Sí. Cada barbero tiene su agenda y tu cliente elige con quién reservar; tú decides qué ve cada quien y ves cuánto vendió cada uno. Las cuentas para tu equipo van desde el plan Pro, con +$100 al mes por colaborador."),
    ("¿Puedo cancelar cuando quiera?", "Sí. Es mes a mes, sin plazo forzoso."),
    ("Mi negocio no es barbería ni salón, ¿me sirve?", "Vamos giro por giro y solo ofrecemos lo que ya probamos. Escríbenos y te decimos con honestidad si hoy VantTS le sirve a tu negocio."),
]

faq_items = "\n".join(f"""        <details class="faq-item">
          <summary><span>{p}</span><span class="faq-mas" aria-hidden="true"></span></summary>
          <p>{r}</p>
        </details>""" for p, r in FAQ)

preguntas = f"""
  <section class="seccion" id="preguntas" aria-label="Preguntas frecuentes">
    <div class="contenedor faq-grid">
      <div class="encabezado encabezado-izq">
        <p class="eyebrow">Preguntas frecuentes</p>
        <h2>Lo que más nos preguntan</h2>
        <p class="lead">¿Tienes otra duda? Escríbenos y te contestamos nosotros, no un robot.</p>
        {btn_wa("Pregúntanos por WhatsApp", "btn btn-sec")}
      </div>
      <div class="faq">
{faq_items}
      </div>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# 8. NOSOTROS
# ---------------------------------------------------------------------------
nosotros = f"""
  <section class="seccion seccion-alt" id="nosotros" aria-label="Nosotros">
    <div class="contenedor nosotros-grid">
      <div>
        <p class="eyebrow">Nosotros</p>
        <h2>Por qué existe VantTS</h2>
        <p class="lead">VantTS nace en Guadalajara con una idea simple: los pequeños negocios de servicios merecen herramientas de gestión pensadas para ellos, no versiones reducidas de software para empresas grandes.</p>
        <p>Detrás de VantTS está Luis P. Reyes, construyendo la empresa desde cero y aprendiendo en el camino, con apoyo de inteligencia artificial para desarrollar el producto. Todavía estamos en una etapa temprana: preferimos construir bien antes que construir rápido.</p>
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

# ---------------------------------------------------------------------------
# 9. CONTACTO (cierre)
# ---------------------------------------------------------------------------
contacto = f"""
  <section class="cierre" id="contacto" aria-label="Contacto">
    <div class="contenedor cierre-grid">
      <div>
        <h2>¿Lo vemos juntos?</h2>
        <p class="lead">Escríbeme por WhatsApp y te enseño VantTS Barber con la cuenta de demostración. Es la forma más rápida de contactarnos.</p>
        <div class="cta-fila">{btn_wa("Escríbeme por WhatsApp", "btn btn-claro")}</div>
      </div>
      <ul class="contacto-lista">
        <li><span class="etiqueta">WhatsApp</span><a href="{WHATSAPP}" target="_blank" rel="noopener">33 1250 6541</a></li>
        <li><span class="etiqueta">Correo</span><a href="mailto:direccion@vantts.com.mx">direccion@vantts.com.mx</a></li>
        <li><span class="etiqueta">Ubicación</span>Guadalajara, Jalisco</li>
        <li><span class="etiqueta">Redes</span><span><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a> · <a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a> · <a href="{YOUTUBE}" target="_blank" rel="noopener">YouTube</a></span></li>
      </ul>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# PIE DE PÁGINA (franja verde, propuesta A)
# ---------------------------------------------------------------------------
FOOTER = f"""<footer class="pie">
  <div class="pie-columnas">
    <div class="pie-marca">
      <span class="pie-logo"><img class="logo-ico" src="assets/img/icono.png" alt="" width="36" height="36"><img src="assets/img/wordmark-claro.png" alt="VantTS" width="150" height="28"></span>
      <p>Software de gestión + IA para negocios.</p>
    </div>
    <div>
      <h4>Producto</h4>
      <ul>
        <li><a href="#solucion">Qué resuelve</a></li>
        <li><a href="#funciones">Cómo funciona</a></li>
        <li><a href="#precios">Planes y precios</a></li>
        <li><a href="#casos">Casos</a></li>
      </ul>
    </div>
    <div>
      <h4>Giros</h4>
      <ul>
        <li><a href="#funciones">Barberías y salones</a><span class="pie-tag on">Hoy</span></li>
        <li>Masajes y bienestar<span class="pie-tag">En desarrollo</span></li>
        <li>Veterinarias<span class="pie-tag">En planeación</span></li>
        <li>Abarrotes<span class="pie-tag">En análisis</span></li>
      </ul>
    </div>
    <div>
      <h4>Empresa</h4>
      <ul>
        <li><a href="#nosotros">Nosotros</a></li>
        <li><a href="#mision">Nuestra misión</a></li>
        <li><a href="#preguntas">Preguntas frecuentes</a></li>
        <li><a href="#contacto">Contacto</a></li>
      </ul>
    </div>
    <div>
      <h4>Hablemos</h4>
      <ul>
        <li><a href="{WHATSAPP}" target="_blank" rel="noopener">{ICO_TEL}33 1250 6541</a></li>
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
  <a class="wa-flotante" href="{WHATSAPP}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">{I_WA}</a>
</div>"""


def nav_html():
    links = "\n".join(f'        <a href="#{sid}" data-seccion="{sid}">{label}</a>' for sid, label in NAV)
    return f"""<div class="anuncio">
  <a href="#precios"><span class="anuncio-tag">Nuevo</span>VantTS Barber ya tiene 4 planes, desde $0. Ultra llega pronto con facturación.<span class="anuncio-flecha">{I_FLECHA}</span></a>
</div>
<header class="nav" id="nav">
  <div class="contenedor nav-in">
    <a class="nav-logo" href="#inicio" aria-label="VantTS, ir al inicio"><img class="logo-ico" src="assets/img/icono.png" alt="" width="36" height="36"><img class="logo-texto" src="assets/img/wordmark.png" alt="VantTS" width="147" height="28"></a>
    <nav class="nav-links" id="navLinks" aria-label="Secciones">
{links}
        <a class="nav-wa" href="{WHATSAPP}" target="_blank" rel="noopener">{I_WA}<span>Escríbeme por WhatsApp</span></a>
    </nav>
    <a class="btn btn-chico nav-cta" href="{WHATSAPP}" target="_blank" rel="noopener">{I_WA}<span>WhatsApp</span></a>
    <button class="nav-boton" id="navBoton" aria-label="Abrir menú" aria-expanded="false" aria-controls="navLinks"><span></span><span></span><span></span></button>
  </div>
</header>"""


# Movimiento del sitio (aprobado por Luis el 22 oct 2026): cada idea M2-M12 es una clase en <html>.
# Para apagar una, quítala de esta lista. Detalle en Investigación/VantTS_Investigacion_Movimiento_del_sitio.docx.
MOVIMIENTO = "m-progreso m-hero m-parallax m-cascada m-titulos m-pestanas m-tarjetas m-faq m-botones m-whatsapp m-menu"


def pagina_unica(cuerpo):
    return f"""<!doctype html>
<html lang="es-MX" class="{MOVIMIENTO}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>VantTS · Software de gestión + IA para negocios</title>
<meta name="description" content="VantTS Barber: tu agenda, tus clientes y tus ventas en un solo lugar, para que sepas cuánto ganas de verdad. Planes Básico gratis, Pro $249 y Max $599 al mes, IVA incluido; Ultra, próximamente.">
<meta name="theme-color" content="#1F4E3D">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_MX">
<meta property="og:url" content="https://vantts.com.mx/">
<meta property="og:title" content="VantTS · Cuánto gana tu barbería, sin adivinar">
<meta property="og:description" content="Tu agenda, tus clientes y tus ventas en un solo lugar. Plan Básico gratis, IVA incluido, mes a mes.">
<meta property="og:image" content="https://vantts.com.mx/assets/icono-512.png">
<link rel="canonical" href="https://vantts.com.mx/">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/outfit-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/motion.css">
</head>
<body>
<a class="saltar" href="#solucion">Saltar al contenido</a>
{nav_html()}

<main>
{cuerpo}
</main>

{FOOTER}

<script src="assets/script.js"></script>
<script src="assets/motion.js"></script>
</body>
</html>
"""


def redireccion(sid):
    """Las direcciones anteriores (p. ej. /precios.html) llevan a su sección."""
    return f"""<!doctype html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<title>VantTS</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="https://vantts.com.mx/#{sid}">
<meta http-equiv="refresh" content="0; url=/#{sid}">
<script>location.replace("/#{sid}");</script>
</head>
<body><a href="/#{sid}">Continuar a VantTS</a></body>
</html>
"""


cuerpo = "".join([inicio, solucion, funciones, ia, casos, precios, preguntas, nosotros, contacto])
with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(pagina_unica(cuerpo))
print("Generado: index.html (página única, v3)")

for sid in PAGINAS_ANTERIORES:
    with open(os.path.join(OUT_DIR, f"{sid}.html"), "w", encoding="utf-8") as f:
        f.write(redireccion(sid))
    print(f"Generado: {sid}.html -> /#{sid}")
