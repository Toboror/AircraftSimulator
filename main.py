import aircraft
import events

# Creates different aircraft.
spitfire = aircraft.AircraftBlueprint('Spitfire', 3200, 100, 1000, 3200, 100, 1000)
test = aircraft.AircraftBlueprint('Test', 10, 10, 10, 10, 10, 10)
superConsumer = aircraft.AircraftBlueprint('SuperConsumer', 10000, 100, 2000, 10000, 100, 2000)

aircraftList = [spitfire, test, superConsumer]

# Var for setting the chosen aircraft. Default is spitfire.
chosenCraft = spitfire


# The frame stitching everything together.
def startSimulation():
    while True:
        events.whatToDo()


if __name__ == '__main__':
    startSimulation()
