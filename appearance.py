
import random
import sys
appearance = {
    "lifestyle": {
        "modest": {
            "earrings": [
                "simple carved wooden studs",
                "small hoops made of braided hemp",
                "basic hoops made of copper wire",
                "simple dangle earrings with colored clay beads",
                "small studs with colored glass beads"
            ],
            "necklace": [
                "a simple wooden necklace, carved with the image of a deer",
                "a sturdy necklace featuring a series of small clay tokens",
                "a slightly tarnished, but obviously well loved simple pendant, engraved with family initials",
                "a well worn leather cord supporting a small bronze disc",
                "a homely necklace made of braided grass or straw"
            ],
            "circlet": [
                "a simple circlet made from braided twine, adorned with small, colorful glass beads",
                "a plain circlet fashioned from thin, twisted copper wire with small, hammered copper discs hanging along the band, creating a subtle jingle with movement",
                "a sturdy leather circlet made from leftover scraps, featuring a few carved wooden beads for decoration",
                "a circlet woven from fresh or dried wildflowers and grasses",
                "a circlet made from a strip of cloth, dyed in a single, modest color and adorned with a single, tiny charm"
            ],
            "bracelet": [
                "a simple braided cord of twine, adorned with a small wooden bead",
                "a worn-out piece of cloth wrapped around the wrist, once colorful but now faded from age and use",
                "a plain bangle made from cheap copper, tarnished from years of wear",
                "a basic bracelet crafted from a strip of leather, fastened with a crude knot",
                "a string of rounded beads, made from clay, glass, and wooden beads strung together"
            ],
            "outfit": [
                "a smooth, dark wool coat that reaches mid-thigh, secured with a series of brass buttons",
                "a tailored linen shirt, soft and breathable, with a fine, embroidered collar",
                "a mid-length skirt of brushed suede, accented with intricate beadwork along the hem",
                "a pair of fitted trousers in charcoal gray, with a subtle pinstripe and crisp creases",
                "a durable denim apron, layered over a checkered cotton blouse, both practical and neat",
                "a quilted vest, forest green, filled with down feathers for warmth and comfort",
                "a lightweight tunic of woven silk, dyed in a rich cobalt blue, with a loose, flowing fit",
                "a knee-length wrap dress in terracotta red, cinched with a leather belt",
                "a pair of soft, moleskin breeches, fitted snugly at the waist and flaring slightly at the cuffs",
                "a crisp poplin robe, with a subtle floral pattern and deep, practical pockets"
            ],
            "hats": [
                "a felt fedora, olive green, with a wide brim and a leather band around the base",
                "a soft, crocheted cap made from wool, in a neutral taupe, with a delicate scalloped edge",
                "a sturdy canvas sun hat, with a broad brim and a chin strap for windy days",
                "a woven straw boater, trimmed with a navy blue ribbon and a small bow at the side",
                "a classic beret, crafted from fine wool, in a deep burgundy shade",
                "a practical cloth cap with a small, stiff brim, suitable for keeping the sun out of one's eyes",
                "a decorative turban, wrapped in luxurious silk, patterned with vibrant, swirling colors",
                "a formal top hat, modest in height, made from felt and adorned with a single feather",
                "a lightweight linen scarf, wrapped around the head and tied at the nape, in a dusty rose color",
                "a knitted beanie, simple yet cozy, in a muted forest green with a small, rolled cuff"
            ]
        },

        "comfortable": {
            "earrings": [
                "simple drop earrings featuring polished agate stones",
                "small, round hematite studs",
                "thin hoops with small obsidian beads",
                "teardrop-shaped lapis lazuli earrings",
                "dangle earrings with small turquoise stones"
            ],
            "necklace": [
                "a beaded necklace featuring smooth turquoise gemstones, ranging in color from tranquil blue to vibrant green, interspersed with silver beads",
                "a heart-shaped pendant necklace featuring a polished rhodochrosite gemstone",
                "a choker-style necklace crafted from smooth obsidian beads interspersed with silver accents",
                "a bold statement necklace featuring chunky malachite beads, each displaying mesmerizing swirls of vibrant green hues",
                "an amulet crafted from a single large blue quartz crystal, suspended from a sturdy leather cord"
            ],
            "circlet": [
                "a delicate circlet made of polished copper, adorned with small azurite stones",
                "a sturdy leather circlet featuring banded agate stones set in simple silver settings",
                "a slender circlet made of silver, with evenly spaced blue quartz gemstones",
                "a circlet crafted from brass, embellished with lapis lazuli gemstones",
                "a robust circlet made of bronze, featuring tiger eye stones"
            ],
            "bracelet": [
                "a simple metal bracelet featuring small azurite gemstones interspersed with metal charms and decorative beads",
                "a beaded bracelet, incorporating lapis lazuli beads along with other semi-precious stones",
                "a cuff-style bracelet crafted from polished tiger eye gemstones set into a metal band",
                "a bracelet intricately woven with bands of banded agate gemstones",
                "an elegant bracelet composed of polished malachite gemstones set in delicate metal links"
            ],
            "outfits": [
                "a richly embroidered velvet jacket, deep navy in color, with silver thread accents along the cuffs",
                "a soft, fine cashmere sweater in cream, featuring a high neck and ribbed trim",
                "a pair of tailored silk trousers, midnight blue, with a relaxed fit and a satin stripe down each leg",
                "a brocade vest, ornate with golden floral patterns, fitted snugly over a crisp white shirt",
                "a flowing chiffon skirt, reaching the ankles, in a subtle shade of lavender, with a delicate drawstring waist",
                "a leather duster, oiled for a sleek finish, with intricate tooling around the lapels and cuffs",
                "a silk kimono-style robe, richly patterned with an exotic landscape, tied with a wide sash",
                "a tweed blazer, impeccably tailored, with elbow patches and a felted collar",
                "a merino wool tunic, charcoal gray, with a lace-up front and split side hems",
                "a suede cape, buttery and soft, with a hood lined in faux fur"
            ],
            "hats": [
                "a structured felt hat in burgundy, with a grosgrain ribbon encircling the crown",
                "a plush velvet beret, emerald green, soft to the touch and subtly luminous",
                "a wide-brimmed leather hat, weather-resistant, with a braided band",
                "a sophisticated silk top hat, black, with a band of peacock feathers for flair",
                "a tweed flat cap, expertly woven, in shades of brown and cream",
                "a finely knitted wool beanie, dove gray, with a folded brim and a single large pom-pom",
                "a panama hat, woven from fine straw, with an elegant silk band around the base",
                "a luxuriously soft angora fur hat, white, with a rounded crown and wide brim",
                "a trilby hat made of cashmere, light taupe, with a narrow brim turned up at the back",
                "a decorative turban, crafted from silk brocade, with a jeweled brooch at the front"
            ]
        },

        "wealthy": {
            "earrings": [
                "dark green bloodstone with red flecks, set in delicate gold hooks",
                "smooth black onyx beads dangling from thin silver hoops",
                "iridescent moonstone beads that catch the light with a subtle glow, set in dangling silver settings",
                "soft blue chalcedony stones in a smooth, drop-shaped design, set in delicate silver settings",
                "sunny yellow citrine stones cut into teardrop shapes, set in elegant gold settings"
            ],
            "necklace": [
                "a beaded necklace crafted from sparkling zircon gemstones, each shimmering with hues of blue, green, or yellow interspersed with silver beads",
                "a pendant necklace featuring a star rose quartz gemstone, radiating gentle pink hues reminiscent of a blush at dawn",
                "a cameo necklace featuring a meticulously carved sardonyx gemstone, depicting intricate scenes and figures from mythology or history",
                "a rosary-style necklace crafted from smooth onyx beads, each displaying a glossy black sheen like the depths of night",
                "a statement necklace featuring bold jasper gemstones, each showcasing unique patterns and earthy tones ranging from deep red to sandy beige"
            ],
            "circlet": [
                "a refined gold circlet adorned with deep green bloodstones, each stone flecked with red",
                "a sleek silver circlet featuring vibrant carnelian gemstones",
                "a mystical pewter circlet set with luminous moonstones",
                "a exquisite platinum circlet adorned with star rose quartz gemstones",
                "a robust bronze circlet featuring clear, sparkling zircon stones"
            ],
            "bracelet": [
                "a luxurious bracelet featuring smooth, polished bloodstone beads strung on a durable cord",
                "an exquisite accessory adorned with vibrant carnelian gemstones set in intricate metal charms",
                "a stunning cuff-style bracelet crafted from gleaming chalcedony gemstones, intricately carved and polished",
                "a dazzling bracelet adorned with sparkling zircon gemstones set in delicate metal links, shimmering with brilliance",
                "a mesmerizing bracelet adorned with alternating moonstone and quartz gemstones set in intricate metal links"
            ],
            "outfits": [
                "a finely tailored frock coat in deep burgundy velvet, adorned with gold brocade and silk lining",
                "a luxurious silk gown, emerald green, with a full skirt and intricate silver embroidery at the bodice",
                "a bespoke three-piece suit, crafted from fine wool, in a subtle check pattern, with a silk waistcoat underneath",
                "an opulent fur-trimmed cloak, midnight blue, lined with satin and fastened with a golden clasp",
                "a delicate lace blouse, ivory, with hand-stitched pearls along the cuffs and collar",
                "a pair of high-waisted trousers in charcoal tweed, with satin stripes and a perfect, crisp crease",
                "a rich tapestry tunic, adorned with exotic animal motifs and edged with fine golden thread",
                "an elegant brocade jacket, fitted and flared at the waist, in shades of sapphire and gold",
                "a flowing satin cape, soft pink, with an oversized hood and intricate floral embroidery in gold thread",
                "a fine leather doublet, dyed in jet black and embossed with intricate designs, laced with gold threads"
            ],
            "hats": [
                "a sophisticated top hat in black silk, featuring a wide band of velvet and a large, exotic feather",
                "an ornate headdress, composed of delicate golden chains and rare gemstones, resting lightly on flowing hair",
                "a plush, wide-brimmed hat made of sable fur, encircled by a band of embroidered silk",
                "a dramatic tricorn hat, edged with lace and adorned with a spray of peacock feathers",
                "a finely woven straw hat, elegantly shaped, with a silk ribbon dyed in vibrant turquoise",
                "a luxurious velvet turban, rich purple, studded with sapphires and twisted artfully at the crown",
                "a stylish beret, made from cashmere, in a deep plum color, accented with a small, glittering brooch",
                "an imposing riding cap, in polished leather, with a gleaming silver badge at the side",
                "a delicate filigree tiara, worn more as a hat than a crown, intricate in design and studded with tiny diamonds",
                "a refined bowler hat, glossy and black, with a subtle band of gray pearls around the rim"
            ]
        },

        "aristocratic": {
            "earrings": [
                "deep purple amethyst stones set into simple yet elegant silver studs",
                "rich red garnet stones cut into teardrop shapes, set in intricate gold settings",
                "small coral beads paired with delicate pearls, set in dangling gold settings",
                "polished green jade stones set into simple silver stud settings",
                "small, round amber beads adorning thin gold or silver hoops"
            ],
            "necklace": [
                "a pendant necklace featuring a polished amber gemstone, glowing with warm honey hues like sunlight captured in resin",
                "a meticulously cut and polished, collar-style necklace adorned with amethyst gemstones, ranging in color from pale lavender to deep purple",
                "a lariat-style necklace adorned with garnet gemstones, each exuding deep red hues reminiscent of a smoldering ember",
                "a pendant necklace featuring a jade gemstone, intricately carved with auspicious motifs meant to attract luck and prosperity",
                "a strand necklace featuring lustrous pearls, each shimmering with iridescent hues of white, pink, or black"
            ],
            "circlet": [
                "a radiant gold circlet adorned with warm, honey-colored amber stones",
                "a refined silver circlet featuring deep purple amethysts",
                "a brass circlet set with smooth, vibrant green jade stones",
                "a delicate platinum circlet adorned with lustrous white pearls",
                "a sturdy bronze circlet featuring deep red garnet gemstones"
            ],
            "bracelet": [
                "a statement piece crafted from gleaming chrysoberyl gemstones, intricately carved or polished to highlight their natural beauty and unique coloration",
                "an elegant bracelet featuring faceted garnet gemstones set in delicate metal links, shimmering with deep red hues",
                "a prestigious bangle bracelet made from lustrous jade gemstones, offering a symbol of prosperity, harmony, and protection to the wearer",
                "an exquisite bracelet adorned with lustrous pearls set in delicate metal links, shimmering with iridescence and capturing the timeless beauty of the sea",
                "a mesmerizing bracelet adorned with alternating spinel and tourmaline gemstones, wrapped around the wrist in multiple layers"
            ],
            "outfits": [
                "a regal velvet gown, royal blue, with a corseted bodice and full, sweeping train",
                "a sophisticated silk suit, pearl white, tailored to perfection with a satin lapel",
                "a sumptuous brocade doublet, burgundy and gold, detailed with intricate hand-stitched patterns",
                "an exquisite lace dress, champagne colored, adorned with tiny pearls and a silk ribbon waist",
                "a fine damask waistcoat, silver-gray, over a high-collared silk shirt with lace cuffs",
                "a pair of velvet breeches, deep forest green, fitted tightly and buttoned at the knee",
                "a luxurious satin blouse, soft peach, with billowing sleeves and crystal button closures",
                "a tailored riding habit, dark chocolate brown, with gold braiding and a fitted jacket",
                "a richly embroidered tunic, midnight black, with silver threads and semi-precious stones",
                "a sleek silk jumpsuit, charcoal, with a plunging neckline and tapered legs"
            ],
            "hats": [
                "a majestic wide-brimmed hat, adorned with ostrich feathers and a velvet band",
                "a delicate lace bonnet, ivory, trimmed with silk roses and thin ribbons",
                "an opulent jeweled crown, set with rubies and diamonds, on a filigree gold base",
                "a stately plumed top hat, jet black, with a satin band and a spray of peacock feathers",
                "an elegant riding cap, hunter green, with a crisp, curved brim and leather strap",
                "a refined silk turban, lilac, twisted high and dotted with pearls",
                "a grand cavalier hat, navy blue, edged with lace and adorned with a large, curled feather",
                "a stylish fedora, ash gray, made of fine felt and circled with a silk ribbon",
                "a sophisticated beret, powder blue, crafted from cashmere and accented with a gold brooch",
                "an extravagant headpiece, sculpted from silk flowers and delicate birdcage netting"
            ],
            "cloaks": [
                "a majestic fur-lined cloak, deep burgundy, with a heavy golden clasp",
                "an ornate silk cape, midnight blue, with a cascading lace overlay and silver embroidery",
                "a plush velvet cloak, emerald green, trimmed with white ermine and fastened with a jeweled pin",
                "a dramatic satin cape, blood red, with a high collar and black velvet lining",
                "an opulent cloak of golden brocade, floor-length and lined with sable fur",
                "a delicate chiffon cloak, pale violet, floating ethereally with each movement",
                "a heavy wool cloak, charcoal gray, with intricate needlework depicting ancient legends",
                "a lavish cloak of peacock feathers, shimmering with iridescent blues and greens",
                "a stately cape of midnight velvet, with a collar of raised silver thread embroidery",
                "an aristocratic oilcloth cloak, navy, tailored with a waterproof silk lining for practical elegance"
            ]
        },

        "monsterous": {
            "earrings": [
                "rugged hoop earrings, crafted from polished animal bones",
                "mismatched earrings, made from bits of scavenged metal",
                "sturdy iron studs, engraved with what looks to be a clan symbol",
                "oddly shaped earrings made of the shells and teeth of aquatic creatures",
                "small, irregular shards of colorful gems, crudely attached to metal hooks"
            ],
            "necklace": [
                "the fangs of defeated beasts or enemies on a crude hempen string",
                "a string bits of discarded metal, broken gears, and shiny objects",
                "a simple bronze medallion engraved with a faded military rank",
                "a string of brightly colored fish scales and bones",
                "several rough gemstone shards on a leather thong"
            ],
            "circlet": [
                "a circlet forged from crude iron, adorned with spikes and jagged edges",
                "a circlet woven from delicate vines and flowers, embellished with small feathers and beads",
                "a circlet fashioned in the shape of a serpent, with coiled metal forming the band and jeweled eyes that glint in the light",
                "a circlet adorned with miniature goblin skulls, each intricately carved and painted with tribal markings",
                "a circlet made from woven reeds or vines, adorned with small animal bones and feathers"
            ],
            "bracelets": [
                "a bracelet crafted from braided hair or sinew, adorned with small stones representing mountain peaks",
                "a sinister bracelet made from blackened metal, adorned with dark gemstones and spider motifs",
                "a bracelet made from twisted wire and adorned with small crystals and shards of precious metals",
                "a bracelet made from twisted vines, adorned with small bells and charms",
                "a bracelet crafted from intricately carved bone, adorned with small feathers and teeth"
            ],
            "outfit": [
                "a faded blue tunic, patched at the elbows and frayed at the hem",
                "a rugged burlap vest over a threadbare cotton shirt, both stained with mud",
                "a thick woolen sweater, pilled and snug, with mismatched buttons down the front",
                "a coarse linen robe, dyed a deep forest green, dragging slightly on the ground",
                "a patched leather jerkin, tough and weathered, with deep pockets on each side",
                "a simple but well-made wool dress, dyed in muted earth tones, with a modest lace collar",
                "a pair of soft leather trousers, dyed black, with a drawstring waist and reinforced knees",
                "a sturdy canvas apron, covering a plaid flannel shirt, both smeared with paint",
                "a quilted doublet, faded from years of use but clean and neatly stitched",
                "a lightweight silk tunic, hand-dyed in a swirl of earthy colors, with a v-neck cut"
            ],
            "hats": [
                "a wide-brimmed straw hat, frayed around the edges, shielding from the sun",
                "a floppy woolen cap, pulled low over the ears, with a tiny, tattered feather tucked into a band",
                "a simple coif made from rough linen, tied snugly under the chin",
                "a faded cotton bandana, wrapped tightly around the head, stained with sweat",
                "a tall pointed hat of felt, drooping awkwardly to one side",
                "a leather hood, worn and soft, with eye slits cut for better visibility",
                "a knit beanie, speckled with bits of colorful yarn, stretched from frequent use",
                "a patched burlap sack, ingeniously converted into a head covering, with holes for eyes",
                "a sturdy helmet, formerly metallic and now coated with rust, repurposed from battlefield leftovers",
                "a delicate lace bonnet, oddly out of place but lovingly maintained, with silk ribbons to tie under the chin"
            ]
        }
    },

    "old injury": {
        "scar": [
            "a slightly faded, but still noticeably prominent scar on their forehead",
            "a relatively fresh, long pink scar down their left forearm",
            "a faded and slightly discolored burn scar on their neck",
            "a mostly healed, but still quite visible scar across their right cheek",
            "a fresh, deep red and still healing cut on the left side of their jaw",
            "a healed, mostly faded, but still noticeable scar on their hand",
            "a partially faded, slightly pinkish scar across their collarbone",
            "a fresh, slightly swolen scar on their upper arm",
            "a healed, but still visible scar from a bite mark on their shoulder",
            "a faded, thin white scar along their throat"
        ],
        "teeth": [
            "a prominent gap in their front teeth, visible when they smile or speak",
            "stained, visibly yellowed teeth",
            "a missing front tooth, clearly visible as they talk",
            "a shining golden tooth that can be seen when they smile or laugh",
            "very crooked teeth, behind a very crooked smile"
        ],
        "missing body part": [
            "lost their right eye, covering the empty socket with a distinctive eye patch",
            "lost their right leg below the knee, using a sturdy metal prosthetic to move around the shop",
            "lost their left arm, which they have replaced with a beautifully crafted wooden prosthetic",
            "lost two fingers on their left hand, but have adapted to perform tasks with remarkable skill",
            "lost part of their left ear, the result of an old battle wound that has long since healed"
        ]
    },

    "eye color": {
        "real": [
            "dark brown eyes that resemble rich, dark chocolate",
            "light brown eyes that shimmer with a warm, amber glow",
            "deep blue eyes that are as dark and profound as the midnight ocean",
            "light blue eyes that sparkle like the clear, summer sky",
            "green eyes that resemble the vibrant, fresh leaves of spring",
            "hazel eyes that shift between green and brown, depending on the light",
            "sunlit amber, glowing with a warm, honeyed light that feels soothing and inviting"
        ],
        "fantasy": [
            "a deep pool of liquid silver",
            "the exact shade of a gold piece",
            "nearly as luminous and ethereal as polished moonstone",
            "like pools of shimmering sapphire, glistening with an otherworldly brilliance that seems to hold the secrets of the deep sea",
            "storm grey, turbulent and brooding, like thunderclouds gathering before a tempest",
            "oceanic blue, deep and tranquil, with a serene clarity that mirrors the endless sea",
            "dappled jade, mottled with shades of green that evoke the mystery of an ancient forest",
            "like crimson flame, flickering with an inner fire that blazes with an insatiable hunger",
            "vibrant turquoise, shining with a lively energy, reminiscent of the clear, tropical seas under a bright sun",
            "phantom violet, ethereal and haunting, with a spectral glow that hints at otherworldly connections",
            "prismatic opal, shifting through a spectrum of colors that dance and change with every glance",
            "pitch black, you could swear, for only the briefest of moments, before becoming a calming blue"
        ]
    },

    "tattoo": {
        "image": [
            "a detailed of dragon's eye, with scales surrounding it and a fiery pupil, located on their forearm, wrapping slightly around the wrist",
            "an intricate Elven script spelling out a meaningful phrase or name, carefully and delicately tattooed on their inner forearm",
            "a series of small moons showing the phases from new to full moon, wrapping around their wrist",
            "a tree with sprawling roots and branches, intertwining with flowers and leaves on the side of their torso",
            "a night sky with twinkling stars and a crescent moon, fading into dawn across the collarbone",
            "a fierce lion with a mane flowing like flames, representing protection and courage, located on their thigh, extending down towards the knee",
            "a detailed mandala with intricate patterns and spiritual symbols, located on the center of their back",
            "a coiled serpent with scales and piercing eyes, symbolizing wisdom and danger, wrapping around their upper arm, almost entirely hidden by their clothes",
            "a circle of ancient runes, each symbolizing a different element or power, located on the palm of their hand",
            "an  eye surrounded by mystical symbols and patterns, on the nape of their neck"
        ],
        "name": [
            'the name "Ander" in bold, ancient script with a flourish of vines, on the inside of their forearm',
            'the name "Bella" in elegant cursive, surrounded by delicate roses on their upper arm',
            'the name "Caelynn" with a stylized elven design and sparkling stars on their collarbone',
            'the name "Faye" with fairy wings and glittering dust on their wrist',
            'the name "Gideon" with a shield and lion head on their chest',
            'the name "Halia" in a flowing script with waves and seashells on their ankle',
            'the name "Ireena" with a gothic font and bat wings, hinting at dark beauty on the side of their neck',
            'the name "Lira" with musical notes and a lyre, symbolizing harmony on their shoulder blade',
            'the name "Milo" in playful script with paw prints and a small heart on their wrist',
            'the name "Yara" with a floral design and butterflies, symbolizing transformation on their ankle',
        ]
    },

    "birthmark": {
        "a faint heart-shaped birthmark on the left side of their neck",
        "a birthmark resembling the shape of a dragon's wing on their upper back, spreading across the shoulder blade",
        "a sun-shaped birthmark with rays extending outward on the center of their chest",
        "a delicate spiderweb-shaped birthmark on their left elbow",
        "a jagged, lightning bolt-shaped birthmark on their right forearm",
    },

    "hair": {
        "hair": [
            "smooth, silky hair that flows like water",
            "loose, wavy hair that falls in soft waves",
            "a full, thick head of hair that looks lush and voluminous",
            "intricately braided hair, with multiple braids woven together",
            "long dreadlocks that cascade down their back",
            "thinning hair with noticeable balding areas",
            "hair tied back in a ponytail",
            "hair with natural-looking highlights that catch the light",
            "a voluminous curly afro that frames their face",
            "a bold mohawk, with the sides shaved and a strip of hair down the center"
        ],
        "beard": [
            "a clean-shaven face with no facial hair",
            "a light stubble, giving them a rugged look",
            "a thick, full beard that covers their cheeks and chin",
            "a prominent mustache above their upper lip",
            "thick, friendly mutton chops that connect to a mustache",
            "a handlebar mustache with curled ends",
            "a small patch of hair just below the lower lip",
            "a long, flowing beard that reaches down their chest",
            "a beard adorned with small beads woven into the hair",
            "a scruffy beard that looks rugged and a bit unkempt"
        ],
    },

    "other": {
        "nose": [
            "a nose that appears slightly asymmetrical, with one nostril larger or higher than the other",
            "a curved nose with a prominent bridge, resembling an eagle's beak",
            "a small, rounded nose with a gentle slope",
            "a broad, flat nose with wide nostrils and a low bridge",
            "a nose with a pronounced hook shape, curving downward at the tip",
            "a short, slightly upturned nose with a rounded tip",
            "a thin, narrow nose with a straight bridge and small nostrils",
            "an upturned nose with a slight upward tilt at the tip",
            "a nose with a noticeable bend or deviation in the bridge, previously broken but healed"
        ],
        "posture": [
            "a tall posture with shoulders back, chest out, and head held high, exuding self-assurance",
            "hunched shoulders and a head slightly forward, giving a tired or indifferent impression",
            "a casual lean against a wall or piece of furniture, often with arms crossed or hands in pockets",
            "a very straight posture with a stiff, almost military demeanor, indicating strict discipline or nervousness",
            "a relaxed posture with weight shifted to one leg, shoulders relaxed, and hands resting easily at their sides or on hips",
            "a wide-legged stance, arms crossed over the chest, and a stern expression, designed to intimidate or command respect",
            "an elegant and fluid stance, movements smooth and deliberate",
            "shoulders up, arms close to the body, often with a wary expression, ready to react to threats",
            "a confident, exaggerated walk with shoulders swinging and a slight bounce in the step",
            "a forward-leaning body, feet slightly apart, hands often gesturing"
        ],
        "beauty": [
            "a captivating, mysterious aura with features that draw people in with curiosity",
            "lively, colorful features with a dynamic, energetic presence",
            "polished, sophisticated features and an air of elegance",
            "a handsome, striking appearance with sharp, well-defined features",
            "a dazzling, infectious smile that lights up their entire face",
            "alluring, seductive features with a captivating, magnetic charm",
            "fine, fragile features that give them a delicate, porcelain-like appearance",
            "strong, striking features and a confident, daring presence",
            "a grounded, natural look with simple, wholesome features",
            "striking, unusual features that set them apart and captivate attention"
        ]
    }
}


available_lifestyles = ["Modest", "Comfortable", "Wealthy", "Aristocratic", "Monsterous"]


def main():
    print()
    appearance = get_appearance_UI()
    print(appearance)


def get_appearance():
    for i in range(len(sys.argv)):
        if len(sys.argv) >= 1 and sys.argv[i] not in available_lifestyles:
            char_appearance_choice = get_random_appearance()
        elif len(sys.argv) >= 2 and sys.argv[i] in available_lifestyles:
            char_appearance_choice = (f"They are wearing {get_specific_appearance()}.")
    return char_appearance_choice


def get_appearance_UI():
    print("What kind of appearance would you like this character to have?")
    print()
    supported_lifestyles()
    print()
    lifestyle = input("Answer: ").casefold()

    if lifestyle in available_lifestyles and lifestyle != "random":
        random_type = random.choice(list(appearance["lifestyle"][lifestyle].keys()))
        specific = random.choice(appearance["lifestyle"][lifestyle][random_type])
        char_appearance_choice = (f"They are wearing {specific}.")
    elif lifestyle in available_lifestyles and lifestyle == "random":
        char_appearance_choice = get_random_appearance()
    else:
        char_appearance_choice = print_unsupported_error(lifestyle)

    print()
    return char_appearance_choice


def print_unsupported_error(str):
    print("The race that you entered is either not a currently supported lifestyle, or there was a typo.")
    print("You entered the word(s): ")
    print('')
    print(f"{str}")
    print('')
    print("The current available lifestyles are: ")
    print('')
    supported_lifestyles()
    print('')


def supported_lifestyles():
    for i in range(len(available_lifestyles)):
        print(f"{available_lifestyles[i]:<20}", end="")
        if (i + 1) % 3 == 0:
            print()
    if len(available_lifestyles) % 3 != 0:
        print()


def get_specific_appearance():
    for i in range(len(sys.argv)):
        if sys.argv[i] in available_lifestyles:
            lifestyle = sys.argv[i].lower()
            random_type = random.choice(list(appearance["lifestyle"][lifestyle].keys()))
            specific = random.choice(appearance["lifestyle"][lifestyle][random_type])
            return specific


def get_random_appearance():
    char_appearance_list = []

    char_appearance_list.append(f"They are wearing {get_random_outfit()}.")
    char_appearance_list.append(f"They have {get_injury()}.")
    char_appearance_list.append(f"Their eyes are {get_eye_color()}.")
    char_appearance_list.append(f"They have a tattoo of {get_tattoo()}.")
    char_appearance_list.append(f"They have {get_birthmark()}.")
    char_appearance_list.append(f"They have {get_hair()}.")
    char_appearance_list.append(f"They have {get_other()}.")

    char_appearance_choice = random.choice(char_appearance_list)
    return char_appearance_choice


def get_random_outfit():
    random_lifestyle = random.choice(list(appearance["lifestyle"].keys()))
    random_type = random.choice(list(appearance["lifestyle"][random_lifestyle].keys()))
    clothes = random.choice(appearance["lifestyle"][random_lifestyle][random_type])
    return clothes


def get_injury():
    random_type = random.choice(list(appearance["old injury"].keys()))
    random_injury = random.choice(appearance["old injury"][random_type])
    return random_injury


def get_eye_color():
    real_or_fake = random.choice(list(appearance["eye color"].keys()))
    color = random.choice(appearance["eye color"][real_or_fake])
    return color


def get_tattoo():
    image_or_name = random.choice(list(appearance["tattoo"].keys()))
    tattoo = random.choice(appearance["tattoo"][image_or_name])
    return tattoo


def get_birthmark():
    birthmark = random.choice(list(appearance["birthmark"]))
    return birthmark


def get_hair():
    hair_or_beard = random.choice(list(appearance["hair"].keys()))
    hair = random.choice(appearance["hair"][hair_or_beard])
    return hair


def get_other():
    nose_posture_beauty = random.choice(list(appearance["other"].keys()))
    other = random.choice(appearance["other"][nose_posture_beauty])
    return other


if __name__ == "__main__":
    main()
