class Parent:
    def __init__(self, Father, Mother):
        self.father = Father
        self.mother = Mother

    def age_diff(self):
        return self.father - self.mother

class Child(Parent):
    def __init__(self, Father, Mother, Son):
        super().__init__(Father, Mother)
        self.son = Son
    def age_diff(self):
        father_major = self.father - self.son
        mother_major = self.mother - self.son
        if father_major > self.son:
            return father_major
        return mother_major

    
Age = Parent(50, 48)
print(Age.age_diff())
Child_age = Child(50, 48, 23)
print(Child_age.age_diff())
