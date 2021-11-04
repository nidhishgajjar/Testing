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
        return self.father - self.son
    
Age = Parent(50, 48)
print(Age.age_diff())
Child_age = Child(50, 48, 23)
print(Child_age.age_diff())
