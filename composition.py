class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "%s has reached %s" % (self.name, self.distance)
class MarsRover:
    def __init__(self, name, distance, maker):
        self.rocket = Rocket(name, distance) # instantiating the base

        self.maker = maker

    def get_maker(self):
        return "%s Launched by %s" % (self.rocket.name, self.maker)

if __name__ == "__main__":
    z = MarsRover("mars_rover2", "till Mars", "ISRO")
    print(z.rocket.launch())
    print(z.get_maker())