# Sitio web de VantTS

Software de gestión + IA para negocios — vantts.com.mx

- `build_site.py` genera dos páginas: `index.html` (inicio de VantTS: servicios a la medida, cómo trabajamos, productos, cómo cobramos) y `barber/index.html` (todo lo de VantTS Barber: funciones, IA, precios y preguntas). También genera las redirecciones de las direcciones anteriores (`precios.html`, `solucion.html`, ...).
- Para cambiar contenido, edita `build_site.py` y corre `python build_site.py` en esta carpeta; no edites los HTML a mano.
- Estilos en `assets/style.css` y `assets/motion.css`; menú y pestañas en `assets/script.js`; logo y favicon en `assets/`.
- Publicado en Vercel (proyecto `vantts-sitio`): cada `git push` a `main` se publica solo.
