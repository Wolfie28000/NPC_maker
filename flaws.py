flaws = {
    "Pride": [
        "They strut as if the world revolves around them.",
        "They scoff at the mere suggestion of their imperfection.",
        "They crave the adoration of everyone they encounter.",
        "They dismiss even the wisest counsel if it contradicts their views.",
        "They constantly remind others of their supposed greatness.",
        "They shun any offer of assistance, seeing it as beneath them.",
        "They look down their noses at those they deem inferior.",
        "They expect royal treatment, regardless of the setting.",
        "They view their accomplishments as unparalleled, unmatched by any.",
        "They refuse to acknowledge any achievements but their own."
    ],
    "Greed": [
        "They clutch their coins so tightly, it's as if their life depended on it.",
        "They hoard treasures and trinkets, never parting with a single item.",
        "They constantly plot to expand their wealth by any means necessary.",
        "They sacrifice friendships and morals on the altar of gold.",
        "They keep their wealth locked away, never to be spent or shared.",
        "They see people as mere stepping stones to greater riches.",
        "They are insatiable, never finding contentment in their vast fortune.",
        "They would sell their own kin if the price were right.",
        "They seethe with envy at the sight of others' possessions.",
        "They twist situations to squeeze out every last coin for themselves."
    ],
    "Lust": [
        "They are driven by a burning desire that blinds them to all else.",
        "They weave a web of charm to ensnare those they desire.",
        "They flit from one lover to the next, never satisfied.",
        "They pursue physical pleasure with a single-minded intensity.",
        "They reduce others to mere objects of their insatiable desire.",
        "They are a slave to their own passions, never knowing peace.",
        "They make advances that border on obsession, heedless of boundaries.",
        "They grow possessive and jealous over the slightest competition.",
        "They leave a trail of broken hearts and shattered trust.",
        "They are led by their base instincts, heedless of the consequences."
    ],
    "Envy": [
        "They burn with resentment at others' good fortune.",
        "They measure their worth by the successes of those around them.",
        "They lay traps and spread lies to topple their rivals.",
        "They find no joy in their own achievements, only in others' failures.",
        "They whisper venomous rumors to tarnish others' glory.",
        "They refuse to acknowledge anyone else's accomplishments.",
        "They seek to overshadow others, always striving to be better.",
        "They are consumed by a smoldering bitterness.",
        "They lash out at those they perceive as more fortunate.",
        "They are haunted by an ever-present feeling of inadequacy."
    ],
    "Gluttony": [
        "They feast as though every meal were their last.",
        "They lack the willpower to resist any temptation.",
        "They consume more than their share, leaving little for others.",
        "They live for the next indulgence, never considering the future.",
        "They abandon responsibilities in favor of their appetites.",
        "They are often found in a stupor, bloated from overindulgence.",
        "They waste resources, heedless of the needs of others.",
        "They are indifferent to the plight of the hungry or needy.",
        "They are never satisfied, always seeking more excess.",
        "They are easily lured by promises of indulgence and pleasure."
    ],
    "Wrath": [
        "They are a tinderbox, ready to explode at the slightest spark.",
        "They nurse grudges with a fervent intensity, seeking vengeance.",
        "They react with explosive violence to any perceived insult.",
        "They are quick to anger, holding onto their rage like a weapon.",
        "They strike out in fury, consequences be damned.",
        "They are ruled by their emotions, a storm of anger and hate.",
        "They thrive on conflict, always looking for a fight.",
        "They blame everyone else for their problems, never themselves.",
        "They are consumed by a seething resentment and bitterness.",
        "They find joy in the suffering of those who have wronged them."
    ],
    "Sloth": [
        "They shirk duties and responsibilities at every turn.",
        "They are perpetually bored, indifferent to the world.",
        "They delay tasks indefinitely, living in a haze of procrastination.",
        "They drift through life without purpose or ambition.",
        "They let obligations slide, unbothered by the consequences.",
        "They are content to do the bare minimum, avoiding effort.",
        "They depend on others to carry their weight.",
        "They lack the motivation to pursue anything meaningful.",
        "They are stagnant, resistant to growth or change.",
        "They prefer idleness and inactivity, embracing laziness."
    ]
}

keys = sorted(list(flaws.keys()))

import random

def main():
    flaw = get_flaw_UI()
    print(f"{flaw}")


def get_flaw():
    flaw_class = random.choice(list(flaws))
    flaw = random.choice(list(flaws[flaw_class]))
    return flaw


def get_flaw_UI():
    while True:
        print()
        print("Which flaw would you like this character to have?")
        print()
        for fl in keys:
            print(f"{fl:<20}", end="")
            if (keys.index(fl) + 1) % 3 == 0:
                print()
        print()
        print()
        answer = input("Answer: ")
        print()
        a = answer.title()
        if a in keys:
            flaw = random.choice(list(flaws[a]))
            return flaw
        else:
            print(f"Unrecognized input: {answer}")
            continue

if __name__ == "__main__":
    main()
