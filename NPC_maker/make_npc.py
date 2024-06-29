import random
import sys
from random_npc import random_basic_npc, random_full_npc
from name_maker import get_random_name, get_specific_name
from appearance_maker import get_appearance, get_random_appearance, get_specific_appearance
from attributes import get_attribute, random_att, specific_att
from talents import get_talent, random_talent, specific_talent
from mannerisms import get_mannerism
from interactions import get_interaction
from ideals import get_ideal
from knowledge import get_useful_knowledge
from bonds import get_bond
from flaws import get_flaw

length_of_description = ["basic", "full"]

available_races = ["dragonborn", "dwarf", "elf", "gnome", "halfling", "human",
                   "halfelf", "halforc", "tiefling"]

available_att = ["highstr", "highdex", "highcon", "highint", "highwis", "highcha",
                 "lowstr", "lowdex", "lowcon", "lowint", "lowwis", "lowcha"]

available_lifestyles = ["modest", "comfortable", "wealthy", "aristocratic", "monsterous"]

talent_list = ['instruments', 'languages', 'luck', 'memory', 'animals', 'children', 'puzzles', 'game',
               'impersonations', 'drawing', 'painting', 'singing', 'drinking', 'carpentry', 'cooking', 'darts', 'dancing']

full_list = [
    'dragonborn', 'dwarf', 'elf', 'gnome', 'halfling',
    'human', 'halfelf', 'halforc', 'tiefling', 'highstr',
    'highdex', 'highcon', 'highint', 'highwis', 'highcha',
    'lowstr', 'lowdex', 'lowcon', 'lowint', 'lowwis', 'lowcha',
    'modest', 'comfortable', 'wealthy', 'aristocratic', 'monsterous',
    'instruments', 'languages', 'luck', 'memory', 'animals', 'children',
    'puzzles', 'games', 'impersonations', 'drawing', 'painting',
    'singing', 'drinking', 'carpentry', 'cooking', 'darts', 'dancing'
    ]

    '''
    full_list_new = []
    for i in range(len(full_list)):
        full_list_new.append(full_list[i])
    print(full_list_new)
    '''


def main():
    get_NPC()



def get_NPC():
    NPC_info = []
    while True:
        if len(sys.argv) >= 1:
            '''
            Get description length if random
            '''
            for i in range(len(sys.argv)):
                if sys.argv[i] in length_of_description:
                    if "basic" in sys.argv[i]:
                        descript = random_basic_npc()
                    elif "full" in sys.argv[i]:
                        descript = random_full_npc()
                    return descript


            '''
            Get name
            '''
            for n in range(len(sys.argv)):
                if sys.argv[n] not in full_list:
                    name = get_random_name()
                elif sys.argv[n] in available_races:
                    name = get_specific_name()
            print('')
            print(name)
            print('')



            '''
            Get appearance
            '''
            for j in range(len(sys.argv)):
                if sys.argv[j] not in full_list:
                    appearance = get_random_appearance()
                elif sys.argv[j] in available_lifestyles:
                    appearance = (f"They are wearing {get_specific_appearance()}.")
            NPC_info.append(appearance)


            '''
            Get attributes
            '''
            for at in range(len(sys.argv)):
                if sys.argv[at] not in full_list:
                    att = random_att()
                elif sys.argv[at] in available_att:
                    att = specific_att()
            NPC_info.append(att)


            '''
            Get talents
            '''
            for tal in range(len(sys.argv)):
                if sys.argv[tal] not in full_list:
                    talent = random_talent()
                elif sys.argv[tal] in talent_list:
                    talent = specific_talent()
            NPC_info.append(talent)


        '''
        Print it out
        '''
        print("Description:")
        print("")
        for i in range(len(NPC_info)):
            print(f"{NPC_info[i]}")
        print("")
        return



def get_rand_basic_NPC():
    description = []

    description.append(get_appearance())
    description.append(get_attribute())
    description.append(get_talent())
    description.append(get_mannerism())
    description.append(get_interaction())
    description.append(get_ideal())
    description.append(get_useful_knowledge())
    description.append(get_bond())
    description.append(get_flaw())

    random.shuffle(description)
    print("Description:")
    print("")
    print(f"{description[0]}")
    print(f"{description[1]}")
    print(f"{description[2]}")
    print("")


def get_rand_full_NPC():
    description = []

    description.append(get_appearance())
    description.append(get_attribute())
    description.append(get_talent())
    description.append(get_mannerism())
    description.append(get_interaction())
    description.append(get_ideal())
    description.append(get_useful_knowledge())
    description.append(get_bond())
    description.append(get_flaw())

    random.shuffle(description)

    print("Description:")
    print("")
    for i in range(len(description)):
        print(f"{description[i]}")
        i += 1
    print("")


if __name__ == "__main__":
    main()
