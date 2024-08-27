import random
from appearance import get_appearance
from attributes import get_attribute
from talents import get_talent
from mannerisms import get_mannerism
from interactions import get_interaction
from ideals import get_ideal
from knowledge import get_useful_knowledge
from bonds import get_bond
from flaws import get_flaw


def main():
    random_len_npc_description()


def random_basic_npc():
    description = []

    
    description.append(get_appearance())
    description.append(get_attribute())
    description.append(get_interaction())

    print("Description:")
    print("")
    print(f"{description[0]}")
    print(f"{description[1]}")
    print(f"{description[2]}")
    print("")


def random_full_npc():
    description = []

    description.append(get_appearance())
    description.append(get_attribute())
    description.append(get_interaction())
    description.append(get_mannerism())
    description.append(get_talent())
    description.append(get_ideal())
    description.append(get_useful_knowledge())
    description.append(get_bond())
    description.append(get_flaw())

    print("Description:")
    print("")
    for i in range(len(description)):
        print(f"{description[i]}")
        i += 1
    print("")



def random_len_npc_description():
    description = []

    description.append(get_appearance())
    description.append(get_attribute())
    description.append(get_interaction())
    description.append(get_mannerism())
    description.append(get_talent())
    description.append(get_ideal())
    description.append(get_useful_knowledge())
    description.append(get_bond())
    description.append(get_flaw())

    random.shuffle(description)
    desc_len = random.randrange(3, len(description))

    print("Description:")
    print("")
    for i in range(desc_len):
        print(f"{description[i]}")
    print("")




if __name__ == "__main__":
    main()
