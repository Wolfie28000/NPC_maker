
Thank you for using this tool. Please let me know if you experience bugs or would like to see a specific feature that
you might be able to use. I cant guarantee that I can do it but I can for sure try.

Love and Luck, 
- Z



if you'd like to reach out to me directly, or sign up for updates as I work on this, please send an email to:

    npc.generator.tool@gmail.com




This tool is designed to create a fully fleshed out, named and described NPC for DND5e 
    as close to plug-and-play with RAW (rules as written) as possible.



The included source materials are:
    The Dungeon Master's Guide
    The Player's Handbook
    Xanathar's Guide to Everything
    (may expand later)




The default for this program is an entirely randomized NPC, with a full, 10-11 part description.

1.) How to run the program:
    
    From the Command Line Interface (CLI):
        a.) Get into the program by typing: cd NPC_maker
        b.) Run the program by typing: python npc_maker.py
        c.) If you would like to make an adjustment to the output:
            - After you call (write the name of) the program, write any of the following inputs immediately after the program:
                ex: to make a Half-Orc, with a basic length description, and strength as their highest attribute, type:
                    
                    python npc_maker.py halforc basic highstr
    
            - The list of available output adjustments for CLI are listed below.
            
                descriptions: "basic", "full"
                race: "dragonborn", "dwarf", "elf", "gnome", "halfling", "human", "halfelf", "halforc", "tiefling"
                lifestyles: "modest", "comfortable", "wealthy", "aristocratic", "monsterous"
                attributes: "highstr", "highdex", "highcon", "highint", "highwis", "highcha",
                            "lowstr", "lowdex", "lowcon", "lowint", "lowwis", "lowcha"
                            
    From the User Interface (UI):
        a.) Get into the program by typing: cd NPC_maker
        b.) Run the program by typing: python npc_maker.py
        c.) Follow the prompts on screen.

2.) How to exit the program:

    a.) Press CTRL + C
    b.) If you would like to run the program more than once quickly, press the up arrow on your keyboard.


3.) NPC Description Terms:

    Randomized Generation:
        Will build a character for you using randomly generated output in either a basic or full sized format. 

        Basic: 
            Generates a name and race, appearance, and one other randomly determined aspect of the character

        Full:
            Generates a name and race, appearance, highest/lowest attribute, how they interact with the world
            around them, talents, mannerisms, ideals, bonds, flaws, and general knowledge
    
    Customized Generation:
        Will build a character for you using whatever specific choices you select, depending on which output length
        you choose.

        Basic: Generates a name and race, either randomly or selected by you, and however many other choices you decide
        to select for your customization.

        Full: Allows full customization of character, and if not every option is customized, provides a randomized output
        for all aspects not otherwise chosen for customization.

    Character Aspects:
        This is a simplified description of the character creation options found in the Dungeon Master's Guide (p. 89 - 91)

        Race:
            The kind of npc you are generating (E.g. Half-Orc, Dragonborn, Tiefling, etc.)
        
            Current supported races are from the Player's Handbook (p. 17 - 44)

        Appearance:
            How does this character look?
            
            You can decide if you want the character to be from a specific social standing (modest, comfortable, wealthy, etc.)
            or if you want them to have a randomized appearance
        
        Attributes:
            What is this character good/bad at?

            You can decide if you want the character to be super strong, or really smart, or incredibly unlikable here.

        Ideals:
            What shapes their actions and beliefs?

            Things like Self-Sacrifice, Revenge, Greed, etc.

        Bonds:
            What is particularly important to this NPC?

            Things like family heirlooms, friends, a lover, etc.

        Flaws:
            Why aren't they a perfect person?

            Things like greed, envy, and pride.

        Mannerisms:
            How do they move or speak?

        Interactions:
            How do they interact with the world around them?

            Are they particulary quiet? Suspicious? Friendly? Etc.

        Knowledge:
            Do they know anything useful?

            Maybe they know where a special cave is, or how to read thieves cant



4.) Future Goals:

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


        Would you like this NPC to be a questgiver?
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

        Would you like this NPC to be a shopkeeper?
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



