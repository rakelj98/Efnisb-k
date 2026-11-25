"""Sækir vörumyndir fyrir Efnisbók.

Fyrir hverja vöru í data.json sem hefur vefslóð á vöru (ekki bara flokk) en
enga mynd í img/: sækir síðuna, finnur og:image (eða fyrstu vörumynd), minnkar
hana í 600 px JPEG og vistar sem img/<id>.jpg. Uppfærir svo data.json þannig að
item.img vísi í staðbundnu myndina. Keyrt af GitHub Actions.
"""
import collections, io, json, os, re, sys, time
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data.json')
IMG = os.path.join(ROOT, 'img')
UA = {'User-Agent': 'Mozilla/5.0 (Efnisbok image fetcher; personal design catalogue)'}
LIMIT = int(os.environ.get('LIMIT', '3000'))

# slóðir sem eru flokkasíður, ekki einstakar vörur
CATEGORY = re.compile(r'/(voruflokk|voruflokkar|categories|category|product-category|vorumerki)/|[?&]brand=|/page/\d+/?$')


def is_product(url):
    if not url or CATEGORY.search(url):
        return False
    p = urlparse(url)
    return len([x for x in p.path.split('/') if x]) >= 1 and p.path not in ('', '/')


def find_image(html, base):
    soup = BeautifulSoup(html, 'html.parser')
    for sel in [('meta', {'property': 'og:image'}), ('meta', {'name': 'og:image'}),
                ('meta', {'name': 'twitter:image'}), ('link', {'rel': 'image_src'})]:
        t = soup.find(*sel)
        if t:
            u = t.get('content') or t.get('href')
            if u and not re.search(r'logo|placeholder', u, re.I):
                return urljoin(base, u)
    for img in soup.select('.woocommerce-product-gallery img, .product img, .gallery img, main img'):
        u = img.get('data-large_image') or img.get('data-src') or img.get('src')
        if u and not re.search(r'logo|icon|placeholder|\.svg', u, re.I):
            return urljoin(base, u)
    return None


def save_image(url, path):
    r = requests.get(url, headers=UA, timeout=30)
    r.raise_for_status()
    im = Image.open(io.BytesIO(r.content))
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
        bg = Image.new('RGB', im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert('RGB')
    im.thumbnail((600, 600))
    im.save(path, 'JPEG', quality=82, optimize=True)


def main():
    os.makedirs(IMG, exist_ok=True)
    d = json.load(open(DATA, encoding='utf-8'))
    done = tried = 0
    # slóð sem margar vörur deila er flokkasíða: mynd þaðan á ekki við eina vöru
    shared = {u for u, n in collections.Counter(i.get('url') for i in d['items']).items() if n > 1}
    for it in d['items']:
        local = f"img/{it['id']}.jpg"
        if os.path.exists(os.path.join(ROOT, local)):
            it['img'] = local
            continue
        src = it.get('img') if (it.get('img') or '').startswith('https://') else None
        if not src and (it.get('url') in shared or not is_product(it.get('url'))):
            continue
        if tried >= LIMIT:
            break
        tried += 1
        try:
            if not src:
                r = requests.get(it['url'], headers=UA, timeout=30)
                r.raise_for_status()
                src = find_image(r.text, it['url'])
            if not src:
                print('engin mynd:', it['n'])
                continue
            save_image(src, os.path.join(ROOT, local))
            it['img'] = local
            done += 1
            print('ok:', it['n'])
        except Exception as e:
            print('villa:', it['n'], '-', e)
        time.sleep(0.6)
    # sama mynd á mörgum vörum frá sama seljanda = "mynd vantar"-merki, ekki vörumynd
    import hashlib
    groups = collections.defaultdict(list)
    for it in d['items']:
        p = os.path.join(ROOT, it.get('img') or '')
        if (it.get('img') or '').startswith('img/') and os.path.exists(p):
            groups[(it['c'], hashlib.md5(open(p, 'rb').read()).hexdigest())].append(it)
    for v in groups.values():
        if len(v) >= 8:
            for it in v:
                os.remove(os.path.join(ROOT, it['img'])); it.pop('img')
            print('fjarlægði sameiginlega mynd af', len(v), 'vörum')
    json.dump(d, open(DATA, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    have = sum(1 for i in d['items'] if (i.get('img') or '').startswith('img/'))
    print(f'Sótti {done} nýjar myndir ({tried} reyndar). Samtals með mynd: {have}/{len(d["items"])}')


if __name__ == '__main__':
    sys.exit(main())
