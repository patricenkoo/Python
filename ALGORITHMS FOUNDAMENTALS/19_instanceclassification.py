
class person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

firstInstance = person("Mr Burdell", 56)
secondInstance = person("Mrs Burdell", 57)
george_p = person("George P. Burdell", 25, firstInstance, secondInstance)

print(george_p.name)
print(george_p.mother.name)
print(george_p.father.name)