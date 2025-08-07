class Bird:
    def sound(self):
        print("Bird chirps")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow sings")

def make_sound(bird):
    bird.sound()

b = Sparrow()
make_sound(b)
