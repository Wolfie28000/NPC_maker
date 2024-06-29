flaws_and_secrets = {
    "Forbidden love or susceptibility to romance": [
        "They are secretly in love with a member of a rival family, risking scandal if discovered.",
        "They have a weakness for charming travelers, often giving discounts and special treatment.",
        "They engage in clandestine meetings with a forbidden lover, always fearful of being caught.",
        "They are easily swayed by romantic gestures, sometimes making unwise business decisions as a result.",
        "They maintain a hidden stash of love letters and tokens from various admirers, each one a potential source of trouble."
    ],
    "Enjoys decadent pleasures": [
        "They spend their evenings indulging in expensive wines and gourmet foods, often to the detriment of their finances.",
        "They have a hidden room in their shop filled with luxury items they keep for personal enjoyment.",
        "They frequently visit opulent parties and gatherings, sometimes neglecting their shop duties.",
        "They are known to hire bards and entertainers for private performances, spending lavishly on their whims.",
        "They have a secret account used to fund their lavish lifestyle, kept hidden from prying eyes."
    ],
    "Arrogance": [
        "They believe they are the most knowledgeable person in the village, often dismissing others' opinions.",
        "They boast about their successes and belittle competitors, creating tension in the community.",
        "They refuse to take advice from anyone, believing their way is always the best.",
        "They often argue with customers who question their prices or quality, driving some away.",
        "They have lost business deals due to their unwillingness to compromise or admit they are wrong."
    ],
    "Envies another creature's possessions or station": [
        "They secretly covet the wealth and status of the town's mayor, plotting ways to surpass them.",
        "They often make snide comments about a rival shopkeeper's success, revealing their jealousy.",
        "They spend time and money trying to replicate the success of others, often to no avail.",
        "They feel deep resentment towards a more successful family, wishing they could trade places.",
        "They have attempted to sabotage a competitor's business in subtle ways, driven by envy."
    ],
    "Overpowering greed": [
        "They charge exorbitant prices for basic goods, driven by a desire for wealth.",
        "They hoard rare items, refusing to sell them in hopes of driving up their value.",
        "They frequently cheat customers, shortchanging them or selling subpar products.",
        "They secretly smuggle goods to avoid paying taxes, increasing their profit margins.",
        "They have hired thugs to intimidate competitors, securing their position as the top shopkeeper."
    ],
    "Prone to rage": [
        "They have a quick temper, often shouting at employees and customers over minor issues.",
        "They have broken merchandise in fits of anger, costing themselves money.",
        "They have a reputation for getting into physical altercations when provoked.",
        "They have been banned from local taverns due to their aggressive behavior.",
        "They have a strained relationship with their family due to their frequent outbursts."
    ],
    "Has a powerful enemy": [
        "They are constantly looking over their shoulder, fearing retribution from a former business partner they betrayed.",
        "They receive threatening letters from a rival who seeks to ruin them.",
        "They have hired a bodyguard to protect them from an enemy with significant influence.",
        "They have been attacked multiple times, barely escaping with their life each time.",
        "They avoid certain parts of town, knowing their enemy's allies are always watching."
    ],
    "Specific phobia": [
        "They have a paralyzing fear of fire, keeping multiple buckets of water around the shop at all times.",
        "They are terrified of spiders, often refusing to enter certain areas of the shop.",
        "They avoid going near the river, haunted by a childhood accident involving water.",
        "They have an intense fear of heights, never climbing ladders or stairs.",
        "They are scared of the dark, always keeping the shop brightly lit even at night."
    ],
    "Shameful or scandalous history": [
        "They were once a notorious thief, using their ill-gotten gains to start their shop.",
        "They had an affair with a high-ranking official, causing a scandal that forced them to move towns.",
        "They were implicated in a smuggling ring, narrowly escaping imprisonment.",
        "They have a secret child from a past relationship, hidden away in another town.",
        "They were once a member of a criminal gang, their past still haunting them."
    ],
    "Secret crime or misdeed": [
        "They once committed a serious crime to protect a loved one, a secret they guard closely.",
        "They have forged documents to gain an advantage in business, fearing exposure.",
        "They have stolen valuable items from competitors, hiding them in a secret location.",
        "They were involved in a heist that went wrong, leaving a trail that could lead back to them.",
        "They blackmail a local official, using information from a past misdeed."
    ],
    "Possession of forbidden lore": [
        "They possess a tome of dark magic, kept hidden from prying eyes.",
        "They have a map to a forbidden place, known only to a few.",
        "They know a ritual that can summon powerful entities, a knowledge that could bring ruin.",
        "They have detailed knowledge of a forgotten language, used in forbidden spells.",
        "They possess a relic of an ancient cult, its secrets known only to them."
    ],
    "Foolhardy bravery": [
        "They often take unnecessary risks, believing they are invincible.",
        "They have a habit of challenging dangerous individuals, often getting into trouble.",
        "They frequently volunteer for perilous tasks, seeking to prove their bravery.",
        "They have a collection of scars from reckless actions, each with a story.",
        "They once ventured into a dragon's lair on a dare, narrowly escaping with their life."
    ]
}


import random

def main():
    flaw = get_flaw()
    print(f"{flaw}")


def get_flaw():
    flaw_class = random.choice(list(flaws_and_secrets))
    flaw = random.choice(list(flaws_and_secrets[flaw_class]))
    return flaw

if __name__ == "__main__":
    main()
