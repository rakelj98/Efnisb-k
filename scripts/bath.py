# Baðherbergisvörur: blöndunartæki (vaskur/sturta), vaskar, klósett, skolhnappar
T = 'https://www.tengi.is/vorur/hreinlaetistaeki/badherbergi/'
B = 'https://www.bauhaus.is/'
BI = 'https://secure.bauhaus.is/media/catalog/product/cache/92d871c11ed9d8ca05ea58bfc9f49daf/'

def load(add):
    # ---------- Blöndunartæki fyrir vask (Tengi) ----------
    tv = [
     ('Mora INXX II Soft medium handlaugartæki króm',51429,'blondunartaeki/mora-inxx-ii-soft-medium-handl-taeki-2/'),
     ('Mora INXX II Sharp handlaugartæki króm',47999,'blondunartaeki/mora-inxx-ii-sharp-handl-taeki-2/'),
     ('Mora INXX II Sharp handlaugartæki matt svart',64573,'blondunartaeki/mora-inxx-ii-sharp-handl-taeki-3/'),
     ('Kaja handlaugartæki f. kalt vatn',6831,'blondunartaeki/kaja-handlaugart-f-kalt-vatn/'),
     ('FMM Eco handlaugartæki',14274,'blondunartaeki/fmm-eco-handlt-kedjuf-mbarka/'),
     ('Hansa Basic handlaugartæki',14337,'blondunartaeki/hansabasic-handl-t-an-lyftitapp/'),
     ('Kaja handlaugartæki með keðjufesti',18229,'blondunartaeki/kaja-handl-taeki-med-kedjufesti/'),
     ('Hansa Polo handlaugartæki',18415,'blondunartaeki/hansapolo-handllt/'),
     ('Hansa Basic XL handlaugartæki',13056,'blondunartaeki/hansabasic-xl-handl-t-an-lyftitapp/'),
     ('Mora CERA B5 handlaugartæki',25166,'blondunartaeki/mora-cera-b5-handl-taeki-an-ly/'),
     ('Hansa Primo handlaugartæki',26682,'blondunartaeki/hansaprimo-handlaugart/'),
     ('Demm VARA handlaugartæki króm',27337,'blondunartaeki/demm-handl-taeki-vara-krom/'),
     ('Demm Spike handlaugartæki',28071,'blondunartaeki/demm-spike-handlaugartaeki/'),
     ('Demm Spike boga handlaugartæki',28071,'blondunartaeki/demm-spike-boga-handlaugartaeki/'),
     ('Oras Safira handlaugartæki',29373,'blondunartaeki/oras-safira-handlaugartaeki/'),
     ('Mora MMIX II handlaugartæki',20352,'blondunartaeki/mora-mmix-ii-handl-taeki-an-lyf/'),
     ('Hansa Vantis handlaugartæki',31513,'blondunartaeki/hansavantis-handl-taeki-nytt/'),
     ('Hansa Vantis handlaugartæki matt svart',52711,'blondunartaeki/handlaugartaeki/hansavantis-handlaugartaeki-matt-svart/'),
     ('FMM Siljan handlaugartæki',32101,'blondunartaeki/fmm-siljan-handlaugartaeki-an-botnv/'),
     ('Hansa Vantis Style handlaugartæki',33350,'blondunartaeki/hansavantis-style/'),
     ('Hansa Twist handlaugartæki',35707,'blondunartaeki/hansatwist-handlaugart-an-lyftitappa/'),
     ('Mora MMIX W1 Care handlaugartæki á vegg',35786,'blondunartaeki/mora-mmix-w1-care-handl-taeki-a-vegg/'),
     ('Demm Sterling handlaugartæki króm',36806,'blondunartaeki/demm-handl-taeki-sterling-kro/'),
     ('Mora INXX II Soft handlaugartæki',33599,'blondunartaeki/mora-inxx-ii-soft-handl-taeki/'),
     ('Mora INXX II Sharp medium handlaugartæki',51429,'blondunartaeki/mora-inxx-ii-sharp-medium-handl-taeki/'),
     ('Hansa Ronda handlaugartæki',53174,'blondunartaeki/hansaronda-handlaugart-an-lt/'),
     ('Hansa Loft handlaugartæki',73860,'blondunartaeki/handlaugartaeki/hansaloft-handlaugartaeki/'),
     ('Hansa Ligna handlaugartæki',79840,'blondunartaeki/handlaugartaeki/hansaligna-handlaugart-an-lt/'),
     ('Dornbracht META handlaugartæki',84356,'blondunartaeki/handlaugartaeki/dornbracht-meta-handlaugartaeki/'),
     ('Demm handlaugartæki ryðfrítt',86675,'blondunartaeki/handlaugartaeki/demm-handlaugartaeki-rydfritt/'),
     ('Dornbracht IMO handlaugartæki króm',97928,'blondunartaeki/handlaugartaeki/db-handl-t-imo-an-lyftit/'),
     ('VOLA HV1 handlaugartæki',101411,'blondunartaeki/handlaugartaeki/vola-hv1-handlaugartaeki/'),
     ('Dornbracht META handlaugartæki dark platinum matt',137128,'blondunartaeki/handlaugartaeki/dornbracht-meta-handlaugartaeki-an-lyft-dark-pl-m/'),
     ('Dornbracht TARA Logic handlaugartæki',148102,'blondunartaeki/handlaugartaeki/db-handl-t-tara-logic-med-lyftit/'),
     ('Dornbracht TARA handlaugartæki matt svart',166933,'blondunartaeki/handlaugartaeki/dornbracht-tara-handl-t-m-lyftitappa-matt-svart/'),
     ('Dornbracht LULU handlaugartæki',201005,'blondunartaeki/handlaugartaeki/dornbracht-handl-t-lulu/'),
     ('Dornbracht MEM handlaugartæki króm',218652,'blondunartaeki/handlaugartaeki/dornbracht-mem-handl-taeki-krom/'),
     ('Dornbracht VAIA handlaugartæki dark platinum matt',263135,'blondunartaeki/handlaugartaeki/db-handl-t-vaia-an-lyftit-dark-platinum-matt/'),
     ('Dornbracht CYO handlaugartæki platinum matt',283640,'blondunartaeki/handlaugartaeki/dornbracht-handl-t-cyo-an-lyftitappa-platinum-matt/'),
     ('Frístandandi handlaugartæki FS2 króm',676239,'blondunartaeki/handlaugartaeki/fristandandi-handl-taeki-krom/'),
     ('Vola innbyggt handlaugartæki burstað króm',160695,'blondunartaeki/handlaugartaeki-vegghengd/vola-innbyggt-handlaugartaeki-burstad-krom/'),
    ]
    for n,p,u in tv:
        sub='Innbyggt / úr vegg' if ('vegg' in n or 'innbyggt' in n) else ('Hátt' if 'hátt' in n.lower() else 'Á borð / vask')
        add('bt_vask',n,'tengi',p,s=sub,b=n.split()[0],url=T+u,f=fin(n))
    for n,p in [('Demm Spike handlaugartæki hátt',36834),('Mora INXX II handlaugartæki, hærri gerð',57715),('Demm handlaugartæki ryðfrítt hátt',126299),('VOLA handlaugartæki 170 hátt',126301),('Hansa Ronda handlaugartæki hærri',84625),('Hansa Twist XL handlaugartæki matt svart',68346)]:
        add('bt_vask',n,'tengi',p,s='Hátt (f. borðhandlaug)',b=n.split()[0],url='https://www.tengi.is/voruflokkur/hreinlaetistaeki/badherbergi/blondunartaeki/handlaugartaeki-haerri/',f=fin(n))
    for n,p in [('Mora MMIX Tronic snertifrítt handlaugartæki',72152),('Hansa Fit snertifrítt handlaugartæki',51420),('Hansa Electra snertifrítt, rafhlaða/Bluetooth',55000)]:
        add('bt_vask',n,'tengi',p,s='Snertifrítt',b=n.split()[0],url='https://www.tengi.is/voruflokkur/hreinlaetistaeki/badherbergi/blondunartaeki/snertifritt/',f='Króm')
    bv = [('Camargue Samsø Dueodde','Messing burstað','handlaugartaeki-camargue-samso-dueodde-messing-burstad','1/0/1048651.jpg',12995),
          ('Camargue Samsø Dueodde','Matt svart','handlaugartaeki-camargue-samso-dueodde-matt-svart','1/0/1048650.jpg',None),
          ('Camargue Samsø Dueodde','Króm','handlaugartaeki-camargue-samso-dueodde-krom','1/0/1048649.jpg',12995),
          ('Camargue Samsø Dueodde','Messing pússað','handlaugartaeki-camargue-samso-dueodde-messing-pussad','1/0/1050760.jpg',None),
          ('Camargue Mocha','Matt svart','handlaugartaeki-camargue-mocha-matt-svart','1/0/1049916.jpg',15795),
          ('Camargue Mocha','Antík messing','handlaugartaeki-camargue-mocha-antik-messing','1/0/1049804.jpg',16295),
          ('Camargue Mocha','Króm','handlaugartaeki-carmargue-mocha-krom','1/0/1049803.jpg',10495),
          ('Camargue Mocha','Gun metal','handlaugartaeki-camargue-mocha-gun-metal','1/0/1049919_A.jpg',None),
          ('Camargue Erie','Króm','handlaugartaeki-camargue-erie-krom','3/0/3009782l.jpg',4195),
          ('Camargue Futuna','Matt svart','handlaugartaeki-camargue-futuna-matt-svart','7/9/79ac3dd5-7158-4681-84d6-b5d36fb57328.jpg',16495),
          ('Camargue Futuna','Antík messing','handlaugartaeki-camargue-futuna-antik-messing','f/7/f7026c17-c907-44bf-865e-092f9964c030.jpg',16495),
          ('Camargue Futuna','Pólerað messing','handlaugartaeki-camargue-futuna-polerad-messing','5/7/5708952990107_1.jpg',None),
          ('Camargue Nadi','Matt svart','handlaugartaeki-camargue-nadi-matt-svart','f/5/f51080f9-42d0-48a6-bb61-666fbf937592.jpg',None),
          ('Camargue Mili','Króm','handlaugartaeki-camargue-mili-krom','b/9/b9e22ffa-2c2a-4820-9142-d645d37a072c.jpg',None),
          ('Camargue Mili','Matt svart','handlaugartaeki-camargue-mili-matt-svart','1/0/1049564.jpg',None),
          ('Camargue Flat','Króm','handlaugartaeki-camargue-flat-krom','1/0/1050920.jpg',None),
          ('Camargue Elba','Króm','handlaugartaeki-elba-krom-camargue','1/0/1001530.jpg',None),
          ('Hansgrohe Talis E110 m. botnventli','Matt svart','handlaugartaeki-hansgrohe-talis-e110-matt-svart-m-botnventil','1/0/1049284_1.jpg',None),
          ('Hansgrohe Talis E110 m. botnventli','Svart','handlaugartaeki-hansgrohe-talis-e110-svart-med-botnventil','4/0/4059625229521_p.jpg',None),
          ('Hansgrohe MySport M m. botnventli','Króm','handlaugartaeki-hansgrohe-mysport-m-krom-med-botnventil','4/0/4011097753386_18.jpg',None),
          ('Hansgrohe MySport L m. botnventli','Króm','handlaugartaeki-hansgrohe-mysport-l-krom-med-botnventil','4/0/4011097753409_17.jpg',None),
          ('Hansgrohe Logis E 70 m. botnventli','Króm','handlaugartaeki-hansgrohe-logis-e-70-krom-med-botnventil','4/0/4011097834221_p.jpg',None),
          ('Hansgrohe Logis Fine','Króm','handlaugartaeki-hansgrohe-logis-fine-krom','1/2/1218550_1.jpg',None),
          ('Hansgrohe Blend 70','Matt svart','handlaugartaeki-hansgrohe-blend-70-matt-svart','3/2/325fd8a3-2143-43ab-81cc-397b017e3dfb.png',None),
          ('Hansgrohe Vernis Blend 100','Króm','handlaugartaeki-vernis-blend-100-hansgrohe','2/e/2e3ce22c-de45-4815-90d8-5708ac88be11.jpg',None),
          ('Hansgrohe Ecos L','Króm','handlaugartaeki-hansgrohe-ecos-l-krom','4/0/4011097686196_p.jpg',None),
          ('Hansgrohe Vivenis','Króm','handlaugataeki-hansgrohe-vivenis-krom','4/0/4059625334980_p.jpg',None),
          ('Hansgrohe Rebris E CoolStart 80','Króm','handlaugartaeki-rebris-e-coolstart-80-hansgrohe','4/0/4059625402337_produkt.png',None),
          ('Grohe Start M m. botnventli','Króm','handlaugartaeki-grohe-start-m-kromad-med-botnventil','1/0/1048832.jpg',None),
          ('Grohe Start S m. botnventli','Króm','handlaugartaeki-grohe-start-s-kromad-med-botnventil','1/0/1048831.png',None),
          ('Grohe Essence m. botnventli','SuperSteel','handlaugartaeki-og-botnventill-grohe-essence-supersteel','7/e/7eddc56b-9845-44d9-9f2c-4f467bc7121d.jpg',None),
          ('Grohe Essence S m. botnventli','Messing','handlaugartaeki-med-botnventli-grohe-essence-s-messing','6/5/6550b17d-5ddb-4595-8d63-7a7e8b31ae86.jpg',None),
          ('Grohe Dice M','Svart','handlaugartaeki-grohe-dice-m-svart','1/6/1669058.png',None),
          ('Grohe Tingsted hátt','Króm','handlaugartaeki-grohe-tingsted-krom-hatt','1/5/1547276.jpg',None),
          ('Grohe Tingsted hátt','Messing','handlaugartaeki-grohe-tingsted-messing-hatt','1/5/1547275.jpg',None),
          ('Gustavsberg Estetic','Matt svart','handlaugartaeki-gustavsberg-estetic-matt-svart','1/0/1049554.jpg',None),
          ('Gustavsberg Estetic hátt','Matt svart','handlaugartaeki-gustavsberg-estetic-matt-svart-hatt','1/0/1049547.jpg',None),
          ('Gustavsberg Dynamic','Króm','handlaugartaeki-gustavsberg-dynamic-krom','8/1/819817ce-1fdc-4729-8ca1-830770cc60c2.jpg',None),
          ('Adora Imperia','Burstað gyllt','handlaugataeki-adora-imperia-burstad-gyllt','4/d/4d172be1-85f3-4b73-8f03-8afa96bb2fdd.jpg',34995),
          ('Adora Imperia','Rós gyllt','handlaugataeki-adora-imperia-ros-gyllt','4/b/4bbbd3f4-ecc3-47a4-9292-eaf77c4b2cbe.jpg',34995)]
    for n,f,u,im,p in bv:
        add('bt_vask',n+' – '+f.lower(),'bauhaus',p,s='Hátt (f. borðhandlaug)' if 'hátt' in n else 'Á borð / vask',b=n.split()[0],f=f,url=B+u,img=BI+im)
    for n,p in [('Adora Opus m. botnventli króm',17195),('Adora Imperia m. botnventli króm',25295),('Adora Simplex króm',22195),('Adora Gracili matt',24995)]:
        add('bt_vask',n,'bauhaus',p,s='Á borð / vask',b='Adora',f=fin(n),url=B+'badherbergid/blondunartaeki/handlaugartaeki?brand=Adora')
    for n,p in [('Grohe Essence handlaugartæki úr vegg',48790),('Grohe Essence úr vegg svart 183 mm',66990),('Grohe Essence úr vegg króm 183 mm',46890),('Handlaugartæki úr vegg 19408DC1',67890),('Damixa Silhouet úr vegg svart',46090),('Damixa Space handlaugartæki m. smellutappa',12143)]:
        add('bt_vask',n,'husa',p,s='Innbyggt / úr vegg' if 'vegg' in n else 'Á borð / vask',b=n.split()[0],f=fin(n),url='https://www.husa.is/eldhus-og-badherbergi/blondunartaeki/innbyggd-taeki/')

    # ---------- Blöndunartæki fyrir sturtu ----------
    ts = 'sturta/sturtutaeki-sturta-badherbergi/'
    for n,p,u in [('Kaja sturtutæki',11237,'kaja-sturtutaeki/'),('Demm Sterling sturtutæki króm',26618,'demm-sturtutaeki-sterling-kro/'),('Demm hitastýrt sturtutæki, stútur upp',29010,'demm-hitastyrt-sturtuaeki-m-stut-upp/'),('Demm hitastýrt sturtutæki, stútur niður',29010,'demm-hitastyrt-sturtuaeki-m-stut-nidur/'),('Demm VARA sturtutæki',32928,'demm-vara-sturtutaeki/'),('Demm hitastýrt sturtutæki upp/niður',33664,'demm-hitastyrt-sturtutaeki/'),('Mora CERA T4 sturtutæki, niður',34900,'mora-cera-t4-sturtutaeki-s-nid/'),('Mora CERA T4 sturtutæki, upp',34900,'mora-cera-t4-sturtutaeki-s-upp/'),('Demm sturtutæki upp/niður matt svart',38147,'demm-sturtutaeki-stut-upp-nidur-matt-svart/'),('Demm hitastýrt sturtutæki niður matt svart',38147,'demm-hitastyrt-sturtutaeki-m-stut-nidur-matt-svart/'),('Mora MMIX II sturtutæki, niður',39527,'mora-mmix-ii-sturtutaeki-s-nidu/'),('Mora MMIX II sturtutæki, upp',39527,'mora-mmix-ii-sturtutaeki-s-upp/'),('Hansa Micra hitastýrt sturtutæki',39692,'hansamicra-hitast-blondtaeki-stut-nidur/'),('FMM Siljan sturtutæki',48268,'fmm-siljan-sturtutaeki/'),('Mora CERA T4 sturtutæki öfugt',52545,'mora-cera-t4-sturtutaeki-ofugt/'),('Frístandandi sturtutæki króm',961873,'fristandandi-sturtutaeki-krom/')]:
        add('bt_sturta',n,'tengi',p,s='Sturtutæki (á vegg)',b=n.split()[0],f=fin(n),url=T+ts+u)
    for n,p,u in [('Mora CERA sturtusett + tæki',90897,'sturta/sturtusett/mora-cera-sturtusett-taeki/'),('Mora MMIX II sturtusett + tæki',117652,'sturta/sturtusett/mora-mmix-ii-sturtusett-taeki/'),('Mora INXX II sturtusett + tæki (30 cm haus)',158942,'sturta/sturtusett/mora-inxx-ii-sturtusett/'),('Mora Classic family sturtusett (án tækja)',119948,'sturta/sturtusett/mora-classic-family-sturtusett/'),('Mora INXX S5 family sturtusett (án tækja)',None,'sturta/sturtusett/morainxx-s5-family-sturtusett/')]:
        add('bt_sturta',n,'tengi',p,s='Sturtusett',b='Mora',f='Króm',url=T+u)
    for n,p in [('Hansa Micra sturtusett',97981),('Mora MMIX S5 sturtusett (án tækja)',18493),('Mora Classic sturtusett L=540 mm',57490),('Mora INXX II handsturtusett matt svart',150284)]:
        add('bt_sturta',n,'tengi',p,s='Sturtusett',b=n.split()[0],f=fin(n),url='https://www.tengi.is/voruflokkur/hreinlaetistaeki/badherbergi/sturta/handsturtusett/')
    for n,p,u in [('Hansa Bluebox Vantis innbyggt sturtusett, króm kringlótt',191830,'sturta/innbyggd-bad-sturtutaeki-sturta/bluebox-sturtusett-krom-vantis-kringl-2/'),('Hansa Bluebox Designo innbyggt sturtusett, króm ferkantað',252678,'sturta/innbyggd-bad-sturtutaeki-sturta/bluebox-designo-sturtusett-krom-ferk/'),('Hansa Bluebox Living innbyggt sturtusett, svart ferkantað',295832,'sturta/innbyggd-bad-sturtutaeki-sturta/bluebox-living-sturtusett-svart-ferk/')]:
        add('bt_sturta',n,'tengi',p,s='Innbyggt sturtusett',b='Hansa',f=fin(n),url=T+u)
    for n,p in [('Grohe Precision innbyggt sturtusett 250 króm',154900),('Grohe Precision innbyggt sturtusett 250 svart',195900),('Damixa Silhouet innbyggt sturtusett burstað grafít',172900)]:
        add('bt_sturta',n,'husa',p,s='Innbyggt sturtusett',b=n.split()[0],f=fin(n),url='https://www.husa.is/eldhus-og-badherbergi/blondunartaeki/innbyggd-taeki/')
    for n,f,u,im in [('Grohe Vitalio Start System 250 sturtusett','Króm','sturtusett-grohe-vitalio-start-symtem-250-krom','4/0/4005176767227_1.jpg'),('Camargue sturtusett með blöndunartæki','Króm','sturtusett-med-blondunartaeki-camargue-krom','1/0/1046891.png'),('Grohe Vitalio Start 250 sturtusett f. baðkar','Króm','sturtusett-fyrir-badkar-grohe-vitalio-start-250-krom','1/5/1515559.jpg')]:
        add('bt_sturta',n,'bauhaus',None,s='Sturtusett',b=n.split()[0],f=f,url=B+u,img=BI+im)
    for n,f,u,im in [('Camargue Nemo Eco sturtuhaus Ø20','Króm','sturtuhaus-hringlaga-o20cm-camargue-nemo-eco-krom','1/0/1049395.jpg'),('Grohe Vitalio Comfort 110 handsturta','Króm','handsturta-grohe-vitalio-comfort-110-iii-krom','1/4/1466563.jpg'),('Camargue handsturta og slanga Ø12','Króm','handsturta-og-slanga-camargue-o12cm','5/7/5708705121000_1.jpg')]:
        add('bt_sturta',n,'bauhaus',None,s='Sturtuhaus / handsturta',b=n.split()[0],f=f,url=B+u,img=BI+im)
    add('bt_sturta','Sturtutæki – allt úrval','bauhaus',None,s='Sturtutæki (á vegg)',url=B+'badherbergid/blondunartaeki/sturtutaeki',col='Stál / málmur',x='Opnaðu flokkinn hjá BAUHAUS')

    # ---------- Vaskar / handlaugar ----------
    tl = [('Geberit Selnova handlaug á vegg 50×41',10813,'handlaugar/vegghengdar/geberit-selnova-handlaug-a-vegg-50cm41-cm/','Vegghengd',50,41),
          ('Geberit Selnova handlaug á vegg 40×25',14705,'handlaugar/vegghengdar/geberit-selnova-handl-a-vegg-40x26cm-bl-h/','Vegghengd',40,25),
          ('IFÖ Cera handlaug 57×44',18145,'handlaugar/vegghengdar/ifo-cera-handlaug-57x44-cm/','Vegghengd',57,44),
          ('IFÖ VariForm borðhandlaug hringlaga 40 niðurfelld',19562,'handlaugar/bordhandlaugar/ifo-variform-bordhandlaug-hringlaga-40cm-nidurfell/','Niðurfelld',40,40),
          ('IFÖ Spira handlaug, gat í miðju',20541,'handlaugar/vegghengdar/spira-handlaug-gat-midju/','Vegghengd',None,None),
          ('IFÖ VariForm borðhandlaug kringlótt 48 niðurfelld',21321,'handlaugar/bordhandlaugar/ifo-variform-bordhandlaug-kringlott-48-cm-nidurfe/','Niðurfelld',48,48),
          ('IFÖ VariForm borðhandlaug hálfniðurfelld',21458,'handlaugar/bordhandlaugar/ifo-variform-bordhandlaug-halfnidurfelld/','Hálfniðurfelld',50,45),
          ('Geberit Selnova handlaug á vegg 60×37',21970,'handlaugar/vegghengdar/geberit-selnova-handlaug-a-vegg-60x37cm/','Vegghengd',60,37),
          ('IFÖ Cera handlaug 50×43',22052,'handlaugar/vegghengdar/ifo-cera-handlaug-50x43/','Vegghengd',50,43),
          ('IFÖ Spira rétthyrnd handlaug',22065,'handlaugar/vegghengdar/ifo-spira-retthyrnd-handlaug/','Vegghengd',None,None),
          ('Geberit Renova Plan handlaug 45×34',22544,'handlaugar/vegghengdar/geberit-renova-plan-handlaug-a-vegg-45x34/','Vegghengd',45,34),
          ('Geberit Renova handlaug 50×38',22853,'handlaugar/vegghengdar/geberit-renova-handlaug-a-vegg-50x38cm/','Vegghengd',50,38),
          ('Geberit Selnova handlaug á vegg 65×48',22872,'handlaugar/vegghengdar/geberit-selnova-handlaug-a-vegg-65x48cm/','Vegghengd',65,48),
          ('IFÖ VariForm undirlímd sporöskjulaga 50',24080,'handlaugar/undirlimdar/ifo-variform-undirlimd-handlaug-sporoskjul-50-cm/','Undirlímd',50,40),
          ('Geberit Smyle Square handlaug',24624,'handlaugar/handlaugar-a-innrettingar/geberit-smyle-squre-handlaug/','Á innréttingu',None,None),
          ('Geberit Selnova handlaug rétthyrnd (ofan á borð)',24811,'handlaugar/bordhandlaugar/geberit-selnova-handlaug-retthyrnd/','Ofan á borð',None,None),
          ('IFÖ Spira handlaug 57×43,5',25379,'handlaugar/vegghengdar/ifo-spira-handlaug-15120-57x435cm-boltud-an-gats-f-blond-taeki/','Vegghengd',57,43.5),
          ('IFÖ VariForm borðhandlaug sporöskjulaga 60×45',25997,'handlaugar/bordhandlaugar/ifo-variform-bordhandlaug-sporoskulaga-60x45-cm/','Niðurfelld',60,45),
          ('Tanger S undirlímd handlaug 45×29 hvít',18446,'handlaugar/undirlimdar/tanger-s-undirlimd-handlaug-48x32cm-hvit/','Undirlímd',45,29),
          ('Nice undirlímd handlaug kringlótt 37 hvít',26351,'handlaugar/undirlimdar/nice-undirlimd-handlaug-kringlott-37cm-hvit/','Undirlímd',37,37),
          ('IFÖ VariForm undirlímd rétthyrnd 45×35',26840,'handlaugar/undirlimdar/ifo-variform-undirlimd-handlaug-retthyrnd-45-cm/','Undirlímd',45,35),
          ('IFÖ VariForm borðhandlaug rétthyrnd 55×45',27305,'handlaugar/bordhandlaugar/ifo-variform-bordhandlaug-retthyrnd-55-cm-2/','Niðurfelld',55,45),
          ('IFÖ VariForm borðhandlaug hringlaga hálfinnfelld',38960,'handlaugar/bordhandlaugar/ifo-variform-bordhandlaug-hringlaga-half-innfelld/','Hálfniðurfelld',None,None),
          ('IFÖ VariForm ofan á borð sporöskjulaga 50',38960,'handlaugar/ofan-a-bord/ifo-variform-bordhandlaug-sporoskjulaga-50-cm/','Ofan á borð',50,None),
          ('IFÖ VariForm ofan á borð hringlaga 40',38960,'handlaugar/ofan-a-bord/ifo-variform-bordhandlaug-hringlaga-40-cm/','Ofan á borð',40,40),
          ('IFÖ Spira handlaug ofan á innréttingu',41639,'handlaugar/handlaugar-a-innrettingar/spira-handlaug-ofan-a-innrettingu/','Á innréttingu',None,None),
          ('IFÖ VariForm ofan á borð hringlaga 45',42534,'handlaugar/ofan-a-bord/ifo-variform-bordhandlaug-hringlaga-45-cm/','Ofan á borð',45,45),
          ('IFÖ VariForm ofan á borð sporöskjulaga 55',43711,'handlaugar/ofan-a-bord/ifo-variform-bordhandlaug-sporoskjulaga-55-cm/','Ofan á borð',55,None),
          ('Alape EB.K handlaug (stál, glerjuð)',45081,'handlaugar/bordhandlaugar/alape-eb-k-handlaugar/','Ofan á borð',None,None),
          ('IFÖ VariForm ofan á borð rétthyrnd 55',45093,'handlaugar/ofan-a-bord/ifo-variform-bordhandlaug-retthyrnd-55-cm/','Ofan á borð',55,None),
          ('IFÖ VariForm ofan á borð sporöskjulaga 60',46778,'handlaugar/ofan-a-bord/ifo-variform-bordhandlaug-sporoskjulaga-60-cm/','Ofan á borð',60,None),
          ('IFÖ VariForm ofan á borð rétthyrnd 60',46778,'handlaugar/ofan-a-bord/ifo-variform-bordhandlaug-retthyrnd-60-cm/','Ofan á borð',60,None),
          ('Handlaug stál RS72',50909,'handlaugar/serlausnir/handlaug-stal-rs72/','Sérlausn',None,None),
          ('IFÖ Sense handlaug 60',51491,'handlaugar/handlaugar-a-innrettingar/ifo-sense-handlaug-15402-60cm/','Á innréttingu',60,None),
          ('Alape stálhandlaug UB.O425 undirlímd hvít',52469,'handlaugar/undirlimdar/stalhandlaug-hvit-ub-o425-undirlimd/','Undirlímd',42.5,None),
          ('Heart handlaug á innréttingu 80×50 hvít',53098,'handlaugar/handlaugar-a-innrettingar/heart-handlaug-a-innrettingu-80x50-l70-hvit/','Á innréttingu',80,50),
          ('IFÖ Spira handlaug 92×41',56855,'handlaugar/handlaugar-a-innrettingar/ifo-spira-handlaug-15382007-92x41cm-comp-vinkl/','Á innréttingu',92,41),
          ('Alape stálhandlaug UB.K400 undirlímd hvít',57034,'handlaugar/undirlimdar/stalhandlaug-hvit-ub-k400-undirlimd/','Undirlímd',40,40),
          ('Alape stálhandlaug EB.O500H hvít',60821,'handlaugar/bordhandlaugar/stalhandlaug-hvit-eb-o500h/','Ofan á borð',50,None),
          ('Geberit Smyle Square handlaug 90×48',61080,'handlaugar/handlaugar-a-innrettingar/geberit-smyle-squre-handlaug-90x48cm-inrettingu-vegg/','Á innréttingu',90,48),
          ('Flaminia Twin Set handlaug Ø42',85414,'handlaugar/twin-set-42cm/','Ofan á borð',42,42)]
    for n,p,u,s,w,h in tl:
        add('vaskar',n,'tengi',p,s=s,b=n.split()[0],z=f'{w:g} × {h:g} cm' if (w and h) else (f'{w:g} cm' if w else ''),url=T+u,col='Hvítt',wid=int(w) if w else None)
    bl = [('Bath Deluxe Camden 60 cm hvít','handlaug-60cm-bath-deluxe-camden-hvit','1/0/1045471.jpg',60,None,None),('Bath Deluxe Camden 90 cm hvít','handlaug-90cm-bath-deluxe-camden-hvit','1/0/1047597.jpg',90,None,None),('Bath Deluxe Camden 40 cm hvít','handlaug-40cm-bath-deluxe-camden-hvit','1/0/1053171.jpg',40,None,None),('Bath Deluxe Camden 120 cm hvít','handlaug-120cm-bath-deluxe-camden-hvit','1/0/1046285.jpg',120,None,None),('Bath Deluxe Camden tvöföld 120 cm hvít','handlaug-tvofold-120cm-bath-deluxe-camden-hvit','1/0/1047259.jpg',120,None,None),('Sydney 46×60','handlaug-46x60-cm-sydney','3/1/3195998A.jpg',60,46,None),('Sydney 40×50','handlaug-40x50-cm-sydney','3/1/3196996A.jpg',50,40,None),('Ifö Spira 40×32','handlaug-40x32-cm-ifo-spira','6/6/669d37bd-3979-4347-89b7-dfc884f23457.jpg',40,32,None),('Ifö Spira 50×36','handlaug-50x36-cm-ifo-spira','3/3/33a51ddf-5ed4-45e1-b460-eb8da14e4890.jpg',50,36,None),('Ifö Spira 57×43,5','handlaug-57x43-5-cm-ifo-spira','b/f/bfbb8eea-ec66-41ac-8439-a05dbefb5bf6.jpg',57,43.5,None),('Camargue El Hiero 33,5×29,5','handlaug-33-5x29-5-cm-camargue-el-hiero','0/b/0bfe4eb6-985d-43bd-898f-44400ae58bc5.jpg',33.5,29.5,None),('Laufen Pro-N 50×36','handlaug-50x36-cm-laufen-pro-n','4/e/4ef89a90-a599-4c8c-9e03-3e10c5998906.jpg',50,36,21995),('Laufen Pro-N 36×25','handlaug-36x25-cm-laufen-pro-n','4/e/4e0fb63c-ab9f-4e28-bc79-eb8ec1e5d198.jpg',36,25,23895),('Laufen Pro-N 56×42','handlaug-56x42-cm-laufen-pro-n','f/8/f8b94216-69d5-435f-8f82-39276057f2cc.jpg',56,42,24995),('Laufen Pro-N 60×42','handlaug-60x42-cm-laufen-pro-n','c/3/c35c7761-8cf8-4625-82a0-d5be05d83956.jpg',60,42,25395),('Laufen Pro-N 40×32','handlaug-40x32-cm-laufen-pro-n','8/c/8c7e5b71-57de-4eeb-94cd-c0cfcac38053.jpeg',40,32,22295),('Laufen Pro-N 48×28','handlaug-48x28-cm-laufen-pro-n','f/0/f005a083-5a75-45a0-b910-523147022d3b.jpg',48,28,28995),('Hansgrohe Xanuia Q 45×34','handlaug-45x34-cm-hansgrohe-xanuia-q','4/0/4059625478684.jpg',45,34,None),('Hansgrohe Xanuia Q 60×48','handlaug-60x48-cm-hansgrohe-xanuia-q','4/0/4059625478899.jpg',60,48,None),('Hansgrohe Xanuia Q 55×48','handlaug-55x48-cm-hansgrohe-xanuia-q','4/0/4059625478905_1.jpg',55,48,None),('Camargue Zonda 2.0 Ø43 hvít','handlaug-o43-camargue-zonda-2-0-hvit','f/8/f8289eb2-8801-4f48-97c7-09ed04ae1539.jpg',43,43,None),('Camargue Teneriffa 45×27','handlaug-45x27-cm-camargue-teneriffa','a/4/a43efcf0-6dbc-480c-a50b-0172468f7727.jpg',45,27,None),('Camargue Los Angeles 46,5×42 svört','handlaug-46-5x42-cm-camargue-los-angeles-svort','c/9/c9af6a1f-c854-44ed-8c86-58f58879ef59.jpg',46.5,42,None),('Camargue Perth 50×44','handlaug-50x44-cm-camargue-perth','c/d/cdd16487-b02d-419e-b878-c2f31989a5c4.jpg',50,44,None),('Duravit Vero 45×35','handlaug-45x35cm-duravit-vero','e/e/eeff1d97-083a-4fb6-bd2e-9571c4fd0a99.jpg',45,35,37495),('Duravit Vero 50×47','handlaug-50x47cm-duravit-vero','4/6/46056101-1bfa-42bd-9628-a7ebe2a8a1b4.jpg',50,47,44495),('Duravit Vero 60×47','handlaug-60x47cm-duravit-vero','b/5/b55525ba-5c9d-45a2-bb56-dc18667ad250.jpg',60,47,47995),('Camargue Fuerteventura 45×30','handlaug-45x30-cm-camargue-fuerteventura','7/b/7bce2d9b-2990-436a-9448-daff8c3f6cac.jpg',45,30,None),('Camargue Adelaide 45×40','handlaug-45x40-cm-camargue-adelaide','b/1/b1478274-c459-4820-807a-e86b1733a5c8.jpg',45,40,None),('Camargue Levanzo 25,5×36,5','handlaug-25-5x36-5-cm-camargue-levanzo','e/9/e9ff3b85-a5c7-4afe-95b2-90124eb56e1b.jpg',36.5,25.5,None),('Camden Slim 40 cm hvít','handlaug-40cm-camden-slim-hvit','1/4/1470706.jpg',40,None,None),('Camargue Los Angeles 46×30,5','handlaug-46x30-5-cm-camargue-los-angeles','d/1/d176429a-4156-4779-9c6c-40aebeaecbab.jpg',46,30.5,None),('Skärgård Loknes 80 cm hvít','handlaug-loknes-80cm-skargard-hvit','1/0/1052738.png',80,None,None),('Laufen 60 cm hvít','handlaug-60cm-laufen-hvit','1/0/1053113.jpg',60,None,None),('Camargue Skärgård 80×46 hvít','handlaug-80x46cm-camargue-skargard-hvit','6/a/6a43a522-5d3f-44bc-b69f-12f9edaf1447.jpg',80,46,None),('Laufen Meda 77,7×44,5 hvít','handlaug-77-7x44-5cm-laufen-meda-hvit','1/5/1518817.png',77.7,44.5,None)]
    for n,u,im,w,h,p in bl:
        add('vaskar',n,'bauhaus',p,s='Ofan á borð' if any(k in n for k in ['El Hiero','Zonda','Teneriffa','Los Angeles','Perth','Fuerteventura','Adelaide','Levanzo']) else ('Á innréttingu' if any(k in n for k in ['Camden','Sydney','Loknes','Skärgård','Meda','Laufen 60']) else 'Vegghengd'),b=n.split()[0] if n.split()[0]!='Bath' else 'Bath Deluxe',z=f'{w:g} × {h:g} cm' if h else f'{w:g} cm',url=B+u,img=BI+im,col='Svart' if 'svört' in n else 'Hvítt',wid=int(w))
    for n,p,s,col in [('Handlaug í plötu matt svört 61 cm',36190,'Á innréttingu','Svart'),('Handlaug í plötu matt svört 101 cm',56790,'Á innréttingu','Svart'),('Handlaug í plötu matt svört 121 cm',80790,'Á innréttingu','Svart'),('Borðhandlaug sporöskjulaga matt svört 46 cm',24000,'Ofan á borð','Svart'),('Borðhandlaug hringlaga matt hvít 35 cm',22000,'Ofan á borð','Hvítt'),('Handlaug á vaskaskáp 81 cm Elide',28390,'Á innréttingu','Hvítt'),('Handlaug á vaskaskáp 101 cm Elide',38890,'Á innréttingu','Hvítt'),('Handlaug á vaskaskáp 121 cm Elide',65290,'Á innréttingu','Hvítt'),('Kamé Vessel handlaug 55×36 matt hvít',40000,'Ofan á borð','Hvítt'),('Undirlímd handlaug í plötu Black Moon 101 cm',78990,'Á innréttingu','Svart'),('Jika Ibon borðhandlaug 52×41',14243,'Ofan á borð','Hvítt')]:
        add('vaskar',n,'husa',p,s=s,url='https://www.husa.is/eldhus-og-badherbergi/badinnrettingar/handlaugar/',col=col)

    # ---------- Klósett ----------
    tk = [('IFÖ Cera vegghengt klósett',21960,'salerni/wc-ifo-cera-veggh-f-innb-kassa/'),('Geberit Selnova klósettskál',22925,'salerni/geberit-selnova-wc-skal/'),('Geberit Selnova klósettskál RimFree',37473,'salerni/geberit-selnova-wc-skal-rimfree/'),('Geberit Selnova Premium RimFree',54017,'salerni/geberit-selnova-premium-wc-skal-rimfree/'),('Laufen Meda 54 silent/rimless matt svört',68025,'salerni/laufen-wc-skal-meda-54-silent-rimless-matt-svort/'),('Geberit Acanto RimFree',53780,'salerni/geberit-acanto-wc-skal-rimfree/'),('Geberit iCon RimFree',100182,'salerni/geberit-icon-wc-rimfree-veggh-innb/'),('IFÖ Spira 6293 vegghengt m. kassa',101957,'salerni/wc-ifo-spira-6293-vegghengt-m-kassa/'),('Flaminia App GoSilent vegghengt',102502,'salerni/wc-flaminia-app-gosilent-veggh-innb/'),('Geberit Smyle Square TurboFlush m. setu',109106,'salerni/geberit-smyle-square-wc-skal-turboflush-m-setu-hvit/'),('IFÖ Spira Art rimfree vegghengt',109878,'salerni/ifo-spira-art-rimfree-veggh-wc-f-innb-18-23/'),('Geberit Acanto TurboFlush m. setu',120509,'salerni/geberit-acanto-wc-skal-turboflush-m-setu-hvit/'),('Geberit iCon TurboFlush m. setu',129892,'salerni/geberit-icon-wc-skal-turboflush-m-setu-hvit/'),('Geberit ONE TurboFlush m. setu',144992,'salerni/geberit-one-wc-skal-m-setu-hvit/'),('Geberit ONE TurboFlush m. setu hvítt/króm',152794,'salerni/geberit-one-wc-skal-m-setu-hvit-krom/'),('Geberit ALBA skolsalerni (pakkatilboð m. kassa)',175000,'salerni/alba-pakkatilbod/'),('Geberit ALBA skolsalerni',197491,'salerni/geberit-alba-skolsalerni-hvitt/'),('Geberit SELA skolsalerni',556128,'salerni/vegghengd/geberit-sela-skolsalerni-hvitt/'),('Geberit MERA Classic skolsalerni',928853,'salerni/geberit-mera-classic-skolklosett-hvit-umgjord/'),('Geberit MERA Comfort skolsalerni',993600,'salerni/geberit-mera-skolklosett-hvit-umgjord/')]
    for n,p,u in tk:
        add('klosett',n,'tengi',p,s='Skolsalerni' if 'skolsal' in n else 'Vegghengt',b=n.split()[0],url=T+u,col='Svart' if 'svört' in n else 'Hvítt')
    bk = [('Gustavsberg Skandic 1410 P-lás','salerni-p-las-gustavsberg-skandic-1410-hf','4/0/4062373912461.jpg','Gólfsalerni',None),('Ideal Standard Alpha vegghengt án skolbrúnar','vegghengt-salerni-an-skolbrunar-ideal-standard-alpha','3/8/3800828026742_1.jpg','Vegghengt',None),('Ellisse vegghengt m. hæglokandi setu','veggfest-salerni-ellisse-med-haeglokandi-setu','1/4/1488364.jpg','Vegghengt',None),('Laufen Roca The Gap vegghengt m. setu','vegghengt-salerni-an-skolbrunar-laufen-roca-the-gap-m-setu','1/0/1050894.jpg','Vegghengt',None),('Grohe Solido Compact klósett + kassi','vegghengt-salerni-og-salerniskassi-grohe-solido-compact','1/5/1520405.jpg','Vegghengt',None),('Laufen Rigo S-lás','salerni-s-las-laufen-rigo','7/6/7612738922719_0.jpg','Gólfsalerni',49995),('Hansgrohe EluPura Original m. setu','veggfest-salerni-hansgrohe-elupura-original-m-setu','1/4/1471109_0.jpg','Vegghengt',None),('Hansgrohe EluPura m. setu','veggfest-salerni-hansgrohe-elupura-m-setu','1/4/1471108_0.jpg','Vegghengt',None),('Flow vegghengt án skolbrúnar m. setu, svart','vegghengt-salerni-an-skolbrunar-flow-med-setu-svart','1/4/1496190.png','Vegghengt',None),('Camargue Norden 4300 S-lás','salerni-s-las-camargue-norden-4300','5/0/5010284c-39f6-4a6b-8eda-b934adb1215f.jpg','Gólfsalerni',None),('Ifö Sign S-lás hvítt','salerni-s-las-ifo-sign-hvitt','0/a/0a619dce-f080-412f-b14d-0fedab60b2a9.jpg','Gólfsalerni',None),('Duravit Starck 3 vegghengt án skolbrúnar m. setu','veggfest-salerni-an-skolbrunar-stark-3-duravit-m-setu','1/0/1052996.jpg','Vegghengt',99995),('Laufen Lua vegghengt m. hæglokandi setu','veggfest-salerni-laufen-lua-med-haeglokandi-setu','7/6/7612738004279.jpg','Vegghengt',None),('Villeroy & Boch O.novo Combi-Pack m. setu','vegghengt-salerni-villeroy-boch-o-novo-combi-pack-m-setu','1/0/1051017.jpg','Vegghengt',46295),('Ifö Sign 6860 S-lás án setu','salerni-s-las-ifo-sign-6860-an-setu','1/0/1053727.jpg','Gólfsalerni',None),('Laufen Kartell vegghengt grafítgrátt','veggfest-salerni-laufen-kartell-an-setu-grafit-gratt','1/4/1486719.png','Vegghengt',None),('Ifö Spira 6260 S-lás án skolbrúnar','salerni-s-las-an-skolbrunar-ifo-spira-6260-an-setu','1/0/1050897.jpg','Gólfsalerni',None),('Laufen Kompas S-lás án skolbrúnar','salerni-s-las-an-skolbrunar-laufen-kompas-an-setu','1/0/1053158.jpg','Gólfsalerni',None),('Ifö Sign P-lás án setu','salerni-p-las-ifo-sign-an-setu','c/4/c48875d8-5460-4d03-859d-a02f76a15883.jpg','Gólfsalerni',None)]
    for n,u,im,s,p in bk:
        add('klosett',n,'bauhaus',p,s=s,b=n.split()[0],url=B+u,img=BI+im,col='Svart' if 'svart' in n else ('Grátt' if 'grátt' in n else 'Hvítt'))
    for n,p,u in [('Keramag Renova nr.1 án skolbrúnar m. setu',69995,'https://www.bauhaus.is/vorumerki/keramag'),('Laufen Pro-N án skolbrúnar m. setu',80195,'https://www.bauhaus.is/vegghengt-salerni-an-skolbrunar-laufen-pro-n-m-setu'),('Geberit iCon án skolbrúnar m. setu',99995,'https://www.bauhaus.is/vorumerki/keramag')]:
        add('klosett',n,'bauhaus',p,s='Vegghengt',b=n.split()[0],url=u,col='Hvítt')
    add('klosett','Hatria Centrica Pure Vortex m. setu','husa',72990,s='Vegghengt',b='Hatria',url='https://www.husa.is/eldhus-og-badherbergi/salerni/veggtengd-salerni/wc-veggskal-med-setu-hatria-centrica-pure-vortex/',col='Hvítt')
    add('klosett','Hatria Centrica svört m. setu','husa',84990,s='Vegghengt',b='Hatria',url='https://www.husa.is/eldhus-og-badherbergi/salerni/veggtengd-salerni/wc-veggskal-svort-med-setu-hatria-centrica-pure-vortex/',col='Svart')
    add('klosett','Duravit Starck 3 vegghengt (seta sér)','isleifur',121582,s='Vegghengt',b='Duravit',url='https://isleifur.is/vegghengd-salerni',col='Hvítt')
    # kassar
    for n,u,im,p in [('Grohe Rapid SL 3in1 innbyggður kassi 113 cm','innbyggdur-salerniskassi-113cm-grohe-rapid-sl-3in1','1/0/1050840.jpg',None),('Grohe Solido 3in1 innbyggður kassi 113 cm króm','innbyggdur-salerniskassi-113cm-solido-3in1-grohe-krom','1/0/1003954.jpg',None),('Laufen Roca Duplo N innbyggður kassi 112 cm','innbyggdur-salerniskassi-112cm-laufen-roca-duplo-n','1/0/1053747.jpg',None),('Grohe Rapid SLX innbyggður kassi 113 cm','innbyggdur-salerniskassi-113cm-rapid-slx-grohe','4/c/4c136a40-2e16-4aaa-bf69-96eb11e55a0b.jpg',None),('Grohe Rapid SL innbyggður kassi 82 cm','innbyggdur-salerniskassi-82cm-grohe-rapid-sl','1/0/1053931.jpg',None)]:
        add('klosett',n,'bauhaus',p,s='Innbyggður kassi',b=n.split()[0],url=B+u,img=BI+im,col='Annað')
    add('klosett','TECE innbyggður kassi 82–112 cm','isleifur',49900,s='Innbyggður kassi',b='TECE',url='https://www.isleifur.is/product-category/badherbergi/salerni/salerniskassar/grindur/',col='Annað',x='Frá-verð')

    # ---------- Skolhnappar ----------
    sp = [('Geberit Delta 25',9686,'delta-25-thrystispjald/'),('Geberit Delta 15',11649,'delta-11-thrystispjald/'),('Geberit Delta 35',11649,'delta-50-thrystispjald/'),('Geberit Delta 50',13284,'delta-51-thrystispjald/'),('Geberit Sigma01 Round',13835,'sigma-01-thrystispjald/'),('Geberit Sigma20',20971,'sigma-20-thrystispjald/'),('Þrýstihnappur einfaldur króm',23954,'thrystihnappur-einfaldur-krom/'),('Geberit Sigma10',24682,'sigma-10-thrystispjald/'),('Geberit Omega30',24923,'omega-30-thrystispjald/'),('Geberit Omega20',24923,'omega-20-thrystispjald/'),('Geberit Delta15 stál',33339,'thrystispjald-delta-15-stal/'),('Geberit Sigma30 einfalt',34669,'sigma-30-einfalt-thrystispjald/'),('Geberit Sigma20 dual ryðfrítt',43236,'thrystispjald-sigma20-dual-rydfritt/'),('Geberit Sigma50',58411,'thrystispjald-sigma50/'),('Geberit Sigma21',64924,'sigma-21-thrystispjald/'),('VOLA þrýstihnappur burstað króm',73138,'vola-thrystihnappur-f-innb-wc-burstad-krom/'),('Geberit Sigma70 svart gler (snertifrítt)',83602,'thrystispjald-snertifritt-f-typu-70-svart-gler/'),('VOLA þrýstihnappur ryðfrítt',91048,'vola-thrystihnappur-f-innb-wc-rydfritt/'),('VOLA þrýstihnappur brushed brass',91048,'vola-thrystihnappur-f-innb-wc-brushed-brass/'),('VOLA þrýstispjald króm',150710,'vola-thrystispjald-krom-f-innb-wc/'),('VOLA þrýstispjald matt svart',162775,'vola-thrystispjald-matt-svart-f-innb-wc/'),('Dornbracht þrýstispjald',164047,'dornbracht-thrystispjald/'),('VOLA þrýstispjald ryðfrítt stál',174361,'vola-thrystispjald-rydfritt-stal-f-innb-wc/'),('VOLA þrýstispjald burstaður kopar',198137,'vola-thrystispjald-burstadur-kopar-f-innb-wc/')]
    for n,p,u in sp:
        add('skolhn',n,'tengi',p,s='Fyrir Geberit kassa' if 'Geberit' in n else 'Hönnunarhnappur',b=n.split()[0],url=T+'salerni/'+u,f=fin(n),col=fincol(n),x='Athugaðu hvort passar við kassann (Delta / Sigma / Omega)')
    for n,u,im in [('Laufen skolspjald tvöfalt hvítt','skolspjald-tvof-laufen-hvitt','1/0/1053135.jpg'),('Laufen skolspjald tvöfalt svart','skolspjald-tvof-laufen-svart','1/0/1051473.jpg'),('Grohe Skate Cosmopolitan króm','skolspjald-grohe-skate-cosmopolitan-krom','1/0/1053927.png'),('Oleas skolspjald hvítt','skolspjald-oleas-hvitt','3/3/3391500588509.jpg'),('Grohe Cosmopolitan burstað messing','skolspjald-grohe-cosmopolitan-burstad-messing','3/0/3003840C.jpg'),('Grohe Skate Cosmopolitan S hvítt','skolspjald-grohe-skate-cosmopolitan-s-hvitt','9/2/92d0390d-75d6-4e18-a000-e1e018f2cbae.jpg'),('Grohe Skate Cosmopolitan burstaður kopar','skolspjald-grohe-skate-cosmopolitan-burstadur-kopar','a/2/a22e25d1-30c2-4754-bb8d-b2fbdcc5d450.jpg'),('Grohe Cosmopolitan burstað svart','skolspjald-grohe-cosmopolitan-burstad-svart','3/7/377584d4-d407-4b61-b976-1c197faff6c1.jpg'),('Grohe Skate Cosmopolitan burstað stál','skolspjald-grohe-skate-cosmopolitan-burstad-stal','4/0/4005176431371.jpg'),('Symfo NT rafmagns skolspjald svart','skolspjald-rafmagns-symfo-nt-220x150-mm-svart','1/4/1488707.png'),('Oleas skolspjald PVD silfur','skolspjald-oleas-pvd-silfur','1/4/1488702.png')]:
        add('skolhn',n,'bauhaus',None,s='Fyrir Grohe kassa' if 'Grohe' in n else ('Fyrir Laufen kassa' if 'Laufen' in n else 'Annað'),b=n.split()[0],url=B+u,img=BI+im,f=fin(n),col=fincol(n))
    for n,p in [('Alcaplast M371 króm',6495),('Grohe Skate Cosmopolitan Al',23618),('Grohe Even',10943),('Grohe Even svartur',20468),('Alcaplast M575 gull',11094),('Skolhnappur hvítur',3495),('Grohe Alpine White',13418),('Alcaplast M570 hvítur',6160),('Alcaplast M572 matt króm',4977),('Grohe Skate Cosmopolitan DC',19194)]:
        add('skolhn',n,'husa',p,s='Fyrir Alcaplast kassa' if 'Alcaplast' in n else ('Fyrir Grohe kassa' if 'Grohe' in n else 'Annað'),b=n.split()[0],url='https://www.husa.is/eldhus-og-badherbergi/salerni/skolhnappar/',f=fin(n),col=fincol(n),x='Tilboðsverð 24.11.26')

def fin(n):
    l = n.lower()
    for k,v in [('matt svart','Matt svart'),('svart','Svart'),('svört','Svart'),('burstað króm','Burstað króm'),('króm','Króm'),('brass','Messing'),('messing','Messing'),('gyllt','Gyllt'),('gull','Gyllt'),('kopar','Kopar'),('ryðfrí','Ryðfrítt stál'),('stál','Stál'),('platinum','Platinum'),('grafít','Grafít'),('hvít','Hvítt')]:
        if k in l: return v
    return ''
def fincol(n):
    f = fin(n)
    return {'Matt svart':'Svart','Svart':'Svart','Hvítt':'Hvítt','Messing':'Gyllt / messing','Gyllt':'Gyllt / messing','Kopar':'Gyllt / messing'}.get(f, 'Stál / málmur' if f else 'Annað')
