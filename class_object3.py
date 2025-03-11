class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno

    def student(self):
        print(f'Name:{self.name}')
        print(f'Regno:{self.regno}')
st1=teacher('python',1990)
st1.student()