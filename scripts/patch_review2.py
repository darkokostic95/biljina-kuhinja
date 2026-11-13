import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from patchlib import *
# torta s piškotama: variant with puslice (IMG_5659)
rep("torta-s-piskotama", "notes:", "notes:") if "notes:" in docs["torta-s-piskotama"][1] else None
docs["torta-s-piskotama"][1] += '\nnotes: {sr: "Druga verzija (IMG_5659/5660): umesto drugog reda piškota ide 400 g puslica potopljenih u preliv od 1/2 margarina, 300 g čokolade i malo mleka.", en: "Another version (IMG_5659/5660): the second layer is 400 g meringue kisses dipped in a glaze of 1/2 margarine block, 300 g chocolate and a little milk."}'
rep("pita-s-jogurtom-od-kora", "Kore iseckati na komadiće.", "Kore iseckati na faltice (trake).")
rep("pita-s-jogurtom-od-kora", "pola čaše zejtina, deblja čaša kisele vode", "malo više od pola čaše zejtina, ostatak čaše dopuniti kiselom vodom")
rep("pita-s-jogurtom-od-kora", "half a glass oil, a large glass sparkling water", "a little over half a glass oil, glass topped up with sparkling water")
title("opera-torta", "Opera torta")
rep("keks-torta-sa-bananama-i-kivijem", "2 l soka od narandže", "2 l Sinalka od narandže")
rep("keks-torta-sa-bananama-i-kivijem", "2 l orange drink", "2 l Sinalco orange soda")
delete("pita-iz-rastvora")
title("domace-kore-za-pitu", "Pure (domaće kore)", "Pure (Homemade Pastry Layers)")
rep("domace-kore-za-pitu", "Napraviti oko 70 loptica i svaku razvući oklagijom.", "Napraviti oko 70 loptica, svaku razvući oklagijom i uvijati.")
rep("domace-kore-za-pitu", "Make about 70 small balls and roll each out with a rolling pin.", "Make about 70 small balls, roll each out with a rolling pin and roll them up.")
rep("pileca-corba", "Meso izvaditi; posoliti čorbu dodati luk i kuvati još 10 minuta pa luk baciti.", "Posoliti po ukusu i dodati isečen crni luk zapečen na ringli; kuvati još 10 minuta pa luk izvaditi i baciti.")
rep("pileca-corba", "Remove the meat; salt the soup add the onion and cook 10 more minutes then discard the onion.", "Season and add the halved onion charred on the hob; cook 10 more minutes then remove and discard the onion.")
rep("pileca-corba", "Meso iseckati i vratiti.", "Meso izvaditi, iseckati i vratiti.")
rep("pileca-corba", "Chop the meat and return it.", "Take out the meat, chop it and return it.")
title("peckana-paprika-sa-medom", "Peckana paprika sa medom")
title("pecena-paprika-zimnica", "Cepkana paprika (zimnica)", "Chopped Roasted Peppers in Jars")
rep("pecena-paprika-zimnica", "Paprike iseckati i staviti zejtin da pokrije dno.", "Paprike iseckati; staviti zejtin da pokrije dno šerpe i smlačiti ga.")
rep("pecena-paprika-zimnica", "Chop the peppers and add enough oil to cover the base of the pot.", "Chop the peppers; warm enough oil to cover the base of the pot.")
title("sne-nokle", "Šnenokle")
rep("proja-sa-sirom", "sources: [IMG_5644, IMG_5673, IMG_5674, IMG_5669]", "sources: [IMG_5644, IMG_5673, IMG_5674]")
rep("slani-stapici", "Jednu stranu posuti susamom.", "Jednu stranu premazati smesom a drugu posuti susamom.")
rep("slani-stapici", "Sprinkle one side with sesame.", "Brush one side with the mixture and sprinkle the other with sesame.")
rep("meke-kiflice-sa-mascu", "Razvaljati i uviti kiflice", "Testo razvlačiti prema spolja i uviti kiflice")
rep("posni-slani-rolat-s-oblandom", "200 g kuvane žute soje (kockice)", "200 g kuvane žute soje (ljuspice)")
rep("posni-slani-rolat-s-oblandom", "200 g cooked soy chunks", "200 g cooked soy flakes")
rep("tulumbe", "Kad se testo ohladi dodati prašak i jaja i umutiti.", "Kad se testo ohladi dodati prašak i jaja (mutiti po 2 jaja).")
rep("tulumbe", "When cool beat in the baking powder and eggs.", "When cool beat in the baking powder and the eggs, two at a time.")
rep("tulumbe", "[600 g šećera, voda]", "[600 g šećera, vode koliko da prelije šećer]")
rep("tulumbe", "[600 g sugar, water]", "[600 g sugar, enough water to cover]")
rep("posne-zakusne-korice", "posne zakusne", "posne zakusne")
rep("sirup-za-iskasljavanje-sa-ratlukom", "4 lista rezede", "4 lista rezetle")
rep("sirup-za-iskasljavanje-sa-ratlukom", "4 leaves of reseda (herb)", "4 leaves of rezetla (herb)")
rep("domaci-sladoled", "1 limuntus (limunska kiselina)", "1 limontus (limunska kiselina)")
rep("domaci-sladoled", "sources: [IMG_5689, IMG_5690]", "sources: [IMG_5689]")
d = docs["domaci-sladoled"][1]; docs["domaci-sladoled"][1] = re.sub(r"\nnotes: .*", "", d)
rep("mons-torta", "200 g kapućino", "200 g Lions napolitanki")
rep("mons-torta", "200 g cappuccino powder", "200 g Lions wafer biscuits")
rep("mons-torta", "šlag kreme i kapućinom", "šlag kreme i napolitankama")
rep("mons-torta", "topping and the cappuccino", "topping and the crushed wafers")
title("kosa-piramida", "Posna piramida", "Lenten Turkish Delight Pyramid")
rep("kosa-piramida", "„Kosa piramida“ (IMG_5694)", "„Posna piramida“ (IMG_5694)")
rep("kosa-piramida", '\\"Kosa piramida\\"', '\\"Posna piramida\\"')
setdoc("susam-stanglice", """slug: susam-stanglice
title: {sr: Susam štanglice, en: Sesame Biscuit Bars}
category: bez-pecenja
tags: [bez-pecenja, susam, keks, orasi, cokolada]
sources: [IMG_5694]
ingredients:
- group: {sr: Sastojci, en: Ingredients}
  sr: [200 g šećera, srednja šolja vode, 100 g čokolade, 100 g seckanih oraha, 100 g mlevenih oraha, 100 g mlevenog keksa, 1/2 margarina, 100 g susama]
  en: [200 g sugar, a medium cup of water, 100 g chocolate, 100 g chopped walnuts, 100 g ground walnuts, 100 g ground biscuits, 1/2 margarine block, 100 g sesame]
steps:
  sr: [Susam ispržiti na suvo., Šećer i vodu ukuvati (ušpilovati)., Dodati čokoladu orahe keks margarin i susam i sve sjediniti., Rasporediti u pleh i kad se stegne seći na štanglice.]
  en: [Dry-toast the sesame., Boil the sugar and water to a syrup., Add the chocolate walnuts biscuits margarine and sesame and mix., Spread in a tin and cut into bars once set.]
notes: {sr: U svesci označeno „dobre“., en: Marked "good" in the notebook.}""")
rep("piramida-sa-keksom", "1 šaka izlomljenog keksa", "1 tanjir izlomljenog keksa")
rep("piramida-sa-keksom", "1 handful broken biscuits", "1 plateful broken biscuits")
rep("piramida-sa-keksom", "Šećer i vodu da provri pa skloniti.", "Šećer i vodu ukuvati (ušpilovati).")
rep("piramida-sa-keksom", "Bring the sugar and water to a boil then take off the heat.", "Boil the sugar and water to a syrup.")
title("orasnici", "Oraščići", "Walnut Chocolate Balls")
rep("kiflice-s-kokosom", "600 g brašna", "500 g brašna"); rep("kiflice-s-kokosom", "600 g flour", "500 g flour")
rep("ruske-kape", "Ispeći iz 2 dela i vaditi krugove čašicom.", "Ispeći iz 2 dela i patišpanj seći čašicom.")
setdoc("resetka", docs["resetka"][1].replace("slug: resetka", "slug: detelina"), "detelina")
title("detelina", "Detelina", "Clover Three-Colour Pyramid")
rep("rupice-od-butera", "150 g butera, 100 g šećera u prahu", "150 g putera, 120 g šećera u prahu")
rep("rupice-od-butera", "150 g butter, 100 g powdered sugar", "150 g butter, 120 g powdered sugar")
rep("kokos-stangle", "dodati 125 g butera", "dodati 125 g putera")
setdoc("stanglice-sa-ratlukom", """slug: stanglice-sa-keksom-i-rumom
title: {sr: Štanglice sa keksom i rumom, en: Biscuit and Rum Bars}
category: kolaci
tags: [orasi, keks, cokolada]
sources: [IMG_5698]
ingredients:
- group: {sr: Patišpanj, en: Sponge}
  sr: [6 jaja, 250 g šećera, 3 šoljice ulja, 200 g brašna, 1 prašak za pecivo, sok od pola limuna, džem od kajsije]
  en: [6 eggs, 250 g sugar, 3 small cups oil, 200 g flour, 1 baking powder, juice of half a lemon, apricot jam]
- group: {sr: Fil, en: Topping}
  sr: [2 šolje od bele kafe šećera, 1 šolja vode, 250 g keksa, 200 g oraha, 2 čašice ruma, 1 margarin, 2 štanglice čokolade, glazura]
  en: [2 coffee cups sugar, 1 cup water, 250 g biscuits, 200 g walnuts, 2 small glasses rum, 1 margarine block, 2 small bars chocolate, glaze]
steps:
  sr: [Ispeći patišpanj i kad se ohladi premazati džemom od kajsije., Šećer i vodu da provri pa dodati keks orahe rum margarin i čokoladu., Sve sjediniti i staviti preko patišpanja., Odozgo glazura i seći na štanglice.]
  en: [Bake the sponge and spread with apricot jam when cool., Boil the sugar and water then add the biscuits walnuts rum margarine and chocolate., Mix and spread over the sponge., Glaze and cut into bars.]""", "stanglice-sa-keksom-i-rumom")
rep("londonske-stangle-bez-oraha", "100 g butera", "100 g putera")
rep("londonske-stangle-bez-oraha", "Pomešati buter", "Pomešati puter")
rep("stangle-sa-dva-nadeva", "i sušiti na 150 °C.", "i pustiti na 150 °C da se osuši.")
setdoc("posne-bombice-sa-ratlukom", """slug: posne-grozdjice
title: {sr: Posne grožđice, en: Lenten Turkish Delight Grape Cluster}
category: bez-pecenja
tags: [posno, bez-pecenja, keks, cokolada]
sources: [IMG_5702]
ingredients:
- group: {sr: Sastojci, en: Ingredients}
  sr: [250 g roze ratluka, 200 g keksa, čokolada]
  en: [250 g pink Turkish delight, 200 g biscuits, chocolate]
steps:
  sr: [Ratluk i keks zamesiti i napraviti 6 loptica., Od loptica napraviti štapiće., "Ređati: 3 štapića pa čokolada, 2 štapića pa čokolada, 1 štapić pa čokolada.", Ostaviti da se stegne i seći.]
  en: [Knead the Turkish delight with the biscuits and make 6 balls., Roll the balls into sticks., "Stack: 3 sticks then chocolate, 2 sticks then chocolate, 1 stick then chocolate.", Leave to set and slice.]""", "posne-grozdjice")
rep("rozen-torta", "100 g šećera u prahu]", "100 g šećera u prahu, otopljen margarin]")
rep("rozen-torta", "100 g powdered sugar]", "100 g powdered sugar, melted margarine]")
rep("oblanda-s-eurokremom", "100 g mlevenih oraha, 100 g kokosa i 100 g seckanih oraha.", "100 g mlevenih oraha, 50 g seckanih oraha i 100 g kokosa; filovati oblandu i uviti u salamu.")
rep("oblanda-s-eurokremom", "100 g ground walnuts, 100 g coconut and 100 g chopped walnuts.", "100 g ground walnuts, 50 g chopped walnuts and 100 g coconut; spread on a wafer and roll into a log.")
setdoc("baklava", """slug: baklava
title: {sr: Baklava, en: Walnut Baklava Rolls}
category: pite
tags: [orasi, praznicno]
aliases: {sr: [baklava sa orasima], en: [walnut baklava]}
sources: [IMG_5719, IMG_5720]
ingredients:
- group: {sr: Sastojci, en: Ingredients}
  sr: [1/2 kg kora za pitu, 150 g margarina, 300 g mlevenih oraha, 100 g šećera, 1 dcl mleka, 3 kašike ulja, zejtin za premazivanje]
  en: [1/2 kg filo sheets, 150 g margarine, 300 g ground walnuts, 100 g sugar, 1 dl milk, 3 tbsp oil, oil for brushing]
- group: {sr: Sirup, en: Syrup}
  sr: [2 dcl vode, 500 g šećera, 1 isečen limun, 1 vanilin šećer]
  en: [2 dl water, 500 g sugar, 1 sliced lemon, 1 vanilla sugar sachet]
steps:
  sr: [Margarin orahe šećer mleko i ulje umutiti mikserom., Tri kore premazati zejtinom a na četvrtu staviti fil., Uviti u rolat i staviti u pleh — ponavljati dok ima kora., Peći na 200 °C., Prokuvati sirup i preliti pečenu baklavu.]
  en: [Beat the margarine walnuts sugar milk and oil with a mixer., Brush three sheets with oil and spread the filling on the fourth., Roll up and place in the tin — repeat with the remaining sheets., Bake at 200 °C., Boil the syrup and pour over the baked baklava.]""")
setdoc("kuglice-sa-kokosom-i-susamom", docs["kuglice-sa-kokosom-i-susamom"][1].replace("slug: kuglice-sa-kokosom-i-susamom", "slug: puslice-sa-kokosom-i-susamom"), "puslice-sa-kokosom-i-susamom")
title("puslice-sa-kokosom-i-susamom", "Puslice sa kokosom i susamom", "Coconut Sesame Cookies")
rep("puslice-sa-kokosom-i-susamom", "1 jogurtska čaša zejtina,", "1 jogurtska čaša zejtina (sipati do venca),")
rep("puslice-sa-kokosom-i-susamom", "Praviti kuglice i ispeći.", "Praviti bombice (kuglice) i ispeći.")
d = docs["vocni-kolac"][1]
docs["vocni-kolac"][1] = re.sub(r"\nnotes: .*", "", d) + '\nnotes: {sr: "Druga verzija (IMG_5706): patišpanj od 5 jaja, preko pošećerene jagode; fil od 1 l mleka, 8 kašika brašna i 8 kašika šećera, sjedinjen sa margarinom umućenim sa 200 g šećera u prahu, pa dodati 1 šlag kremu i koru od 1 limuna i mutiti još 5 minuta; odozgo šlag.", en: "Another version (IMG_5706): a 5-egg sponge topped with sugared strawberries; filling of 1 l milk, 8 tbsp flour and 8 tbsp sugar combined with margarine creamed with 200 g powdered sugar, then 1 whipped topping and the zest of 1 lemon beaten in for 5 more minutes; whipped cream on top."}'
rep("keks-torta-dobra", "Mutiti dok se ne ujednači i ostaviti da se prohladi.", "Još malo mutiti na pari da se masa izjednači i ostaviti da se prohladi.")
rep("keks-torta-dobra", "Beat until smooth and let cool.", "Beat a little more over steam until smooth and let cool.")
rep("vocna-torta-sa-keksom", "fil, voće, keks, fil, keks.", "fil, voće, fil, keks.")
rep("vocna-torta-sa-keksom", "filling, fruit, biscuits, filling, biscuits.", "filling, fruit, filling, biscuits.")
setdoc("stangle-sa-zelatinom", """slug: stangle-sa-zelatinom
title: {sr: Štangle sa želatinom, en: Marshmallow Wafer Bars}
category: bez-pecenja
tags: [bez-pecenja, oblanda]
sources: [IMG_5708]
ingredients:
- group: {sr: Sastojci, en: Ingredients}
  sr: [1 kesica želatina (10 g), 2 šoljice vode, 300 g šećera u prahu, žele po želji, listovi oblande]
  en: [1 sachet gelatine (10 g), 2 small cups water, 300 g powdered sugar, jelly (optional), wafer sheets]
steps:
  sr: [Želatin staviti u vodu i ostaviti pola sata na kraju šporeta., Preliti u vanglicu i dodati šećer u prahu., Mutiti dok ne postane gusta bela masa., Po želji dodati žele i sve staviti u oblandu; seći na štangle.]
  en: [Soak the gelatine in the water and leave it at the side of the stove for half an hour., Pour into a bowl and add the powdered sugar., Beat until thick and white., Add jelly if you like spread between wafer sheets and cut into bars.]""")
title("posne-bombice-sa-limunom", "Posna bombonjera", "Lenten Raspberry Lemon Bonbons")
rep("posne-bombice-sa-limunom", "Odozgo glazura od čokolade.", "Odozgo glazura od čokolade a preko nje malo bele glazure.")
rep("posne-bombice-sa-limunom", "Top with chocolate glaze.", "Top with chocolate glaze and a drizzle of white icing.")
rep("sareni-rolat", "300 g mlevenog keksa", "500 g mlevenog keksa"); rep("sareni-rolat", "300 g ground biscuits", "500 g ground biscuits")
rep("mak-pita", "ostaviti da malo odstoji.", "ostaviti sat vremena da odstoji.")
rep("mak-pita", "let stand a while.", "let stand for an hour.")
setdoc("car-na-dar", """slug: car-na-dar
title: {sr: Čar na dar štangle, en: Honey Sesame Cocoa Snack Bars}
category: bez-pecenja
tags: [bez-pecenja, med, susam, orasi, cokolada]
sources: [IMG_5713, IMG_5714]
ingredients:
- group: {sr: Sastojci, en: Ingredients}
  sr: [1 margarin, 250 g šećera u prahu, 200 g čokolade, 7 kašika meda, 100 g preprženog susama, 100 g seckanih oraha, malo manje od 1 kutije Čar na dar sa kakaom]
  en: [1 margarine block, 250 g powdered sugar, 200 g chocolate, 7 tbsp honey, 100 g toasted sesame, 100 g chopped walnuts, just under 1 box Čar na dar cocoa cereal]
steps:
  sr: [U većoj šerpi istopiti iseckan margarin šećer u prahu i čokoladu., Dodati med susam i orahe pa Čar na dar i sve izmešati., Sipati u podmazan pleh i dobro istapkati rukom., Kad se prohladi staviti u frižider 1-2 sata i seći oštrim nožem na štangle.]
  en: [Melt the chopped margarine powdered sugar and chocolate in a large pan., Add the honey sesame and walnuts then the cereal and mix., Tip into a greased tin and press down firmly by hand., When cool chill 1–2 hours and cut into bars with a sharp knife.]""")
rep("polumeseci-sa-alvom-i-kikirikijem", "200 g iseckanog i samlevenog kikirikija", "200 g pečenog i samlevenog kikirikija")
rep("polumeseci-sa-alvom-i-kikirikijem", "200 g chopped and ground peanuts", "200 g roasted ground peanuts")
rep("polumeseci-sa-alvom-i-kikirikijem", "mlaka voda,", "1 šoljica mlake vode,")
rep("polumeseci-sa-alvom-i-kikirikijem", "warm water,", "1 small cup warm water,")
rep("snikers-sa-kikirikijem", "100 g seckanog i mlevenog kikirikija]", "100 g pečenog i mlevenog kikirikija]")
rep("snikers-sa-kikirikijem", "100 g chopped and ground peanuts]", "100 g roasted ground peanuts]")
rep("snikers-sa-kikirikijem", "rasporediti u podmazan pleh.", "rasporediti u podmazan pleh debljine 1 cm.")
rep("snikers-sa-kikirikijem", "spread in a greased tin.", "spread 1 cm thick in a greased tin.")
rep("snikers-sa-kikirikijem", "rastopiti na pari", "rastopiti na tihoj vatri")
rep("snikers-sa-kikirikijem", "Melt the egg sugar and margarine over steam", "Melt the egg sugar and margarine over low heat")
setdoc("pusice-sa-orasima", """slug: padobranci
title: {sr: Padobranci, en: Walnut Meringue Parachutes}
category: sitni-kolaci
tags: [orasi]
sources: [IMG_5715]
ingredients:
- group: {sr: Sastojci, en: Ingredients}
  sr: [5 belanaca, 250 g šećera, 300 g mlevenih oraha, 5 žumanaca, 5 kašika šećera, šećer u prahu]
  en: [5 egg whites, 250 g sugar, 300 g ground walnuts, 5 egg yolks, 5 tbsp sugar, powdered sugar]
steps:
  sr: [Umutiti belanca sa šećerom pa dodati orahe., Špricem stavljati u pleh kao puslice i peći (sušiti)., Žumanca i šećer skuvati na pari i filovati., Iseći na kocke i valjati u šećer u prahu.]
  en: [Whisk the whites with the sugar then fold in the walnuts., Pipe onto a tray like meringue kisses and bake (dry)., Cook the yolks and sugar over steam and use as filling., Cut into pieces and roll in powdered sugar.]""", "padobranci")
rep("macje-oci", "Ispeći koru.", "Ispeći koru i vruću uviti u vlažnu krpu.")
rep("macje-oci", "Bake the sponge.", "Bake the sponge and roll it up in a damp cloth while hot.")
title("gnezdo-torta", "Ljubavno gnezdo", "Love Nest Cake")
rep("gnezdo-torta", "sušiti na 180 °C", "sušiti na 150 °C"); rep("gnezdo-torta", "dry at 180 °C", "dry at 150 °C")
rep("sedmo-nebo", "dodati umućen margarin i čokoladu.", "dodati umućen margarin (može i čokolada).")
rep("sedmo-nebo", "add the creamed margarine and chocolate.", "add the creamed margarine (chocolate optional).")
title("kiflice-pecene-u-kalupu", "Kiflice pečene u kalupu", "Walnut Crescents Dipped in Chocolate")
rep("kiflice-pecene-u-kalupu", "100 g šećera u prahu", "400 g šećera u prahu"); rep("kiflice-pecene-u-kalupu", "100 g powdered sugar", "400 g powdered sugar")
setdoc("cokoladna-torta-sa-lesnikom", """slug: cembrlen-torta
title: {sr: Čembrlen torta, en: Chamberlain Cake}
category: torte
tags: [cokolada, orasi, lesnik, praznicno]
sources: [IMG_5720, IMG_5721]
ingredients:
- group: {sr: Kore (×3), en: Layers (×3)}
  sr: [4 belanca, 130 g šećera, 130 g prepečenih mlevenih oraha, 1 i po kašika ulja]
  en: [4 egg whites, 130 g sugar, 130 g toasted ground walnuts, 1.5 tbsp oil]
- group: {sr: Fil, en: Filling}
  sr: [2 žumanca, 4 kašike šećera, 2 kašike gustina, 250 ml mleka, 12 žumanaca, 12 kašika šećera, 2 štangle čokolade, 5 vanilin šećera, 350 g margarina]
  en: [2 egg yolks, 4 tbsp sugar, 2 tbsp cornstarch, 250 ml milk, 12 egg yolks, 12 tbsp sugar, 2 bars chocolate, 5 vanilla sugar sachets, 350 g margarine]
- group: {sr: Grilijaš, en: Hazelnut brittle}
  sr: [250 g šećera, 200 g pečenih mlevenih lešnika, šlag]
  en: [250 g sugar, 200 g roasted ground hazelnuts, whipped cream]
steps:
  sr: [Umutiti belanca uz postepeno dodavanje šećera pa dodati orahe i ulje; ispeći 3 kore na 200 °C u dobro podmazanom plehu ili na papiru za pečenje., I fil (2 žumanca šećer gustin mleko) skuvati na pari., II fil (12 žumanaca i šećer) kuvati na pari a pred kraj dodati čokoladu i vanilu., Ohlađene filove sjediniti i dodati umućen margarin., Šećer rastopiti dodati lešnik izručiti u podmazan pleh da se stegne pa izlomiti i samleti., "Filovati: kora, fil, mleveni grilijaš — na kraju šlag."]
  en: [Whisk the whites adding the sugar gradually then the walnuts and oil; bake 3 layers at 200 °C in a well-greased tin or on baking paper., Cook filling I (2 yolks sugar cornstarch milk) over steam., Cook filling II (12 yolks and sugar) over steam adding the chocolate and vanilla at the end., Combine the cooled fillings and beat in the margarine., Melt the sugar add the hazelnuts pour onto a greased tray to set then break up and grind., "Layer: sponge, filling, ground brittle — finish with whipped cream."]""", "cembrlen-torta")
setdoc("pijane-stangle", """slug: grilijas-stangle
title: {sr: Grilijaš štangle, en: Nut Brittle Wafer Bars}
category: bez-pecenja
tags: [bez-pecenja, oblanda, orasi]
sources: [IMG_5721]
ingredients:
- group: {sr: Sastojci, en: Ingredients}
  sr: [300 g šećera, 2 jaja, 250 g šećera u prahu, 1 margarin, 100 g seckanih oraha, 100 g suvog grožđa, 3 male oblande]
  en: [300 g sugar, 2 eggs, 250 g powdered sugar, 1 margarine block, 100 g chopped walnuts, 100 g raisins, 3 small wafer sheets]
steps:
  sr: [Šećer otopiti na suvo (grilijaš)., Jaja i šećer u prahu kuvati na pari i dodati margarin., Kad se skuva dodati u vreo grilijaš zajedno sa orasima i grožđem., Promešati još malo na tihoj vatri pa lepiti sa 3 male oblande.]
  en: [Melt the sugar dry to a caramel., Cook the eggs and powdered sugar over steam and add the margarine., Stir into the hot caramel together with the walnuts and raisins., Stir a little longer over low heat then sandwich between 3 small wafer sheets.]""", "grilijas-stangle")
d = docs["cokoladna-torta-jednostavna"][1]
docs["cokoladna-torta-jednostavna"][1] = d.replace("Filovati koru i odozgo šlag.", "Koru natopiti mlekom filovati i odozgo šlag.").replace("Fill the sponge and top with whipped cream.", "Soak the sponge with milk fill it and top with whipped cream.") + '\nnotes: {sr: "Bilјin fil (\\"fil moj\\"): 750 g mleka, 3 pudinga od čokolade, 200 g čokolade, 2 kašike kakaa, 1 i po margarin, 150 g šećera u prahu.", en: "Bilja\'s own filling: 750 g milk, 3 chocolate puddings, 200 g chocolate, 2 tbsp cocoa, 1.5 margarine blocks, 150 g powdered sugar."}'
docs["cokoladna-torta-jednostavna"][1] = docs["cokoladna-torta-jednostavna"][1].replace("Bilјin", "Biljin")
rep("oblanda-sa-mlekom-u-prahu", "[100 g šećera, malo vode", "[400 g šećera, malo vode")
rep("oblanda-sa-mlekom-u-prahu", "[100 g sugar, a little water", "[400 g sugar, a little water")
title("oblanda-sa-mlekom-u-prahu", "Oblanda sa pahuljicama", "Wafer Slice with White Flakes")
save()
