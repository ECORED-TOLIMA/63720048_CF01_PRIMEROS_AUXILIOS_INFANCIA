#!/usr/bin/env python3
"""Paso 0 de un entregable NUEVO, automatizado. Hace todo lo determinista de arrancar un curso, que
en CF1 llevó un buen rato a mano:

  1. MAPA artboard -> pantalla -> página -> XD_DX/XD_DY, leído del `manifest` del XD
     (`uxdesign#bounds`: DX = -x, DY = -y). No hay que medir nada ni usar `offsets.py`.
  2. CACHÉ del PDF a 144 dpi, una página por pantalla, en `/tmp/xd-pdf-144dpi/<ENTREGABLE>/pN.png`
     (va POR CURSO: con una común, las correlaciones de otro curso salen sin sentido).
  3. TEXTO de los DOCX (`_DI` y `_AD`) volcado a `docs/`.
  4. INVENTARIO de cada artboard (`inventario_xd.py`) volcado a `docs/inventario-<tema>.txt`:
     colores+radios por par, máscaras con radio, pestañas de 25x8, señal de tarjeta hover y
     degradados no horizontales.

Uso:  preparar_curso.py
"""
import glob
import json
import os
import re
import subprocess
import sys

import config as C

RAIZ = C.ENTREGABLE
DOCS = os.path.join(RAIZ, 'docs')
os.makedirs(DOCS, exist_ok=True)
C.descomprimir()


def mapa():
    m = json.load(open(os.path.join(C.XDDIR, 'manifest')))
    filas = []

    def walk(n):
        for c in n.get('children', []):
            b = c.get('uxdesign#bounds')
            if b and c.get('path', '').startswith('artboard-'):
                filas.append({'nombre': c['name'], 'id': c['path'][9:17],
                              'dx': round(-b['x']), 'dy': round(-b['y']),
                              'w': round(b['width']), 'h': round(b['height'])})
            walk(c)
    walk(m)
    filas.sort(key=lambda f: (round(f['dy'] / 100), -f['dx']))
    for i, f in enumerate(filas, 1):
        f['pag'] = i
    return filas


def main():
    filas = mapa()
    print('=== 1. MAPA artboard -> pantalla -> página -> offsets (del manifest del XD)')
    print(f'{"pág":>4} {"artboard":10} {"nombre":22} {"XD_DX":>7} {"XD_DY":>7}  alto')
    for f in filas:
        print(f'{f["pag"]:>4} {f["id"]:10} {f["nombre"][:22]:22} {f["dx"]:>7} {f["dy"]:>7}  {f["h"]}')
    json.dump(filas, open(f'{DOCS}/mapa-artboards.json', 'w'), indent=1, ensure_ascii=False)
    print(f'  -> {DOCS}/mapa-artboards.json')
    print('  ⚠️ el orden página↔artboard se DEDUCE de las coordenadas: confirmarlo leyendo el h1 '
          'de cada artboard antes de fiarse.')

    print('\n=== 2. caché del PDF a 144 dpi')
    os.makedirs(C.CACHE_PDF, exist_ok=True)
    for f in filas:
        dst = f'{C.CACHE_PDF}/p{f["pag"]}.png'
        if os.path.exists(dst):
            continue
        subprocess.run(['pdftoppm', '-png', '-r', '144', '-f', str(f['pag']), '-l', str(f['pag']),
                        C.PDF, f'{C.CACHE_PDF}/x'], check=True)
        hit = sorted(glob.glob(f'{C.CACHE_PDF}/x-*.png'))
        if hit:
            os.rename(hit[0], dst)
    print(f'  {len(glob.glob(C.CACHE_PDF + "/p*.png"))} páginas en {C.CACHE_PDF}')

    print('\n=== 3. texto de los DOCX')
    for suf in ('_DI.docx', '_AD.docx'):
        try:
            d = C.uno_docx(suf)
        except SystemExit:
            print(f'  (no hay {suf})')
            continue
        dst = f'{DOCS}/{suf[1:3].lower()}.txt'
        out = subprocess.run([sys.executable, f'{C.SCRIPTS}/docx_text.py', d],
                             capture_output=True, text=True).stdout
        open(dst, 'w').write(out)
        print(f'  {os.path.basename(d)} -> {dst} ({len(out.splitlines())} líneas)')

    print('\n=== 4. inventario de cada artboard')
    for f in filas:
        if re.search(r'tablet|m[oó]vil', f['nombre'], re.I):
            continue
        env = dict(os.environ, XD_DX=str(f['dx']), XD_DY=str(f['dy']))
        out = subprocess.run([sys.executable, f'{C.SCRIPTS}/inventario_xd.py', f['id']],
                             capture_output=True, text=True, env=env).stdout
        dst = f'{DOCS}/inventario-{f["nombre"].replace(" ", "-").replace("/", "-")}.txt'
        open(dst, 'w').write(out)
        pest = len(re.findall(r'^  \(', out, re.M))
        hover = 'SÍ' if 'ESTADO HOVER' in out else 'no'
        print(f'  {f["nombre"][:22]:22} -> {os.path.basename(dst):42} pestañas 25x8={pest:2} hover={hover}')

    print('\n=== SIGUIENTE PASO')
    print('  Maquetar pantalla por pantalla con el inventario delante: el color Y el radio de cada')
    print('  bloque salen de la sección 1, las fotos redondeadas de la 2, los `.cajon` de la 3 y las')
    print('  tarjetas hover de la 4. Al cerrar cada tema: verificar_maqueta.py + los dos pushes.')


if __name__ == '__main__':
    main()
