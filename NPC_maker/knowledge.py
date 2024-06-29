useful_knowledge = {
    "Herbal Remedies": [
        "They know how to identify and harvest medicinal herbs from the wild.",
        "They can create effective poultices for treating wounds and burns.",
        "They have recipes for teas that can alleviate common ailments like colds and headaches.",
        "They understand the properties of different plants and their uses in healing.",
        "They can recognize poisonous plants and know how to treat poisoning.",
        "They have knowledge of rare herbs that can boost vitality and energy.",
        "They can make salves and ointments that relieve pain and inflammation.",
        "They know which herbs can be used to improve sleep and reduce anxiety.",
        "They can prepare tinctures that strengthen the immune system.",
        "They understand the seasonal cycles of herbs and when they are most potent."
    ],
    "Local History": [
        "They know the legends and myths of the region, often sharing them with visitors.",
        "They can recount the history of the village and its founding.",
        "They have knowledge of ancient ruins and their significance.",
        "They know the stories of notable figures and heroes from the past.",
        "They can explain the origins of local festivals and traditions.",
        "They are aware of past conflicts and their impact on the village.",
        "They know the locations of old battlefields and significant historical sites.",
        "They can describe the changes in the landscape over the centuries.",
        "They are familiar with old maps and how the village has grown.",
        "They can recount tales of past natural disasters and how the village recovered."
    ],
    "Trade and Barter": [
        "They know the fair prices for various goods and services in the region.",
        "They can identify high-quality merchandise and detect counterfeit items.",
        "They understand the principles of supply and demand and how to maximize profits.",
        "They have knowledge of trade routes and the best times to buy and sell.",
        "They can negotiate effectively, ensuring favorable deals.",
        "They know how to appraise items and determine their true value.",
        "They are aware of the reputations of various merchants and traders.",
        "They can recognize market trends and adjust their inventory accordingly.",
        "They understand the logistics of transporting goods safely and efficiently.",
        "They can offer advice on bartering and getting the best possible exchange."
    ],
    "Cooking and Culinary Arts": [
        "They know how to prepare a wide variety of dishes from different cultures.",
        "They can identify the best ingredients and where to source them.",
        "They understand the principles of flavor pairing and seasoning.",
        "They have recipes for hearty meals that can sustain travelers and adventurers.",
        "They can bake bread, pastries, and other baked goods to perfection.",
        "They know techniques for preserving food, such as smoking, drying, and pickling.",
        "They can create delicious and nutritious meals from simple ingredients.",
        "They understand the dietary needs of different races and can cater to them.",
        "They have knowledge of rare and exotic spices and how to use them.",
        "They can prepare special meals for festivals and celebrations, adding to the joy of the occasion."
    ],
    "Weapon Maintenance and Repair": [
        "They know how to sharpen blades to a razor edge.",
        "They can repair damaged weapons, restoring them to their former glory.",
        "They understand the properties of different metals and their uses in weaponry.",
        "They can craft basic weapons and tools in a pinch.",
        "They know how to maintain bows and crossbows, ensuring they are always ready for use.",
        "They can recognize quality craftsmanship in weapons and armor.",
        "They understand the importance of balance and weight in a good weapon.",
        "They can offer advice on the best weapons for different combat styles.",
        "They know techniques for reinforcing armor and making it more durable.",
        "They can create custom modifications to weapons, enhancing their effectiveness."
    ],
    "Animal Husbandry": [
        "They know how to care for and train horses, making them reliable mounts.",
        "They can treat common illnesses and injuries in livestock.",
        "They understand the dietary needs of different animals and how to provide for them.",
        "They can recognize signs of distress or illness in animals and take appropriate action.",
        "They know techniques for breeding healthy and strong animals.",
        "They can shear sheep and process wool for various uses.",
        "They understand the importance of proper shelter and hygiene for animals.",
        "They can train dogs for hunting, guarding, or companionship.",
        "They know how to milk cows, goats, and other dairy animals efficiently.",
        "They can manage a small farm, ensuring all animals are well cared for."
    ],
    "Survival Skills": [
        "They know how to build a shelter using natural materials found in the wilderness.",
        "They can start a fire in any weather, using various techniques.",
        "They understand how to find and purify water in the wild.",
        "They can identify edible plants and berries, as well as those to avoid.",
        "They know how to navigate using the stars, sun, and natural landmarks.",
        "They can set traps and snares to catch small game for food.",
        "They understand basic first aid and how to treat injuries in the field.",
        "They can signal for help using various methods, such as smoke or mirrors.",
        "They know how to pack efficiently for long journeys, ensuring all essentials are covered.",
        "They can improvise tools and weapons from natural materials, aiding in their survival."
    ],
    "Lore of Magical Creatures": [
        "They know the habits and habitats of various magical creatures.",
        "They can identify signs of a magical creature’s presence, such as tracks or sounds.",
        "They understand the strengths and weaknesses of different creatures.",
        "They can offer advice on how to avoid or defend against dangerous magical beings.",
        "They know the lore and legends surrounding rare and mythical creatures.",
        "They can recognize artifacts and items associated with magical creatures.",
        "They understand the significance of creature sightings and what they may foretell.",
        "They can recount tales of famous encounters with magical creatures.",
        "They know how to approach and interact with friendly magical beings.",
        "They can identify the best times and places to observe certain creatures."
    ],
    "Potion Brewing": [
        "They know recipes for a wide variety of potions, from healing draughts to strength elixirs.",
        "They understand the properties of different ingredients and how they interact.",
        "They can identify and harvest rare plants and materials for potion making.",
        "They know techniques for safely brewing and storing potions.",
        "They can recognize the signs of a properly brewed potion and its effects.",
        "They understand the dangers of potion making and how to avoid accidents.",
        "They can create antidotes for various poisons and toxins.",
        "They know how to enhance potions with magical components for greater efficacy.",
        "They can offer advice on the best potions for different situations and needs.",
        "They have knowledge of historical and legendary potions and their recipes."
    ],
    "Architecture and Building": [
        "They know how to design and construct sturdy buildings using local materials.",
        "They understand the principles of structural integrity and load-bearing.",
        "They can plan and lay out a construction site efficiently.",
        "They know techniques for building in different terrains and climates.",
        "They can recognize and work with various building materials, from wood to stone.",
        "They understand the importance of insulation and ventilation in building design.",
        "They can create detailed blueprints and plans for construction projects.",
        "They know how to repair and reinforce existing structures.",
        "They can oversee a construction crew, ensuring work is done correctly and safely.",
        "They have knowledge of historical architectural styles and can replicate them accurately."
    ]
}

import random

def main():
    knowledge = get_useful_knowledge()
    print(f"{knowledge}")


def get_useful_knowledge():
    k_class = random.choice(list(useful_knowledge))
    knows = random.choice(list(useful_knowledge[k_class]))
    return knows

if __name__ == "__main__":
    main()
