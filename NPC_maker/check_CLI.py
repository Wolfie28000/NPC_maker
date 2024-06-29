import sys
from name_maker import get_random_name, get_specific_name
from appearance_maker import get_rand_appearance, get_specific_lifestyle
from attributes import specific_att, random_att
from talents import get_talent
from mannerisms import get_mannerism
from interactions import get_interaction
from ideals import get_ideal
from knowledge import get_useful_knowledge
from bonds import get_bond
from flaws import get_flaw
from make_npc import get_complete_NPC, get_specific_description

type_of_description = ["basic", "full"]

available_races = ["dragonborn", "dwarf", "elf", "gnome", "halfling",
                   "human", "halfelf", "halforc", "tiefling"]

available_att = ["highstr", "highdex", "highcon", "highint", "highwis", "highcha",
                 "lowstr", "lowdex", "lowcon", "lowint", "lowwis", "lowcha"]

available_lifestyles = ["modest", "comfortable", "wealthy", "aristocratic", "monsterous"]

def main():
    check_CLI()


def check_CLI():
    print(check_desc_len())
    print(check_lifestyle())
    print(check_name())
    print(check_att())


def check_desc_len():
    for i in range(len(sys.argv)):
        if len(sys.argv) >= 1 and sys.argv[i] not in type_of_description:
            arg = get_complete_NPC()
        if len(sys.argv) > 1 and sys.argv[i] in type_of_description:
            arg = get_specific_description()
        return arg


def check_lifestyle():
    for i in range(len(sys.argv)):
        if len(sys.argv) >= 1 and sys.argv[i] not in available_lifestyles:
            arg = get_rand_appearance()
        if len(sys.argv) > 1 and sys.argv[i] in available_lifestyles:
            arg = get_specific_lifestyle()
        return arg


def check_name():
    for i in range(len(sys.argv)):
        if len(sys.argv) >= 1 and sys.argv[i] not in available_races:
            name = get_random_name()
        elif len(sys.argv) > 1 and sys.argv[i] in available_races:
            name = get_specific_name()
    return name


def check_att():
    for i in range(len(sys.argv)):
        if len(sys.argv) >= 1 and sys.argv[i] not in available_att:
            att = random_att()
        elif len(sys.argv) > 1 and sys.argv[i] in available_att:
            att = specific_att()
    return att


if __name__ == "__main__":
    main()
