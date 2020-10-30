import random

# Here is the code for user input which generates number of spell slots and level of spells that can be used.
#caster_level = input("What is your Spellcasting level?")
#caster_type = input("What is your Spellcasting type?")

# Here are the dictionaries of spells by level Include name, school, type, and ritual (y/n)
level_0 = {
            'Accio' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Alohomora' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Capto' : {
                  'school' : 'Charms' ,
                  'type' : 'Utility' ,
                  'ritual' : 'no' ,
                  },
            'Carpe Retractum' : {
                     'school' : 'Charms' ,
                     'type' : 'Utility' ,
                     'ritual' : 'no' ,
                     },
            'Cistem Apero' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Colloportus' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Colovaria' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Defodio' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Duro' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Finestra' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Flagrate' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Glisseo' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Illegibilus' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Impervius' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Lumos_Nox' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Molliare' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Pereo' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Periculum_Verdimllious' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Scourgify' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Sonorus_Quietus' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Spongify' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Tergeo' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
            'Wingardium Leviosa' : {
                'school' : 'Charms' ,
                'type' : 'Utility' ,
                'ritual' : 'no' ,
                },
}


level_1 = {
    'Level 1 Spell 1' : {
        'school' : 'Charms' ,
        'type' : 'Utility' ,
        'ritual' : 'no' ,
        },
    'Level 1 Spell 2' : {
            'school' : 'Charms' ,
            'type' : 'Utility' ,
            'ritual' : 'no' ,
            },

}



# Here is the code to pick random cantrips.
def pick_cantrips():
    cantrips = list(level_0.items())
    random_cantrips = random.sample(cantrips, 4)
    return(random_cantrips)

# Here is the code to generate a list.
known_cantrips = []

known_cantrips.append(pick_cantrips())

print('Your cantrips are:', '\n' .join(map(str, known_cantrips)))
