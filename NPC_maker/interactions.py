interactions = {
    "Argumentative": [
        "They always challenge others' opinions, turning even simple discussions into debates.",
        "They enjoy playing devil's advocate, often sparking lively arguments.",
        "They never back down from a dispute, eager to prove their point.",
        "They frequently interrupt others to correct them, which can be quite annoying.",
        "They thrive on conflict, often seeking out arguments for the sake of debate."
    ],
    "Honest": [
        "They always tell the truth, even when it's difficult or unwelcome.",
        "They value honesty above all else, never sugarcoating their words.",
        "They are known for their integrity, always keeping their promises.",
        "They believe in transparency, sharing information openly with others.",
        "They are respected for their straightforwardness, even if it sometimes hurts."
    ],
    "Arrogant": [
        "They often boast about their achievements, making sure everyone knows their worth.",
        "They look down on those they consider less capable, often dismissing their opinions.",
        "They refuse to admit when they are wrong, convinced of their own infallibility.",
        "They have a tendency to dominate conversations, believing their views are superior.",
        "They seldom listen to advice, preferring to rely on their own judgment."
    ],
    "Hot tempered": [
        "They have a short fuse, easily angered by minor annoyances.",
        "They often raise their voice in frustration, startling those around them.",
        "They react impulsively when provoked, sometimes regretting their outbursts.",
        "They struggle to stay calm in heated situations, their temper flaring quickly.",
        "They are quick to anger but also quick to cool down, often apologizing afterward."
    ],
    "Blustering": [
        "They speak loudly and boastfully, often exaggerating their abilities.",
        "They try to intimidate others with their bluster, though it rarely works.",
        "They often make grandiose claims, seeking to impress or intimidate.",
        "They rely on their loud voice and big gestures to make a point.",
        "They are known for their blustering talk, but actions rarely match their words."
    ],
    "Irritable": [
        "They get annoyed easily, often snapping at people for little things.",
        "They have a low tolerance for frustration, showing their irritation openly.",
        "They frequently complain about minor inconveniences, letting everyone know their displeasure.",
        "They are quick to express dissatisfaction, often making others uncomfortable.",
        "They struggle to hide their irritation, their mood affecting those around them."
    ],
    "Rude": [
        "They often interrupt others, showing little regard for their feelings.",
        "They make blunt comments, often offending those around them.",
        "They dismiss others' opinions with a wave, acting superior and condescending.",
        "They rarely say 'please' or 'thank you,' expecting others to cater to them.",
        "They have a habit of making snide remarks, putting others down."
    ],
    "Ponderous": [
        "They speak slowly and deliberately, taking time to choose their words.",
        "They often pause to think deeply before responding, valuing thoughtfulness over speed.",
        "They move with a deliberate grace, each action considered carefully.",
        "They take their time with decisions, ensuring every aspect is weighed thoroughly.",
        "They enjoy long, thoughtful conversations, exploring topics in depth."
    ],
    "Curious": [
        "They ask numerous questions, eager to learn and understand more.",
        "They are always exploring new ideas and concepts, never satisfied with surface-level knowledge.",
        "They enjoy investigating mysteries, often delving into books or experiments.",
        "They listen intently to others, always seeking new perspectives.",
        "They are quick to engage in new experiences, driven by their insatiable curiosity."
    ],
    "Quiet": [
        "They prefer to listen rather than speak, often observing silently.",
        "They speak softly, their words carrying weight despite their quiet tone.",
        "They enjoy solitude, finding peace in quiet moments away from crowds.",
        "They are often lost in thought, their silence a sign of deep contemplation.",
        "They are content to let others lead conversations, contributing sparingly but meaningfully."
    ],
    "Friendly": [
        "They greet everyone with a warm smile, instantly putting people at ease.",
        "They go out of their way to help others, always offering a hand when needed.",
        "They make friends easily, their open and welcoming nature attracting others.",
        "They remember details about people, showing genuine interest in their lives.",
        "They spread positivity wherever they go, lifting the spirits of those around them."
    ],
    "Suspicious": [
        "They are wary of strangers, always questioning their motives.",
        "They rarely take things at face value, preferring to investigate further.",
        "They often assume the worst in others, their trust hard to earn.",
        "They are cautious in their dealings, always looking for hidden agendas.",
        "They keep their guard up, seldom revealing personal information."
    ]
}

import random

def main():
    interaction = get_interaction()
    print(f"{interaction}")


def get_interaction():
    inter_chosen = random.choice(list(interactions))
    inter = random.choice(list(interactions[inter_chosen]))
    return inter


if __name__ == "__main__":
    main()
