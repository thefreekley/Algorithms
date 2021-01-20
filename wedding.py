class Wedding:
    def __init__(self,couple,count):
        self.couple = couple
        self.count = count
        self.tribes = self.group_by_tribes()
        self.number_of_combinations_pairs = self.count_combinations_pairs()

    class Tribe:
        def __init__(self,*persons):
            self.people = set()
            self.females_in_tribe = set()
            self.males_in_tribe = set()

            for person in persons:
                self.add(person)

        def add(self,*persons):
            for person in persons:
                self.people.add(person)
                self.sort_genders(person)

        def sort_genders(self,person):
            if person % 2 == 0 :
                self.females_in_tribe.add(person)
            else: self.males_in_tribe.add(person)


    def group_by_tribes(self):
        tribes = []
        for person in self.couple:
            for tribe in tribes:
                if person[1] in tribe.people:
                    tribe.add(person[0])
                    break
                if person[0] in tribe.people:
                    tribe.add(person[1])
                    break
            else:
                tribes.append(self.Tribe(person[0], person[1]))

        return tribes


    def count_combinations_pairs(self):

        combinations = 0

        for check_male in self.tribes:
            for check_female in self.tribes:
                if check_male == check_female: continue
                combinations += len(check_male.males_in_tribe) * len(check_female.females_in_tribe)

        return combinations



    def cross_connection(self, list_1,list_2):
        string = ""
        for i in list_1:
            for j in list_2:
                string += f'{i}/{j}, '

        return  string


    def __str__(self):
        string = str(self.number_of_combinations_pairs) + " (Possible couples: "
        for males in self.tribes:
            for females in self.tribes:
                if males == females or len(males.males_in_tribe) ==0 or len(females.females_in_tribe) ==0: continue
                string += self.cross_connection(females.females_in_tribe,males.males_in_tribe)

        string = string[:-2] + ")"
        return string




