#main character class. has a name, hp, attack and boolean to determine if defeated. has method to take damage in battle
class Character:
    def __init__(self, name, hp, attack, is_defeated):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.is_defeated = False
    #not used currently
    def status(self):
        print(f"you have created a new character with {self.hp} hit points and {self.attack} attack points")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} took {damage} and has {self.hp} hp left")
        if self.hp <= 0 :
            self.is_defeated = True

# Very similar to character above but with an option to cast a spell.  Redundant class for practice. can use "super" and
# and just add the cast spell method when I'm feeling less lazy.
class Monster:
    def __init__(self, name, hp, attack, magic, is_defeated):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.magic = magic
        self.is_defeated = False
    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} took {damage} and has {self.hp} hp left")
        if self.hp <= 0 :
            self.is_defeated = True

    def cast_spell(self, defender):
        print(f"{self.name} has cast a spell for {self.magic}")
        defender.hp -= self.magic

