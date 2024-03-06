import aircraft
import events

# Creates different aircraft.
spitfire = aircraft.AircraftBlueprint('Spitfire', 594, 3200, 100, 1000, 3200, 100, 1000)
test = aircraft.AircraftBlueprint('Test', 300, 10, 10, 10, 10, 10, 10)

# This is a super consumer aircraft. It's fuel burn rate is 10 times higher than the Spitfire.
superConsumer = aircraft.AircraftBlueprint('SuperConsumer', 300, 10000, 100, 2000, 10000, 100, 2000)

# SuperSpeed is a super-fast aircraft. Its HP is 10 times higher than the Spitfire.
superSpeed = aircraft.AircraftBlueprint('SuperSpeed', 300, 3200, 100, 10000, 3200, 100, 10000)

aircraftList = [spitfire, test, superConsumer, superSpeed]

# Var for setting the chosen aircraft. Default is spitfire.
chosenCraft = spitfire


# The frame stitching everything together.
def startSimulation():
    while True:
        events.whatToDo()


if __name__ == '__main__':
    startSimulation()
