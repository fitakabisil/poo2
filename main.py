lancer_dé6.remove(min(lancer_dé6))
Sum6 = sum(lancer_dé6)


class NPC:

    def __int__(self):

        self.Force = Sum1

        self.Agilité = Sum2

        self.Constitution = Sum3

        self.Intelligence = Sum4

        self.Sagesse = Sum5

        self.Charisme = Sum6

        self.class_armure = random.randint(1, 12)

        self.points_vie = random.randint(1, 20)

        self.race = 'Human'

        self.profession = 'fermier'

    def afficher_stats(self):

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


NPC().afficher_stats()
