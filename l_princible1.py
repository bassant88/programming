class Bird:
    def fly(self):
        return "I can fly"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly")

def make_bird_fly(bird: Bird):
    print(bird.fly())

bird = Bird()
penguin = Penguin()

make_bird_fly(bird)    
make_bird_fly(penguin)  
