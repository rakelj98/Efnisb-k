import json, re

CO = {
 # id: (name, address, web, categories, note)
 'sminor': ('Smith & Norland', 'Nóatún 4, 105 Reykjavík', 'https://www.sminor.is', 'Tæki', 'Siemens, Bosch, NEFF, Gaggenau-umboðið'),
 'rafland': ('Rafland', 'Síðumúli 2–4, 108 Reykjavík', 'https://rafland.is', 'Tæki', 'AEG, Electrolux, Samsung, Siemens, LG. Allt að 5 ára ábyrgð'),
 'ht': ('Heimilistæki', 'Suðurlandsbraut 26, 108 Reykjavík', 'https://ht.is', 'Tæki', 'Whirlpool, Samsung, LG, Electrolux, Siemens, Bosch, Witt'),
 'elko': ('ELKO', 'Lindir, Kópavogi', 'https://elko.is', 'Tæki', 'Electrolux, Bosch, Miele, Samsung, Epoq, Logik'),
 'rafha': ('Rafha', 'Suðurlandsbraut 16, 108 Reykjavík', 'https://rafha.is', 'Tæki · Eldhús', 'Siemens, AEG, Elica, AirForce. Kvik innréttingar'),
 'ormsson': ('Ormsson', 'Lágmúli 8, 108 Reykjavík', 'https://ormsson.is', 'Tæki · Eldhús', 'AEG, Samsung, BORA. HTH innréttingar'),
 'eirvik': ('Eirvík', 'Suðurlandsbraut 20, 108 Reykjavík', 'https://www.eirvik.is', 'Tæki · Eldhús', 'Miele, Liebherr, Smeg. bulthaup, Häcker'),
 'ikea': ('IKEA', 'Kauptún 4, 210 Garðabæ', 'https://www.ikea.is', 'Eldhús · Bað', 'METOD og ENHET eldhús, baðinnréttingar'),
 'byko': ('BYKO', 'Skemmuvegur 2a, 200 Kópavogi', 'https://byko.is', 'Eldhús · Bað · Flísar · Borðplötur', 'JKE innréttingar, Salgar baðinnréttingar, Grohe'),
 'husa': ('Húsasmiðjan', 'Skútuvogur, 104 Reykjavík', 'https://www.husa.is', 'Bað · Parket · Flísar', 'Laufen, Grohe, Damixa, baðinnréttingar'),
 'bauhaus': ('BAUHAUS', 'Lambhagavegur 2–4, 113 Reykjavík', 'https://www.bauhaus.is', 'Bað · Parket · Flísar', 'Duravit, Laufen, V&B, Geberit, Parador, Pergo'),
 'fri': ('Fríform', 'Askalind 3, 201 Kópavogi', 'https://www.friform.is', 'Eldhús · Bað', 'Nettoline innréttingar (DK), BORA, ELBA'),
 'gks': ('GKS Innréttingar', 'Síðumúli 4, 108 Reykjavík', 'https://gks.is', 'Eldhús · Bað · Sérsmíði', 'Nobilia og Leicht, eigið trésmíðaverkstæði'),
 'parki': ('Parki', 'Dalvegur 10–14, Kópavogi', 'https://parki.is', 'Eldhús · Parket · Flísar', 'Schmidt innréttingar, parket, flísar, hurðir'),
 'mood': ('Mood Interiors', 'Síðumúli 28, 108 Reykjavík', 'https://www.moodinteriors.is', 'Parket · Flísar · Borðplötur · Eldhús', 'Eigin parketframleiðsla (Parketverksmiðjan), Sapienstone, Scavolini'),
 'scav': ('Scavolini Store Reykjavík', 'Síðumúli 28, 108 Reykjavík', 'https://www.scavolini.is', 'Eldhús · Bað', 'Ítalskar innréttingar, rekið af Bitter ehf'),
 'hth': ('HTH Innréttingar (Ormsson)', 'Lágmúli 8, 108 Reykjavík', 'https://hth.ormsson.is', 'Eldhús · Bað', 'Dönsk hönnun, afhent samsett, ~6 vikur'),
 'kvik': ('Kvik (Rafha)', 'Suðurlandsbraut 16, 108 Reykjavík', 'https://rafha.is/kvik', 'Eldhús · Bað', 'Danskar innréttingar'),
 'egill': ('Egill Árnason', 'Suðurlandsbraut 20, 108 Reykjavík', 'https://egillarnason.is', 'Flísar · Parket', 'Marazzi, Ragno, Kronos, Pergo, Junckers, Wicanders'),
 'birg': ('Birgisson', 'Ármúli 8, 108 Reykjavík', 'https://birgisson.is', 'Parket · Flísar', 'Kährs, Bjelin, Swiss Krono'),
 'parketis': ('Parket.is', 'Krókháls 4, 110 Reykjavík', 'https://parket.is', 'Parket', 'Harðparket og viðarparket, Quick-Step'),
 'alfa': ('Álfaborg', 'Skútuvogur, 104 Reykjavík', 'https://www.alfaborg.is', 'Flísar · Parket · Bað', 'Porcelanosa, Marazzi, Equipe, Imola'),
 'vidd': ('Vídd', 'Bæjarlind 4, 201 Kópavogi', 'https://vidd.is', 'Flísar', 'Atlas Concorde, Mirage, Marca Corona, CE.SI.'),
 'murb': ('Múrbúðin', 'Klettháls 7, 110 Reykjavík', 'https://murbudin.is', 'Flísar · Parket', 'Hagstæðar flísar, parket og vínyl'),
 'golfval': ('Gólfefnaval', 'Höfðabakki 9b, 110 Reykjavík', 'https://golfefnaval.is', 'Parket · Vínyl · Teppi', 'Tarkett, Polyflor, Moduleo, ter Hürne'),
 'teppa': ('Teppaland', 'Ármúli 18, 108 Reykjavík', '', 'Teppi · Gólfefni', ''),
 'flisab': ('Flísabúðin', 'Stórhöfði 21, 110 Reykjavík', '', 'Flísar', 'Úr fyrirtækjaskrá – staðfestið'),
 'tengi': ('Tengi', 'Smiðjuvegur 76, 200 Kópavogi', 'https://www.tengi.is', 'Bað · Eldhústæki', 'Mora, Vola, Dornbracht, Hansa, Geberit, Laufen'),
 'isleifur': ('Ísleifur Jónsson', 'Draghálsi 14–16, 110 Reykjavík', 'https://www.isleifur.is', 'Bað', 'Duravit, Hansgrohe, Burlington, GSI, TECE'),
 'orgus': ('Orgus', 'Axarhöfði 18, 110 Reykjavík', 'https://www.orgus.is', 'Borðplötur · Blöndunartæki', 'Corian, Tapwell'),
 'iogt': ('Innréttingar & Tæki', 'Síðumúli 16, 108 Reykjavík', '', 'Bað', 'Baðvörur, steinsturtubotnar'),
 'shelg': ('S. Helgason', 'Vesturvör 32b, 200 Kópavogi', 'https://shelgason.is', 'Borðplötur', 'Steinsmiðja síðan 1953'),
 'granit': ('Granítsmiðjan', 'Smiðsbúð 3, 210 Garðabæ', 'https://granitsmidjan.is', 'Borðplötur', 'Kvarts, granít, marmari, kvartsít, travertín, ónyx'),
 'rein': ('REIN steinsmiðja', 'Viðarhöfði 1, 110 Reykjavík', 'https://www.rein.is', 'Borðplötur', 'Kvarts, granít, marmari'),
 'steinl': ('Steinlausnir', 'Hvaleyrarbraut 12, 220 Hafnarfirði', 'https://www.steinlausnir.is', 'Borðplötur', 'Kvartsít, granít, marmari, kvarts'),
 'hqs': ('HQS', '', 'https://hqs.is', 'Borðplötur', 'TechniStone kvarts, uppsetning'),
 'fanno': ('Fanntófell', 'Bíldshöfði 12, Reykjavík', '', 'Borðplötur', 'Harðplast og Rauvisio (upplýsingar frá 2013)'),
 'heggur': ('Heggur', 'Bíldshöfði 18, 110 Reykjavík', 'https://www.heggur.is', 'Sérsmíði', 'Gegnheill viður, spónn, sprautulakk'),
 'smida': ('Smíðaþjónustan', 'Hyrjarhöfði 6, 110 Reykjavík', 'https://www.innretting.is', 'Sérsmíði', 'Fast tilboð, þarf teikningar'),
 'svans': ('Svansverk', 'Bæjarflöt 5–7, 112 Reykjavík', 'https://www.svansverk.is', 'Sérsmíði', 'Hannar og smíðar, sýningarsalur'),
 'treborg': ('Tréborg', 'Eldshöfði 4, 110 Reykjavík', 'https://www.treborg.is', 'Sérsmíði', 'Innréttingar, borðplötur, hurðir'),
 'jh': ('JH Trésmíði', '', 'https://jhtresmidi.is', 'Sérsmíði', 'Síðan 1978'),
 'vidogvid': ('Við og Við', 'Gylfaflöt 3, 112 Reykjavík', '', 'Sérsmíði', ''),
}

COLS = [
 ('Viður / brúnt', r'brown|brún|walnut|hnot|toffee|chestnut|kastan|merbau|mocha'),
 ('Hvítt', r'hvít|hvit|white|bianco|blanco|ivory|cream|krem|polar|snow|everwhite|alabast|offwhite|pearl|perla|perlu|calacatta|carrara|statuario|arctic|artic|lasa|platinum|ice|skall'),
 ('Svart', r'svart|black|nero|noir|antras|anthra|antrac|antraz|dark|midnight|lava|kuroca|basalt|mustang|coal|carbon|deep'),
 ('Grátt', r'grá|grey|gray|gris|grigio|argent|silver|steel|stál|concrete|beton|cement|cenere|pietra|ash|smoke|plaster|flint|urban|palladium|platin|slate|mica'),
 ('Beige / sandur', r'beige|sand|sabbia|arena|crema|cotto|taupe|greige|musk|bone|natural|nude|ficelle|almond|linen|desert|sahara|travert|cashmere|dune|champagne|limestone|caramel|ambra|amber|honig'),
 ('Viður / brúnt', r'eik|oak|hnot|walnut|wood|viður|brún|brown|valn|merbau|toffee|pepper|kastan|chestnut|hlyn|maple|askur|ash |furu|pine|rustik|rustic|beyki|cottage|teak|mocha|bronze|kopar|copper'),
 ('Blátt', r'blá|blue|blu|azz|azur|cielo|fjord|navy|azimut'),
 ('Grænt', r'græn|green|salvia|olive|oliven|moss|teal|turchese'),
 ('Bleikt / rautt', r'pink|bleik|rauð|red|berry|coral|rosa|prugna|viola|terracotta'),
]
def colour(*txt):
    t = ' '.join([x or '' for x in txt]).lower()
    for name, rx in COLS:
        if re.search(rx, t):
            return name
    return 'Annað'

def shape(w, h, name=''):
    if not w or not h: return ''
    a, b = sorted([w, h])
    nl = name.lower()
    if 'mosai' in nl or 'mósaí' in nl or b <= 10: return 'Mósaík / smáflísar'
    if a == b: return 'Ferningur'
    if b / a >= 3: return 'Ræmur / listar'
    return 'Ferhyrnt'

def sizecls(w, h):
    if not w: return ''
    b = max(w, h)
    if b <= 20: return 'Lítil (≤20 cm)'
    if b <= 60: return 'Miðlungs (≤60 cm)'
    if b <= 120: return 'Stór (≤120 cm)'
    return 'Risaflísar (>120 cm)'

items = []
def add(k, n, c, p=None, u='stk', z='', s='', b='', f='', url='', x='', w=None, h=None, col=None, wall=None, floor=None, wid=None, img=None):
    it = {'k': k, 'n': n, 'c': c}
    if img: it['img'] = img
    if s: it['s'] = s
    if b: it['b'] = b
    if p is not None: it['p'] = int(round(p)); it['u'] = u
    if z: it['z'] = z
    if f: it['f'] = f
    if url: it['url'] = url
    if x: it['x'] = x
    it['col'] = col or colour(n, f, z)
    if w and h:
        it['w'] = w; it['h'] = h
        it['sh'] = shape(w, h, n); it['sz'] = sizecls(w, h)
    if wid: it['wid'] = wid
    if wall is not None: it['wall'] = wall
    if floor is not None: it['floor'] = floor
    items.append(it)

def num(s):
    return float(str(s).replace('.', '').replace(',', '.'))

# ---------------- ELDHÚSINNRÉTTINGAR ----------------
jke = [('Nordic Basic',1300256),('Nordic Craft',2341921),('Nordic Cubic',1538874),('Nordic Inline',1288376),('Nordic Modern',2344075),('Nordic Multifront',2049563),('Nordic Nature',2298359),('Nordic One',1255236),('Nordic Silk',1400707),('Nordic Vintage',1538874),('Nordic Woodlands',2298359)]
for n,p in jke:
    add('eldhus', 'JKE '+n, 'byko', p, 'frá', s='Heilt eldhús', b='JKE Design (DK)', x='Án blöndunartækja, borðplötu og heimilistækja. 6–10 vikur.', url='https://byko.is/serlausnir/innrettingar/jke-innrettingar/hvad-gaeti-eldhusid-thitt-kostad', col=colour(n) if n not in ('Nordic Basic','Nordic One','Nordic Inline','Nordic Silk','Nordic Cubic','Nordic Modern','Nordic Multifront') else 'Hvítt')
for n,p in [('Nordic One eyja',919107),('Nordic Multifront eyja',1662786),('Nordic Craft eyja',1987629)]:
    add('eldhus','JKE '+n,'byko',p,'frá',s='Eyja',b='JKE Design (DK)',x='Án borðplötu og tækja.',url='https://byko.is/serlausnir/innrettingar/jke-innrettingar/hvad-gaeti-eldhusid-thitt-kostad',col='Hvítt')
add('eldhus','METOD skápakerfi','ikea',4250,'frá',s='Skápar (stakir)',b='IKEA',f='Spónaplata, framhliðar valdar sér',z='Veggskápur 30×37×80 frá 4.250 kr · hár skápur 60×60×220 18.950 kr',url='https://www.ikea.is/is/products/eldhusinnrettingar/eldhusskapar/allir-eldhusskapar/metod-har-skapur-art-90212564',col='Hvítt',x='Framhliðar, höldur, borðplata og tæki bætast við.')
add('eldhus','ENHET eldhús','ikea',None,s='Heilt eldhús',b='IKEA',f='Einfalt kerfi, 10 ára ábyrgð',url='https://www.ikea.is/products/kitchen-systems/enhet-kitchens',col='Grátt')
for n,f,cl in [('Venezia','22 mm höldulaust, mattlakkað MDF, 10 litir','Hvítt'),('Shaker','18 mm MDF, matt filma, 6 litir','Hvítt'),('Stecca','Gegnheil eik, glært eða brúnt lakk','Viður / brúnt'),('Tirano','19 mm spónaplata, melamín, eik','Viður / brúnt'),('Silva','16 mm spónaplata, melamín, ljós/brún eik','Viður / brúnt'),('Vione','19 mm spónaplata, hvítt matt lakk','Hvítt'),('Capri','18 mm MDF, matt filma, grænt','Grænt'),('Paris','Nettoline lína','Hvítt'),('Nice','Nettoline lína','Hvítt'),('Satin','Nettoline lína','Hvítt'),('Trend','Nettoline lína','Hvítt')]:
    add('eldhus','Nettoline '+n,'fri',None,s='Lína',b='Nettoline (DK)',f=f,url='https://www.friform.is/eldhus',col=cl)
for n,f,cl in [('MUSA','Spónlagðir rimlar · Pepper Oak','Viður / brúnt'),('SAX','Melamín · Fashion Walnut','Viður / brúnt'),('DIESEL OPEN WORKSHOP','Gler · Smoky Glass','Svart'),('MIA','Melamín · Flint Grey','Grátt'),('DELINEA','Melamín · Azimut','Grátt'),('CARATTERE','Mattlakkað · Iron Grey','Grátt'),('LIBERAMENTE','Melamín · Venus Stone','Beige / sandur'),('JEOMETRICA INSIDE','Quercia Toffee','Viður / brúnt')]:
    add('eldhus','Scavolini '+n.title(),'scav',None,s='Lína (til sýnis)',b='Scavolini (IT)',f=f,url='https://www.scavolini.is/eldhus',col=cl)
for n,f,cl in [('Scandinavian Classic','Málaðar framhliðar','Hvítt'),('Art','Málaðar framhliðar','Hvítt'),('Tendens','Málaðar framhliðar','Hvítt'),('Plain White','Málaðar framhliðar','Hvítt'),('Nova','Harðklæðning','Hvítt'),('Trend White Oak','Melamín með gegnheilum kanti','Viður / brúnt'),('Fenix','Fenix harðklæðning, margir litir','Svart'),('Viðarstrimlar','Handvaldir viðarstrimlar','Viður / brúnt')]:
    add('eldhus','HTH '+n,'hth',None,s='Framhlið',b='HTH (DK)',f=f,url='https://hth.ormsson.is/eldhus-hurdir',col=cl,x='Sérsmíðað að rými, afhent samsett ~6 vikur. Teikning 10.000 kr.')
add('eldhus','Kvik eldhús','kvik',1300000,'tilboð frá',s='Heilt eldhús',b='Kvik (DK)',x='Tilboð gildir við kaup frá 1.300.000 kr (til 30.11.26). Oakwood lína 20% afsl.',url='https://rafha.is/kvik',col='Hvítt')
add('eldhus','Kvik Oakwood','kvik',None,s='Lína',b='Kvik (DK)',f='Eik',url='https://rafha.is/kvik',col='Viður / brúnt')
add('eldhus','Nobilia eldhús','gks',None,s='Heilt eldhús',b='Nobilia (DE)',f='Kemur samsett, mikið úrval framhliða, N-lína höldulaus',url='https://gks.is/innrettingar/eldhus/',col='Hvítt')
add('eldhus','Leicht eldhús','gks',None,s='Heilt eldhús',b='Leicht (DE)',f='Þýskar gæðainnréttingar, koma samsettar',url='https://gks.is/innrettingar/eldhus/',col='Grátt')
add('eldhus','Schmidt eldhús','parki',None,s='Heilt eldhús',b='Schmidt (FR)',f='Eldhús, bað og fataskápar',url='https://parki.is/',col='Hvítt')
add('eldhus','bulthaup b3','eirvik',None,s='Heilt eldhús',b='bulthaup (DE)',f='Lúxus',url='https://bulthaup.com/en/partner/reykjavik/bulthaup-reykjavik/',col='Grátt')
add('eldhus','bulthaup b Solitaire','eirvik',None,s='Heilt eldhús',b='bulthaup (DE)',f='Lúxus, frístandandi einingar',url='https://bulthaup.com/en/partner/reykjavik/bulthaup-reykjavik/',col='Viður / brúnt')
add('eldhus','Häcker eldhús','eirvik',None,s='Heilt eldhús',b='Häcker (DE)',url='https://www.eirvik.is/verslun/innrettingar/',col='Hvítt')
add('eldhus','Eirvík innréttingar','eirvik',None,s='Heilt eldhús',b='Eirvík',f='Íslensk hönnun, þýsk framleiðsla, rakavarðar',url='https://www.eirvik.is/verslun/innrettingar/',col='Hvítt')
for cid,f in [('heggur','Gegnheill viður, spónn eða sprautulakk'),('smida','Fast tilboð, þarf teikningar hönnuðar'),('svans','Hannar og smíðar, framhliðar og borðplötur'),('treborg','Innréttingar, borðplötur, sólbekkir'),('gks','Stórt verkstæði, þarf teikningar arkitekts'),('jh','Eldhús, bað, fataskápar, heildarlausn'),('vidogvid','Innréttingar og trésmíði')]:
    add('eldhus','Sérsmíðað eldhús – '+CO[cid][0],cid,None,s='Sérsmíði',f=f,url=CO[cid][2],col='Annað')

# ---------------- BORÐPLÖTUR ----------------
sap = ['White Calacatta','Arabescato','Bright Onyx','Crema Avorio','Crema Neve','Taj Mahal','Pietra Grey','Calacatta Aureo 4D','Calacatta Statuario 4D','Calacatta Macchia Vecchia','Black Diamond','Urban Argento','Palladium Grey','Platinum White','Piasentina','Bianco Lasa','Fior di Bosco','Grand Antique 4D','Kuroca 4D','Quarzite Vals','Silver Wave 4D','Jatoba Brown 4D','Fior di Viola 4D']
for n in sap:
    add('bord','Sapienstone '+n,'mood',None,s='Keramik (sintered)',b='SapienStone (IT)',f='Postulínsplata, 12 mm',z='320 × 160 cm',url='https://moodinteriors.is/categories/Sapienstone',x='Einnig á veggi, gólf og vaska.')
for n,cl in [('Bianco White','Hvítt'),('Bianco Diamond / Nova','Hvítt'),('Bianco Madreperola','Hvítt'),('Calacatta Chakra','Hvítt'),('Noble Carrara','Hvítt')]:
    add('bord','Kvartssteinn '+n,'granit',None,s='Kvarts',f='~95% steinn + epoxý',url='https://granitsmidjan.is/bordplotur/kvartsteinn/',col=cl,x='Mæling til uppsetningar.')
for n in ['Granít','Marmari','Kvartsít','Travertín','Ónyx']:
    add('bord',n+' (sérsmíði)','granit',None,s='Náttúrusteinn',url='https://granitsmidjan.is/bordplotur/',col={'Granít':'Svart','Marmari':'Hvítt','Kvartsít':'Hvítt','Travertín':'Beige / sandur','Ónyx':'Beige / sandur'}[n])
for n,s_ in [('Nero Assoluto','Granít'),('Via Lattea','Granít'),('Steel Grey','Granít'),('Nero Angola','Granít'),('Makalu','Granít'),('Dark Arabescato','Granít'),('Cristallo del Mare','Kvartsít'),('Silver Roots','Marmari')]:
    add('bord',n,'steinl',None,s=s_,url='https://www.steinlausnir.is/vorur/bordplotur/',col=colour(n) if n!='Makalu' else 'Grátt')
for n,s_,cl in [('Stone Italiana kvarts','Kvarts','Hvítt'),('Nero Afrika','Granít','Svart'),('Íslenskt blágrýti','Náttúrusteinn','Svart'),('Gabbró','Náttúrusteinn','Svart'),('Ítalskur marmari','Marmari','Hvítt')]:
    add('bord',n,'shelg',None,s=s_,url='https://shelgason.is/',col=cl)
add('bord','Kvarts / granít / marmari','rein',None,s='Kvarts',url='https://www.rein.is',col='Hvítt')
add('bord','TechniStone La Natura Badal Grey','hqs',None,s='Kvarts',b='TechniStone',url='https://hqs.is/tilbod/',col='Grátt',x='Smíða og setja upp, setja líka upp plötur frá öðrum.')
add('bord','Corian','orgus',None,s='Akrýlsteinn',b='Corian',f='Samskeytalaus, vaskar úr sama efni',url='https://www.orgus.is',col='Hvítt')
add('bord','Harðplast með rúnuðum köntum','fanno',None,s='Harðplast',b='Arpa',col='Annað')
add('bord','Rauvisio akrýlsteinn','fanno',None,s='Akrýlsteinn',b='Rehau',col='Hvítt')
add('bord','Harðplast / viðarplötur, sagaðar í verslun','byko',None,s='Harðplast',url='https://byko.is/serlausnir/innrettingar',col='Annað')
add('bord','Borðplötur (Nettoline)','fri',None,s='Harðplast',url='https://www.friform.is/eldhus',col='Annað')

# ---------------- OFNAR ----------------
smi_ov = [('Baksturs- og örbylgjuofn studioLine','SECM 924G1B1S',259900,'45 l','Svartur'),('Baksturs- og gufuofn NEFF N 90 (sýningareintak)','B69FY5CY0',359900,'71 l','Flex Design'),('Veggofn Siemens studioLine','SEHB 974GLB1',229900,'71 l','Svartur'),('Veggofn Siemens iQ300','SEHB 272ABB3',139900,'71 l','Svartur'),('Veggofn Siemens iQ500','SEHB 478G5B7',189900,'71 l','Svartur'),('Baksturs- og örbylgjuofn studioLine','SECM 936GCB1',329900,'45 l','Svartur'),('Sambyggður ofn + örbylgja Siemens','SECM 485AGB1B',199900,'44 l','Svart stál'),('Veggofn Siemens iQ700','SEHB 976GMM1',279900,'71 l','Svartur matt'),('Veggofn Siemens iQ100','SEHB 010FBA1',73900,'66 l','Svartur'),('Veggofn Bosch Serie 2','BCHBF 113BR1S',94900,'66 l','Stál'),('Baksturs- og gufuofn Siemens studioLine','SEHR 976GMB1',369900,'71 l','Svartur'),('Veggofn Siemens iQ700','SEHB 772G2B2S',219900,'71 l','Svartur'),('Sambyggður ofn + örbylgja Siemens iQ700','SECM 724G1B1',269900,'45 l','Svartur'),('Veggofn m. örbylgjum Siemens iQ700','SEHM 976GMB1',389900,'67 l','Svartur'),('Veggofn Siemens iQ100','SEHB 013FBB1',79900,'66 l','Svartur'),('Veggofn Bosch Serie 2','BCHBF 113BV1S',94900,'66 l','Hvítur'),('Veggofn Siemens iQ100','SEHB 010FBV1S',73900,'66 l','Hvítur'),('Veggofn Siemens iQ100','SEHB 010FBR1S',73900,'66 l','Stál'),('Veggofn Siemens iQ100','SEHB 510ABR0S',109900,'71 l','Stál'),('Veggofn Bosch Serie 8','BCHBG 7221B1S',159900,'71 l','Svartur'),('Veggofn NEFF N 70','B59CR72Y0',299900,'71 l','Flex Design'),('Gufuofn Siemens iQ700 (síðasta eintak)','SECS 856GDB7S',239900,'47 l','Svart stál'),('Sambyggður ofn + örbylgja Bosch Serie 8','BCCMG 7241B1',309900,'45 l','Svartur'),('Veggofn Bosch Serie 8','BCHBG 7721B1',179900,'71 l','Svartur')]
for n,m,p,z,c in smi_ov:
    sub = 'Combi / örbylgja' if ('örbylg' in n.lower()) else ('Gufuofn' if 'gufu' in n.lower() else 'Veggofn 60 cm')
    add('ofnar',n,'sminor',p,z=z+' · '+m,s=sub,b=n.split()[1] if 'Siemens' not in n else 'Siemens',f=c,url='https://www.sminor.is/vorur/flokkur/bakstursofnar',col=colour(c),wid=60)
for it in items:
    if it['k']=='ofnar' and it['c']=='sminor':
        it['b'] = 'NEFF' if 'NEFF' in it['n'] else ('Bosch' if 'Bosch' in it['n'] else 'Siemens')
raf = [('Samsung sambyggður ofn og örbylgjuofn','SAM-NQ5B5763DBKU1',104996,'https://rafland.is/samsung-sambyggdur-ofn-og-orbylgjuofn-1.html'),('Electrolux Excellence blástursofn','ELE-XO52CBK',93496,'https://rafland.is/electrolux-excellence-blastursofn-til-innbyggingar-excellence-7.html'),('Electrolux Excellence blástursofn','ELE-XOP0PNK',79996,'https://rafland.is/electrolux-excellence-blastursofn-til-innbyggingar-excellence-5.html'),('Siemens iQ300 blástursofn','SIE-HB272ABB3',111996,'https://rafland.is/siemens-blastursofn-til-innbyggingar-iq300.html'),('Siemens iQ700 extraKlasse blástursofn','SIE-HR776GMB1',207996,'https://rafland.is/siemens-extraklasse-blastursofn-til-innbyggingar-iq700-extraklasse-2.html'),('Electrolux Excellence blástursofn','ELE-XOP3PNK',95996,'https://rafland.is/electrolux-excellence-blastursofn-til-innbyggingar-excellence-2.html'),('AEG 5000 SurroundCook blástursofn','AEG-TU5PB40PK',101996,'https://rafland.is/aeg-blastursofn-til-innbyggingar-rl-5.html'),('AEG 5000 SurroundCook blástursofn','AEG-TU5AB20SCK',67996,'https://rafland.is/aeg-blastursofn-til-innbyggingar-rl-2.html'),('AEG 5000 SurroundCook blástursofn','AEG-TA5PB522PB',111996,'https://rafland.is/aeg-blastursofn-til-innbyggingar-rl.html'),('AEG 8000 MealAssist blástursofn','AEG-TB8SB631AB',195496,'https://rafland.is/aeg-blastursofn-til-innbyggingar-rl-1.html'),('AEG sambyggður ofn og örbylgjuofn','AEG-TK6NK40PB',161496,'https://rafland.is/aeg-sambyggdur-ofn-og-orbylgjuofn-rl.html'),('Samsung blástursofn','SAM-NV7B4430ZABU1',101996,'https://rafland.is/samsung-blastursofn-til-innbyggingar.html'),('Electrolux Excellence Sous Vide blástursofn','ELE-XO93SSK',212496,'https://rafland.is/electrolux-excellence-blastursofn-til-innbyggingar-excellence-6.html'),('Bosch Serie 2 blástursofn','BOS-HBA571BB4',79996,'https://rafland.is/bosch-blastursofn-til-innbyggingar-serie-2.html'),('Siemens iQ100 blástursofn','SIE-HB010FBA1',59996,'https://rafland.is/siemens-blastursofn-til-innbyggingar-iq100.html'),('Electrolux Excellence blástursofn','ELE-XO93PCK',161496,'https://rafland.is/electrolux-excellence-blastursofn-til-innbyggingar-excellence-4.html'),('LG blástursofn','LG-WSED7613S',91996,'https://rafland.is/lg-blastursofn-til-innbyggingar-rl-1.html'),('LG blástursofn','LG-WS7D7632WB',97746,'https://rafland.is/lg-blastursofn-til-innbyggingar-rl.html'),('LG örbylgjuofn m. grilli til innbyggingar','LG-MG7Z2593B',47996,'https://rafland.is/lg-orbylgjuofn-m-grilli-til-innbyggingar-rl.html'),('Siemens iQ500 örbylgjuofn til innbyggingar','SIE-BF525LMB1',51996,'https://rafland.is/siemens-orbylgjuofn-til-innbyggingar-iq500-1.html'),('Electrolux Excellence sambyggður ofn og örbylgjuofn','ELE-XO93MNK',144496,'https://rafland.is/electrolux-excellence-sambyggdur-ofn-og-orbylgjuofn-excellence.html'),('Siemens iQ700 extraKlasse blástursofn','SIE-HB774GLB1',159996,'https://rafland.is/siemens-extraklasse-blastursofn-til-innbyggingar-iq700-extraklasse-1.html'),('Siemens iQ500 extraKlasse blástursofn','SIE-HQ379G6S7',143996,'https://rafland.is/siemens-extraklasse-blastursofn-til-innbyggingar-iq500-extraklasse.html'),('Siemens iQ700 extraKlasse ofn m. örbylgjum','SIE-HM776GNB1F',329995,'https://rafland.is/siemens-blastursofn-til-innbyggingar-5.html'),('Siemens iQ700 örbylgjuofn til innbyggingar','SIE-BF722L1B1',149995,'https://rafland.is/siemens-orbylgjuofn-til-innb-svartur-iq700.html')]
def appsub(n):
    l=n.lower()
    if 'örbylgjuofn til' in l or 'örbylgjuofn m. grill' in l: return 'Örbylgjuofn'
    if 'örbylg' in l: return 'Combi / örbylgja'
    if 'gufu' in l: return 'Gufuofn'
    return 'Veggofn 60 cm'
for n,m,p,url in raf:
    add('ofnar',n,'rafland',p,z=m.split('-',1)[1],s=appsub(n),b=n.split()[0],url=url,col='Svart',wid=60,x='Verð 24.11.26 – mögulega tilboðsverð')
ht = [('Samsung blástursofn','SAM-NV68A1110BSEE',69995),('Electrolux blástursofn','ELE-EO40CBK',84995),('Electrolux blástursofn','ELE-COP905B',149995),('Siemens iQ300 blástursofn','SIE-HB272ABB3',139995),('Siemens iQ700 extraKlasse blástursofn','SIE-HR776GMB1',259995),('Elvita blástursofn','ELV-CUI1700S',44995),('Electrolux blástursofn','ELE-COB402X',99995),('Electrolux Excellence blástursofn','ELE-XO80PNK',99995),('Ecotronic blástursofn svartur','ECO-EO601B',49995),('Siemens iQ100 blástursofn','SIE-HB013FBB1',79995),('Siemens iQ300 extraKlasse blástursofn svartur','SIE-HR372G0S3',179995),('Siemens iQ700 extraKlasse gufuofn svartur','SIE-HS736GDB1',319995),('Beko sambyggður ofn 45 cm','BEK-BBCM17400B',62995),('Siemens iQ500 blástursofn','SIE-HB517GCS1S',139995),('Husqvarna blástursofn','HUS-QCE8600X',249995),('Electrolux Excellence blástursofn','ELE-XO50CBK',119995)]
for n,m,p in ht:
    sub='Combi / örbylgja' if 'sambyggð' in n.lower() else ('Gufuofn' if 'gufu' in n.lower() else 'Veggofn 60 cm')
    add('ofnar',n,'ht',p,z=m.split('-',1)[1],s=sub,b=n.split()[0],url='https://ht.is/heimilistaeki/ofnar.html',col='Hvítt' if m.endswith('V') else 'Svart',wid=60)
add('ofnar','AEG veggofn BKB6P2BO','ormsson',169990,s='Veggofn 60 cm',b='AEG',url='https://ormsson.is',col='Svart',wid=60)
add('ofnar','Siemens iQ500 veggofn 90 cm','rafha',None,s='Veggofn 90 cm',b='Siemens',z='85 l · VB558C0S0',url='https://rafha.is/product/vb558c0s0-ofn-90-cm-siemens',col='Stál / málmur',wid=90)
for n,m,p in [('Siemens iQ700 örbylgjuofn','BF922R1B1',174950),('Siemens StudioLine sambyggður ofn og örbylgjuofn','CM924G1B1S',269950),('Siemens StudioLine sambyggður ofn og örbylgjuofn','CM936GCB1',349950),('Siemens iQ700 gufuofn með örbylgjum','CS936GCB1',349950),('Siemens iQ700 ofn með örbylgjum','CM978GNB1',479950),('Siemens örbylgjuofn','BF425LMB0',89950)]:
    add('ofnar',n,'rafha',p,z=m,s=appsub(n) if 'gufu' not in n else 'Gufuofn',b='Siemens',url='https://rafha.is/product/bf425lmb0-orbylgjuofn-siemens',col='Svart',wid=60)
add('ofnar','Miele ofnar (H-lína)','eirvik',None,s='Veggofn 60 cm',b='Miele',url='https://www.eirvik.is/',col='Svart',wid=60,x='Verð í verslun')
add('ofnar','Gaggenau 200 / 400 lína','sminor',None,s='Veggofn 60 cm',b='Gaggenau',url='https://www.sminor.is/itarefni/gaggenau',col='Svart',wid=60,x='Lúxus, sýningarsalur Nóatúni 4')
add('ofnar','Smeg Victoria / Opera eldavélar 90 cm','eirvik',None,s='Eldavél',b='Smeg',url='https://www.eirvik.is/',col='Svart',wid=90)

# ---------------- HELLUBORÐ ----------------
hth_ = [('AEG spanhelluborð 60cm','AEG-IBB64200CB',69995,60),('Witt spanhelluborð 80cm','WIT-CIP805R',99995,80),('Samsung spanhelluborð 60cm','SAM-NZ64B5046FKU1',74995,60),('Samsung spanhelluborð 60cm','SAM-NZ64M3NM1BBUR',59995,60),('Siemens iQ500 Matt Edition 80cm','SIE-ED81AHWB1E',149995,80),('Siemens iQ500 60cm','SIE-ED61AHSC1E',129995,60),('Electrolux spanhelluborð 60cm','ELE-EH206IC',69995,60),('Witt spanhelluborð 78cm','WIT-WIP78ICW',279995,78),('Witt spanhelluborð 60cm','WIT-WIP60ICW',199995,60),('Witt spanhelluborð 82cm','WIT-WIMP828',169995,82),('Ecotronic spanhelluborð 59cm','WIT-EIP602',29995,59),('Witt spanhelluborð 70cm','WIT-WIP70SQW4',249995,70),('Whirlpool spanhelluborð 77cm','WHI-WFS5077NEIXL',69995,77),('Siemens iQ700 80cm','SIE-EX807NYV6E',249995,80),('Siemens iQ700 80cm','SIE-EX807NVV6E',229995,80),('Electrolux Excellence SaphirMatt 77cm','ELE-XH628BCBS',169995,77),('Electrolux Excellence SaphirMatt 60cm','ELE-XH626BCBS',139995,60),('Witt spanhelluborð 78cm','WIT-WIP78SQW4',299995,78),('Electrolux Excellence 78cm','ELE-XH608BFB',124995,78),('Electrolux Excellence 60cm','ELE-XH606BFB',99995,60),('Witt spanhelluborð 90cm','WIT-WIP90SQW4',349995,90),('Witt spanhelluborð 100×40cm','WIT-WIP100SQ',279995,100),('Siemens iQ500 extraKlasse 71cm','SIE-ED751HSC1E',139995,71),('Siemens iQ700 extraKlasse 81cm','SIE-EX875HYC1M',179995,81),('Siemens iQ100 60cm','SIE-EU611BEB6E',84995,60),('Siemens iQ500 extraKlasse 80cm','SIE-ED851HWB1M',139995,80),('Elvita spanhelluborð 59cm','ELV-CIH4662S',49995,59),('Samsung spanhelluborð 80cm','SAM-NZ84C6058KKU1',189995,80)]
for n,m,p,w in hth_:
    add('hellubord',n,'ht',p,z=f'{w} cm · '+m.split('-',1)[1],s='Spanhelluborð',b=n.split()[0],url='https://ht.is/heimilistaeki/hellubor/spanhellubor.html',col='Svart',wid=w)
for n,m,p,w in [('Siemens iQ700 spanhelluborð með gufugleypi 80cm','EX807NX68E',549995,80),('Siemens iQ300 spanhelluborð með gufugleypi 80cm','ED811BS16E',299995,80),('Siemens iQ500 spanhelluborð með gufugleypi 70cm','ED751HQ26E',299995,70),('Thermex spanhelluborð með gufugleypi 80cm','TXE80',249995,80)]:
    add('hellubord',n,'ht',p,z=f'{w} cm · '+m,s='Helluborð með viftu',b=n.split()[0],url='https://ht.is/brand/siemens/category/54991',col='Svart',wid=w)
for n,p,w in [('AEG spanhelluborð IAE64841FB 60cm',129900,60),('AEG spanhelluborð IKE74441IB 70cm',159990,70),('AEG spanhelluborð IKE95771FB 90cm',289900,90)]:
    add('hellubord',n,'ormsson',p,z=f'{w} cm',s='Spanhelluborð',b='AEG',url='https://ormsson.is',col='Svart',wid=w)
add('hellubord','Siemens iQ700 spanhelluborð EX877NYV6E','rafha',289950,z='81,2 cm · PowerBoost, app',s='Spanhelluborð',b='Siemens',url='https://rafha.is/search2/siemens/?page=2',col='Svart',wid=80)
for cid in ['gks','fri','ormsson']:
    add('hellubord','BORA helluborð með innbyggðri viftu','cid' and cid,None,s='Helluborð með viftu',b='BORA',f='Pure, S Pure, M Pure, X Pure',url=CO[cid][2],col='Svart',wid=80,x='Verð í verslun')

# ---------------- HÁFAR ----------------
for n,m,p,w,c,t in [('Franke eyjuháfur','FSMSF42BKMATT',74990,42,'Svartur','Eyjuháfur'),('Witt eyjuháfur 90cm','WFT916G',79995,90,'Stál','Eyjuháfur'),('Electrolux veggháfur LFT429X','LFT429X',79995,90,'Stál','Veggháfur'),('Witt veggháfur 90cm','WTE90BR',54394,90,'Svartur','Veggháfur'),('Thermex Vertical 360 veggháfur','VERTICAL360BL',44990,60,'Svartur','Veggháfur'),('Ecotronic veggháfur EPH609S','EPH609S',39995,60,'Stál','Veggháfur'),('Ecotronic veggháfur EVL605B','EVL605B',24995,60,'Svartur','Veggháfur'),('Epoq Maxima útdraganlegur','3150741464',59990,80,'Stál','Innbyggður / útdraganlegur'),('Epoq útdraganlegur gufugleypir','3150700872',54990,60,'Stál','Innbyggður / útdraganlegur'),('Electrolux gufugleypir EFU216W','EFU216W',14995,60,'Hvítur','Innbyggður / útdraganlegur'),('Thermex Stripe 20','STRIPE20',14995,60,'Hvítur','Innbyggður / útdraganlegur'),('Ecotronic gufugleypir 53cm í skáp','EBUF530L2',12594,53,'Stál','Innbyggður / útdraganlegur')]:
    add('hafar',n,'elko',p,z=f'{w} cm · {m}',s=t,b=n.split()[0],f=c,url='https://elko.is/heimilistaeki/hafar',col=colour(c),wid=w)
for n,m,p,w,c,t in [('Siemens iQ100 veggháfur','SELC 65KDK60',79900,60,'Svartur','Veggháfur'),('Siemens iQ300 veggháfur','SELC 67KFN60',149900,60,'Svartur','Veggháfur'),('Siemens iQ100 veggháfur 80','SELC 85KDK60',89900,80,'Svartur','Veggháfur'),('Siemens iQ500 hallandi veggháfur','SELC 81KAN65',189900,80,'Svartur','Veggháfur'),('Siemens iQ100 gufugleypir','SELI 64MB521',59900,60,'Stál','Innbyggður / útdraganlegur'),('Bosch Serie 4 gufugleypir','BCDUL 63CC50',39900,60,'Stál','Innbyggður / útdraganlegur'),('Siemens iQ300 gufugleypir','SELI 64MC521',59900,60,'Silfur','Innbyggður / útdraganlegur'),('Bosch Serie 2 gufugleypir','BCDFM 064W54',57900,60,'Stál','Innbyggður / útdraganlegur'),('Gram innbyggður gufugleypir','GREFU 604-90 X',39900,60,'Stál','Innbyggður / útdraganlegur')]:
    add('hafar',n,'sminor',p,z=f'{w} cm · {m}',s=t,b=n.split()[0],f=c,url='https://www.sminor.is/vorur/flokkur/hafar-og-gufugleypar',col=colour(c),wid=w)
for n,m,p,w,c in [('Airforce eyjuháfur svartur','F164B-8',69950,45,'Svartur'),('Airforce Luna eyjuháfur','LUNA-W-45574',74950,45,'Perluhvítur'),('Airforce Luna eyjuháfur','LUNA-B-45575',74950,45,'Matt svartur'),('Faber Beat eyjuháfur','BEAT-BK-MATT',79950,43,'Matt svartur'),('Airforce New Moon eyjuháfur kopar','NewMoon-COPPER',79950,45,'Kopar'),('Elica IKONA Light eyjuháfur','PRF0165082',84950,60,'Matt svartur'),('Elica IKONA Light eyjuháfur','PRF0165083',84950,60,'Hvítur'),('Elica Easy eyjuháfur','PRF0120352A',114950,50,'Svartur'),('Elica Easy eyjuháfur','PRF0119940A',114950,50,'Hvítur'),('AirForce Ballerina eyjuháfur','BALLERINA-W-AF',139950,47,'Hvítur'),('AirForce Ballerina eyjuháfur','BALLERINA-BK-AF',139950,47,'Svartur'),('Elica Hilight loftháfur 100cm','PRF0146246A',359950,100,'Hvítt gler'),('Elica Interstellar eyjuháfur','INTERSTELLAR/BL/F/65',799950,67,'Dökkt gler')]:
    add('hafar',n,'rafha',p,z=f'{w} cm · {m}',s='Loftháfur' if 'loft' in n.lower() else 'Eyjuháfur',b=n.split()[0],f=c,url='https://rafha.is/products/eyjuhafar',col='Viður / brúnt' if 'kopar' in n else colour(c),wid=w)

# ---------------- UPPÞVOTTAVÉLAR ----------------
for n,m,p,w,db in [('Bosch uppþvottavél','SMV6ZCX13E',119990,60,None),('Electrolux 800','E82LA210S',97495,60,None),('Hisense','HFI663AXXL',74995,60,None),('AEG Series 6000','FSB64907Z',89994,60,44),('Electrolux 300','EEA28600L',85995,60,None),('Logik','LIDE60S26E',49995,60,None),('Logik','LID60B24E',57995,60,None),('Siemens iQ300','SN63HX72MS',124995,60,None),('Electrolux 900','E92LX221P',149990,60,37),('Epoq','EDW60A42I25',99990,60,None),('Miele G 7657 SCVi XXL AutoDos','G7657SCVIXXL',319995,60,None),('Logik 45 cm','LID45B26B',59995,45,None),('Bosch','SMV4ECX30E',139995,60,None),('Miele','G5862SCVI',249995,60,None),('Electrolux 700','EEG63420L',109995,60,44),('Epoq 45 cm','EDW45B42I23',74990,45,None),('Asko','DFI8557AMMXXL',169995,60,None),('Bosch','SPV6ZMX17E',179995,45,None),('Bosch','SPV4HMX12E',129995,45,None)]:
    add('uppthv',n if 'uppþv' in n else n+' uppþvottavél','elko',p,z=f'{w} cm · {m}'+(f' · {db} dB' if db else ''),s='Til innbyggingar',b=n.split()[0],url='https://elko.is/heimilistaeki/uppvask/uppthvottavelar-til-innbyggingar',col='Annað',wid=w)
add('uppthv','AEG uppþvottavél FSK84728P','ormsson',199990,s='Til innbyggingar',b='AEG',url='https://ormsson.is',col='Annað',wid=60)
add('uppthv','AEG SmartSelect 6000 NG62IC20SK','rafha',109950,s='Til innbyggingar',b='AEG',f='44 dB, AirDry',url='https://rafha.is/search2/aeg',col='Annað',wid=60)

# ---------------- KÆLISKÁPAR ----------------
for n,m,p,hh,v in [('Samsung kæli- og frystiskápur','BRB80F26ADS0EF',119995,177.5,'190/74 l'),('Epoq kæliskápur','ETR177I24D',109990,178.5,'304 l'),('Electrolux kæli- og frystiskápur','ENS3LE18S',119994,177,''),('Samsung kæliskápur','BRR29723DWWEF',149994,177.5,'289 l'),('Samsung kæli- og frystiskápur','BRB70F26DES0EF',119995,177.5,'193/74 l'),('Electrolux kæliskápur','ERD6DE18S1',107995,177,'310 l'),('Logik kæli- og frystiskápur','LBF177I25E',74995,177.5,'176/76 l'),('Bosch kæli- og frystiskápur','KIV87SFE0',169995,177.2,'200/70 l'),('Epoq kæli- og frystiskápur','EBF177I24D',119990,178.5,'193/74 l'),('Electrolux kæli- og frystiskápur','ENA7NE18S',129995,177.2,'195/62 l'),('Electrolux frystiskápur','LUB3AE88S',89995,87.3,'98 l'),('Epoq frystiskápur','ETF177I24D',109990,178.5,'212 l'),('Hisense kæli- og frystiskápur','RI32F4NSYWE',119994,178,'180/68 l'),('Logik kæliskápur undir borð','LUL82I24E',59995,81.8,'138 l'),('Samsung frystiskápur','BRZ22620EWWEF',199995,177.5,'218 l')]:
    add('kaeli',n,'elko',p,z=f'H {hh} cm · {v} · {m}'.replace(' ·  ·',' ·'),s='Frystiskápur' if n.split()[1].startswith('frysti') else ('Kæli + frysti' if 'frysti' in n else 'Kæliskápur'),b=n.split()[0],url='https://elko.is/voruflokkar/kaelitaeki-til-innbyggingar-311',col='Annað',wid=60)
for n,p,z in [('AEG kæli- og frystiskápur 5000 ColdSense 177cm',119900,'H 177 cm'),('AEG kæli- og frystiskápur 5000 122cm',129990,'H 122 cm'),('AEG innbyggður kæliskápur (bara kælir)',179900,''),('AEG innbyggður kæliskápur',199900,''),('Samsung kæli og frystiskápur 194cm',229990,'H 194 cm'),('Samsung kæli og frystiskápur 194cm, 70 cm breiður',249990,'H 194 · B 70 cm'),('BORA innbyggður kæliskápur',622990,'')]:
    add('kaeli',n,'ormsson',p,z=z,s='Kæli + frysti' if 'frysti' in n else 'Kæliskápur',b=n.split()[0],url='https://ormsson.is/products/stor-heimilistaki/kalitaki/innbyggdir-kaliskapar/',col='Annað',wid=70 if '70 cm' in n else 60)
for n,m,p in [('Siemens iQ100 klæðanlegur kæli- og frystiskápur','SEKI 87VNSE0',169900),('Siemens iQ500 klæðanlegur kæliskápur','SEKI 81RAFE1',199900),('Vínkælir til innbyggingar (21 fl.)','',229900),('Vínkælir 2 hitasvæði (44 fl.)','',339900)]:
    add('kaeli',n,'sminor',p,z=m,s='Vínkælir' if 'Vín' in n else ('Kæli + frysti' if 'frysti' in n else 'Kæliskápur'),b='Siemens' if 'Siemens' in n else '',url='https://www.sminor.is/vorur/flokkur/kaeli-og-frystitaeki',col='Svart' if 'Vín' in n else 'Annað',wid=60)
add('kaeli','Electrolux kæliskápur m. frysti 177cm','rafland',159995,s='Kæli + frysti',b='Electrolux',z='ENA7CE18S1',url='https://rafland.is/brand/electrolux/category/40221',col='Annað',wid=60)
add('kaeli','Liebherr og Miele kæliskápar','eirvik',None,s='Kæliskápur',b='Liebherr / Miele',url='https://www.eirvik.is/',col='Annað',wid=60,x='Verð í verslun')

# ---------------- FLÍSAR (veggur/gólf) ----------------
def sz(s):
    m = re.search(r'(\d+(?:[.,]\d+)?)\s*[x×\*]\s*(\d+(?:[.,]\d+)?)', s)
    if not m: return None, None
    return float(m.group(1).replace(',','.')), float(m.group(2).replace(',','.'))
eg = """Tibur Falda 120x120|n/s|45988
Everwhite 100x100|Cercom|4990
Mystone Berici Beige 60x60|Marazzi|5724
Stream Beige 3D 25x76|Marazzi|3169
Travertino Cross Bianco 120x120|Ragno|27216
Lume Bone Lux 10x10|Marazzi|168
Slow Cotto 60x60|Marazzi|5366
Mystone Berici Beige 75x150|Marazzi|20138
Mystone Berici Beige R10 60x120|Marazzi|12169
Tibur Vena 120x280|Kronos|127700
Gleeze Turchese 10x10|Ragno|159
Everwhite 60x120|Cercom|6384
Evergreige 60x120|Cercom|6384
Incanto Statuario Venato Glossy 60x60|Ragno|12601
Mattone Spakko 7,5x30|Kronos|724
Lume Bone Lux 6x24|Marazzi|183
Lume Caramel Lux 6x24|Marazzi|279
Freistil Sand 60x120|Ragno|6895
Realstone Ceppo Beige 60x60|Ragno|3924
Look Lino Lux 6x24|n/s|215
Look Lino Lux 3D 6x24|n/s|229
Studio Sabbia 60x60|Ragno|2840
Incanto Paonazzetto Glossy 120x278|Ragno|96548
Richmond Musk 60x60|n/s|3563
Richmond Taupe 60x120|n/s|9050
Richmond Musk 60x120|n/s|9050
Block White 30x60|Marazzi|1364
Mitica Gris 120x120|Grespania|13900
Mystone Basalto Pomice 60x120|Marazzi|6424
Dune Antique Nat 60x60|Kronos|6476
Taupe Muro 3D 29x33|Kronos|6960
Stream Ivory 60x60|Marazzi|2108
Lume Cardiff Pink 6x24|Marazzi|224
Domus Arena 60x60|Grespania|2516
Zellige China 10x10|Marazzi|68
Stream Beige 60x60|Marazzi|2108
Lume Musk 6x24|Marazzi|192
Nexos hvítar 30x60|Hitit|649
Plaster Antracite 30x60|Marazzi|1237
Everwhite 60x60|Cercom|2844
Zellige Cielo 10x10|Marazzi|76
Stream Grey 30x60|Marazzi|881
Lume Offwhite 6x24|Marazzi|183
Richmond Ivory 60x120|n/s|9050
Bruges Rett 60x120|Kronos|13990
Naturalia Taupe 60x60|Marazzi|2843
Taupe Carve 80x80|Kronos|14990
Evercream 60x60|Cercom|2844
Stream Ivory 30x60|Marazzi|882
Nuit Antique Heritage 60x60|Kronos|11468
Nuit Antique Heritage 80x80|Kronos|26392
Lux Falda Konfort 60x120|Kronos|19513
Rice Grigio Lux 15x15|Marazzi|297
Lapillo Vena 60x120|Kronos|16133
Nexos Grey Telis Mosaic 30x30|Hitit|1733
Aurum Vena 80x180|Kronos|35925
Tibur Vena 80x180|Kronos|35925
Evergreige 30x60|Cercom|1407
Evercream 30x60|Cercom|1407
Lux Vena 120x280|Kronos|113161
Dune Elegance Nat 60x120|Kronos|20171
Taupe Elegance Nat 60x60|Kronos|8669
Mustang 60x60 heflað|n/s|4990
Opal Mosaico 5x5 30x30|Kronos|4750
Incanto Emperador Glossy 120x120|Ragno|62328
Opal Antique Nat 60x60|Kronos|8475
Naturalia Beige 60x60|Marazzi|4156
Namur Anticato 60x60|Kronos|7728
Lume White 6x24|Marazzi|183
Gent Anticato 60x60|Kronos|5440
Plaster Sand 30x60|Marazzi|1237
Lux Falda 60x60|Kronos|3598
Aurum Vena Mini Baguette 3D 30x120|Kronos|31544
Taupe Elegance Nat 120x120|Kronos|33125
Stream White 30x60|Marazzi|882
Stream White 60x60|Marazzi|2108
Plaster Moss Grey Mosaic 30x30|Marazzi|2464
Rain Grigio Strutturato 60x60|Ragno|2862
Rice Natural Lux 15x15|Marazzi|390
Mitica Arena 60x60|Grespania|2516
Incanto Calacatta Michelangelo Glossy 60x60|Ragno|10640
Plaster Grigio 60x60|Marazzi|2840
Cenere Rett 20x80|Kronos|1933
Hvítar mattar flísar 30x60|n/s|1315
Patch Beige 60x60|Ragno|2144
Junoon Beige 30x260|Apavisa|6840
Stream Grey 60x60|Marazzi|2028
Sandalo Rett 80x80|Kronos|9231
Gent Mariniere 60x120|Kronos|45160
Dune Carved Grip 60x60|Kronos|9208
Corda 80x180|Kronos|27867
Ossimori Avario Extra 20x120|Ragno|4212
Patch Grey 60x60|Ragno|2144
Gent Anticato 20x20|Kronos|435
Calce Spakko 7,5x30|Kronos|483
Ottocento Ambra 20x20|Ragno|759
Plaster Grigio 30x60|Marazzi|1237
Lume Pink 6x24|Marazzi|224
Uni Tech Lux Bianco glans 10x30|Ragno|390
Uni Tech Nero matt 10x30|Ragno|335"""
for line in eg.strip().split('\n'):
    n,mk,p = line.split('|'); p=float(p)
    w,h = sz(n)
    area = w*h/10000
    ppm = p/area
    small = max(w,h) <= 30 or any(k in n for k in ['Lume','Zellige','Gleeze','Spakko','3D','Baguette','Rice','Look Lino','Uni Tech','Mosai'])
    wall = True
    floor = not small
    name = n
    add('flisar', name, 'egill', ppm, 'm²', z=f'{w:g} × {h:g} cm · {p:,.0f} kr/stk'.replace(',', '.'), b='' if mk=='n/s' else mk, f='Glans' if ('Lux' in n or 'Glossy' in n or 'glans' in n) else '', url='https://egillarnason.is/flisar/', w=w, h=h, wall=wall, floor=floor, x='m²-verð reiknað úr stykkjaverði')
bh = [('Dome Ash','60x60','Grátt',None),('Dome Anthracite','60x60','Svart',5395),('Koncept Argent','30x60','Grátt',None),('Koncept Argent','60x60','Grátt',None),('Uyuni hvítar','60x60','Hvítt',None),('Uyuni hvítar','30x60','Hvítt',None),('Beton antracit','60x60','Svart',None),('Hvítar flísar','9.2x36.8','Hvítt',None),('Hannover steel','60x60','Grátt',5495),('Hannover svartar','60x60','Svart',None),('Country Acero','31x62','Grátt',3995),('Koncept mica','30x60','Grátt',None),('Lux Azzurro','60x120','Blátt',None),('Gobi nude','60x60','Beige / sandur',None),('Gobi blu','60x60','Blátt',None),('Start Argent Natural','30x60','Grátt',None),('Start Argent Natural','60x60','Grátt',None),('Start Silver Natural','30x60','Grátt',None),('Start Mud Natural','60x60','Viður / brúnt',None),('Luni Blanco','30x60','Hvítt',None),('Luni Blanco','60x60','Hvítt',None),('Rako matt hvítar veggflísar','19.8x39.8','Hvítt',None),('Ajour teal green','9.2x36.8','Grænt',None),('Lux Berry','60x120','Bleikt / rautt',None),('Lux Almond','60x120','Beige / sandur',None),('Autumn Perla gráar','30x60','Grátt',None),('Autumn Marengo','30x60','Grátt',None),('Sena crema','30x60','Beige / sandur',None),('Quarzo','30x60','Grátt',None),('Quarzo','15x15','Grátt',None),('Quarzo','60x60','Grátt',None),('Antibes Ivory','60x120','Hvítt',None),('Nature Perla','60x60','Hvítt',None),('Nature Gris','60x60','Grátt',None),('Time ficelle','60x60','Beige / sandur',None),('Arkety gráar','59x120','Grátt',None),('Arkety stálgráar','60x60','Grátt',None),('Erding Pearl','60x60','Hvítt',None),('Petra natural','60x60','Beige / sandur',None),('Veggflísar hvítar','15x15','Hvítt',None)]
for n,s_,cl,p in bh:
    w,h = sz(s_)
    add('flisar',n,'bauhaus',p,'m²',z=f'{s_.replace("x"," × ")} cm',url='https://www.bauhaus.is/golf-og-veggir/flisar/veggflisar',col=cl,w=w,h=h,wall=True,floor=('veggfl' not in n.lower() and 'Rako' not in n and 'Ajour' not in n),x='' if p else 'Verð á vef bauhaus.is')
for n,s_,cl,p,wl,fl in [('Mustang náttúrusteinn svart','30x60','Svart',5459,True,True),('Hvítar gloss veggflísar','25x40','Hvítt',3228,True,False),('Valley gráar','45x45','Grátt',3788,True,True),('Quarry hvítar','60x60','Hvítt',4799,True,True),('Pietra Beige','60x60','Beige / sandur',4199,False,True),('Pietra Beige','30x60','Beige / sandur',5199,False,True),('Cementi milligráar','30x60','Grátt',5199,False,True),('Cementi ljós','30x60','Hvítt',4899,False,True),('Cementi ljós','60x60','Hvítt',4699,False,True),('Ceraviva milligráar','60x60','Grátt',4595,False,True),('Midnight Steel matt','60x60','Grátt',5125,False,True),('Delphi hvítar','25x50','Hvítt',3488,True,False),('White-matte veggflísar','20x20','Hvítt',1890,True,False),('Bílskúrsflísar Antrasite','33.3x33.3','Svart',2999,False,True)]:
    w,h=sz(s_)
    add('flisar',n,'murb',p,'m²',z=f'{s_.replace("x"," × ")} cm',url='https://murbudin.is/voruflokkur/flisar-parket-undirlag-ofl/flisar/',col=cl,w=w,h=h,wall=wl,floor=fl)
for n,mk,p,s_,cl in [('Pro Stone Grey','NAXB',8990,'30x60','Grátt'),('Verbier Dark','Porcelanosa',13990,'60x60','Svart'),('Vibe (10 litir, íhvolfar)','Equipe',14480,'6x24.6','Annað'),('The Room','Imola',14990,'60x120','Grátt')]:
    w,h=sz(s_)
    add('flisar',n,'alfa',p,'m²',b=mk,z=f'{s_.replace("x"," × ")} cm (fleiri stærðir)',url='https://www.alfaborg.is/voruflokkar/flisar/pro-stone-grey-30x60',col=cl,w=w,h=h,wall=True,floor=(n!='Vibe (10 litir, íhvolfar)'),x='Listaverð')
add('flisar','Maiolica Prugna veggflísar','parki',7490,'m²',b='Iris',url='https://parki.is/product/maiolica-prugna-veggflisar/',col='Bleikt / rautt',wall=True,floor=False)
add('flisar','Emil Sixty Brick Cenere','husa',7315,'m²',b='Emil',z='5 × 15 cm (tilboð, áður 14.497)',url='https://www.husa.is/golfefni/flisar/',col='Grátt',w=5,h=15,wall=True,floor=False)
add('flisar','Tau Cosmopolita White','husa',8269,'m²',b='Tau',z='60 × 60 cm',url='https://www.husa.is/golfefni/flisar/',col='Hvítt',w=60,h=60,wall=True,floor=True)
for n,mk,s_,cl in [('Boost Natural (Ash, Coal, Coral, Ecru, Kaolin)','Atlas Concorde','60x60','Beige / sandur'),('Nöriven Bands Cream Vein','Mirage','60x120','Beige / sandur'),('Marvel Shine Calacatta Prestigio','Atlas Concorde','120x120','Hvítt'),('Miniature Soda Blu Galassia','Marca Corona','7.5x15','Blátt'),('ReStone (5 litir)','Mirage','60x60','Grátt'),('CE.SI. einlitar','CE.SI.','30x60','Annað'),('Elèrn','Mirage','60x60','Beige / sandur'),('Terrasale','Marca Corona','60x60','Beige / sandur')]:
    w,h=sz(s_)
    add('flisar',n,'vidd',None,b=mk,z=f'{s_.replace("x"," × ")} cm (fleiri stærðir)',url='https://vidd.is/flisar',col=cl,w=w,h=h,wall=True,floor=('Miniature' not in n),x='Verð á vidd.is / í verslun')
for n in ['Sapienstone veggplötur 320 × 160']:
    add('flisar',n,'mood',None,b='SapienStone',z='320 × 160 cm, 12 mm',url='https://moodinteriors.is/categories/Sapienstone',col='Hvítt',w=160,h=320,wall=True,floor=True)
add('flisar','Veggflís hvít 10 × 30','byko',None,b='Vilar Albaro',z='10 × 30 cm, glerjuð',url='https://byko.is/vara/veggflis-10x30cm-169600',col='Hvítt',w=10,h=30,wall=True,floor=False,x='Stykkjaverð á byko.is')
add('flisar','Veggflís hvít 10 × 10 (matt/glans)','byko',None,b='Vilar Albaro',z='10 × 10 cm',url='https://byko.is/vara/veggflis-10-x-10-cm-hvit-313332',col='Hvítt',w=10,h=10,wall=True,floor=False)

# ---------------- PARKET ----------------
def pk(c,n,p,s,url,b='',f='',z='',x=''):
    add('parket',n,c,p,'m²',s=s,b=b,f=f,z=z,url=url,x=x)
for n,p in [('Hobart Oak',2490),('Oak Grey Brown',2490),('Oak Nature Grey',2490),('Oak Nature Yellow',2490),('Lifestyle Ovilo',2490),('Lifestyle Badesi',2490),('Lifestyle Iscala',2490),('Oak Light Beige',2890),('Skyline Chino',2990),('Skyline Sonolta',2990),('Skyline Hayden',2990),('Eik Diadema XXL',3588)]:
    pk('parketis',n,p,'Harðparket','https://parket.is/product-category/hardparket/')
for n,p,b in [('Vatnshelt harðparket Eik Soft Medium',7250,''),('Desert Oak Brushed Dark Brown',8990,''),('Valley Oak Light Beige',8990,''),('Brushed Oak Grey',8795,'Quick-Step'),('Cracked Oak Natural',8795,'Quick-Step')]:
    pk('parketis',n,p,'Vatnshelt harðparket','http://www.parket.is/parket',b=b)
for n,p in [('Eik Cottage 3 stafa',7990),('Eik Super Rustik',10680),('Eik Superrustik breið borð',10680),('Eik Rustic Microfasað',11880),('Eik Rustic Cashmere',13499),('Eik Rustik',14280)]:
    pk('parketis',n,p,'Viðarparket','https://parket.is/product-category/vidarparket/')
pk('parketis','Cinnamon raw oak síldarbein (smellt)',16990,'Síldarbein / chevron','http://www.parket.is/parket',z='58 × 14,5 cm, 14 mm')
eg_p = [('Eik Rustic 1R Matt Lakk',16842,'Baltic Wood','Viðarparket'),('Eik Unique 1R Cream Matt Lakk',16276,'Baltic Wood','Viðarparket'),('Eik Classic 1R Matt Lakk',19900,'Baltic Wood','Viðarparket'),('Eik Classic Raw Supermatt',19900,'Baltic Wood','Viðarparket'),('Eik Earthquake burstuð',13487,'Baltic Wood','Viðarparket'),('Swing Ivory Oak síldarbein',18749,'','Síldarbein / chevron'),('Eik Rustic Cashmere Matt Lakk',20651,'Baltic Wood','Viðarparket'),('Eik Unique Coconut Supermatt',13317,'Baltic Wood','Viðarparket'),('Chevron Oak Markant Matt Lakk',24900,'Holzexport','Síldarbein / chevron'),('Eik Rustik Country Planki XXL',19763,'Wicanders','Viðarparket'),('Eik Cottage Cocon Supermatt',11482,'','Viðarparket'),('Eik Victoria Ivory',20332,'Wicanders','Viðarparket'),('Eik Klassik 3R Cashmere',12490,'Baltic Wood','Viðarparket'),('Eik Rustic gegnheil síldarbein 16×70×450',14283,'','Síldarbein / chevron'),('Oak Rustic XXL óunnið',12334,'Wicanders','Viðarparket'),('Herringbone Oak Markant ómeðhöndlað',15681,'Holzexport','Síldarbein / chevron'),('Chevron Oak Markant ómeðhöndlað',23900,'Holzexport','Síldarbein / chevron'),('Summit Sahara Oak Rustic Light',18400,'','Viðarparket'),('Eik Rustik gegnheil síldarbein 16×70×350',12972,'','Síldarbein / chevron'),('Eik Rustic Victoria Sand',20322,'Wicanders','Viðarparket'),('Eik Hvíttuð Classic Supermatt',19900,'Baltic Wood','Viðarparket'),('Oak Classic Matt Lakk 1R',19900,'Baltic Wood','Viðarparket'),('Kentucky Denvrust dekkri',22639,'Wicanders','Viðarparket'),('Hlynur Club Silk Matt (gegnheill)',26681,'Junckers','Viðarparket'),('Saltholm Natural Herringbone Oak',19900,'Pergo','Síldarbein / chevron'),('Oak Rustik Brown Diamond',21268,'Wicanders','Viðarparket'),('Merbau Elegance semimatt',18778,'Baltic Wood','Viðarparket'),('Eik Unique 3R Matt Lakk',25960,'Baltic Wood','Viðarparket'),('Oak Variation Ultra Matt (gegnheil)',21236,'','Viðarparket'),('Eik Cottage 3R',11867,'','Viðarparket')]
for n,p,b,s in eg_p:
    pk('egill',n,p,s,'https://egillarnason.is/vidarparket/',b=b)
for n,p in [('Oak Beach Town Wide Plank',10249),('Island Oak Plank',9315),('Eik Farmhouse Sensation Plank',9315),('Visby Sand Drift Oak',9315),('Lillehammer Bronze Oak',8990)]:
    pk('egill',n,p,'Vatnshelt harðparket','https://egillarnason.is/verslun/',b='Pergo')
pk('egill','Aspecta Macadamia vínylparket',10613,'Vínyl','https://egillarnason.is/verslun/',b='Aspecta')
for n,p,b,s in [('Oak Cosenza 3 stafa 15 mm',16490,'Kährs','Viðarparket'),('Beyki Hellerup',9990,'','Viðarparket'),('Askur Ceriale',9990,'','Viðarparket'),('Artisan Linen',14490,'','Viðarparket'),('Höja 3.0 XL Oak Misty White Brushed',12390,'Bjelin','Viðarparket'),('Herringbone Sandviken (útsala)',9500,'','Síldarbein / chevron'),('Starby 3.0 XL Oak Bronce Smoked',12390,'Bjelin','Viðarparket'),('Kvarnby 3.0 XL Oak Natural',12390,'Bjelin','Viðarparket'),('Lya 3.0 XXL Oak',13690,'Bjelin','Viðarparket'),('Vejby 3.0 XXL',13690,'Bjelin','Viðarparket'),('Hasslarp 3.0 XL Oak Misty White',12390,'Bjelin','Viðarparket'),('Stehag 3.0 XL Oak Earth Grey',12390,'Bjelin','Viðarparket'),('Advanced Trend Oak Brown AC4 8 mm',2990,'Swiss Krono','Harðparket'),('Zermatt Oak AC4 8 mm',4690,'Swiss Krono','Harðparket'),('Mammut Plus Mountain Oak Sand AC5 10 mm',5590,'Swiss Krono','Harðparket'),('Mammut Everest Oak Beige AC5 12 mm',5890,'Swiss Krono','Harðparket')]:
    pk('birg',n,p,s,'https://birgisson.is/product-category/parket/vidarparket/',b=b)
for n,p,b,s in [('Parador Basic 200 Acacia',2195,'Parador','Harðparket'),('Parador Basic eik hvít',2195,'Parador','Harðparket'),('Parador Basic 400 Natural grey eik',2895,'Parador','Harðparket'),('Parador Classic eik Natural',3595,'Parador','Harðparket'),('Parador Basic 600 Montana',3195,'Parador','Harðparket'),('Logoclic Ambienta Honig Oak 8+2 mm',3995,'Logoclic','Harðparket'),('Logoclic Aquaprotect Nature Oak',3995,'Logoclic','Vatnshelt harðparket'),('Logoclic Altitude Blonde eik 12 mm',4495,'Logoclic','Harðparket'),('Herringbone Firebrand eik 8 mm',3995,'','Síldarbein / chevron'),('MyArt Desperados 12 mm',3595,'Kronoflooring','Harðparket'),('Pergo Visby Coastal Oak 8 mm',6995,'Pergo','Harðparket'),('BerryAlloc AC6 ljós eik',6995,'BerryAlloc','Harðparket'),('Vínylparket Grá eik Anelyst 7 mm',4995,'Anelyst','Vínyl'),('Vínylparket fiskibeina natural oak',5995,'Anelyst','Vínyl'),('Wallmann vínylparket Pacific hvít rustic eik',6995,'Wallmann','Vínyl')]:
    pk('bauhaus',n,p,s,'https://www.bauhaus.is/golf-og-veggir/parket/hardparket',b=b)
add('parket','Gólfteppi Bali grátt (400 cm breitt)','bauhaus',2695,'m²',s='Teppi',url='https://www.bauhaus.is/golfteppi-bali-gratt-400cm-verd-a-m',col='Grátt')
for n,p,s in [('Harðparket 8 mm Eik Gondola AC4',2787,'Harðparket'),('Harðparket 8 mm Artisan Eik AC5',3490,'Harðparket'),('Harðparket 8 mm Nature Eik AC5',4124,'Harðparket'),('Harðparket 8 mm Grey Eik AC5',4124,'Harðparket'),('Harðparket 12 mm Rafia Eik AC6',5759,'Harðparket'),('Harðparket 10 mm Passion Batu Eik AC4',5990,'Harðparket'),('Harðparket Sardinia Eik 12 mm AC6',6490,'Harðparket'),('Viðarparket 14 mm eik hvíttuð matt',8990,'Viðarparket')]:
    pk('husa',n,p,s,'https://www.husa.is/golfefni/parket')
for n,p,s in [('Loft Oak',3590,'Harðparket'),('Enchanted Oak',3590,'Harðparket'),('Bedrock Oak',3890,'Harðparket'),('Aspen Oak',3890,'Harðparket'),('Colorado Oak',4190,'Harðparket'),('Boulder Oak',4190,'Harðparket'),('Binyl Pro Stockholm Oak',4890,'Vatnshelt harðparket'),('Binyl Pro Tortona Oak',4890,'Vatnshelt harðparket'),('Oak Tradition 8 mm',5990,'Harðparket'),('Oak Montana Limed',6990,'Harðparket'),('Mohair Grey Vintage Oak',7790,'Harðparket'),('Polar Oak',7990,'Harðparket'),('Eik Rustik planki',15500,'Viðarparket'),('MontBlanc Beyki 3ja stafa',6900,'Viðarparket')]:
    pk('parki',n,p,s,'https://parki.is/hardparket/?orderby=price')
add('parket','EGE teppi – Poetry in the floorscape (57 litir)','parki',None,s='Teppi',b='EGE',url='https://parki.is/teppi/',col='Annað')
mood_p = ['Deep Lava','Ashy Waters','Pernambuco','Winter Spice','Rustic Treehouse','Caramel Church','Summer Hay','Brown Moss','Dark Sauna','Warm Springs','Arctic Elegance','Midnight Sun','Glaciers Natural','Wallis Desert','Smoked White Oil','Djúpreykt eik','American Walnut','Eik Autentisk Greige','Eik Autentisk Olivengrå','Eik Natur Champagne','Eik Natur Polar Hvit','Eik Krem Hvit','Askur Super White','Askur Basalt Grey','Askur Black Oil','Eik Bandsöguð','Eik Deep Black Bandsöguð','Gegnheilir furuplankar']
for n in mood_p:
    add('parket',n,'mood',None,s='Viðarparket',b='Parketverksmiðjan / Mood',url='https://www.moodinteriors.is/categories/parket',x='Eigin framleiðsla. Verð í verslun.')
for n in ['Herringbone Brennero','Herringbone Windsor','Chevron St. Pauls','Herringbone St. Pauls','Canterbury Chevron','Louvre (Versalamynstur)']:
    add('parket',n,'mood',None,s='Síldarbein / chevron',b='Parketverksmiðjan / Mood',url='https://www.moodinteriors.is/categories/parket',x='Verð í verslun.')
for n,s in [('Tarkett / Desso teppaflísar','Teppi'),('Polyflor / Moduleo vínylflísar og vínylparket','Vínyl'),('ter Hürne Ikō Premium harðparket (36 litir)','Harðparket'),('Viðarparket (7 línur)','Viðarparket')]:
    add('parket',n,'golfval',None,s=s,url='https://golfefnaval.is/',col='Annað')
add('parket','Vínylparket 5 mm','murb',4490,'m²',s='Vínyl',x='Verð úr grein frá 2017 – staðfestið',url='https://murbudin.is',col='Annað')

# ---------------- BAÐHERBERGI ----------------
for n,p,s in [('Mora Rexx B5 handlaugartæki',68633,'bt_vask'),('Mora One handlaugartæki',72514,'bt_vask'),('Mora Inxx A2 handlaugartæki, hærri',106262,'bt_vask'),('Mora TRONIC snertifrítt á vegg',88656,'bt_vask'),('Hansa Therm innbyggt sturtutæki',96148,'bt_sturta'),('Sturtugler PA1 svartur rammi, glært',59901,'Sturtugler'),('Sturtugler PA1 svartur rammi, reyklitað',77372,'Sturtugler'),('Spirit sturtugler 6 mm',62877,'Sturtugler'),('Zenith sturtuhurð',99309,'Sturtugler'),('Empire sturtugler fast 125 × 201 svart',109275,'Sturtugler'),('Spirit Nisch sturtuhurð',114926,'Sturtugler')]:
    if s=='Sturtugler': add('bad',n,'tengi',p,s=s,b=n.split()[0],url='https://www.tengi.is/voruflokkur/hreinlaetistaeki/badherbergi/sturta/',col='Svart' if 'svart' in n.lower() else 'Annað')
    else: add(s,n,'tengi',p,s='Sturtutæki (á vegg)' if s=='bt_sturta' else ('Snertifrítt' if 'TRONIC' in n else ('Hátt (f. borðhandlaug)' if 'hærri' in n else 'Á borð / vask')),b=n.split()[0],url='https://www.tengi.is/voruflokkur/hreinlaetistaeki/badherbergi/blondunartaeki/',f='Króm')
for n,p in [('Sturtuveggur Bergen 70 × 190 glær',25095),('Sturtuveggir Ystad 90 × 90 × 190 glærir',45895),('Sturtugler Skärgård 140 × 200 matt svartur prófíll',164295),('Sturtugler Skärgård 160 × 200 matt svartur prófíll',176895)]:
    add('bad',n,'bauhaus',p,s='Sturtugler',url='https://www.bauhaus.is/sturtugler-160x200-cm-matt-svartur-profill-skargard',col='Svart' if 'svartur' in n else 'Annað')
for n,w,cl in [('Salgar Biba 80 cm hnota',80,'Viður / brúnt'),('Salgar Inara 50 cm hvít glans',50,'Hvítt'),('Salgar Silane 100 cm hnota',100,'Viður / brúnt'),('Salgar Silane 100 cm hvít',100,'Hvítt'),('Salgar Aida 44 cm hvít',44,'Hvítt'),('Salgar Noja 90 cm græn',90,'Grænt'),('Salgar Noja 80 cm hvít háglans',80,'Hvítt'),('Salgar Noja 80 cm natural eik',80,'Viður / brúnt'),('Salgar Noja 60 cm svört',60,'Svart'),('Vima 80 cm Montana oak',80,'Viður / brúnt'),('Salgar Marville 40 cm hvít',40,'Hvítt')]:
    add('bad',n,'byko',None,s='Baðinnrétting',b='Salgar',z=f'{w} cm',url='https://byko.is/voruflokkar/innrettingar-303482',col=cl,wid=w,x='Verð á byko.is')
for n,f,cl in [('CITY','Handfangslaus, gegnheill viður eða glans','Viður / brúnt'),('RUSTIC','Náttúruleg viðaráferð','Viður / brúnt'),('Terra','Keramikáferð','Beige / sandur'),('LOFT','Málaðir fletir, rakaþolnir','Grátt')]:
    add('bad','Baðinnrétting '+n,'husa',None,s='Baðinnrétting',f=f+'. Kemur samsett.',url='https://www.husa.is/badinnrettingar/',col=cl)
for n in ['ÄNGSJÖN','TÄNNFORSEN','HAVBÄCK','ENHET']:
    add('bad','Baðinnrétting '+n,'ikea',None,s='Baðinnrétting',b='IKEA',url='https://ikea.is/en/ikea-for-business/residential-development',col='Hvítt')
for c,b_ in [('hth','HTH'),('byko','JKE'),('fri','Nettoline'),('scav','Scavolini'),('parki','Schmidt'),('kvik','Kvik')]:
    add('bad',f'{b_} baðinnrétting (sama og eldhús)',c,None,s='Baðinnrétting',b=b_,url=CO[c][2],col='Annað',x='Passar við eldhúsinnréttingu frá sama aðila.')
add('bt_vask','Tapwell blöndunartæki og vaskar (10 litir)','orgus',None,s='Á borð / vask',b='Tapwell',f='Brons, svart, króm o.fl.',url='https://www.orgus.is',col='Viður / brúnt')
add('bad','Steinsturtubotnar','iogt',None,s='Sturta',col='Grátt')

import sys, os, hashlib; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bath; bath.load(add)
# föst auðkenni: sömu og áður fyrir eldri vörur (svo stjörnur og athugasemdir haldist)
for i,it in enumerate(items):
    it['id'] = f"{it['k'][:2]}{i:04d}"
n_old = len(items)
import merge_scraped; merge_scraped.merge(items, add, colour)
for it in items:
    if 'id' not in it:
        it['id'] = 'x' + hashlib.md5((it['c']+'|'+it.get('url','')+'|'+it['n']).encode()).hexdigest()[:7]
    if os.path.exists(f"img/{it['id']}.jpg"): it['img'] = f"img/{it['id']}.jpg"
assert len({i['id'] for i in items}) == len(items), 'tvítekin auðkenni'
for it in items:
    if 'c' in it and it['c'] not in CO: raise SystemExit('bad company '+str(it))
companies = [{'id':k,'n':v[0],'a':v[1],'w':v[2],'cat':v[3],'x':v[4]} for k,v in CO.items()]
json.dump({'date':__import__('datetime').date.today().isoformat(),'items':items,'companies':companies}, open('data.json','w'), ensure_ascii=False, separators=(',',':'))
from collections import Counter
print(len(items), Counter(i['k'] for i in items))
import os; print(os.path.getsize('data.json'))
