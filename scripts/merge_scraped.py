"""Bætir vörum sem scrape.py sótti (scraped.json) inn í vörulistann."""
import json, os, re, hashlib, urllib.parse
from collections import Counter, defaultdict

PRODUCT_RX = {
 'ofnar': r'ofn', 'hellubord': r'hellub|span|helluborð|induction|keramik', 'hafar': r'h[áa]f|vift|gufugleyp|hood',
 'uppthv': r'upp(þ|th)v|uppvask|dishwasher', 'kaeli': r'k[æa]e?li|[íi]ssk[áa]p|frysti',
 'flisar': r'fl[íi]s|m[óo]sa[íi]k|\d+\s*[x×]\s*\d+', 'parket': r'parket|v[íi]nyl|eik|oak|plank|harð|viðar|ask|hnot',
 'vaskar': r'handlaug(?!art)|vask', 'bt_vask': r'handlaugart|bl[öo]ndunart|handl\.?\s*t', 'bt_sturta': r'sturt',
 'klosett': r'salern|kl[óo]sett|wc|skál|kassi', 'skolhn': r'skolhn|skolspj|(þ|th)r[ýy]sti|hnapp|front', 'bord': r'.', 'eldhus': r'.', 'bad': r'.'}
APPL = ('ofnar', 'hellubord', 'hafar', 'uppthv', 'kaeli')
JUNK = re.compile(r'vöruupplýsing|flokkayfirlit|^(skoða|sjá|bóka|opnunart|um okkur|hafa samband|tilboð|svartur|vefverslun|karfa|innskrá)|gjafabr', re.I)
ACCESS = re.compile(r'gólflist|golflist|\blisti|listar\b|kíttisp|kittisp|spinni|þröskuld|undirlag|parketlím|fitusí|kolasí|mótorsí|microsí|míkró|\bsía|pera\b|ábyrgð|skynjari|pottasett|potta sett|teppan|grill|tengilist|rafmagnsofn|olíuofn|gasofn|hitari|hitablás|bökunarplat|bokunarplat|ofnskúff|skúffa|kveikjar|\bfata\b|límband|rúðuvökv|frostlög|ofnhreins|ofnhansk|ofnvettl|bakki|bakka|plata\b|silicon|kvoð|grunnur|\bdf\d|fúg|hraðsuð|kanna|startsett|rekki|glasar|pizza|miðstöðv|olíufyllt|hitablás|vínkæl|motta|slanga|sturtubark|\bbarki|gúmm|haldari|veggfesting|vegghald|stútur|aukahlut|varahlut|brautir|kolasí|\bsía\b|síur|filter|hreinsi|pönnu|panna|pott(ur|ar)\b|grind|festing|tengistykki|framlenging|lok fyrir|sökkull|hurðarfesting|þéttilist|botnventil|lím\b|kísill|fúga|flísalím|undirlag|lista|rofi|tannbursti|ryksug', re.I)
NOPRICE = {'egill', 'birg', 'vidd', 'granit', 'steinl', 'scav', 'mood', 'hth', 'fri', 'ikea', 'parki', 'alfa'}
OLD_JUNK = set(json.load(open(os.environ['OLDKEYS']))) if os.environ.get('OLDKEYS') else set()
OLD_JUNK = {k for k in OLD_JUNK if any(k.startswith(c + '|') for c in ('alfa', 'byko', 'mood', 'parki', 'ormsson', 'rafland', 'isleifur', 'ikea', 'hth', 'fri', 'rafha', 'sminor', 'vidd'))
            or k.split('|', 2)[2] in {'https://www.bauhaus.is/golf-og-veggir/parket/vidarparket', 'https://www.bauhaus.is/golf-og-veggir/parket/vinylparket', 'https://www.bauhaus.is/eldhus/heimilistaeki/ofnar',
                                       'https://ht.is/heimilistaeki/ofnar.html', 'https://ht.is/heimilistaeki/hellubor.html'}}

TENGI_STURTA = {'sturtuhausar': ('bt_sturta', 'Sturtuhaus / handsturta'), 'handsturtuhausar': ('bt_sturta', 'Sturtuhaus / handsturta'),
                'sturtusett': ('bt_sturta', 'Sturtusett'), 'sturtutaeki-sturta-badherbergi': ('bt_sturta', 'Sturtutæki (á vegg)'),
                'innbyggd-bad-sturtutaeki-sturta': ('bt_sturta', 'Innbyggt sturtusett'), 'handsturtusett': ('bt_sturta', 'Sturtustöng / handsturtusett'),
                'sturtustangir': ('bt_sturta', 'Sturtustöng / handsturtusett'), 'sturtubotnar': ('bad', 'Sturtubotn'), 'utisturta': ('bt_sturta', 'Útisturta')}


def norm(s):
    return set(re.findall(r'[a-z0-9áéíóúýþæöð]{2,}', (s or '').lower())) - {'cm', 'mm', 'og', 'með', 'm', 'fyrir', 'án', 'til'}


def dims(n):
    m = re.search(r'(\d+(?:[.,]\d+)?)\s*[x×X\*]\s*(\d+(?:[.,]\d+)?)', n)
    if not m:
        return None, None
    w, h = float(m.group(1).replace(',', '.')), float(m.group(2).replace(',', '.'))
    if w > 250 or h > 250:  # mm
        w, h = w / 10, h / 10
    return round(w, 1), round(h, 1)


def sub_for(k, n, url):
    l = (n + ' ' + url).lower()
    if k == 'bt_vask':
        return 'Hátt (f. borðhandlaug)' if re.search(r'hátt|hatt|hærri|haerri|xl', l) else ('Innbyggt / úr vegg' if re.search(r'vegg|innbygg', l) else ('Snertifrítt' if 'snerti' in l else 'Á borð / vask'))
    if k == 'bt_sturta':
        if re.search(r'innbygg', l): return 'Innbyggt sturtusett'
        if re.search(r'sturtusett|sturtukerfi', l): return 'Sturtusett'
        if re.search(r'sturtuhaus|handsturt', l): return 'Sturtuhaus / handsturta'
        return 'Sturtutæki (á vegg)'
    if k == 'vaskar':
        if 'undirl' in l: return 'Undirlímd'
        if re.search(r'borðhandl|bordhandl|ofan á|ofan-a', l): return 'Ofan á borð'
        if re.search(r'innrétt|innrett|vaskask|plötu|platu', l): return 'Á innréttingu'
        return 'Vegghengd'
    if k == 'klosett':
        if re.search(r'kassi|grind', l): return 'Innbyggður kassi'
        if 'skolsal' in l: return 'Skolsalerni'
        if re.search(r'gólf|golf|s-lás|p-lás|s-las|p-las', l): return 'Gólfsalerni'
        return 'Vegghengt'
    if k == 'ofnar':
        if 'örbylg' in l or 'orbylg' in l: return 'Combi / örbylgja'
        if 'gufu' in l: return 'Gufuofn'
        if re.search(r'frístand|fristand|eldavél|eldavel', l): return 'Eldavél'
        return 'Veggofn 60 cm'
    if k == 'hellubord':
        if 'vift' in l or 'háf' in l: return 'Span m. innb. viftu'
        if 'gas' in l: return 'Gas'
        if 'keram' in l: return 'Keramik'
        return 'Span'
    if k == 'hafar':
        if 'eyju' in l: return 'Eyjuháfur'
        if re.search(r'innbygg|skáp|skap|gufugleyp', l): return 'Innbyggður'
        if 'borð' in l or 'bord' in l: return 'Borðvifta'
        return 'Veggháfur'
    if k == 'kaeli':
        if re.search(r'k[æa]e?li', l) and 'frysti' in l: return 'Kæli- og frystiskápur'
        if 'frysti' in l: return 'Frystiskápur'
        return 'Kæliskápur'
    if k == 'parket':
        if re.search(r'vínyl|vinyl|spc|lvt', l): return 'Vínylparket'
        if re.search(r'harð|hard|laminat|ac\d', l): return 'Harðparket'
        if re.search(r'fisk|herring|síldarb|chevron', l): return 'Fiskibeinamynstur'
        return 'Viðarparket'
    return ''


def merge(items, add, colour):
    global FINCOL
    import bath; FINCOL = bath.fincol
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scraped.json')
    if not os.path.exists(path):
        return
    raw = json.load(open(path, encoding='utf-8'))
    cat_urls = {k.split('|', 2)[2] for k in raw}
    byurl = {i.get('url'): i for i in items if i.get('url')}
    shared = Counter(i.get('url') for i in items)
    cands = defaultdict(list)  # (c,k) -> placeholders without own product url
    for i in items:
        if shared[i.get('url')] > 1 or not i.get('url'):
            cands[(i['c'], i['k'])].append(i)
    seen, stats, got = set(), Counter(), Counter()
    for key, prods in raw.items():
        if key in OLD_JUNK or re.search(r'ofnar-og-lagnaefni|pizzaofn|grillvorur|midstodvar|hitunarbunadur|/contact|/page/|baeklingar|fylgiefni|um-okkur|wishlist|login|account|/20\d\d/', key):
            continue
        for p in prods:
            url, n, k, c = p['url'].split('#')[0], (p.get('n') or '').strip(), p['k'], p['c']
            if c == 'bauhaus' and k in APPL:
                continue
            if url in seen or url in cat_urls or not n or JUNK.search(n):
                continue
            n = re.sub(r'\s*Vnr:.*$', '', n).strip(' .-')
            if re.match(r'^(sérpöntun|tilboð|nýtt|uppselt|.*afsl[áa]tt.*)$', n, re.I):
                n = url.rstrip('/').split('/')[-1].replace('-', ' ').strip().capitalize()
            if k == 'eldhus' and 'badherbergi' in key:
                k = 'bad'
            if c == 'tengi' and k == 'bad' and '/sturta/' in key:
                seg = url.rstrip('/').split('/')[-2]
                if seg not in TENGI_STURTA:
                    continue
                k, forced = TENGI_STURTA[seg]
            else:
                forced = 'Baðinnrétting' if (k == 'bad' and 'innretting' in key) else None
            if ACCESS.search(n) and k not in ('bord', 'eldhus'):
                continue
            n = re.sub(r'\s*vörumynd$', '', n, flags=re.I).strip()
            if k not in ('bord', 'eldhus', 'bad') and not re.search(PRODUCT_RX[k], n.lower()):
                page = urllib.parse.unquote(key.split('|', 2)[2]).lower()
                other = any(re.search(PRODUCT_RX[o], n.lower()) for o in APPL if o != k)
                food = re.search(r'sult|kaffi|krydd|tannbursti|ryksug|þvottavél(?!.*upp)|þurrkar|sjónvarp|hátalar|ljós|glas|bolli|diskur|hnífa|bók', n.lower())
                if c == 'rafha' or not ((p.get('p') or c in NOPRICE) and re.search(PRODUCT_RX[k], page) and not other and not food):
                    continue
            price = p.get('p') if (p.get('p') or 0) >= 500 and c not in ('vidd',) else None
            if k in ('flisar', 'parket') and p.get('pm2'):
                price, p['u'] = p['pm2'], 'm²'
            elif c == 'husa' and k in ('flisar', 'parket'):
                price = None
            if price is None and c not in NOPRICE:
                continue
            seen.add(url)
            img = p.get('img') if (p.get('img') or '').startswith('https://') else None
            if url in byurl:
                it = byurl[url]
                if img and not it.get('img'): it['img'] = img; stats['mynd á eldri vöru'] += 1
                continue
            # parast við eldri vöru sem hafði bara flokkatengil?
            nt, best, bs = norm(n), None, 0
            for it in cands.get((c, k), []):
                if it.get('_m'): continue
                ot = norm(it['n'])
                if not ot: continue
                sc = len(nt & ot) / len(ot)
                if sc > bs: best, bs = it, sc
            if best and bs >= 0.75:
                best['_m'] = 1; best['url'] = url
                if img: best['img'] = img
                if price and not best.get('p'): best['p'] = price; best['u'] = 'stk'
                stats['parað við eldri vöru'] += 1; got[(c, k)] += 1
                continue
            w, h = dims(n)
            u = 'm²' if (p.get('pm2') or (p.get('u') == 'm²' and c in ('parketis', 'egill', 'birg', 'parki', 'alfa'))) else ('pakki' if re.search(r'm²/?\s*kr|m2/krt|\d,\d+\s*m²|\d,\d+\s*m2', n) else 'stk')
            add(k, n, c, price, u=u, s=forced or sub_for(k, n, url), b=n.split()[0].capitalize() if n else '', url=url, img=img,
                x='Sótt af vef seljanda – staðfestu verð og einingu', w=w if k == 'flisar' else None, h=h if k == 'flisar' else None,
                wall=p.get('wall'), floor=p.get('floor'), wid=int(w) if (k in ('vaskar',) and w) else None, col=FINCOL(n) if k in ('bt_vask','bt_sturta','skolhn') else None)
            stats['nýjar vörur'] += 1; got[(c, k)] += 1
    # fjarlægja gamla staðgengla þar sem nú eru komnar margar alvöru vörur með myndum
    drop = 0
    for (c, k), lst in cands.items():
        if got[(c, k)] >= max(8, 0.8 * len(lst)):
            for it in lst:
                if not it.get('_m') and not it.get('img'):
                    it['_drop'] = 1; drop += 1
    items[:] = [i for i in items if not i.get('_drop')]
    for i in items: i.pop('_m', None)
    print('Samruni:', dict(stats), 'fjarlægðir staðgenglar:', drop)
