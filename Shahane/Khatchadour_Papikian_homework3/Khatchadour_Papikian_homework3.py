import time
    
class Person:
    def __init__(self, name, last_name, age, gender, student):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            func(*args, **kwargs)
            t2 = time.time()
            print('Time: %s' % (t2-t1))
        return wrapper
    
    @decorator
    def Greeting(self, second_person):
        print('Welcome, dear %s.' % second_person.name)
        
    def Goodbye(self):
        print('Bye everyone!')
        
    def Favourite_num(self, num1):
        print('My favourite number is %s.' % num1)
        
p1 = Person('Kim', 'Kardashian', 37, 'female', False)        
p2 = Person('Vardan', 'Mamikonyan', 1630, 'male', False)
p1.Greeting(p2)
p2.Favourite_num(451)
        

        