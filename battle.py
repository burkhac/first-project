
import random
from characters import Character, Monster

# determines the amount of damage the attacker deals and the amount the defender takes
# random damage from 0 to the attackers attack rating defined in characters.py. Take damage is also
# a method from character that allows that player to take damage
def determine_damage(attacker, defender):
    damage_dealt = random.randint(0, attacker.attack)
    defender.take_damage(damage_dealt)


#randomly determines which character damaged the other. If >5 character 1 takes damage if <5 character 2 takes
# also has option for the wizard to "cast spell" method from character. 1/10 chance. Calls determine damage method above
# to manage the damage dealt
def damage_who(character1, character2):
    roll = random.randint(0, 10)
    if roll == 3 and isinstance(character2, Monster):
        character2.cast_spell(character1)

    if  roll >=5 :
        determine_damage(character2, character1)

    else:
        determine_damage(character1, character2)

#starts the action between the two characters.  takes in our hero and wizard in main. while the characters hp > 0 this
# function calls the damage_who method above to determine who is damaged which calls the determine damage method to
# determine how much is dealt.  If the hp drops below 0 the player has been defeated
def start_battle(character1, character2):
    while character1.hp > 0 and character2.hp > 0:
        damage_who(character1, character2)
        if character1.hp < 0:
            print(f"{character1.name} has been defeated")
            break
        if character2.hp < 0:
            print(f"{character2.name} has been defeated")
            break



