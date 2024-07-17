class EngineBlueprint:
    def __init__(self, engineFuel, engineCondition, engineHP):
        self.engineFuel = engineFuel
        self.engineCondition = engineCondition
        self.engineHP = engineHP

    def calculateFuelBurnRate(self):
        # Assuming an arbitrary Efficiency Constant for simplification
        efficiency_constant = 10
        condition_factor = self.engineCondition / 100

        # Calculate fuel burn rate based on the simplified formula
        fuel_burn_rate = (self.engineHP * condition_factor) / efficiency_constant
        return fuel_burn_rate


class AircraftBlueprint:
    def __init__(self, name, topSpeed, leftEngineFuel, leftEngineCondition, leftEngineHP, rightEngineFuel,
                 rightEngineCondition,
                 rightEngineHP):
        self.name = name
        self.topSpeed = topSpeed
        self.leftEngine = EngineBlueprint(leftEngineFuel, leftEngineCondition, leftEngineHP)
        self.rightEngine = EngineBlueprint(rightEngineFuel, rightEngineCondition, rightEngineHP)

    # Calculates total fuel burn rate for both engines.
    def totalFuelBurnRate(self):
        # Sum fuel burn rates of both engines
        total_burn_rate = self.leftEngine.calculateFuelBurnRate() + self.rightEngine.calculateFuelBurnRate()
        return total_burn_rate

    def totalCondition(self):
        # Sum of overall condition of the aircraft
        total_condition = (self.leftEngine.engineCondition + self.rightEngine.engineCondition) / 2
        return total_condition


# Global variables for the simulation
aircraftList = [
    AircraftBlueprint('Spitfire', 3200, 100, 1000, 3200, 100, 1000, 1000),
    AircraftBlueprint('Test', 10, 10, 10, 10, 10, 10, 10),
    AircraftBlueprint('SuperConsumer', 10000, 100, 2000, 10000, 100, 2000, 2000),
    AircraftBlueprint('SuperSpeed', 3200, 100, 10000, 3200, 100, 10000, 10000)
]

# Creates different aircraft.
spitfire = AircraftBlueprint('Spitfire', 594, 3200, 100, 1000, 3200, 100, 1000)
test = AircraftBlueprint('Test', 300, 10, 10, 10, 10, 10, 10)

# This is a super consumer aircraft. It's fuel burn rate is 10 times higher than the Spitfire.
superConsumer = AircraftBlueprint('SuperConsumer', 300, 10000, 100, 2000, 10000, 100, 2000)

# SuperSpeed is a super-fast aircraft. Its HP is 10 times higher than the Spitfire.
superSpeed = AircraftBlueprint('SuperSpeed', 300, 3200, 100, 10000, 3200, 100, 10000)

# Var for setting the chosen aircraft. Default is spitfire.
chosenCraft = spitfire
