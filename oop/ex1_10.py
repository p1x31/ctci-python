class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
print(hasattr(p1, "job"))
print(hasattr(p1.__dict__, "job"))