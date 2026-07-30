#!/usr/bin/env python3
"""Auditoría del entregable YA maquetado. Corre lo que en CF1 hubo que comprobar a mano una y otra
vez, y cada comprobación existe porque algo se colcó por ahí:

  1. ASSETS QUE NO EXISTEN  -> un `@/assets/...` roto deja la vista entera en gris (overlay de Vite)
  2. VISTAS EN GRIS         -> mide el gris oscuro de cada ruta; >0.3 = la vista está rota
  3. AOS SIN ANIMAR        -> con el viewport cubriendo la página, 0 elementos `[data-aos]` sin
                              `aos-animate`; si sale alguno, ese bloque no se ve nunca
  4. DESBORDE EN MÓVIL      -> por CDP, ningún elemento con `right` mayor que el `clientWidth`
  5. COLORES PROHIBIDOS     -> hex que NO están en el XD (p. ej. los de un remapeo revertido)

Uso:  verificar_maqueta.py [--base URL] [--prohibidos HEX,HEX] [--movil 485]
"""
import glob
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

BASE = 'http://localhost:5173/CF1_63720048/'
RUTAS = ['', 'introduccion', 'curso/tema1', 'curso/tema2', 'curso/tema3', 'curso/tema4',
         'curso/tema5', 'curso/tema6', 'sintesis', 'actividad', 'glosario', 'referencias',
         'creditos']
if '--base' in sys.argv:
    BASE = sys.argv[sys.argv.index('--base') + 1]
PROHIBIDOS = []
if '--prohibidos' in sys.argv:
    PROHIBIDOS = [h.strip().lstrip('#').upper() for h in sys.argv[sys.argv.index('--prohibidos') + 1].split(',')]
ANCHO_MOVIL = int(sys.argv[sys.argv.index('--movil') + 1]) if '--movil' in sys.argv else 485

fallos = []


def paso(titulo):
    print(f'\n=== {titulo}')


def chrome(args):
    return subprocess.run(['google-chrome', '--headless=new', '--disable-gpu', '--no-sandbox',
                           '--hide-scrollbars'] + args, capture_output=True, text=True)


# ---------------------------------------------------------------- 1. assets inexistentes
paso('1. assets referenciados que no existen')
faltan = []
for f in glob.glob('src/views/*.vue') + ['src/config/global.js']:
    txt = open(f).read()
    for ref in set(re.findall(r"@/assets/[\w./-]+", txt)):
        if not os.path.exists('src/' + ref[2:]):
            faltan.append(f'{os.path.basename(f)} -> {ref}')
print('  ' + ('\n  '.join(faltan) if faltan else 'ninguno'))
if faltan:
    fallos.append(f'{len(faltan)} assets inexistentes')

# ---------------------------------------------------------------- 2. vistas en gris
paso('2. vistas rotas (overlay de error de Vite)')
from PIL import Image                                   # noqa: E402
import numpy as np                                      # noqa: E402
Image.MAX_IMAGE_PIXELS = None
tmp = '/tmp/verificar-maqueta'
os.makedirs(tmp, exist_ok=True)
rotas = []
for r in RUTAS:
    png = f'{tmp}/{r.replace("/", "-") or "inicio"}.png'
    chrome(['--virtual-time-budget=9000', '--window-size=1400,1300',
            f'--screenshot={png}', f'{BASE}?noaos#/{r}'])
    a = np.asarray(Image.open(png).convert('RGB')).astype(int)
    g = (((abs(a[:, :, 0] - a[:, :, 1]) < 12) & (abs(a[:, :, 1] - a[:, :, 2]) < 12) & (a[:, :, 0] < 80)).mean())
    if g > 0.3:
        rotas.append(r or 'inicio')
print(f'  {len(RUTAS)} rutas revisadas -> rotas: ' + (', '.join(rotas) if rotas else 'ninguna'))
if rotas:
    fallos.append(f'rutas rotas: {rotas}')

# ---------------------------------------------------------------- 3. AOS
paso('3. elementos [data-aos] que no llegan a animarse')
sin = 0
for r in RUTAS[:10]:
    out = chrome(['--virtual-time-budget=20000', '--window-size=1600,16000', '--dump-dom',
                  f'{BASE}#/{r}']).stdout
    tags = re.findall(r'<[a-zA-Z][^>]*data-aos=[^>]*>', out)
    n = len([t for t in tags if 'aos-animate' not in t])
    if n:
        print(f'  {r or "inicio"}: {n} sin animar')
    sin += n
print('  total sin animar:', sin)
if sin:
    fallos.append(f'{sin} elementos con data-aos que no se ven')

# ---------------------------------------------------------------- 4. desborde en móvil
paso(f'4. desborde horizontal a {ANCHO_MOVIL}px')
try:
    import websocket
    proc = subprocess.Popen(['google-chrome', '--headless=new', '--disable-gpu', '--no-sandbox',
                             '--remote-debugging-port=9399', '--remote-allow-origins=*',
                             f'--window-size={ANCHO_MOVIL},1200', f'{BASE}?noaos#/curso/tema1'],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(7)
    tg = [t for t in json.load(urllib.request.urlopen('http://127.0.0.1:9399/json')) if t['type'] == 'page']
    ws = websocket.create_connection(tg[0]['webSocketDebuggerUrl'], suppress_origin=True, timeout=30)
    i = [0]

    def ev(e):
        i[0] += 1
        ws.send(json.dumps({'id': i[0], 'method': 'Runtime.evaluate',
                            'params': {'expression': e, 'returnByValue': True}}))
        while True:
            m = json.loads(ws.recv())
            if m.get('id') == i[0]:
                return m['result']['result'].get('value')
    res = ev('''(()=>{const w=document.documentElement.clientWidth;const o=[];
    document.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect();const cs=getComputedStyle(e);
      if(r.right>w+2 && cs.overflowX==='visible' && cs.position!=='fixed'
         && !e.closest('.slyder-f__main,.scroll-horizontal,.tabla-a,.accesibilidad,.barra-avance'))
        o.push(e.tagName+'.'+(e.className||'').toString().slice(0,44));});
    return JSON.stringify({w, n:o.length, ej:o.slice(0,5)})})()''')
    d = json.loads(res)
    print(f'  clientWidth={d["w"]}  elementos que se salen: {d["n"]}')
    for x in d['ej']:
        print('   ', x)
    if d['n']:
        fallos.append(f'{d["n"]} elementos se desbordan en móvil')
    ws.close()
    proc.kill()
except Exception as e:                                   # noqa: BLE001
    print('  (no se pudo medir por CDP:', e, ')')

# ---------------------------------------------------------------- 4b. cajones vs pestañas del XD
paso('4b. `.cajon` maquetados vs pestañas de 25x8 del XD')
mapa = f'{RAIZ_DOCS}/mapa-artboards.json' if (RAIZ_DOCS := 'docs') else None
if os.path.exists(mapa):
    filas = json.load(open(mapa))
    for f in filas:
        vista = None
        m = re.match(r'Tema-?(\d)', f['nombre'])
        if m:
            vista = f'src/views/Tema{m.group(1)}.vue'
        if not vista or not os.path.exists(vista):
            continue
        env = dict(os.environ, XD_DX=str(f['dx']), XD_DY=str(f['dy']))
        out = subprocess.run([sys.executable, 'scripts/inventario_xd.py', f['id']],
                             capture_output=True, text=True, env=env).stdout
        sec = out.split('=== 3.')[1].split('=== 4.')[0] if '=== 3.' in out else ''
        n = len([l for l in sec.splitlines() if l.startswith('  (')])
        maq = open(vista).read().count('.cajon.color1')
        estado = 'OK' if n == maq else 'DESCUADRE'
        print(f'  {f["nombre"][:10]:10} XD={n}  maquetados={maq}  {estado}')
        if n != maq:
            fallos.append(f'{f["nombre"]}: {maq} .cajon pero {n} pestañas en el XD')
else:
    print('  (falta docs/mapa-artboards.json: correr preparar_curso.py)')

# ---------------------------------------------------------------- 4c. altos contra el XD
# ⚠️ SIN IMPLEMENTAR DE FORMA FIABLE. Dos intentos y los dos midieron la VENTANA, no el contenido:
#   1) «última fila no blanca» -> el fondo de página es #F3F9FF, no blanco, así que devolvía el alto
#      de la ventana;
#   2) «primera y última fila blanca de la columna central» -> Chrome pinta blanco FUERA del body,
#      así que también devolvía la ventana (render = XD + 5999 en los seis temas, exacto).
# La forma buena es por CDP: `document.querySelector('.container.tarjeta--blanca').getBoundingClientRect().height`
# y comparar con el alto del artboard del `mapa-artboards.json`. Hasta entonces, el alto se mide A
# MANO y la entrada `medir-a-ojo` del diccionario queda como comprobación manual.
paso('4c. altos contra el XD — PENDIENTE (ver el comentario del código)')
print('  medir por CDP el alto de `.container.tarjeta--blanca` contra el alto del artboard')

# ---------------------------------------------------------------- 5. colores prohibidos
if PROHIBIDOS:
    paso('5. colores prohibidos en los assets')
    malos = []
    for f in glob.glob('src/assets/**/*.png', recursive=True):
        a = np.asarray(Image.open(f).convert('RGB'))
        for h in PROHIBIDOS:
            r, g_, b = (int(h[k:k + 2], 16) for k in (0, 2, 4))
            if ((a[:, :, 0] == r) & (a[:, :, 1] == g_) & (a[:, :, 2] == b)).sum() > 300:
                malos.append(f'{f} #{h}')
                break
    print('  ' + ('\n  '.join(malos) if malos else 'ninguno'))
    if malos:
        fallos.append(f'{len(malos)} assets con color prohibido')

print('\n' + ('❌ ' + ' | '.join(fallos) if fallos else '✅ todo en orden'))
sys.exit(1 if fallos else 0)
