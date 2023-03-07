class Team:
    def __init__(*members):
       self.members = members
       self.index = None

    def __iter__(self):
        return self,

    def __next__(self):
        return datetime.now().year - age
    
    def show_best(self):
        print(self.marks.sorted(key=lambda x:x))