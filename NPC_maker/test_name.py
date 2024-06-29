import random
sex = ["male", "female"]

race = {
    "dragonborn": {
        "color": [
            "black", "blue", "brass", "bronze", "copper", "gold", "green", "red", "silver", "white"
        ],
        "male": [
            "Adrex", "Arjhan", "Azzakh", "Balasar", "Baradad", "Bharash", "Bidreked", "Dadalan", "Dazzazn", "Direcris",
            "Donaar", "Fax", "Gargax", "Ghesh", "Gorbundus", "Greethen", "Heskan", "Hirrathak", "Ildrex", "Kaladan",
            "Kerkad", "Kiirith", "Kriv", "Maagog", "Medrash", "Mehen", "Mozikth", "Mreksh", "Mugrunden", "Nadarr",
            "Nithther", "Norkruuth", "Nykkan", "Pandjed", "Patrin", "Pijjirik", "Quarethon", "Rathkran", "Rhogar",
            "Rivaan", "Sethrekar", "Shamash", "Shedinn", "Srorthen", "Tarhun", "Torinn", "Trynnicus", "Valorean",
            "Vrondiss", "Zedaar"
        ],
        "female": [
            "Akra", "Aasathra", "Antrara", "Arava", "Biri", "Blendaeth", "Burana", "Chassath", "Daar", "Dentratha",
            "Doudra", "Driindar", "Eggren", "Farideh", "Findex", "Furrele", "Gesrethe", "Gilkass", "Harann",
            "Havilar", "Hethress", "Hillanot", "Jaxi", "Jezean", "Jheri", "Kadana", "Kava", "Korinn", "Megren",
            "Mijira", "Mishann", "Nala", "Nuthra", "Perra", "Pogranix", "Pyxrin", "Quespa", "Raiann", "Rezena",
            "Ruloth", "Saphara", "Savaran", "Sora", "Surina", "Synthrin", "Tatyan", "Thava", "Uadjit", "Vezera",
            "Zykroff"
        ],
        "clan": [
            "Akambherylliax", "Argenthrixus", "Baharoosh", "Beryntolthropal", "Bhenkumbyrznaax", "Caavylteradyn",
            "Chumbyxirinnish", "Clethtinthiallor", "Daardendrian", "Delmirev", "Dhyrktelonis", "Ebynichtomonis",
            "Esstyrlynn", "Fharngnarthnost", "Ghaallixirn", "Grrrmmballhyst", "Gygazzylyshrift", "Hashphronyxadyn",
            "Hshhsstoroth", "Imbixtellrhyst", "Jerynomonis", "Jharthraxyn", "Kerrhylon", "Kimbatuul",
            "Lhamboldennish", "Linxakasendalor", "Mohradyllion", "Mystan", "Nemmonis", "Norixius", "Ophinshtalajiir",
            "Orexijandilin", "Pfaphnyrennish", "Phrahdrandon", "Pyraxtallinost", "Qyxpahrgh", "Raghthroknaar",
            "Shestendeliath", "Skaarzborroosh", "Sumnarghthrysh", "Tiammanthyllish", "Turnuroth", "Umbyrphrael",
            "Vangdondalor", "Verthisathurgiesh", "Wivvyrholdalphiax", "Wystongjiir", "Xephyrbahnor", "Yarjerit",
            "Zzzxaaxthroth"
        ]
    },

    "dwarf": {
        "subrace": [
            "mountain", "hill"
        ],
        "male": [
            "Adrik", "Alberich", "Baern", "Barendd", "Beloril", "Brottor", "Dain", "Dalgal", "Darrak", "Delg",
            "Duergath", "Dworic", "Eberk", "Einkil", "Elaim", "Erias", "Fallond", "Fargrim", "Gardain", "Gilthur",
            "Gimgen", "Gimurt", "Harbek", "Kildrak", "Kilvar", "Morgran", "Morkral", "Nalral", "Nordak", "Nuraval",
            "Oloric", "Olunt", "Orsik", "Oskar", "Rangrim", "Reirak", "Rurik", "Taklinn", "Thoradin", "Thorin",
            "Thradal", "Tordek", "Traubon", "Travok", "Ulfgar", "Uraim", "Veit", "Vonbin", "Vondal", "Whurbin"
        ],
        "female": [
            "Anbera", "Artin", "Audhild", "Balifra", "Barbena", "Bardryn", "Bolhild", "Dagnal", "Dariff", "Delre",
            "Diesa", "Eldeth", "Eridred", "Falkrunn", "Fallthra", "Finellen", "Gillydd", "Gunnloda", "Gurdis",
            "Helgret", "Helja", "Hlin", "Ilde", "Jarana", "Kathra", "Kilia", "Kristryd", "Liftrasa", "Marastyr",
            "Mardred", "Morana", "Nalaed", "Nora", "Nurkara", "Oriff", "Ovina", "Riswynn", "Sannl", "Therlin",
            "Thodris", "Torbera", "Tordrid", "Torgga", "Urshar", "Valida", "Vistra", "Vonana", "Werydd", "Whurdred",
            "Yurgunn"
        ],
        "clan": [
            "Aranore", "Balderk", "Battlehammer", "Bigtoe", "Bloodkith", "Bofdann", "Brawnanvil", "Brazzik",
            "Broodfist", "Burrowfound", "Caebrek", "Daerdahk", "Dankil", "Daraln", "Deepdelver", "Durthane",
            "Eversharp", "Fallack", "Fireforge", "Foamtankard", "Frostbeard", "Glanhig", "Goblinbane", "Goldfinder",
            "Gorunn", "Graybeard", "Hammerstone", "Helcral", "Holderhek", "Ironfist", "Loderr", "Lutgehr", "Morigak",
            "Orcfoe", "Rakankrak", "Ruby-Eye", "Rumnaheim", "Silveraxe", "Silverstone", "Steelfist", "Stoutale",
            "Strakeln", "Strongheart", "Thrahak", "Torevir", "Torunn", "Trollbleeder", "Trueanvil", "Trueblood",
            "Ungart"
        ]
    },


    "elf": {
        "subrace": [
            "high", "wood", "drow"
        ],
        "child": [
            "Ael", "Ang", "Ara", "Ari", "Arn", "Aym", "Broe", "Bryn", "Cael", "Cy", "Dae", "Del", "Eli", "Eryn",
            "Faen", "Fera", "Gael", "Gar", "Innil", "Jar", "Kan", "Koeth", "Lael", "Lue", "Mai", "Mara", "Mella",
            "Mya", "Naeris", "Naill", "Nim", "Phann", "Py", "Rael", "Raer", "Ren", "Rinn", "Rua", "Sael", "Sai",
            "Sumi", "Syllin", "Ta", "Thia", "Tia", "Traki", "Vall", "Von", "Wil", "Za"
        ],
        "male": [
            "Adran", "Aelar", "Aerdeth", "Ahvain", "Aramil", "Arannis", "Aust", "Azaki", "Beiro", "Berrian",
            "Caeldrim", "Carric", "Dayereth", "Dreali", "Efferil", "Eiravel", "Enialis", "Erdan", "Erevan", "Fivin",
            "Galinndan", "Gennal", "Hadarai", "Halimath", "Heian", "Himo", "Immeral", "Ivellios", "Korfel", "Lamlis",
            "Laucian", "Lucan", "Mindartis", "Naal", "Nutae", "Paelias", "Peren", "Quarion", "Riardon", "Rolen",
            "Soveliss", "Suhnae", "Thamior", "Tharivol", "Theren", "Theriatis", "Thervan", "Uthemar", "Vanuath",
            "Varis"
        ],
        "female": [
            "Adrie", "Ahinar", "Althaea", "Anastrianna", "Andraste", "Antinua", "Arara", "Baelitae", "Bethrynna",
            "Birel", "Caelynn", "Chaedi", "Claira", "Dara", "Drusilia", "Elama", "Enna", "Faral", "Felosial", "Hatae",
            "Ielenia", "Ilanis", "Irann", "Jarsali", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Maiathah", "Malquis",
            "Meriele", "Mialee", "Myathethil", "Naivara", "Quelenna", "Quillathe", "Ridaro", "Sariel", "Shanairla",
            "Shava", "Silaqui", "Sumnes", "Theirastra", "Thiala", "Tiaathque", "Traulam", "Vadania", "Valanthe", "Valna",
            "Xanaphia"
        ],
        "clan": [
            "Aloro", "Amakiir", "Amastacia", "Ariessus", "Arnuanna", "Berevan", "Caerdonel", "Caphaxath",
            "Casilltenirra", "Cithreth", "Dalanthan", "Eathalena", "Erenaeth", "Ethanasath", "Fasharash", "Firahel",
            "Floshem", "Galanodel", "Goltorah", "Hanali", "Holimion", "Horineth", "Iathrana", "Ilphelkiir", "Iranapha",
            "Koehlanna", "Lathalas", "Liadon", "Meliamne", "Mellerelel", "Mystralath", "NaÃ¯lo", "Netyoive", "Ofandrus",
            "Ostoroth", "Othronus", "Qualanthri", "Raethran", "Rothenel", "Selevarun", "Siannodel", "Suithrasas",
            "Sylvaranth", "Teinithra", "Tiltathana", "Wasanthi", "Withrethin", "Xiloscient", "Xistsrith", "Yaeldrin"
        ]
    },


    "gnome": {
        "subrace": [
            "forest", "rock", "deep"
        ],
        "male": [
            "Alston", "Alvyn", "Anverth", "Arumawann", "Bilbron", "Boddynock", "Brocc", "Burgell", "Cockaby",
            "Crampernap", "Dabbledob", "Delebean", "Dimble", "Eberdeb", "Eldon", "Erky", "Fablen", "Fibblestib",
            "Fonkin", "Frouse", "Frug", "Gerbo", "Gimble", "Glim", "Igden", "Jabble", "Jebeddo", "Kellen", "Kipper",
            "Namfoodle", "Oppleby", "Orryn", "Paggen", "Pallabar", "Pog", "Qualen", "Ribbles", "Rimple", "Roondar",
            "Sapply", "Seebo", "Senteq", "Sindri", "Umpen", "Warryn", "Wiggens", "Wobbles", "Wrenn", "Zaffrab", "Zook"
        ],
        "female": [
            "Abalaba", "Bimpnottin", "Breena", "Buvvie", "Callybon", "Caramip", "Carlin", "Cumpen", "Dalaba",
            "Donella", "Duvamil", "Ella", "Ellyjoybell", "Ellywick", "Enidda", "Lilli", "Loopmottin", "Lorilla",
            "Luthra", "Mardnab", "Meena", "Menny", "Mumpena", "Nissa", "Numba", "Nyx", "Oda", "Oppah", "Orla", "Panana",
            "Pyntle", "Quilla", "Ranala", "Reddlepop", "Roywyn", "Salanop", "Shamil", "Siffress", "Symma", "Tana",
            "Tenena", "Tervaround", "Tippletoe", "Ulla", "Unvera", "Veloptima", "Virra", "Waywocket", "Yebe", "Zanna"
        ],
        "clan": [
            "Albaratie", "Bafflestone", "Beren", "Boondiggles", "Cobblelob", "Daergel", "Dunben", "Fabblestabble",
            "Fapplestamp", "Fiddlefen", "Folkor", "Garrick", "Gimlen", "Glittergem", "Gobblefirn", "Gummen",
            "Horcusporcus", "Humplebumple", "Ironhide", "Leffery", "Lingenhall", "Loofollue", "Maekkelferce", "Miggledy",
            "Munggen", "Murnig", "Musgraben", "Nackle", "Ningel", "Nopenstallen", "Nucklestamp", "Offund", "Oomtrowl",
            "Pilwicken", "Pingun", "Quillsharpener", "Raulnor", "Reese", "Rofferton", "Scheppen", "Shadowcloak",
            "Silverthread", "Sympony", "Tarkelby", "Timbers", "Turen", "Umbodoben", "Waggletop", "Welber", "Wildwander"
        ]
    },

    "halfling": {
        "subrace": [
            "lightfoot", "stout"
        ],
        "male": [
            "Alton", "Ander", "Bernie", "Bobbin", "Cade", "Callus", "Corrin", "Dannad", "Danniel", "Eddie", "Egart",
            "Eldon", "Errich", "Fildo", "Finnan", "Franklin", "Garret", "Garth", "Gilbert", "Gob", "Harol", "Igor",
            "Jasper", "Keith", "Kevin", "Lazam", "Lerry", "Lindal", "Lyle", "Merric", "Mican", "Milo", "Morrin", "Nebin",
            "Nevil", "Osborn", "Ostran", "Oswalt", "Perrin", "Poppy", "Reed", "Roscoe", "Sam", "Shardon", "Tye", "Ulmo",
            "Wellby", "Wendel", "Wenner", "Wes"
        ],
        "female": [
            "Alain", "Andry", "Anne", "Bella", "Blossom", "Bree", "Callie", "Chenna", "Cora", "Dee", "Dell", "Eida",
            "Eran", "Euphemia", "Georgina", "Gynnie", "Harriet", "Jasmine", "Jillian", "Jo", "Kithri", "Lavinia", "Lidda",
            "Maegan", "Marigold", "Merla", "Myria", "Nedda", "Nikki", "Nora", "Olivia", "Paela", "Pearl", "Pennie",
            "Philomena", "Portia", "Robbie", "Rose", "Saral", "Seraphina", "Shaena", "Stacee", "Tawna", "Thea", "Trym",
            "Tyna", "Vani", "Verna", "Wella", "Willow"
        ],
        "clan": [
            "Appleblossom", "Bigheart", "Brightmoon", "Brushgather", "Cherrycheeks", "Copperkettle", "Deephollow",
            "Elderberry", "Fastfoot", "Fatrabbit", "Glenfellow", "Goldfound", "Goodbarrel", "Goodearth", "Greenbottle",
            "Greenleaf", "High-hill", "Hilltopple", "Hogcollar", "Honeypot", "Jamjar", "Kettlewhistle", "Leagallow",
            "Littlefoot", "Nimblefingers", "Porridgepot", "Quickstep", "Reedfellow", "Shadowquick", "Silvereyes",
            "Smoothhands", "Stonebridge", "Stoutbridge", "Stoutman", "Strongbones", "Sunmeadow", "Swiftwhistle",
            "Tallfellow", "Tealeaf", "Tenpenny", "Thistletop", "Thorngage", "Tosscobble", "Underbough", "Underfoot",
            "Warmwater", "Whispermouse", "Wildcloak", "Wildheart", "Wiseacre"
        ]
    },

    "half-orc": {
        "male": [
            "Argran", "Braak", "Brug", "Cagak", "Dench", "Dorn", "Dren", "Druuk", "Feng", "Gell", "Gnarsh", "Grumbar",
            "Gubrash", "Hagren", "Henk", "Hogar", "Holg", "Imsh", "Karash", "Karg", "Keth", "Korag", "Krusk", "Lubash",
            "Megged", "Mhurren", "Mord", "Morg", "Nil", "Nybarg", "Odorr", "Ohr", "Rendar", "Resh", "Ront", "Rrath",
            "Sark", "Scrag", "Sheggen", "Shump", "Tanglar", "Tarak", "Thar", "Thokk", "Trag", "Ugarth", "Varg",
            "Vilberg", "Yurk", "Zed"
        ],
        "female": [
            "Arha", "Baggi", "Bendoo", "Bilga", "Brakka", "Creega", "Drenna", "Ekk", "Emen", "Engong", "Fistula",
            "Gaaki", "Gorga", "Grai", "Greeba", "Grigi", "Gynk", "Hrathy", "Huru", "Ilga", "Kabbarg", "Kansif",
            "Lagazi", "Lezre", "Murgen", "Murook", "Myev", "Nagrette", "Neega", "Nella", "Nogu", "Oolah", "Ootah",
            "Ovak", "Ownka", "Puyet", "Reeza", "Shautha", "Silgre", "Sutha", "Tagga", "Tawar", "Tomph", "Ubada",
            "Vanchu", "Vola", "Volen", "Vorka", "Yevelda", "Zagga"
        ]
    },

    "human": {
        "culture": {
            "arabic": {
                "male": [
                    "Abbad", "Abdul", "Achmed", "Akeem", "Alif", "Amir", "Asim", "Bashir", "Bassam", "Fahim", "Farid",
                    "Farouk", "Fayez", "Fayyaad", "Fazil", "Hakim", "Halil", "Hamid", "Hazim", "Heydar", "Hussein",
                    "Jabari", "Jafar", "Jahid", "Jamal", "Kalim", "Karim", "Kazim", "Khadim", "Khalid", "Mahmud",
                    "Mansour", "Musharraf", "Mustafa", "Nadir", "Nazim", "Omar", "Qadir", "Qusay", "Rafiq", "Rakim",
                    "Rashad", "Rauf", "Saladin", "Sami", "Samir", "Talib", "Tamir", "Tariq", "Yazid"
                ],
                "female": [
                    "Aaliyah", "Aida", "Akilah", "Alia", "Amina", "Atefeh", "Chaima", "Dalia", "Ehsan", "Elham", "Farah",
                    "Fatemah", "Gamila", "Iesha", "Inbar", "Kamaria", "Khadija", "Layla", "Lupe", "Nabila", "Nadine",
                    "Naima", "Najila", "Najwa", "Nakia", "Nashwa", "Nawra", "Nuha", "Nura", "Oma", "Qadira", "Qamar",
                    "Qistina", "Rahima", "Rihanna", "Saadia", "Sabah", "Sada", "Saffron", "Sahar", "Salma", "Shatha",
                    "Tahira", "Takisha", "Thana", "Yadira", "Zahra", "Zaida", "Zaina", "Zeinab"
                ],
                "surname": [
                    "Benchikh", "HabibAllah", "Mekki", "Abid", "Salem", "Saleem", "Omari", "Hamedi", "Hammam", "Hachemi", "Khalil"
                ]
            },

            "celtic": {
                "male": [
                    "Airell", "Airic", "Alan", "Anghus", "Aodh", "Bardon", "Bearacb", "Bevyn", "Boden", "Bran", "Brasil",
                    "Bredon", "Brian", "Bricriu", "Bryant", "Cadman", "Caradoc", "Cedric", "Conalt", "Conchobar",
                    "Condon", "Darcy", "Devin", "Dillion", "Donaghy", "Donall", "Duer", "Eghan", "Ewyn", "Ferghus",
                    "Galvyn", "Gildas", "Guy", "Harvey", "Iden", "Irven", "Karney", "Kayne", "Kelvyn", "Kunsgnos",
                    "Leigh", "Maccus", "Moryn", "Neale", "Owyn", "Pryderi", "Reaghan", "Taliesin", "Tiernay", "Turi"
                ],
                "female": [
                    "Aife", "Aina", "Alane", "Ardena", "Arienh", "Beatha", "Birgit", "Briann", "Caomh", "Cara", "Cinnia",
                    "Cordelia", "Deheune", "Divone", "Donia", "Doreena", "Elsha", "Enid", "Ethne", "Evelina", "Fianna",
                    "Genevieve", "Gilda", "Gitta", "Grania", "Gwyndolin", "Idelisa", "Isolde", "Keelin", "Kennocha",
                    "Lavena", "Lesley", "Linnette", "Lyonesse", "Mabina", "Marvina", "Mavis", "Mirna", "Morgan", "Muriel",
                    "Nareena", "Oriana", "Regan", "Ronat", "Rowena", "Selma", "Ula", "Venetia", "Wynne", "Yseult"
                ],
                "surname": [
                    "Murphy", "Kelly", "O'Brien", "Ryan", "Byrne", "O'Connor", "Walsh", "O'Sullivan", "McCarthy", "Doyle"
                ]
            },

            "chinese": {
                "male": [
                    "Bingwen", "Bo", "Bolin", "Chang", "Chao", "Chen", "Cheng", "Da", "Dingxiang", "Fang",
                    "Feng", "Fu", "Gang", "Guang", "Hai", "Heng", "Hong", "Huan", "Huang", "Huiliang",
                    "Huizhong", "Jian", "Jiayi", "Junjie", "Kang", "Lei", "Liang", "Ling", "Liwei", "Meilin",
                    "Niu", "Peizhi", "Peng", "Ping", "Qiang", "Qiu", "Quan", "Renshu", "Rong", "Ru",
                    "Shan", "Shen", "Tengfei", "Wei", "Xiaobo", "Xiaoli", "Xin", "Yang", "Ying", "Zhong"
                ],
                "female": [
                    "Ai", "Anming", "Baozhai", "Bei", "Caixia", "Changchang", "Chen", "Chou", "Chunhua", "Daianna",
                    "Daiyu", "Die", "Ehuang", "Fenfang", "Ge", "Hong", "Huan", "Huifang", "Jia", "Jiao", "Jiaying",
                    "Jingfei", "Jinjing", "Lan", "Li", "Lihua", "Lin", "Ling", "Liu", "Meili", "Ning", "Qi", "Qiao",
                    "Rong", "Shu", "Shuang", "Song", "Ting", "Wen", "Xia", "Xiaodan", "Xiaoli", "Xingjuan", "Xue",
                    "Ya", "Yan", "Ying", "Yuan", "Yue", "Yun"
                ],
                "surname": [
                    "Wang", "Li", "Zhang", "Liu", "Chen", "Yang", "Huang", "Zhao", "Wu", "Zhou"
                ]
            },

            "egyptian": {
                "male": [
                    "Ahmose", "Akhom", "Amasis", "Amenemhet", "Anen", "Banefre", "Bek", "Djedefre", "Djoser", "Hekaib",
                    "Henenu", "Horemheb", "Horwedja", "Huya", "Ibebi", "Idu", "Imhotep", "Ineni", "Ipuki", "Irsu",
                    "Kagemni", "Kawab", "Kenamon", "Kewap", "Khaemwaset", "Khafra", "Khusebek", "Masaharta", "Meketre",
                    "Menkhaf", "Merenre", "Metjen", "Nebamun", "Nebetka", "Nehi", "Nekure", "Nessumontu", "Pakhom",
                    "Pawah", "Pawero", "Ramose", "Rudjek", "Sabaf", "Sebek-khu", "Sebni", "Senusret", "Shabaka",
                    "Somintu", "Thaneni", "Thethi"
                ],
                "female": [
                    "Airell", "Airic", "Alan", "Anghus", "Aodh", "Bardon", "Bearacb", "Bevyn", "Boden", "Bran", "Brasil",
                    "Bredon", "Brian", "Bricriu", "Bryant", "Cadman", "Caradoc", "Cedric", "Conalt", "Conchobar", "Condon",
                    "Darcy", "Devin", "Dillion", "Donaghy", "Donall", "Duer", "Eghan", "Ewyn", "Ferghus", "Galvyn", "Gildas",
                    "Guy", "Harvey", "Iden", "Irven", "Karney", "Kayne", "Kelvyn", "Kunsgnos", "Leigh", "Maccus", "Moryn",
                    "Neale", "Owyn", "Pryderi", "Reaghan", "Taliesin", "Tiernay", "Turi"
                ],
                "surname": [
                    "Salem", "Hash", "Tahir", "Ramadan", "Salama", "Nasr", "Hamed", "Abbas", "Hussein", "Othman"
                ]
            },

            "english": {
                "male": [
                    "Adam", "Adelard", "Aldous", "Anselm", "Arnold", "Bernard", "Bertram", "Charles", "Clerebold",
                    "Conrad", "Diggory", "Drogo", "Everard", "Frederick", "Geoffrey", "Gerald", "Gilbert", "Godfrey",
                    "Gunter", "Guy", "Henry", "Heward", "Hubert", "Hugh", "Jocelyn", "John", "Lance", "Manfred", "Miles",
                    "Nicholas", "Norman", "Odo", "Percival", "Peter", "Ralf", "Randal", "Raymond", "Reynard", "Richard",
                    "Robert", "Roger", "Roland", "Rolf", "Simon", "Theobald", "Theodoric", "Thomas", "Timm", "William",
                    "Wymar"
                ],
                "female": [
                    "Adelaide", "Agatha", "Agnes", "Alice", "Aline", "Anne", "Avelina", "Avice", "Beatrice", "Cecily",
                    "Egelina", "Eleanor", "Elizabeth", "Ella", "Eloise", "Elysande", "Emeny", "Emma", "Emmeline", "Ermina",
                    "Eva", "Galiena", "Geva", "Giselle", "Griselda", "Hadwisa", "Helen", "Herleva", "Hugolina", "Ida",
                    "Isabella", "Jacoba", "Jane", "Joan", "Juliana", "Katherine", "Margery", "Mary", "Matilda", "Maynild",
                    "Millicent", "Oriel", "Rohesia", "Rosalind", "Rosamund", "Sarah", "Susannah", "Sybil", "Williamina",
                    "Yvonne"
                ],
                "surname": [
                    "Holmes", "Lee", "Davis", "Price", "Bell", "Griffiths", "Shaw", "Murray", "Hill", "Owen"
                ]
            },

            "french": {
                "male": [
                    "Ambroys", "Ame", "Andri", "Andriet", "Anthoine", "Bernard", "Charles", "Charlot", "Colin", "Denis",
                    "Durant", "Edouart", "Eremon", "Ernault", "Ethor", "Felix", "Floquart", "Galleren", "Gaultier",
                    "Gilles", "Guy", "Henry", "Hugo", "Imbert", "Jacques", "Jacquot", "Jean", "Jehannin", "Louis", "Louys",
                    "Loys", "Martin", "Michel", "Mille", "Morelet", "Nicolas", "Nicolle", "Oudart", "Perrin", "Phillippe",
                    "Pierre", "Regnault", "Richart", "Robert", "Robinet", "Sauvage", "Simon", "Talbot", "Tanguy", "Vincent"
                ],
                "female": [
                    "Aalis", "Agatha", "Agnez", "Alberea", "Alips", "AmÃ©e", "Amelot", "Anne", "Avelina", "Blancha",
                    "Cateline", "Cecilia", "Claricia", "Collette", "Denisete", "Dorian", "Edelina", "Emelina", "Emmelot",
                    "Ermentrudis", "Gibelina", "Gila", "Gillette", "Guiburgis", "Guillemette", "Guoite", "Hecelina",
                    "Heloysis", "Helyoudis", "Hodeardis", "Isabellis", "Jaquette", "Jehan", "Johanna", "Juliote",
                    "Katerine", "Luciana", "Margot", "Marguerite", "Maria", "Marie", "Melisende", "Odelina", "Perrette",
                    "Petronilla", "Sedilia", "Stephana", "Sybilla", "Ysabeau", "Ysabel"
                ],
                "surname": [
                    "Martin", "Bernard", "Robert", "Richard", "Durand", "Dubois", "Moreau", "Simon", "Laurent", "Michel"
                ]
            },

            "german": {
                "male": [
                    "Albrecht", "Allexander", "Baltasar", "Benedick", "Berhart", "Caspar", "Clas", "Cristin", "Cristoff",
                    "Dieterich", "Engelhart", "Erhart", "Felix", "Frantz", "Fritz", "Gerhart", "Gotleib", "Hans", "Hartmann",
                    "Heintz", "Herman", "Jacob", "Jeremias", "Jorg", "Karll", "Kilian", "Linhart", "Lorentz", "Ludwig",
                    "Marx", "Melchor", "Mertin", "Michel", "Moritz", "Osswald", "Ott", "Peter", "Rudolff", "Ruprecht",
                    "Sewastian", "Sigmund", "Steffan", "Symon", "Thoman", "Ulrich", "Vallentin", "Wendel", "Wilhelm",
                    "Wolff", "Wolfgang"
                ],
                "female": [
                    "Adelhayt", "Affra", "Agatha", "Allet", "Angnes", "Anna", "Apell", "Applonia", "Barbara", "Brida",
                    "Brigita", "Cecilia", "Clara", "Cristina", "Dorothea", "Duretta", "Ella", "Els", "Elsbeth", "Engel",
                    "Enlein", "Enndlin", "Eva", "Fela", "Fronicka", "Genefe", "Geras", "Gerhauss", "Gertrudt", "Guttel",
                    "Helena", "Irmel", "Jonata", "Katerina", "Kuen", "Kungund", "Lucia", "Madalena", "Magdalen", "Margret",
                    "Marlein", "Martha", "Otilia", "Ottilg", "Peternella", "Reusin", "Sibilla", "Ursel", "Vrsula", "Walpurg"
                ],
                "surname": [
                    "Braun", "Schulz", "Richter", "Reichert", "Meier", "Kaiser", "Fischer", "Müller", "Krause", "Lange"
                ]
            },

            "greek": {
                "male": [
                    "Adonis", "Adrastos", "Aeson", "Aias", "Aineias", "Aiolos", "Alekto", "Alkeides", "Argos", "Brontes",
                    "Damazo", "Dardanos", "Deimos", "Diomedes", "Endymion", "Epimetheus", "Erebos", "Euandros",
                    "Ganymedes", "Glaukos", "Hektor", "Heros", "Hippolytos", "Iacchus", "Iason", "Kadmos", "Kastor",
                    "Kephalos", "Kepheus", "Koios", "Kreios", "Laios", "Leandros", "Linos", "Lykos", "Melanthios",
                    "Menelaus", "Mentor", "Neoptolemus", "Okeanos", "Orestes", "Pallas", "Patroklos", "Philandros",
                    "Phoibos", "Phrixus", "Priamos", "Pyrrhos", "Xanthos", "Zephyros"
                ],
                "female": [
                    "Acantha", "Aella", "Alektos", "Alkippe", "Andromeda", "Antigone", "Ariadne", "Astraea", "Chloros",
                    "Chryseos", "Daphne", "Despoina", "Dione", "Eileithyia", "Elektra", "Euadne", "Eudora", "Eunomia",
                    "Hekabe", "Helene", "Hermoione", "Hippolyte", "Ianthe", "Iokaste", "Iole", "Iphigenia", "Ismene",
                    "Kalliope", "Kallisto", "Kalypso", "Karme", "Kassandra", "Kassiopeia", "Kirke", "Kleio", "Klotho",
                    "KlytiÃ«", "Kynthia", "Leto", "Megaera", "Melaina", "Melpomene", "Nausikaa", "Nemesis", "Niobe",
                    "Ourania", "Phaenna", "Polymnia", "Semele", "Theia"
                ],
                "surname": [
                    "Papadopoulos", "Pappas", "Karagiannis", "Vlahos", "Ioannidis", "Economou", "Papageorgiou", "Konstantinidis",
                     "Dimopoulos", "Georgiadis", "Papadimitriou", "Papadakis", "Papanikolaou", "Panagiotopoulos", "Vasiliou",
                     "Giannopoulos", "Nikolaou", "Vasiliadis"
                ]
            },

            "indian": {
                "male": [
                    "Abhay", "Ahsan", "Ajay", "Ajit", "Akhil", "Amar", "Amit", "Ananta", "Aseem", "Ashok", "Bahadur", "Basu",
                    "Chand", "Chandra", "Damodar", "Darhsan", "Devdan", "Dinesh", "Dipak", "Gopal", "Govind", "Harendra",
                    "Harsha", "Ila", "Isha", "Johar", "Kalyan", "Kiran", "Kumar", "Lakshmana", "Mahavir", "Narayan", "Naveen",
                    "Nirav", "Prabhakar", "Prasanna", "Raghu", "Rajanikant", "Rakesh", "Ranjeet", "Rishi", "Sanjay", "Sekar",
                    "Shandar", "Sumantra", "Vijay", "Vikram", "Vimal", "Vishal", "Yash"
                ],
                "female": [
                    "Abha", "Aishwarya", "Amala", "Ananda", "Ankita", "Archana", "Avani", "Chandana", "Chandrakanta",
                    "Chetan", "Darshana", "Devi", "Dipti", "Esha", "Gauro", "Gita", "Indira", "Indu", "Jaya", "Kala",
                    "Kalpana", "Kamala", "Kanta", "Kashi", "Kishori", "Lalita", "Lina", "Madhur", "Manju", "Meera",
                    "Mohana", "Mukta", "Nisha", "Nitya", "Padma", "Pratima", "Priya", "Rani", "Sarala", "Shakti",
                    "Shanta", "Shobha", "Sima", "Sonal", "Sumana", "Sunita", "Tara", "Valli", "Vijaya", "Vimala"
                ],
                "surname": [
                    "Devi", "Singh", "Kumar", "Das", "Kaur", "Ram", "Yadav", "Kumari", "Lal", "Bai", "Khatun", "Mandal"
                ]
            },

            "japanese": {
                "male": [
                    "Akio", "Atsushi", "Daichi", "Daiki", "Daisuke", "Eiji", "Fumio", "Hajime", "Haru", "Hideaki",
                    "Hideo", "Hikaru", "Hiro", "Hiroki", "Hisao", "Hitoshi", "Isamu", "Isao", "Jun", "Katashi", "Katsu",
                    "Kei", "Ken", "Kenshin", "Kenta", "Kioshi", "Makoto", "Mamoru", "Masato", "Masumi", "Noboru", "Norio",
                    "Osamu", "Ryota", "Sadao", "Satoshi", "Shigeo", "Shin", "Sora", "Tadao", "Takehiko", "Takeo", "Takeshi",
                    "Takumi", "Tamotsu", "Tatsuo", "Toru", "Toshio", "Yasuo", "Yukio"
                ],
                "female": [
                    "Aika", "Akemi", "Akiko", "Amaya", "Asami", "Ayumi", "Bunko", "Chieko", "Chika", "Chiyo", "Cho", "Eiko",
                    "Emiko", "Eri", "Etsuko", "Gina", "Hana", "Haruki", "Hideko", "Hikari", "Hiroko", "Hisoka", "Hishi",
                    "Hotaru", "Izumi", "Kameyo", "Kasumi", "Kimiko", "Kotone", "Kyoko", "Maiko", "Masako", "Mi", "Minori",
                    "Mizuki", "Naoki", "Natsuko", "Noriko", "Rei", "Ren", "Saki", "Shigeko", "Shinju", "Sumiko", "Toshiko",
                    "Tsukiko", "Ume", "Usagi", "Yasuko", "Yuriko"
                ],
                "surname": [
                    "Satō", "Suzuki", "Takahashi", "Tanaka", "Watanabe", "Itō", "Nakamura", "Kobayashi", "Yamamoto", "Katō",
                    "Yoshida", "Yamada", "Matsumoto"
                ]
            },

            "mesoamerican": {
                "male": [
                    "Achcauhtli", "Amoxtli", "Chicahua", "Chimalli", "Cipactli", "Coaxoch", "Coyotl", "Cualli",
                    "Cuauhtémoc", "Cuetlachtilo", "Cuetzpalli", "Cuixtli", "Ehecatl", "Etalpalli", "Huemac",
                    "Huitzilihuitl", "Iccauhtli", "Ilhicamina", "Itztli", "Ixtli", "Mahuizoh", "Manauia", "Matlal",
                    "Matlalihuitl", "Mazatl", "Mictlantecuhtli", "Milintica", "Momoztli", "Namacuix", "Necalli",
                    "Necuametl", "Nezahualcoyotl", "Nexahualpilli", "Nochehuatl", "Nopaltzin", "Ollin", "Quauhtli",
                    "Tenoch", "Teoxihuitl", "Tepiltzin", "Tezcacoatl", "Tlacaelel", "Tlacelel", "Tlaloc", "Tlanextic",
                    "Tlazohtlaloni", "Tlazopillo", "Uetzcayotl", "Xipilli", "Yaotl"
                ],
                "female": [
                    "Ahuiliztli", "Atl", "Centehua", "Chalchiuitl", "Chipahua", "Cihuaton", "Citlali", "Citlalmina",
                    "Coszcatl", "Cozamalotl", "Cuicatl", "Eleuia", "Eloxochitl", "Eztli", "Ichtaca", "Icnoyotl", "Ihuicatl",
                    "Ilhuitl", "Itotia", "Iuitl", "Ixcatzin", "Izel", "Malinalxochitl", "Mecatl", "Meztli", "Miyaoaxochitl",
                    "Mizquixaual", "Moyolehuani", "Nahuatl", "Necahual", "Nenetl", "Nochtli", "Noxochicoztli", "Ohtli",
                    "Papan", "Patli", "Quetzalxochitl", "Sacnite", "Teicui", "Tepin", "Teuicui", "Teyacapan", "Tlaco",
                    "Tlacoehua", "Tlacotl", "Tlalli", "Tlanextli", "Xihuitl", "Xiuhcoatl", "Xiuhtonal"
                ],
                "surname": [
                    "Quispe", "Mamani", "Xicotencatl", "Chan", "Uriana", "Mella", "Yahari", "Ipuana", "Epieyuú",
                    "Jusayuú", "Pushaina", "Apaza", "Apugllón", "Guayasamín", "Mamani", "Lipán", "Huamán",
                    "Wayar", "Sulca", "Qaiana", "Yupanqui", "Campillai", "Menchú", "Canul", "Tecú", "Tuyuc", "Xoo",
                    "Kantún", "Paillamil", "Namuncurá", "Loncón", "Huaiquipán", "Maricahuín", "Tiarayu", "Paracatu",
                    "Ñamandu", "Arapayu", "Yahari", "Guayuán", "Acuayte", "Suchil", "Tlatelpa", "Axotlán", "Tepeyahuitl"
                ]
            },

            "niger_congo": {
                "male": [
                    "Abebe", "Abel", "Abidemi", "Abrafo", "Adisa", "Amadi", "Amara", "Anyim", "Azubuike", "Bapoto",
                    "Baraka", "Bohlale", "Bongani", "Bujune", "Buziba", "Chakide", "Chibuzo", "Chika", "Chimola",
                    "Chiratidzo", "Dabulamanzi", "Dumisa", "Dwanh", "Emeka", "Folami", "Gatura", "Gebhuza", "Gero",
                    "Isoba", "Kagiso", "Kamau", "Katlego", "Masego", "Matata", "Nthanda", "Ogechi", "Olwenyo", "Osumare",
                    "Paki", "Qinisela", "Quanda", "Samanya", "Shanika", "Sibonakaliso", "Tapiwa", "Thabo", "Themba",
                    "Uzoma", "Zuberi", "Zuri"
                ],
                "female": [
                    "Abebi", "Abena", "Abimbola", "Akoko", "Akachi", "Alaba", "Anuli", "Ayo", "Bolanle", "Bosede",
                    "Chiamaka", "Chidi", "Chidimma", "Chinyere", "Chioma", "Dada", "Ebele", "Efemena", "Ejiro", "Ekundayo",
                    "Enitan", "Funanya", "Ifunanya", "Ige", "Ime", "Kunto", "Lesedi", "Lumusi", "Mojisola", "Monifa", "Nakato",
                    "Ndidi", "Ngozi", "Nkiruka", "Nneka", "Ogechi", "Olamide", "Oluchi", "Omolara", "Onyeka", "Simisola",
                    "Temitope", "Thema", "Titlayo", "Udo", "Uduak", "Ufuoma", "Yaa", "Yejide", "Yewande"
                ],
                "surname": [
                    "Dlamini", "Ilunga", "Adeoye", "Tesfaye", "Akello", "Otieno", "Kone", "Musa", "Nkosi", "Moyo",
                    "Azikiwe", "Awolowo", "Bello", "Balewa", "Akintola", "Okotie-Eboh", "Nzeogwu", "Onwuatuegwu", "Okafor", "Okereke",
                    "Okeke", "Okonkwo", "Okoye", "Okorie", "Obasanjo", "Babangida", "Buhari", "Dimka", "Diya", "Odili",
                    "Ibori", "Igbinedion", "Alamieyeseigha", "Yar’Adua", "Akpabio", "Attah", "Chukwumereije", "Akunyili", "Iweala", "Okonjo",
                    "Ezekwesili", "Achebe", "Soyinka", "Solarin", "Gbadamosi", "Olanrewaju", "Magoro", "Madaki", "Jang", "Oyinlola",
                    "Oyenusi", "Onyejekwe", "Onwudiwe", "Jakande", "Kalejaiye",
                ]
            },

            "norse": {
                "male": [
                    "Agni", "Alaric", "Anvindr", "Arvid", "Asger", "Asmund", "Bjarte", "Bjorg", "Bjorn", "Brandr", "Brandt",
                    "Brynjar", "Calder", "Colborn", "Cuyler", "Egil", "Einar", "Eric", "Erland", "Fiske", "Folkvar", "Fritjof",
                    "Frode", "Geir", "Halvar", "Hemming", "Hjalmar", "Hjortr", "Ingimarr", "Ivar", "Knud", "Leif", "Liufr",
                    "Manning", "Oddr", "Olin", "Ormr", "Ove", "Rannulfr", "Sigurd", "Skari", "Snorri", "Sten", "Stigandr",
                    "Stigr", "Sven", "Trygve", "Ulf", "Vali", "Vidar"
                ],
                "female": [
                    "Alfhild", "Arnbjorg", "Ase", "Aslog", "Astrid", "Auda", "Audhid", "Bergljot", "Birghild", "Bodil",
                    "Brenna", "Brynhild", "Dagmar", "Eerika", "Eira", "Gudrun", "Gunborg", "Gunhild", "Gunvor", "Helga",
                    "Hertha", "Hilde", "Hillevi", "Ingrid", "Iona", "Jorunn", "Kari", "Kenna", "Magnhild", "Nanna", "Olga",
                    "Ragna", "Ragnhild", "Ranveig", "Runa", "Saga", "Sigfrid", "Signe", "Sigrid", "Sigrunn", "Solveg",
                    "Svanhild", "Thora", "Torborg", "Torunn", "Tove", "Unn", "Vigdis", "Ylva", "Yngvild"
                ],
                "surname": [
                    "Hansen", "Johansen", "Olsen", "Larsen", "Andersen", "Nilsen", "Pedersen", "Jensen", "Kristiansen", "Karlsen",
                    "Johnsen", "Pettersen", "Eriksen", "Berg", "Haugen", "Hagen", "Johannessen", "Jacobsen", "Andreassen", "Dahl",
                    "Halvorsen", "Lund", "Henriksen", "Jørgensen", "Jakobsen", "Gundersen", "Moen", "Sørensen", "Iversen", "Svendsen",
                    "Strand", "Solberg", "Martinsen", "Paulsen", "Knutsen", "Eide", "Bakken", "Kristoffersen", "Mathisen", "Lie",
                    "Rasmussen", "Bakke", "Amundsen", "Kristensen", "Andresen", "Lunde", "Moe", "Berge", "Holm", "Fredriksen"
                ]
            },

            "polynesian": {
                "male": [
                    "Afa", "Ahohako", "Aisake", "Aleki", "Anewa", "Anitelu", "Aputi", "Ariki", "Butat", "Enele", "Fef",
                    "Fuifui", "Ha’aheo", "Hanohano", "Haunui", "Hekili", "Hiapo", "Hikawera", "Hanano", "Ho’onani", "Hoku",
                    "Hû’eu", "Ina", "Itu", "Ka’aukai", "Ka’eo", "Kaelani", "Kahale", "Kaiea", "Kaikoa", "Kana’I", "Koamalu",
                    "Ka", "Laki", "Makai", "Manu", "Manuka", "Nui", "Pono", "Popoki", "Ruru", "Tahu", "Taurau", "Tuala",
                    "Turoa", "Tusitala", "Uaine", "Waata", "Waipuna", "Zamar"
                ],
                "female": [
                    "Ahulani", "Airini", "Alani", "Aluala", "Anahera", "Anuhea", "Aolani", "Elenoa", "Emele", "Fetia",
                    "Fiva", "Halona", "Hi’ilei", "Hina", "Hinatea", "Huali", "Inia", "Inina", "Iolani", "Isa", "Ka’ana’ana",
                    "Ka’ena", "Kaamia", "Kahula", "Kailani", "Kamaile", "Kamakani", "Kamea", "Latai", "Liona", "Lokelani",
                    "Marva", "Mehana", "Millawa", "Moana", "Ngana", "Nohea", "Pelika", "Sanoe", "Satina", "Tahia", "Tasi",
                    "Tiaho", "Tihani", "Toroa", "Ulanni", "Uluwehi", "Vaina", "Waiola", "Waitara"
                ],
                "surname": [
                    "Haukea", "Etana", "Kapule", "Lui", "Kaiwi", "Iona", "Kalili", "Kekoa", "Manu", "Hawea",
                    "Hikialani", "Lani", "Keona", "Kealani", "Aukai", "Pualani", "Moana", "Pele", "Kahue", "Akana",
                    "Kahale", "Noelani", "Lee", "Nani", "Leo"
                ]
            },

            "roman": {
                "male": [
                    "Aelius", "Aetius", "Agrippa", "Albanus", "Albus", "Antonius", "Appius", "Aquilinus", "Atilus",
                    "Augustus", "Aurelius", "Avitus", "Balbus", "Blandus", "Blasius", "Brutus", "Caelius", "Caius",
                    "Casian", "Cassius", "Cato", "Celsus", "Claudius", "Cloelius", "Cnaeus", "Crispus", "Cyprianus",
                    "Diocletianus", "Egnatius", "Ennius", "Fabricius", "Faustus", "Gaius", "Germanus", "Gnaeus",
                    "Horatius", "Iovianus", "Iulius", "Lucilius", "Manius", "Marcus", "Marius", "Maximus", "Octavius",
                    "Paulus", "Quintilian", "Regulus", "Servius", "Tacitus", "Varius"
                ],
                "female": [
                    "Aelia", "Aemilia", "Agrippina", "Alba", "Antonia", "Aquila", "Augusta", "Aurelia", "Balbina",
                    "Blandina", "Caelia", "Camilla", "Casia", "Claudia", "Cloelia", "Domitia", "Drusa", "Fabia",
                    "Fabricia", "Fausta", "Flavia", "Floriana", "Fulvia", "Germana", "Glaucia", "Gratiana", "Hadriana",
                    "Hermina", "Horatia", "Hortensia", "Iovita", "Iulia", "Laelia", "Laurentia", "Livia", "Longina",
                    "Lucilla", "Lucretia", "Marcella", "Marcia", "Maxima", "Nona", "Octavia", "Paulina", "Petronia",
                    "Porcia", "Tacita", "Tullia", "Verginia", "Vita"
                ],
                "surname": [
                     "Titus", "Aeneas", "Felice", "Evander", "Maxim", "Octavia", "Paulus", "Tiberius", "Seneca", "Valentius",
                     "Amadeus", "Candida", "Severan", "Quirinus", "Delphina", "Nettuno", "Delphi", "Livia", "Ursus", "Vita",
                     "Gavia", "Aeneas", "Tiberiu", "Manius", "Prosper"
                ]
            },

            "slavic": {
                "male": [
                    "Aleksandru", "Berislav", "Blazh", "Bogumir", "Boguslav", "Borislav", "Bozhidar", "Bratomil",
                    "Bratoslav", "Bronislav", "Chedomir", "Chestibor", "Chestirad", "Chestislav", "Desilav", "Dmitrei",
                    "Dobromil", "Dobroslav", "Dragomir", "Dragutin", "Drazhan", "Gostislav", "Kazimir", "Kyrilu",
                    "Lyubomir", "Mechislav", "Milivoj", "Milosh", "Mstislav", "Nikola", "Ninoslav", "Premislav",
                    "Radomir", "Radovan", "Ratimir", "Rostislav", "Slavomir", "Stanislav", "Svetoslav", "Tomislav",
                    "Vasili", "Velimir", "Vladimir", "Vladislav", "Vlastimir", "Volodimeru", "Vratislav", "Yarognev",
                    "Yaromir", "Zbignev"
                ],
                "female": [
                    "Agripina", "Anastasiya", "Bogdana", "Boleslava", "Bozhena", "Danica", "Darya", "Desislava",
                    "Dragoslava", "Dunja", "Efrosinia", "Ekaterina", "Elena", "Faina", "Galina", "Irina", "Iskra",
                    "Jasna", "Katarina", "Katya", "Kresimira", "Lyudmila", "Magda", "Mariya", "Militsa", "Miloslava",
                    "Mira", "Miroslava", "Mokosh", "Morana", "Natasha", "Nika", "Olga", "Rada", "Radoslava", "Raisa",
                    "Slavitsa", "Sofiya", "Stanislava", "Svetlana", "Tatyana", "Tomislava", "Veronika", "Vesna",
                    "Vladimira", "Yaroslava", "Yelena", "Zaria", "Zarya", "Zoria"
                ],
                "surname": [
                    "Volkov", "Kozlov", "Kuzmina", "Sokolova", "Ivanov", "Kuznetsov", "Smirnov", "Stepanova", "Zakharov", "Makarova",
                    "Stepanov", "Zaytseva", "Sokolov", "Nikolaeva", "Vasileva", "Egorov", "Kuznetsova", "Mongush", "Popova", "Sergeeva"
                    "Novikov", "Zakharova", "Pavlov", "Kim", "Morozova", "Pavlova", "Makarov", "Vesnina", "Lebedeva", "Kuzmin"
                ]
            },

            "spanish": {
                "male": [
                    "Alexandre", "Alfonso", "Alonso", "Anthon", "Arcos", "Arnaut", "Arturo", "Bartoleme", "Benito",
                    "Bernat", "Blasco", "Carlos", "Damian", "Diego", "Domingo", "Enrique", "Escobar", "Ettor", "Fernando",
                    "Franciso", "Gabriel", "Garcia", "Gaspar", "Gil", "Gomes", "Goncalo", "Gostantin", "Jayme", "Joan",
                    "Jorge", "Jose", "Juan", "Machin", "Martin", "Mateu", "Miguel", "Nicolas", "Pascual", "Pedro",
                    "Porico", "Ramiro", "Ramon", "Rodrigo", "Sabastian", "Salvador", "Simon", "Tomas", "Tristan", "Valeriano",
                    "Ynigo"
                ],
                "female": [
                    "Abella", "Adalina", "Adora", "Adriana", "Ana", "Antonia", "Basilia", "Beatriz", "Bonita", "Camila",
                    "Cande", "Carmen", "Catlina", "Dolores", "Dominga", "Dorotea", "Elena", "Elicia", "Esmerelda",
                    "Felipina", "Francisca", "Gabriela", "Imelda", "Ines", "Isabel", "Juana", "Leocadia", "Leonor",
                    "Leta", "Lucinda", "Maresol", "Maria", "Maricela", "Matilde", "Melania", "Monica", "Neva", "Nilda",
                    "Petrona", "Rafaela", "Ramira", "Rosario", "Sofia", "Suelo", "Teresa", "Tomasa", "Valentia", "Veronica",
                    "Ynes", "Ysabel"
                ],
                "surname": [
                    "Gonzalez", "Romero", "Gutierrez", "Ortiz", "Garcia", "Martinez", "Alonso", "Jimenez", "Sanchez", "Cortes",
                    "Serrano", "Santos", "Morales", "Perez", "Delgado", "Fernandez", "Iglesias", "Muñoz", "Diaz", "Rubio",
                    "Lopez", "Ortega", "Nuñez", "Martin", "Navarro", "Hernandez", "Moreno", "Gomez", "Medina", "Molina"
                ]
            }
        }
    },

    "tiefling": {
        "male": [
            "Abad", "Ahrim", "Akmen", "Amnon", "Andram", "Astar", "Balam", "Barakas", "Bathin", "Caim",
            "Chem", "Cimer", "Cressel", "Damakos", "Ekemon", "Euron", "Fenriz", "Forcas", "Habor", "Iados",
            "Kairon", "Leucis", "Mamnen", "Mantus", "Marbas", "Melech", "Merihim", "Modean", "Mordai", "Mormo",
            "Morthos", "Nicor", "Nirgel", "Oriax", "Paymon", "Pelaios", "Purson", "Qemuel", "Raam", "Rimmon",
            "Sammal", "Skamos", "Tethren", "Thamuz", "Therai", "Valafar", "Vassago", "Xappan", "Zepar", "Zephan"
        ],
        "female": [
            "Akta", "Anakis", "Armara", "Astaro", "Aym", "Azza", "Beleth", "Bryseis", "Bune", "Criella",
            "Damaia", "Decarabia", "Ea", "Gadreel", "Gomory", "Hecat", "Ishte", "Jezebeth", "Kali", "Kallista",
            "Kasdeya", "Lerissa", "Lilith", "Makaria", "Manea", "Markosian", "Mastema", "Naamah", "Nemeia",
            "Nija", "Orianna", "Osah", "Phelaia", "Prosperine", "Purah", "Pyra", "Rieta", "Ronobe", "Ronwe",
            "Seddit", "Seere", "Sekhmet", "Semyaza", "Shava", "Shax", "Sorath", "Uzza", "Vapula", "Vepar", "Verin"
        ],
        "virtue": [
            "Ambition", "Art", "Carrion", "Chant", "Creed", "Death", "Debauchery", "Despair", "Doom",
            "Doubt", "Dread", "Ecstasy", "Ennui", "Entropy", "Excellence", "Fear", "Glory", "Gluttony",
            "Grief", "Hate", "Hope", "Horror", "Ideal", "Ignominy", "Laughter", "Love", "Lust", "Mayhem",
            "Mockery", "Murder", "Muse", "Music", "Mystery", "Nowhere", "Open", "Pain", "Passion", "Poetry",
            "Quest", "Random", "Reverence", "Revulsion", "Sorrow", "Temerity", "Torment", "Tragedy", "Vice",
            "Virtue", "Weary", "Wit"
        ]
    }
}


def main():
    test_item_location = get_whatever_im_getting()
    print(f"the selected position is: {test_item_location}")


def get_whatever_im_getting():

    NPC_sex = random.choice(sex)

    cultures = list(race["human"]["culture"].keys())
    chosen_culture = random.choice(cultures)

    names = list(race["human"]["culture"][chosen_culture][NPC_sex])
    first_name = random.choice(names)

    return first_name

"""
    # Use this as a scratchpaper before copying the text into main program
    random_culture = random.choice(list(race["human"]))
    random_name = random.choice(list(race["human"][chosen_culture]))
    last_name = random.choice(list(race["human"][random_culture][chosen_culture]["surname"]))
    return first_name, last_name
"""

"""
    random_type = random.choice(list(appearance["old injury"].keys()))
    color = random.choice(appearance["old injury"][random_type])
    return random_injury
"""

if __name__ == "__main__":
    main()
