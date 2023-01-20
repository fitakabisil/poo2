import random

# numéro d'attribue
lancer_dé1 = random.sample(range(1, 6), 4)
lancer_dé1.remove(min(lancer_dé1))
Sum1 = sum(lancer_dé1)
Str1 = str(Sum1)

lancer_dé2 = random.sample(range(1, 6), 4)
lancer_dé2.remove(min(lancer_dé2))
Sum2 = sum(lancer_dé2)
Str2 = str(Sum2)

lancer_dé3 = random.sample(range(1, 6), 4)
lancer_dé3.remove(min(lancer_dé3))
Sum3 = sum(lancer_dé3)
Str3 = str(Sum3)

lancer_dé4 = random.sample(range(1, 6), 4)
lancer_dé4.remove(min(lancer_dé4))
Sum4 = sum(lancer_dé4)
Str4 = str(Sum4)

lancer_dé5 = random.sample(range(1, 6), 4)
lancer_dé5.remove(min(lancer_dé5))
Sum5 = sum(lancer_dé5)
Str5 = str(lancer_dé5)

lancer_dé6 = random.sample(range(1, 6), 4)
lancer_dé6.remove(min(lancer_dé6))
Sum6 = sum(lancer_dé6)
Str6 = str(lancer_dé6)


class NPC:

    def __int__(self):
        self.Force = Str1

        self.Agilité = Str2

        self.Constitution = Str3

        self.Intelligence = Str4

        self.Sagesse = Str5

        self.Charisme = Str6

        self.class_armure = random.randint(1, 12)

        self.points_vie = random.randint(1, 20)

        self.race = 'Human'

        self.profession = 'fermier'

    def set_stats(self, Force, Agilité, Constitution, Intelligence, Sagesse, Charisme, class_armure, points_vie, race, profession):
        
        self.Force = Force

        self.Agilité = Agilité

        self.Constitution = Constitution

        self.Intelligence = Intelligence

        self.Sagesse = Sagesse

        self.Charisme = Charisme

        self.class_armure = class_armure

        self.points_vie = points_vie

        self.race = race

        self.profession = profession

    def print_stats(self):

        print('stats NPC:')
        print('Force:', self.Force)
        print('Agilité:', self.Agilité)
        print('Constitution:', self.Constitution)
        print('Intelligence:', self.Intelligence)
        print('Sagesse:', self.Sagesse)
        print('Charisme:', self.Charisme)
        print("Classe de l'armure:", self.class_armure)
        print('Race:', self.race)
        print('Profession:', self.profession)

npc = NPC()
print(NPC().print_stats())

