possible_att = {
    "high": {
        "strength": [
            "They can lift heavy crates and barrels with ease, effortlessly moving stock around the shop.",
            "They have an impressive grip, able to crush objects with their bare hands if necessary.",
            "They can arm wrestle and defeat the strongest patrons in the tavern, earning their respect.",
            "They can break down doors and barriers when needed, using their sheer strength to clear obstacles.",
            "They have the stamina to work long hours without tiring, thanks to their incredible physical power."
        ],
        "dexterity": [
            "They can catch falling objects mid-air, never letting anything slip through their fingers.",
            "They have nimble fingers that allow them to handle delicate items without causing damage.",
            "They can navigate through crowded spaces with ease, never bumping into anyone or anything.",
            "They can pick locks with precision, using their dexterous hands to open even the trickiest of locks.",
            "They have excellent aim, always hitting their target whether throwing darts or shooting arrows."
        ],
        "constitution": [
            "They rarely get sick, their robust health keeping them active and energetic year-round.",
            "They can endure harsh weather conditions, whether extreme heat or cold, without faltering.",
            "They can consume large quantities of food and drink without any negative effects, impressing everyone with their resilience.",
            "They can work tirelessly from dawn till dusk, rarely needing breaks or rest.",
            "They have an incredible ability to recover quickly from injuries, always bouncing back stronger."
        ],
        "wisdom": [
            "They have a keen sense of intuition, often knowing what a customer needs before they say a word.",
            "They can give sound advice on a wide range of topics, earning the trust and respect of the villagers.",
            "They can read the mood of a room and adjust their behavior accordingly, always making people feel comfortable.",
            "They have a deep understanding of herbal remedies and natural healing, often sought after for their wisdom in medicine.",
            "They can foresee potential problems and take proactive steps to prevent them, ensuring smooth operations in the shop."
        ],
        "intelligence": [
            "They can solve complex puzzles and riddles quickly, often surprising others with their sharp mind.",
            "They have an extensive knowledge of history and lore, able to recount tales and facts from memory.",
            "They can speak multiple languages fluently, easily communicating with travelers and traders from faraway lands.",
            "They have a talent for inventing new gadgets and tools, constantly coming up with innovative ideas.",
            "They can calculate costs and profits in their head, always ensuring the shop's finances are in order."
        ],
        "charisma": [
            "They have a magnetic personality, drawing people in and making them feel valued and welcome.",
            "They can negotiate deals with ease, often getting the best prices for their goods.",
            "They have a talent for storytelling, captivating audiences with their tales and anecdotes.",
            "They can inspire and motivate others, often leading community projects and events with great success.",
            "They have a way with words, able to defuse tense situations and bring peace with just a few sentences."
        ]
    },

    "low": {
        "strength": [
            "They struggle to lift heavy crates, often needing to ask for help from stronger villagers.",
            "They avoid tasks that require brute strength, knowing their physical limitations.",
            "They get easily fatigued after physical exertion, often needing to take breaks.",
            "They can’t carry multiple heavy items at once, slowing down their work pace.",
            "They struggle to open tightly sealed jars and containers, relying on tools or assistance."
        ],
        "dexterity": [
            "They frequently drop items, causing minor accidents in the shop.",
            "They struggle with tasks that require fine motor skills, such as intricate crafts or repairs.",
            "They are often clumsy in crowded spaces, accidentally bumping into people or objects.",
            "They have difficulty picking locks or performing sleight of hand, their fingers lacking the necessary finesse.",
            "They struggle with precise aiming in projectile-based games, rarely hitting their target."
        ],
        "constitution": [
            "They fall ill frequently, often having to close the shop for days at a time.",
            "They get easily winded after minor physical activity, needing to rest frequently.",
            "They have a low tolerance for extreme temperatures, avoiding harsh weather whenever possible.",
            "They can't consume large amounts of food or drink without feeling sick, avoiding eating contests and large meals.",
            "They take a long time to recover from illnesses or injuries, often needing extended periods of rest."
        ],
        "wisdom": [
            "They struggle to read social cues, often misunderstanding the mood of customers.",
            "They frequently give bad advice, leading to unintended consequences.",
            "They have difficulty understanding herbal remedies, often mixing up ingredients.",
            "They often miss warning signs of potential problems, leading to avoidable issues.",
            "They struggle to empathize with others, sometimes coming across as insensitive."
        ],
        "intelligence": [
            "They struggle with solving complex puzzles and riddles, often needing help from others.",
            "They have a hard time remembering historical facts and lore, mixing up details frequently.",
            "They only speak their native language fluently, finding it difficult to learn new languages.",
            "They rarely come up with innovative ideas, sticking to traditional methods instead.",
            "They often need help with calculations, struggling to keep the shop's finances in order."
        ],
        "charisma": [
            "They find it difficult to engage with customers, often coming across as awkward or shy.",
            "They struggle to negotiate deals, frequently accepting less favorable terms.",
            "They have a hard time telling captivating stories, losing their audience's interest quickly.",
            "They rarely take on leadership roles, feeling uncomfortable in the spotlight.",
            "They often say the wrong thing in tense situations, unintentionally escalating conflicts."
        ]
    }
}

available_att = [
    "highstr", "highdex", "highcon", "highint", "highwis", "highcha",
    "lowstr", "lowdex", "lowcon", "lowint", "lowwis", "lowcha"
    ]

import random
import sys

def main():
    attribute = get_attribute()
    print(attribute)


def get_attribute():
    for i in range(len(sys.argv)):
        if len(sys.argv) >= 1 and sys.argv[i] not in available_att:
            att = random_att()
        elif len(sys.argv) >= 2 and sys.argv[i] in available_att:
            att = specific_att()
    return att


def random_att():
    attributes = ["high", "low"]
    h_l = random.choice(attributes)
    if h_l == "high":
        high_att = random.choice(list(possible_att["high"]))
        attribute = random.choice(list(possible_att["high"][high_att]))
    elif h_l == "low":
        low_att = random.choice(list(possible_att["low"]))
        attribute = random.choice(list(possible_att["low"][low_att]))
    return attribute


def specific_att():
    for i in range(len(sys.argv)):
        if sys.argv[i] in available_att:
            req_att = sys.argv[i].lower()

            if req_att == "highstr":
                att = random.choice(possible_att["high"]["strength"])
            elif req_att =="highdex":
                att = random.choice(possible_att["high"]["dexterity"])
            elif req_att == "highcon":
                att = random.choice(possible_att["high"]["constitution"])
            elif req_att == "highint":
                att = random.choice(possible_att["high"]["intelligence"])
            elif req_att == "highwis":
                att = random.choice(possible_att["high"]["wisdom"])
            elif req_att == "highcha":
                att = random.choice(possible_att["high"]["charisma"])

            elif req_att == "lowstr":
                att = random.choice(possible_att["low"]["strength"])
            elif req_att == "lowdex":
                att = random.choice(possible_att["low"]["dexterity"])
            elif req_att == "lowcon":
                att = random.choice(possible_att["low"]["constitution"])
            elif req_att == "lowint":
                att = random.choice(possible_att["low"]["intelligence"])
            elif req_att == "lowwis":
                att = random.choice(possible_att["low"]["wisdom"])
            elif req_att == "lowcha":
                att = random.choice(possible_att["low"]["charisma"])

    return att

if __name__ == "__main__":
    main()
