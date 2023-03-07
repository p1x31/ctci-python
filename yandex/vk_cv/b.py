#https://contest.yandex.ru/contest/27665/problems/B/

from datetime import datetime

class Student:
    def __init__(self, name, age, marks):
       self.name = name
       self.age = age
       marks = self.marks

    def say_hello(self):
        print("Hello, my name is ".format(self.name))

    @staticmethod
    def year(self):
        return datetime.now().year - age
    
    def show_best(self):
        print(self.marks.sorted(key=lambda x:x))