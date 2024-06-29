bonds = {
    "Dedicated to fulfilling a personal life goal": [
        "They have a burning desire to complete a grand project that will leave a lasting legacy.",
        "Their life's mission is to discover a rare artifact that has fascinated them since childhood.",
        "They are committed to building a successful business that will be known throughout the land.",
        "They aim to write a comprehensive history of their village, preserving its stories for future generations.",
        "They dream of mastering a difficult skill or craft, proving their dedication and talent."
    ],
    "Protective of close family members": [
        "They would do anything to ensure the safety and well-being of their family.",
        "They spend much of their time caring for an elderly parent, showing unwavering devotion.",
        "They have a sibling they are fiercely protective of, always ready to defend them.",
        "They prioritize their children's needs above all else, working hard to provide for them.",
        "They are deeply connected to their extended family, maintaining close relationships and offering support."
    ],
    "Protective of colleagues or compatriots": [
        "They stand by their colleagues, believing in the strength of their team.",
        "They have a close-knit group of friends they consider family, always looking out for each other.",
        "They are loyal to their fellow guild members, ready to defend them against any threat.",
        "They mentor younger colleagues, ensuring they have the guidance and support needed to succeed.",
        "They prioritize the well-being of their workmates, fostering a supportive and cooperative environment."
    ],
    "Loyal to a benefactor, patron, or employer": [
        "They owe their success to a generous patron, always striving to repay their kindness.",
        "They are fiercely loyal to their employer, believing in the company's mission and values.",
        "They have a mentor who has guided them through difficult times, earning their eternal gratitude.",
        "They work tirelessly to support a benefactor who has invested in their future.",
        "They are dedicated to their employer, seeing them as a key figure in their life's journey."
    ],
    "Captivated by a romantic interest": [
        "They are deeply in love with someone who inspires and motivates them every day.",
        "They often daydream about their romantic interest, feeling a strong emotional connection.",
        "They go out of their way to spend time with their beloved, cherishing every moment together.",
        "They write poetry and letters to express their feelings, hoping to win their heart.",
        "They are committed to building a future with their romantic interest, working towards shared dreams."
    ],
    "Drawn to a special place": [
        "They feel a profound connection to a tranquil forest where they often go to find peace.",
        "They have a favorite spot by the river where they spend hours reflecting and relaxing.",
        "They are drawn to an ancient ruin that holds a special significance for them.",
        "They feel at home in a bustling marketplace, where they enjoy the vibrant energy and diverse people.",
        "They often visit a sacred temple, finding solace and inspiration in its serene atmosphere."
    ],
    "Protective of a sentimental keepsake": [
        "They cherish a locket given to them by a loved one, always keeping it close.",
        "They have a worn book that holds many memories, treating it with great care.",
        "They carry a small charm that reminds them of their childhood, never parting with it.",
        "They keep a letter from a dear friend, reading it often to feel connected.",
        "They have a handcrafted item that was a gift, valuing it above all other possessions."
    ],
    "Protective of a valuable possession": [
        "They own a rare artifact that they guard closely, knowing its immense value.",
        "They have a family heirloom that they will defend at all costs.",
        "They possess a unique tool that is essential for their trade, never letting it out of their sight.",
        "They have a finely crafted weapon that they rely on for protection.",
        "They own a valuable piece of jewelry that has been passed down through generations."
    ],
    "Out for revenge": [
        "They are driven by a need to avenge a wrong done to them or their loved ones.",
        "They seek justice for a betrayal that left them deeply scarred.",
        "They are determined to find and punish those responsible for their suffering.",
        "They have sworn to avenge the death of a loved one, dedicating their life to this cause.",
        "They harbor a deep grudge against an enemy, planning their retribution carefully."
    ]
}

import random

def main():

    bond = get_bond()
    print(f"{bond}")


def get_bond():
    bond_class = random.choice(list(bonds))
    bond = random.choice(list(bonds[bond_class]))

    roll_twice = [1, 2, 3, 4, 5, 6, 7, 8, 9, "yes"]
    double_roll = random.choice(roll_twice)

    if double_roll == "yes":
        second_bond_class = random.choice(list(bonds))
        second_bond = random.choice(list(bonds[second_bond_class]))
        if second_bond == bond:
            second_bond_class = random.choice(list(bonds))
            second_bond = random.choice(list(bonds[second_bond_class]))
        elif second_bond != bond:
            return (f"{bond}\n{second_bond}")
    else:
        return bond

if __name__ == "__main__":
    main()
