#!/usr/bin/env python3
"""
Genera las 6 páginas del sitio de VantTS (v2 — diseño profesional/minimalista)
a partir de una plantilla común: topbar + menú lateral desplegable + encabezado
de página + franja verde inferior.
"""
import os

OUT_DIR = os.environ.get("VANTTS_SITE_OUT", os.path.dirname(os.path.abspath(__file__)))

NAV = [
    ("index.html", "Inicio"),
    ("solucion.html", "Solución"),
    ("precios.html", "Precios"),
    ("casos.html", "Casos"),
    ("nosotros.html", "Nosotros"),
    ("contacto.html", "Contacto"),
]

WHATSAPP = "https://wa.me/523312506541?text=Hola%2C%20vi%20la%20p%C3%A1gina%20de%20VantTS%20y%20quiero%20saber%20m%C3%A1s"

MOTIVO_V = """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <g fill="none" stroke="#1F4E3D" stroke-width="26" stroke-linecap="round" stroke-linejoin="round">
    <path d="M42 55 L100 150 L158 55"/>
  </g>
</svg>"""

ICON_USERS = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="3.2"/><path d="M5 20c0-3.9 3.1-7 7-7s7 3.1 7 7"/></svg>"""
ICON_CHART = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V10"/><path d="M12 20V4"/><path d="M20 20v-7"/></svg>"""
ICON_COIN = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5v9M9.3 9.6c0-1.1 1.1-2 2.7-2s2.7.7 2.7 1.8c0 2.4-5.4 1.1-5.4 3.4 0 1.1 1.2 1.8 2.7 1.8s2.7-.9 2.7-2"/></svg>"""


def sidebar_nav_html(current_file):
    links = []
    for fname, label in NAV:
        cls = ' class="activa"' if fname == current_file else ""
        links.append(f'      <a href="{fname}"{cls}>{label}</a>')
    return "\n".join(links)


def page(current_file, title, description, pagehead_html, body_html, lg_head=False):
    head_class = "pagehead pagehead-lg" if lg_head else "pagehead"
    return f"""<!doctype html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · VantTS</title>
<meta name="description" content="{description}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>

<div class="hover-zone" aria-hidden="true"></div>
<div class="sidebar-handle" id="sidebarHandle" aria-label="Abrir menú" role="button" tabindex="0">
  <span></span><span></span><span></span>
</div>

<aside class="sidebar" id="sidebar">
  <div class="sidebar-logo"><img src="assets/logo_wordmark_fondo_oscuro.svg" alt="VantTS"></div>
  <nav>
{sidebar_nav_html(current_file)}
  </nav>
  <div class="sidebar-cta">
    <a href="{WHATSAPP}" target="_blank" rel="noopener">Escríbeme por WhatsApp</a>
  </div>
</aside>

<header class="topbar">
  <a href="index.html"><img class="wordmark" src="assets/logo_wordmark.svg" alt="VantTS"></a>
</header>

<main>
  <section class="{head_class}">
    <div class="motivo-v" aria-hidden="true">{MOTIVO_V}</div>
    <div class="wrap">
{pagehead_html}
    </div>
  </section>
{body_html}
</main>

<footer class="franja-verde" aria-hidden="true"></footer>

<script src="assets/script.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# INICIO
# ---------------------------------------------------------------------------
inicio_head = f"""
      <div class="eyebrow">Software de gestión + IA para negocios</div>
      <h1>Cuánto gana tu negocio,<br>sin adivinar.</h1>
      <p class="lead">VantTS te ayuda a llevar el registro de tus clientes, tus ventas y tu ganancia real — empezando con salones y barberías en Guadalajara.</p>
      <div class="cta-row">
        <a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Escríbeme por WhatsApp</a>
        <a class="btn-outline" href="solucion.html">Ver qué resolvemos</a>
      </div>
"""

inicio_body = f"""
  <section class="seccion">
    <div class="wrap-wide">
      <div class="tarjetas">
        <div class="tarjeta">
          <div class="icono">{ICON_USERS}</div>
          <h3>Registro de clientes</h3>
          <p>Quién te visita y qué te compra, sin plantillas complicadas.</p>
        </div>
        <div class="tarjeta">
          <div class="icono">{ICON_CHART}</div>
          <h3>Historial de ventas</h3>
          <p>Tu información ordenada, sin buscar en cuadernos o WhatsApp.</p>
        </div>
        <div class="tarjeta">
          <div class="icono">{ICON_COIN}</div>
          <h3>Ganancia real</h3>
          <p>No solo cuánto entra — cuánto te queda de verdad cada mes.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="seccion alt">
    <div class="wrap">
      <h2>Estamos empezando por el sector belleza en Guadalajara</h2>
      <p>VantTS está construyéndose junto con nuestros primeros negocios piloto — hoy, una barbería con más de dos años operando. Preferimos validar bien con los primeros negocios antes de crecer.</p>
      <a class="btn-outline" href="solucion.html">Ver qué resolvemos</a>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# SOLUCIÓN
# ---------------------------------------------------------------------------
solucion_head = """
      <div class="eyebrow">Solución</div>
      <h1>Lo que resolvemos</h1>
      <p class="lead">Los negocios de belleza y cuidado personal suelen operar sin un registro claro de clientes, ventas o gastos — no por descuido, sino porque nunca tuvieron una herramienta pensada para ellos.</p>
"""

solucion_body = """
  <section class="seccion">
    <div class="wrap">
      <div class="ps-lista">
        <div class="ps-item">
          <div class="problema">No tienes un registro de tus clientes</div>
          <p class="solucion">VantTS te ayuda a llevar el registro de <strong>quién te visita y qué te compra</strong>, sin plantillas ni configuraciones complicadas.</p>
        </div>
        <div class="ps-item">
          <div class="problema">No sabes cuánto vendiste el mes pasado</div>
          <p class="solucion">Ves tu <strong>historial de ventas ordenado</strong>, en un solo lugar, sin buscar en cuadernos o conversaciones de WhatsApp.</p>
        </div>
        <div class="ps-item">
          <div class="problema">No sabes si de verdad estás ganando</div>
          <p class="solucion">VantTS te muestra tu <strong>ganancia real</strong>, no solo cuánto entra, para decidir con información y no con la sensación del día.</p>
        </div>
        <div class="ps-item">
          <div class="problema">Se te acaba el inventario sin avisar</div>
          <p class="solucion"><strong>Próximamente:</strong> alertas para que sepas cuándo se te está agotando algo, antes de que sea un problema.</p>
        </div>
      </div>
      <p class="nota">Estamos construyendo esto por etapas — hoy el enfoque es que entiendas tu negocio con claridad; las alertas y automatizaciones llegan después.</p>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# PRECIOS
# ---------------------------------------------------------------------------
precios_head = f"""
      <div class="eyebrow">Precios</div>
      <h1>Empieza gratis.<br>Paga cuando veas el valor.</h1>
      <p class="lead">Tres planes claros, con IVA incluido y sin letras chiquitas. Hoy están pensados para barberías y salones; si tu negocio es de otro giro, te cotizamos según lo que de verdad necesites.</p>
      <div class="cta-row">
        <a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Escríbeme por WhatsApp</a>
      </div>
"""

def plan_card(nombre, precio, subtitulo, items, destacado=False):
    cls = "plan destacado" if destacado else "plan"
    etiqueta = '<div class="plan-etiqueta">Recomendado</div>' if destacado else ""
    lis = "\n".join(f"            <li>{i}</li>" for i in items)
    return f"""
        <div class="{cls}">
          {etiqueta}
          <h3>{nombre}</h3>
          <div class="plan-precio">{precio}<span>/mes</span></div>
          <p class="plan-sub">{subtitulo}</p>
          <ul>
{lis}
          </ul>
        </div>"""

precios_body = f"""
  <section class="seccion">
    <div class="wrap-wide">
      <div class="planes">
{plan_card("Gratis", "$0", "Para empezar a ordenar tu negocio sin riesgo.", [
    "Agenda: tú capturas tus citas",
    "Reserva en línea que reconoce a tu cliente",
    "Clientes con historial, aunque solo te den su apodo",
    "Catálogo de servicios y precios",
    "Una cuenta de administrador",
])}
{plan_card("Básico", "$249", "Para saber cuánto ganas de verdad.", [
    "Todo lo de Gratis",
    "Las reservas en línea se acomodan solas en tu agenda",
    "Garantía opcional para asegurar cada reserva",
    "Registro de ventas y gastos",
    "Métricas y punto de equilibrio",
    "Metas y estrategia de marketing",
    "Cuentas para tus colaboradores: +$100/mes c/u",
], destacado=True)}
{plan_card("Pro", "$599", "Para hacer crecer tu negocio y a tus clientes fieles.", [
    "Todo lo de Básico",
    "Fidelidad: puntos y niveles por visitas",
    "Membresías VIP de paga para tus clientes",
    "Calendario de contenido para redes",
    "Panel de IA con 500 créditos al mes",
    "Solicitudes de factura electrónica (timbrado próximamente)",
    "Cuentas para tus colaboradores: +$100/mes c/u",
])}
      </div>
      <p class="nota">Precios en pesos mexicanos, con IVA incluido. Vigentes para barberías y salones.</p>
    </div>
  </section>

  <section class="seccion alt">
    <div class="wrap">
      <h2>Preguntas rápidas</h2>
      <div class="faq">
        <h3>¿Los precios incluyen IVA?</h3>
        <p>Sí. El precio que ves es el que pagas.</p>
        <h3>¿Y si con el plan Gratis me basta?</h3>
        <p>Te quedas en Gratis, sin presión. Preferimos que pagues cuando de verdad veas el valor.</p>
        <h3>Mi negocio no es barbería ni salón, ¿me sirve?</h3>
        <p>Vamos giro por giro y solo ofrecemos lo que ya probamos. Escríbenos y te decimos con honestidad si hoy VantTS le sirve a tu negocio.</p>
      </div>
      <a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Escríbeme por WhatsApp</a>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# CASOS
# ---------------------------------------------------------------------------
casos_head = f"""
      <div class="eyebrow">Casos</div>
      <h1>Estamos construyendo nuestro primer caso</h1>
      <p class="lead">Hoy trabajamos con nuestro primer negocio piloto: una barbería en Guadalajara con más de dos años operando. Estamos validando resultados reales junto con ellos.</p>
      <div class="cta-row">
        <a class="btn-outline" href="{WHATSAPP}" target="_blank" rel="noopener">¿Quieres ser de los primeros en probarlo?</a>
      </div>
"""

casos_body = """
  <section class="seccion">
    <div class="wrap">
      <p>En cuanto tengamos números concretos que mostrar, los vas a encontrar aquí — preferimos enseñar resultados reales, no promesas.</p>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# NOSOTROS
# ---------------------------------------------------------------------------
nosotros_head = """
      <div class="eyebrow">Nosotros</div>
      <h1>Por qué existe VantTS</h1>
      <p class="lead">VantTS nace en Guadalajara con una idea simple: los pequeños negocios de servicios merecen herramientas de gestión pensadas para ellos, no versiones reducidas de software para empresas grandes.</p>
"""

nosotros_body = """
  <section class="seccion">
    <div class="wrap">
      <p>Detrás de VantTS está Luis P. Reyes, construyendo la empresa desde cero y aprendiendo en el camino, con apoyo de inteligencia artificial para desarrollar el producto.</p>
      <p>Nuestra misión es ayudar a los pequeños negocios de México a digitalizar su operación y entender su rentabilidad real — empezando por barberías y estéticas en Guadalajara, y creciendo giro por giro.</p>
      <p>Todavía estamos en una etapa temprana: validando con nuestros primeros negocios piloto antes de crecer. Preferimos construir bien antes que construir rápido.</p>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# CONTACTO
# ---------------------------------------------------------------------------
contacto_head = """
      <div class="eyebrow">Contacto</div>
      <h1>Hablemos</h1>
      <p class="lead">La forma más rápida de contactarnos es por WhatsApp.</p>
"""

contacto_body = f"""
  <section class="seccion">
    <div class="wrap">
      <ul class="contacto-lista">
        <li><span class="etiqueta">WhatsApp</span><a href="{WHATSAPP}" target="_blank" rel="noopener">33 1250 6541</a></li>
        <li><span class="etiqueta">Correo</span><a href="mailto:direccion@vantts.com.mx">direccion@vantts.com.mx</a></li>
        <li><span class="etiqueta">Ubicación</span>Guadalajara, México</li>
      </ul>
      <a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Escríbeme por WhatsApp</a>
    </div>
  </section>
"""

pages = [
    ("index.html", "Inicio", "Software de gestión + IA para negocios. Empezando por barberías y estéticas en Guadalajara.", inicio_head, inicio_body, True),
    ("solucion.html", "Solución", "Lo que VantTS resuelve para negocios de belleza y cuidado personal.", solucion_head, solucion_body, False),
    ("precios.html", "Precios", "Planes de VantTS: Gratis, Básico $249 y Pro $599 al mes, con IVA incluido.", precios_head, precios_body, False),
    ("casos.html", "Casos", "El primer caso piloto de VantTS: una barbería en Guadalajara.", casos_head, casos_body, False),
    ("nosotros.html", "Nosotros", "Por qué existe VantTS y quién está detrás.", nosotros_head, nosotros_body, False),
    ("contacto.html", "Contacto", "Escríbenos por WhatsApp o correo.", contacto_head, contacto_body, False),
]

for fname, title, desc, head, body, lg in pages:
    html = page(fname, title, desc, head, body, lg_head=lg)
    with open(os.path.join(OUT_DIR, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("Generado:", fname)
