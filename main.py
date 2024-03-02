import aircraft
import events

# Creates different aircraft.
spitfire = aircraft.AircraftBlueprint(3200, 100, 1000, 3200, 100, 1000)
test = aircraft.AircraftBlueprint(10, 10, 10, 10, 10, 10)

# Var for setting the chosen aircraft. Default is test for testing purposes.
chosenCraft = test


# The frame stitching everything together.
def startSimulation():
    while True:
        events.whatToDo()


if __name__ == '__main__':
    startSimulation()
