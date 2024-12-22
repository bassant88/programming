class Bird:
    def move(self):
        return "I can move"

class FlyingBird(Bird):
    def fly(self):
        return "I can fly"

class Penguin(Bird):
    def swim(self):
        return "I can swim"

def describe_bird(bird: Bird):
    print(bird.move())

bird = Bird()
flying_bird = FlyingBird()
penguin = Penguin()

describe_bird(bird)         
describe_bird(flying_bird)  
describe_bird(penguin)      



