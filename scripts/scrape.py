"""Fer yfir vöruflokkasíður hjá seljendum og safnar hverri vöru: nafn, verð,
vefslóð og mynd. Notar Playwright (alvöru vafra) svo síður sem hlaðast með
JavaScript virki líka. Niðurstaða: scraped.json. Keyrt af GitHub Actions.
"""
import json, os, re, sys, time
from urllib.parse import urljoin, urlparse
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGETS = json.load(open(os.path.join(ROOT, 'scripts', 'targets.json'), encoding='utf-8'))
OUT = os.path.join(ROOT, 'scraped.json')
ONLY = os.environ.get('ONLY', '')          # t.d. "egill,ht" til að keyra bara suma
MAXPAGES = int(os.environ.get('MAXPAGES', '12'))

EXTRACT = r"""
() => {
  const host = location.host.replace(/^www\./,'');
  const abs = u => { try { return new URL(u, location.href).href } catch(e) { return '' } };
  const bad = /logo|icon|sprite|placeholder|loader|spinner|flag|payment|banner|facebook|instagram|\.svg/i;
  const pick = img => {
    let s = img.currentSrc || img.getAttribute('data-src') || img.getAttribute('data-lazy-src') || img.getAttribute('data-original') || img.src || '';
    const ss = img.getAttribute('data-srcset') || img.getAttribute('srcset');
    if (ss) { const parts = ss.split(',').map(x => x.trim().split(/\s+/)); const best = parts.sort((a,b)=>(parseInt(b[1])||0)-(parseInt(a[1])||0))[0]; if (best && best[0]) s = best[0]; }
    return abs(s);
  };
  const isProd = a => {
    const h = a.href || ''; let u; try { u = new URL(h) } catch(e) { return false }
    if (u.host.replace(/^www\./,'') !== host) return false;
    if (u.pathname === location.pathname) return false;
    if (/\/(cart|karfa|checkout|account|login|wishlist|compare|tag|blog|frettir)\b/i.test(u.pathname)) return false;
    if (/[?&](page|p|orderby|sort|filter)/i.test(u.search) && u.pathname === location.pathname) return false;
    return u.pathname.split('/').filter(Boolean).length >= 1;
  };
  const out = new Map();
  for (const img of document.querySelectorAll('img')) {
    const src = pick(img);
    if (!src || bad.test(src) || src.startsWith('data:')) continue;
    const r = img.getBoundingClientRect();
    if (r.width && r.width < 60) continue;
    // finnum "spjald": næsta forföður sem inniheldur hlekk á vöru en bara eina vöru
    let el = img, card = null, link = null;
    for (let i = 0; i < 7 && el && el !== document.body; i++, el = el.parentElement) {
      const as = [...(el.tagName === 'A' ? [el] : []), ...el.querySelectorAll('a[href]')].filter(isProd);
      const hrefs = new Set(as.map(a => a.href.split('#')[0]));
      if (hrefs.size > 1) break;
      if (hrefs.size === 1) { card = el; link = [...hrefs][0]; }
      if (card && /\d[\d.\s]*\s*kr/i.test(el.innerText || '')) { card = el; break; }
    }
    if (!card || !link) continue;
    const txt = (card.innerText || '').replace(/\s+\n/g, '\n').trim();
    const head = card.querySelector('h1,h2,h3,h4,.product-name,.product-title,.woocommerce-loop-product__title,.product-item-link,[class*=title],[class*=name]');
    let name = (head && head.innerText.trim()) || (img.alt || '').trim() || txt.split('\n').find(l => l.length > 3 && !/kr/.test(l)) || '';
    name = name.replace(/\s+/g, ' ').trim();
    if (!name || name.length < 3) continue;
    const prices = [...txt.matchAll(/(\d{1,3}(?:[.\s]\d{3})+|\d{3,7})\s*kr/gi)].map(m => parseInt(m[1].replace(/[.\s]/g, '')));
    const price = prices.length ? Math.min(...prices.filter(p => p > 50)) : null;
    const key = link;
    const prev = out.get(key);
    if (!prev || (r.width > (prev._w || 0))) out.set(key, { n: name, url: link, img: src, p: isFinite(price) ? price : null, _w: r.width });
  }
  // næsta síða
  let next = document.querySelector('a[rel=next], link[rel=next], a.next, .pagination .next a, a.next.page-numbers, li.pages-item-next a');
  if (!next) next = [...document.querySelectorAll('a[href]')].find(a => /^(næsta|next|›|»|>)\s*(síða)?$/i.test((a.innerText || a.getAttribute('aria-label') || '').trim()));
  return { items: [...out.values()].map(({_w, ...x}) => x), next: next ? abs(next.href || next.getAttribute('href')) : null };
}
"""


def scroll(page):
    last = 0
    for _ in range(25):
        page.mouse.wheel(0, 4000)
        page.wait_for_timeout(500)
        h = page.evaluate('document.body.scrollHeight')
        if h == last:
            # reyna "sýna meira" takka
            btn = page.locator('button:has-text("Sýna fleiri"), button:has-text("Sjá fleiri"), button:has-text("Hlaða fleiri"), a:has-text("Sýna fleiri"), button:has-text("Load more")')
            if btn.count():
                try:
                    btn.first.click(timeout=2000); page.wait_for_timeout(1500); continue
                except Exception:
                    pass
            break
        last = h


def main():
    prev = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    res = dict(prev)
    only = set(x for x in ONLY.split(',') if x)
    with sync_playwright() as p:
        br = p.chromium.launch()
        ctx = br.new_context(locale='is-IS', viewport={'width': 1400, 'height': 1000},
                             user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36')
        page = ctx.new_page()
        for t in TARGETS:
            if only and t['c'] not in only:
                continue
            key = f"{t['c']}|{t['k']}|{t['url']}"
            got, url, seen = {}, t['url'], set()
            for n in range(MAXPAGES):
                if not url or url in seen:
                    break
                seen.add(url)
                try:
                    page.goto(url, wait_until='domcontentloaded', timeout=45000)
                    page.wait_for_timeout(2500)
                    for sel in ['button:has-text("Samþykkja")', 'button:has-text("Leyfa allt")', 'button:has-text("Accept")', '#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']:
                        try:
                            if page.locator(sel).count(): page.locator(sel).first.click(timeout=1500); break
                        except Exception: pass
                    scroll(page)
                    r = page.evaluate(EXTRACT)
                except Exception as e:
                    print(f'  villa {url}: {e}'.splitlines()[0]); break
                before = len(got)
                for it in r['items']:
                    got.setdefault(it['url'], it)
                print(f"{t['c']:9} {t['k']:9} síða {n+1}: {len(r['items'])} vörur (+{len(got)-before})  {url}")
                if len(got) == before and n > 0:
                    break
                url = r['next']
            items = list(got.values())
            for it in items:
                it.update(c=t['c'], k=t['k'])
                for f in ('s', 'wall', 'floor', 'u'):
                    if f in t: it[f] = t[f]
            res[key] = items
            print(f"== {t['c']} / {t['k']}: {len(items)} vörur, {sum(1 for i in items if i.get('p'))} með verð")
            time.sleep(1)
        br.close()
    json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('Samtals:', sum(len(v) for v in res.values()))


if __name__ == '__main__':
    sys.exit(main())
