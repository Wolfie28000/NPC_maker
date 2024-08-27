import random
ideals = {
    "Good": {
        "Beauty": [
            "They believe that beauty can be found in all things and strive to bring it into their shop and community.",
            "They take great care in presenting their goods attractively, believing beauty enhances value.",
            "They support local artists and craftsmen, promoting the beauty they create.",
            "They often donate to projects that beautify the village, such as gardens and murals.",
            "They find joy in creating aesthetically pleasing displays, making their shop a place of beauty."
        ],
        "Charity": [
            "They regularly donate a portion of their earnings to those in need, believing in helping others.",
            "They organize charity events and fundraisers, using their shop as a hub for community support.",
            "They offer discounts and free goods to struggling families, showing generosity in times of need.",
            "They volunteer their time to local causes, helping to uplift the less fortunate.",
            "They believe that giving to others enriches their own life, always looking for ways to contribute."
        ],
        "Greater good": [
            "They prioritize actions that benefit the whole community, even at personal cost.",
            "They support policies and initiatives that aim to improve the village as a whole.",
            "They encourage others to think beyond their own needs, promoting a sense of collective responsibility.",
            "They often lead by example, making sacrifices for the greater good of all.",
            "They believe in the power of unity and work tirelessly to bring people together for common causes."
        ],
        "Life": [
            "They cherish all forms of life and treat every creature with respect and kindness.",
            "They refuse to sell goods that harm the environment, promoting sustainable practices.",
            "They advocate for the protection of natural habitats, believing in the sanctity of life.",
            "They support local healers and herbalists, understanding the value of preserving life.",
            "They celebrate life’s milestones with the community, fostering a culture of appreciation for life."
        ],
        "Respect": [
            "They treat everyone with respect, regardless of their status or background.",
            "They value honest and respectful interactions, fostering a welcoming atmosphere in their shop.",
            "They teach others the importance of respect through their own actions.",
            "They stand up against disrespect and injustice, defending those who are mistreated.",
            "They believe that mutual respect is the foundation of a harmonious community."
        ],
        "Self Sacrifice": [
            "They often put the needs of others before their own, believing in the virtue of self-sacrifice.",
            "They are willing to endure hardships if it means others will benefit.",
            "They support those in difficult situations, even if it means personal loss.",
            "They believe that true leadership requires self-sacrifice and lead by example.",
            "They inspire others to act selflessly, promoting a culture of altruism."
        ]
    },
    "Evil": {
        "Domination": [
            "They seek to control others, believing that their vision is the only correct one.",
            "They manipulate situations to gain power over others, asserting their dominance.",
            "They believe in ruling through fear and intimidation, keeping others in line.",
            "They see subjugation as a means to achieve their goals, regardless of the cost to others.",
            "They foster an environment of obedience, where their word is law."
        ],
        "Greed": [
            "They are driven by an insatiable desire for wealth, often at the expense of others.",
            "They prioritize profit above all else, willing to exploit any opportunity for gain.",
            "They hoard resources and wealth, believing that more is never enough.",
            "They manipulate and deceive to increase their fortune, showing little regard for ethics.",
            "They view generosity as a weakness, always seeking to amass more for themselves."
        ],
        "Might": [
            "They believe that strength and power are the ultimate measures of worth.",
            "They respect only those who demonstrate physical or political power.",
            "They use their strength to intimidate and control others, asserting their superiority.",
            "They see conflict as a way to prove their might, often instigating fights to show dominance.",
            "They admire and seek alliances with the powerful, dismissing the weak as unworthy."
        ],
        "Pain": [
            "They take pleasure in causing pain, believing it is a tool for control.",
            "They see suffering as a natural order, often inflicting it to achieve their aims.",
            "They lack empathy for others' pain, viewing it as a necessary consequence of their actions.",
            "They use pain to break the will of others, ensuring compliance and obedience.",
            "They view mercy as a flaw, embracing cruelty as a means to maintain order."
        ],
        "Retribution": [
            "They believe in strict retribution, exacting revenge for any perceived slight.",
            "They hold grudges and seek vengeance, often going to great lengths to settle scores.",
            "They see retribution as justice, believing that those who wrong them deserve punishment.",
            "They are relentless in their pursuit of those who have wronged them, showing no mercy.",
            "They teach others that retaliation is a rightful response, perpetuating cycles of vengeance."
        ],
        "Slaughter": [
            "They believe in swift and decisive action, sometimes resorting to extreme measures to eliminate threats.",
            "They see violence as a necessary tool to maintain control and achieve their goals.",
            "They view the elimination of their enemies as a necessary step to achieve their ambitions.",
            "They have a cold, calculating approach to dealing with threats.",
            "They believe that fear and intimidation through acts of violence can be effective in maintaining order."
        ]
    },
    "Lawful": {
        "Community": [
            "They work tirelessly to strengthen the bonds within their community.",
            "They organize and participate in community events, fostering a sense of unity.",
            "They believe that a strong community is built on cooperation and mutual support.",
            "They advocate for policies and practices that benefit the community as a whole.",
            "They see themselves as a guardian of community values, promoting harmony and togetherness."
        ],
        "Fairness": [
            "They strive to treat everyone equally, ensuring fairness in all their dealings.",
            "They believe in justice and equality, advocating for fair treatment of all individuals.",
            "They work to eliminate biases and prejudices, promoting fairness in the community.",
            "They ensure that their business practices are transparent and just.",
            "They are a vocal advocate for fair laws and practices, striving to create a just society."
        ],
        "Honor": [
            "They live by a code of honor, always keeping their word and standing by their principles.",
            "They value integrity and expect the same from those around them.",
            "They are respected for their unwavering commitment to doing what is right.",
            "They believe that honor is the foundation of a good reputation and a just life.",
            "They often mediate disputes, their sense of honor guiding them to fair resolutions."
        ],
        "Logic": [
            "They approach problems and decisions with a logical and analytical mindset.",
            "They value reason and evidence, avoiding decisions based on emotions or whims.",
            "They are known for their clear thinking and practical solutions.",
            "They believe that logic and reason should guide actions and policies.",
            "They often serve as the voice of reason, helping others see the logical path forward."
        ],
        "Responsibility": [
            "They take their responsibilities seriously, always fulfilling their duties.",
            "They believe that everyone has a role to play and must act responsibly.",
            "They are dependable and trustworthy, known for their reliability.",
            "They advocate for responsible behavior in the community, leading by example.",
            "They hold themselves and others accountable for their actions, promoting a sense of responsibility."
        ],
        "Tradition": [
            "They respect and uphold traditions, seeing them as the backbone of society.",
            "They believe that traditions connect the present with the past, providing stability.",
            "They participate in and organize traditional events, keeping cultural practices alive.",
            "They teach the importance of tradition to younger generations, ensuring its continuity.",
            "They see value in time-honored practices, believing they provide wisdom and guidance."
        ]
    },
    "Chaotic": {
        "Change": [
            "They embrace change, always looking for new ways to improve and innovate.",
            "They believe that progress comes from change and are not afraid to disrupt the status quo.",
            "They adapt quickly to new situations, thriving in dynamic environments.",
            "They encourage others to be open to change, seeing it as a path to growth.",
            "They are known for their forward-thinking and willingness to embrace the unknown."
        ],
        "Creativity": [
            "They value creativity, always looking for unique and innovative solutions.",
            "They encourage artistic expression and support creative endeavors in the community.",
            "They believe that creativity drives progress and personal fulfillment.",
            "They are known for their imaginative ideas and original approaches.",
            "They inspire others to think outside the box and explore their creative potential."
        ],
        "Freedom": [
            "They believe in the importance of personal freedom and autonomy.",
            "They advocate for individual rights, opposing any form of oppression.",
            "They encourage others to pursue their own paths, free from societal constraints.",
            "They value the freedom to make their own choices, even if it means taking risks.",
            "They fight against any forces that threaten personal liberties."
        ],
        "Independence": [
            "They value self-reliance and encourage others to be independent.",
            "They believe that everyone should have the freedom to govern their own lives.",
            "They are known for their strong sense of individuality, often marching to the beat of their own drum.",
            "They resist any attempts to control or constrain them, fiercely guarding their independence.",
            "They inspire others to find their own path, emphasizing the importance of personal freedom."
        ],
        "No Limits": [
            "They reject any form of limitation, believing that potential is boundless.",
            "They constantly push boundaries, seeking to explore and achieve more.",
            "They encourage others to break free from constraints and think beyond conventional limits.",
            "They thrive in environments where creativity and innovation are encouraged without restrictions.",
            "They view rules and regulations as mere suggestions, often bending or breaking them to achieve their goals."
        ],
        "Whimsy": [
            "They approach life with a playful and whimsical attitude, always finding joy in the unexpected.",
            "They often make decisions based on whims, adding an element of surprise to their actions.",
            "They bring a sense of fun and spontaneity to everything they do, making them a delight to be around.",
            "They believe that life is too short to be serious all the time, embracing a lighthearted approach.",
            "They encourage others to embrace their playful side, fostering a carefree and joyful environment."
        ]
    },
    "Neutral": {
        "Balance": [
            "They strive to maintain balance in all aspects of life, believing that extremes are harmful.",
            "They promote harmony and equilibrium, both in their personal life and in the community.",
            "They make decisions that aim to balance competing interests and needs.",
            "They believe in the natural balance of the world, advocating for sustainable practices.",
            "They seek to mediate conflicts and restore balance when things are out of harmony."
        ],
        "Knowledge": [
            "They value the pursuit of knowledge, always seeking to learn and understand more.",
            "They believe that knowledge is the key to personal and societal growth.",
            "They support educational initiatives and encourage others to seek enlightenment.",
            "They are well-read and knowledgeable, often sharing their insights with others.",
            "They believe that an informed community is a strong community, advocating for access to information."
        ],
        "Tolerance": [
            "They believe in allowing others to live their lives as they see fit, without interference.",
            "They respect the choices of others, even when they disagree with them.",
            "They avoid imposing their beliefs on others, promoting a live-and-let-live philosophy.",
            "They advocate for personal freedom and respect for individual lifestyles.",
            "They believe that peace comes from mutual respect and non-interference."
        ],
        "Moderation": [
            "They believe in the virtue of moderation, avoiding excess in all things.",
            "They advocate for a balanced lifestyle, promoting health and well-being.",
            "They approach problems with a moderate perspective, avoiding extreme solutions.",
            "They encourage others to find balance and avoid the pitfalls of excess.",
            "They practice moderation in their own life, setting an example for others."
        ],
        "Neutrality": [
            "They strive to remain neutral in conflicts, believing that taking sides often leads to more harm.",
            "They are seen as impartial and fair, often mediating disputes with an unbiased perspective.",
            "They avoid extreme positions, seeking a middle ground that benefits all parties.",
            "They believe that neutrality helps maintain peace and stability.",
            "They are trusted by others to provide balanced and fair opinions."
        ],
        "People": [
            "They believe that the well-being of people is the highest priority.",
            "They work to improve the lives of others, regardless of personal gain.",
            "They advocate for policies and actions that benefit the broader community.",
            "They believe in the inherent value of every individual, striving to uplift those around them.",
            "They are dedicated to serving others, often putting the needs of people first."
        ]
    },
    "Other": {
        "Aspiration": [
            "They are driven by high aspirations, always striving to achieve their best.",
            "They set ambitious goals for themselves and work tirelessly to reach them.",
            "They inspire others to aim high and pursue their dreams.",
            "They believe that aspiration leads to progress and personal growth.",
            "They are constantly looking for new challenges to conquer, never satisfied with mediocrity."
        ],
        "Discovery": [
            "They have a passion for discovery, always seeking to explore new places and ideas.",
            "They believe that life is an endless journey of discovery and learning.",
            "They encourage others to be curious and adventurous, promoting a culture of exploration.",
            "They find joy in uncovering new knowledge and experiences.",
            "They are known for their adventurous spirit, often leading expeditions into the unknown."
        ],
        "Glory": [
            "They seek glory in their actions, always aiming to achieve great things.",
            "They believe that glory comes from deeds that are remembered and celebrated.",
            "They strive to make a name for themselves, leaving a lasting legacy.",
            "They inspire others to seek glory through honorable and courageous actions.",
            "They are driven by a desire for recognition and acclaim, always pushing their limits."
        ],
        "Nation": [
            "They have a deep sense of patriotism, always working for the betterment of their nation.",
            "They believe in the values and ideals of their homeland, striving to uphold them.",
            "They advocate for policies that benefit their nation, often putting national interest first.",
            "They inspire others with their dedication to their country and its people.",
            "They believe that a strong nation is built on the efforts and loyalty of its citizens."
        ],
        "Redemption": [
            "They believe in the power of redemption, always offering second chances.",
            "They work to help others atone for their mistakes and find a path to redemption.",
            "They are dedicated to their own journey of redemption, striving to right past wrongs.",
            "They inspire hope in others, showing that it is never too late to change.",
            "They believe that redemption is a noble goal, worth pursuing despite the challenges."
        ],
        "Self Knowledge": [
            "They value self-knowledge, always seeking to understand themselves better.",
            "They believe that true wisdom comes from introspection and self-awareness.",
            "They encourage others to embark on journeys of self-discovery.",
            "They practice mindfulness and reflection, constantly learning from their experiences.",
            "They are known for their deep insights into human nature and the self."
        ]
    }
}


def main():
    ideal = get_ideal_UI()
    print(f"{ideal}")


def get_ideal():
    alignment = random.choice(list(ideals))
    ideal = random.choice(list(ideals[alignment]))
    ideal_desc = random.choice(ideals[alignment][ideal])
    return ideal_desc


def get_ideal_UI():
    a_keys = list(ideals.keys())

    while True:
        print()
        print("Would you like this characters ideal to be based off of alignment?")
        print()
        q1 = input("Answer: ")
        print()

        if q1.lower() in ['y', 'yes']:
            print("Which alignment would you like their ideal to belong to?")
            print()
            for align in a_keys:
                print(f"{align:<20}", end="")
                if (a_keys.index(align) + 1) % 3 == 0:
                    print()
            print()
            q2 = input("Answer: ")
            answer2 = q2.title()
            print()

            if answer2 in a_keys:
                i_keys = list(ideals[answer2].keys())
                print("Which ideal would you like this character to have?")
                print()
                for i in i_keys:
                    print(f"{i:<20}", end="")
                    if (i_keys.index(i) + 1) % 3 == 0:
                        print()
                print()
                q3 = input("Answer: ")
                answer3 = q3.title()
                if answer3 in i_keys:
                    ideal = random.choice(ideals[answer2][answer3])
                    return ideal
                else:
                    print(f"Unrecognized input: {answer3}")
                    continue
            else:
                print(f"Unrecognized input: {answer2}")
                continue

        elif q1.lower() in ['n', 'no']:
            sub_key_list = []

            print("Which ideal would you like this character to have?")
            print()

            for k in a_keys:
                sub_keys = (list(ideals[k].keys()))
                for sk in sub_keys:
                    sub_key_list.append(sk)
                    print(f"{sk:<20}", end="")
                    if (sub_keys.index(sk) + 1) % 3 == 0:
                        print()

            print()
            subq2 = input("Answer: ")
            subans2 = subq2.title()
            print()

            if subans2 in sub_key_list:
                for k in a_keys:
                    if subans2 in ideals[k]:
                        ideal = random.choice(ideals[k][subans2])
                        return ideal
            else:
                print(f"Unrecognized input: {subans2}")
                continue

        else:
            print(f"Unrecognized input: {q1}")
            continue


if __name__ == "__main__":
    main()
