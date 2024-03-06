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
    def __init__(self, name, leftEngineFuel, leftEngineCondition, leftEngineHP, rightEngineFuel, rightEngineCondition,
                 rightEngineHP):
        self.name = name
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
