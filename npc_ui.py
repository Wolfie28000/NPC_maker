from appearance import get_appearance_UI, get_appearance
from attributes import get_att_UI, get_attribute
from bonds import get_bond_UI, get_bond
from flaws import get_flaw_UI, get_flaw
from ideals import get_ideal_UI, get_ideal
from interactions import get_interaction_UI, get_interaction
from knowledge import get_know_UI, get_useful_knowledge
from mannerisms import get_mannerism_UI, get_mannerism
from name_maker import get_name_UI, get_random_name
from talents import get_talent_UI, get_talent
from number_strings import convert_text_to_int
import re
import random


random_custom_accepted = ["random", "r", "custom", "randomized", "customized", "c", "ran", "cus"]
len_keys = ["basic", "full", "tell me more"]
approved_atts = ["str", "strength", "dex", "dexterity", "con", "constitution", "int", "intelligence",
                 "wis", "wisdom", "cha", "charisma", "ran", "random"]
npc_build_options = ["Race", "Appearance", "Attributes", "Bonds", "Flaws", "Ideals", "Interactions",
                     "Mannerisms", "Talents", "Useful Knowledge"]

npc_dict = {
    "race": None,
    "appearance": None,
    "attributes": None,
    "interactions": None,
    "mannerisms": None,
    "knowledge": None,
    "bonds": None,
    "ideals": None,
    "flaws": None,
    "talents": None
}

custom_functions = {
    "race": get_name_UI,
    "appearance": get_appearance_UI,
    "attributes": get_att_UI,
    "interactions": get_interaction_UI,
    "mannerisms": get_mannerism_UI,
    "knowledge": get_know_UI,
    "bonds": get_bond_UI,
    "ideals": get_ideal_UI,
    "flaws": get_flaw_UI,
    "talents": get_talent_UI
}

random_functions = {
    "race": get_random_name,
    "appearance": get_appearance,
    "attributes": get_attribute,
    "interactions": get_interaction,
    "mannerisms": get_mannerism,
    "knowledge": get_useful_knowledge,
    "bonds": get_bond,
    "ideals": get_ideal,
    "flaws": get_flaw,
    "talents": get_talent
}


def main():
    collect_all_npcs_UI()


def collect_all_npcs_UI():
    print()
    runs = convert_text_to_int(input("How many NPCs do you want to generate? "))
    npcs = 0
    all_npcs = []

    while npcs < runs:
        if npcs == 0:
            iteration = "first"
        elif runs - npcs > 1:
            iteration = "next"
        elif runs - npcs == 1:
            iteration = "final"
        print()
        print(f"Would you like your {iteration} NPC to be randomly generated, or customized?")
        print()
        rand_cus = input("Answer: ").lower().strip()
        print()

        if rand_cus in random_custom_accepted:
            if rand_cus in ["custom", "cus", "c", "customized"]:
                output_len = get_output_len()
                if output_len == "basic":
                    this_npc = custom_NPC_UI()
                    all_npcs.append(this_npc)
                    npcs += 1
                elif output_len == "full":
                    this_npc = custom_NPC_UI()
                    for i in this_npc:
                        if this_npc[i] == None:
                            this_npc.update({i: random_functions[i]()})
                    all_npcs.append(this_npc)
                    npcs += 1
            if rand_cus in ["random", "rand", "r", "randomized"]:
                output_len = get_output_len()
                if output_len == "basic":
                    this_npc = npc_dict.copy()
                    key_list = list(this_npc.keys())
                    chosen_key = random.choice(key_list[2:])
                    this_npc.update({"race": random_functions["race"]()})
                    this_npc.update({"appearance": random_functions["appearance"]()})
                    this_npc.update({chosen_key: random_functions[chosen_key]()})
                    all_npcs.append(this_npc)
                    npcs += 1
                elif output_len == "full":
                    this_npc = npc_dict.copy()
                    for i in this_npc:
                        if this_npc[i] == None:
                            this_npc.update({i: random_functions[i]()})
                    all_npcs.append(this_npc)
                    npcs += 1
        else:
            continue

    for npc in all_npcs:
        aspect_list = list(npc.values())
        for i, aspect in enumerate(aspect_list):
            if aspect != None:
                print(f"{aspect}")
            else:
                continue
        print()




def custom_NPC_UI():
    npc = npc_dict.copy()

    custom_function_keys = list(custom_functions.keys())

    print("How would you like to customize this character?")
    print("Keep typing your responses, and press enter when complete.")
    print()
    for i, aspect in enumerate(custom_function_keys):
        print(f"{aspect.title():<20}", end="")
        if (i + 1) % 3 == 0 or (i + 1) == len(custom_function_keys):
            print()
    print()

    custom_wanted = input("Answer: ").strip()
    cf_wanted = custom_wanted.casefold()
    cf_wanted = re.split(r'[^a-zA-Z\d]', cf_wanted)

    print()

    check_duplicates = []

    for i in cf_wanted:
        if i in custom_function_keys and i not in check_duplicates:
            npc.update({i: custom_functions[i]()})
            check_duplicates.append(i)
        elif i not in custom_function_keys:
            print("Not a recognized input. Please try again.")
            print()
            custom_NPC_UI()

        if i in check_duplicates:
            continue

    must_haves = ["race", "appearance"]

    for i in must_haves:
        if npc[i] == None:
            npc.update({i: random_functions[i]()})
            check_duplicates.append(i)

    return npc


def get_output_len():

    len_keys = ["basic", "full", "tell", "me", "more"]

    while True:
        key_join = ' '.join(len_keys[2:5])
        update = []
        update.extend(len_keys[:2])
        update.append(key_join)

        print("Would you like a basic or full length character description?")
        for i, key in enumerate(update):
            print(f"{key.title():<15}", end="")
            if (i + 1) == len(len_keys):
                print()
        print()
        print()
        an = input("Answer: ").lower().strip()
        search_for = re.compile(r'|'.join(len_keys))
        answer = search_for.findall(an)
        print()

        if answer and answer[0] in len_keys[:2]:
            return answer[0]

        elif answer[0] in len_keys[2:5]:
            print("This question is asking for your desired length of output.")
            print()
            print("Which option would you like to know more about?")
            print()
            for i, key in enumerate(len_keys[:2]):
                print(f"{key.title():<20}", end="")
                if (i + 1) == len(len_keys):
                    print()
            print()
            print()
            explain_me = input("Answer: ").lower().strip()
            print()
            if explain_me == "basic":
                explain_basic()
            elif explain_me == "full":
                explain_full()
            continue

        else:
            continue


def explain_basic():
    print("If you choose a basic output, you will generate either:")
    print()
    print("(If Customized) - Customized or Random Name/Race and Appearance,")
    print("and only other customization choices you have selected.")
    print()
    print("(If Randomized) - Name/Race, Appearance, and one other")
    print("random descriptor from the list below.")
    print()
    for i, aspect in enumerate(npc_build_options):
        print(f"{aspect.title():<20}", end="")
        if (i + 1) % 3 == 0 or (i + 1) == len(npc_build_options):
            print()
    print()


def explain_full():
    print("If you choose a full output, you will generate either:")
    print()
    print("(If Randomized) - An entirely randomized NPC consisting of their:")
    print()
    for i, aspect in enumerate(npc_build_options):
        print(f"{aspect.title():<20}", end="")
        if (i + 1) % 3 == 0 or (i + 1) == len(npc_build_options):
            print()
    print()
    print("(If Customized) - All customized choices plus whatever else you")
    print("didn't explicitly request from the same list as above.")
    print()



'''
----------------------------------------------------------------
#
More NPC Customization options!:
    Plans include:
        the ability to convert to PDF!!!!!
        adding background options
        adding looted NPC inventory
        adding NPC ability scores (rollable and chosen)
        adding monsterous NPC options
        Other races/names
        Pets!
        NPC subnpcs (The blacksmiths son, the princess's favorite servant, etc.)
        And MORE! Maybe.
#
#

Would you like this NPC to be a questgiver?
#
    ***
    Feature Coming Soon(ish)(probably)
    Plans include:
        Fetch Quest
        Delivery Quests
        Destroy Quests
        HEISTS!!
        Escape Quests
        Defense Quests
        Investigation Quests
        Escort Quests
        Rescue Quests
    ***
#
-----------------------------------------------------------------------
#
Would you like this NPC to be a shopkeeper?
#
    ***
    Feature Coming Soon(ish)
    Shops (Names and Inventories) included:
        Pawnshops and General Stores
        Container and Potion Shops
        Undertakers, Clerics, and Necromancers
        Food and Ingredient Vendors
        Books, Mapmakers, and Scribes
        Weapon / Armor smiths
        Tailor / Jewelers
        Enchanters
    Buying and Selling bonuses and discounts
    ***
#
-----------------------------------------------------------------------
'''

if __name__ == "__main__":
    main()
