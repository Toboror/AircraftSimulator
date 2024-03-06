import random
import main
import time
from main import aircraftList

chosenCraft = main.chosenCraft

# Var for checking if the engines work
leftEngineWorks = True
rightEngineWorks = True

leftEngineOn = False
rightEngineOn = False

# Var for checking if the aircraft has taken off and is/is not flying.
hasTakenOff = False
isFlying = False

# Engine fuel burn rate
leftEngineBurnRate = chosenCraft.leftEngine.calculateFuelBurnRate()
rightEngineBurnRate = chosenCraft.rightEngine.calculateFuelBurnRate()

# Variables for if the aircraft is at city A or city B airport.
atCityAAirport = False
atCityBAirport = False

# Variables for airport names.
cityAAirport = 'City A Airport'
cityBAirport = 'City B Airport'


# Function for showing the state the aircraft is currently in. Engine fuel, condition, HP etc.
def stateOfTheCraft():
    print('The state of the craft is:\n '
          '\nLeft engine: '
          '\nFuel: ' + str(chosenCraft.leftEngine.engineFuel) + ' Litres',
          '\nCondition: ' + str(chosenCraft.leftEngine.engineCondition) + '%',
          '\nHorsepower: ' + str(chosenCraft.leftEngine.engineHP),
          '\nFuel consumption rate: ' + str(chosenCraft.leftEngine.calculateFuelBurnRate()) + ' litres per hour',
          '\n'
          '\nRight engine: '
          '\nFuel: ' + str(chosenCraft.rightEngine.engineFuel) + ' Litres',
          '\nCondition: ' + str(chosenCraft.rightEngine.engineCondition) + '%',
          '\nHorsepower: ' + str(chosenCraft.rightEngine.engineHP),
          '\nFuel consumption rate: ' + str(chosenCraft.rightEngine.calculateFuelBurnRate()) + ' litres per hour'
          '\n'
          '\nTotal fuel amount: ' + str(chosenCraft.leftEngine.engineFuel + chosenCraft.rightEngine.engineFuel) +
          ' litres',
          '\nTotal fuel consumption rate: ' + str(chosenCraft.totalFuelBurnRate()) + ' litres per hour',
          '\nTotal engine condition: ' + str(chosenCraft.totalCondition()) + '%')


# Function for when the aircraft is taking off. Also chooses where to fly. Default start airport is city A. Also runs
# check on the engines to see if they work.
def takeOff():
    global hasTakenOff
    global leftEngineOn
    global rightEngineOn
    # Choose destination.
    chooseDestination()

    # Check if the engines work.
    print('Checking if everything works...')
    time.sleep(1)
    print('Left engine...')
    time.sleep(1)
    print('Right engine...')
    time.sleep(1)
    print('Everything else...')
    time.sleep(1)
    print('Everything seems to be in order! Taking off...')

    time.sleep(1)
    print('-')
    time.sleep(1)
    print('--')
    time.sleep(1)
    print('---')
    time.sleep(1)
    chosenCraft.leftEngine.engineFuel -= chosenCraft.leftEngine.calculateFuelBurnRate()
    chosenCraft.rightEngine.engineFuel -= chosenCraft.leftEngine.calculateFuelBurnRate()
    chosenCraft.leftEngine.engineCondition -= 5
    chosenCraft.rightEngine.engineCondition -= 5


def chooseAircraft():
    global chosenCraft
    print('Which aircraft would you like?'
          '\n1. ' + str(aircraftList[0].name),
          '\n2. ' + str(aircraftList[1].name),
          '\n3. ' + str(aircraftList[2].name),
          '\n4. Exit')
    userInput = input()
    if userInput == '1':
        chosenCraft = aircraftList[0]
        print('Your chosen aircraft is ' + str(aircraftList[0].name))
    elif userInput == '2':
        chosenCraft = aircraftList[1]
        print('Your chosen aircraft is ' + str(aircraftList[1].name))
    elif userInput == '3':
        chosenCraft = aircraftList[2]
        print('Your chosen aircraft is ' + str(aircraftList[2].name))
    else:
        exit()


isOnSecondRound = False


def secondRound():
        print('\nWhat do you want to do?'
              '\n1. Continue flying'
              '\n2. Check aircraft'
              '\n3. Exit')
        userInput = input()
        if userInput == '1':
            flying()
        elif userInput == '2':
            stateOfTheCraft()
        elif userInput == '3':
            exit()


# Function asking the user what to do next.
def whatToDo():
    global isOnSecondRound
    if hasTakenOff:
        if isOnSecondRound:
            secondRound()
            technicalIssue()
        else:
            flying()
            technicalIssue()
            isOnSecondRound = True
    elif not hasTakenOff:
        print('\nWhat do you want to do?'
              '\n1. Take off'
              '\n2. Choose aircraft'
              '\n3. Check aircraft'
              '\n4. Exit')
        userInput = input()
        if userInput == '1':
            takeOff()
        elif userInput == '2':
            chooseAircraft()
        elif userInput == '3':
            stateOfTheCraft()
        else:
            exit()


leftEnoughFuel = True
rightEnoughFuel = True


def checkFuel():
    global leftEnoughFuel
    global rightEnoughFuel
    if chosenCraft.leftEngine.engineFuel > chosenCraft.leftEngine.calculateFuelBurnRate():
        leftEnoughFuel = True
    else:
        leftEnoughFuel = False

    if chosenCraft.rightEngine.engineFuel > chosenCraft.rightEngine.calculateFuelBurnRate():
        rightEnoughFuel = True
    else:
        rightEnoughFuel = False


# Function for aircraft traveling. Changes based on the aircraft's condition, fuel, and weather. The function is modular
# so that it may easily be expanded upon later when more events and aircraft are added. In addition to number changes.
def flying():
    global hasTakenOff
    global leftEnoughFuel
    global rightEnoughFuel
    global leftEngineOn
    global rightEngineOn
    # Record the start time
    start_time = time.time()
    print('You are flying through the skies.')
    encounterWeather()
    elapsed_time = 0
    while elapsed_time < 5:
        checkFuel()
        if leftEnoughFuel and rightEnoughFuel:
            # Reduces fuel + condition for every loop.
            if leftEngineOn:
                chosenCraft.leftEngine.engineCondition -= 2
                chosenCraft.leftEngine.engineFuel -= elapsed_time * chosenCraft.leftEngine.calculateFuelBurnRate()
            else:
                print('Your left engine is not on!')
            if rightEngineOn:
                chosenCraft.rightEngine.engineCondition -= 2
                chosenCraft.rightEngine.engineFuel -= elapsed_time * chosenCraft.rightEngine.calculateFuelBurnRate()
            else:
                print('Your right engine is not on!')
            time.sleep(2)
            end_time = time.time()
            elapsed_time = (end_time - start_time) / 2
            print(f'You have currently flown for {elapsed_time:.2f} hours')
        elif leftEnoughFuel and not rightEnoughFuel:
            rightEngineOn = False
            print('Your right engine has run out of fuel.')
        elif rightEnoughFuel and not leftEnoughFuel:
            leftEngineOn = False
            print('Your left engine has run out of fuel.')
        else:
            print('Both of your engines are out of fuel. You crash.')
            exit()


def encounterWeather():
    global leftEngineBurnRate
    global rightEngineBurnRate
    weather_conditions = ['clear', 'rainy', 'stormy', 'foggy', 'windy']
    current_weather = random.choice(weather_conditions)
    print(f"You are flying through {current_weather} weather.")
    # Adjust fuel consumption and engine condition based on weather
    if current_weather == 'clear':
        print('This has no effect on fuel consumption or engine condition.')
    elif current_weather == 'rainy':
        print('Fuel consumption +10% and engine condition reduced by -20%.')
        leftEngineBurnRate *= 1.1
        chosenCraft.leftEngine.engineCondition *= 0.8
        rightEngineBurnRate *= 1.1
        chosenCraft.rightEngine.engineCondition *= 0.8
    elif current_weather == 'stormy':
        print('Fuel consumption +30% and engine condition reduced by -50%.')
        leftEngineBurnRate *= 1.3
        chosenCraft.leftEngine.engineCondition *= 0.5
        rightEngineBurnRate *= 1.3
        chosenCraft.rightEngine.engineCondition *= 0.5
    elif current_weather == 'foggy':
        print('Fuel consumption +5% and engine condition is unaffected.')
        leftEngineBurnRate *= 1.05
        rightEngineBurnRate *= 1.05
    elif current_weather == 'windy':
        print('Fuel consumption +20% and engine condition reduced by -10%.')
        leftEngineBurnRate *= 1.2
        chosenCraft.leftEngine.engineCondition *= 0.9
        rightEngineBurnRate *= 1.2
        chosenCraft.rightEngine.engineCondition *= 0.9


def emergencySituation():
    emergencies = ['engine fire', 'system failure', 'medical emergency']
    current_emergency = random.choice(emergencies)
    print(f"Emergency: {current_emergency} has occurred.")
    # Require user input to address the emergency


# Function for when the aircraft is running low on fuel and if there are other problems related to fuel. Only called
# when fuel less than 10%.
def fuelManagement():
    if chosenCraft.leftEngine.engineFuel < chosenCraft.leftEngine.engineFuel * 0.1 \
            and chosenCraft.rightEngine.engineFuel < chosenCraft.rightEngine.engineFuel * 0.1:
        print("Fuel is running low. Choose to divert to a closer airport or attempt to reach the planned destination.")
    # Require user input to address the fuel issue with different options.
    userInput = input()
    if userInput == '1':
        print("The aircraft is diverting to a closer airport.")
        # Will call a function for the event for diverting to a closer airport.
        divertToCloserAirport()
    elif userInput == '2':
        print("The aircraft is attempting to reach the planned destination.")
    else:
        exit()


# Function for refueling at a city airport. Will be expanded upon later.
def refuelAtCityAirport():
    global atCityAAirport
    global atCityBAirport
    if atCityAAirport:
        print('Refuel at ' + cityAAirport + 'airport?"'
          "\n1. Yes"
          "\n2. No")
    elif atCityBAirport:
        print('Refuel at ' + cityBAirport + 'airport?"'
          "\n1. Yes"
          "\n2. No")
    userInput = input()
    if userInput == '1':
        if atCityAAirport:
            cityAFuelCosts()    # Will call the function for city A airport fuel costs.
        elif atCityBAirport:
            cityBFuelCosts()    # Will call the function for city B airport fuel costs.
    elif userInput == '2':
        if atCityAAirport:
            print("The aircraft is not refueling at city A airport.")
        elif atCityBAirport:
            print("The aircraft is not refueling at city B airport.")
    # Calls function for taking off again.
    takeOff()

# Function for city A airport fuel costs.
def cityAFuelCosts():
    print("The fuel costs at city A airport are 1.50€ per litre.")
    # Require user input to choose to refuel or not.
    userInput = input()
    if userInput == '1':
        print("The aircraft is refueling at city A airport.")
        # Will call the function for refueling.
    elif userInput == '2':
        print("The aircraft is not refueling at city A airport.")
        # Will call the function for not refueling.


# Function for city B airport fuel costs.
def cityBFuelCosts():
    print("The fuel costs at city B airport are 1.60€ per litre.")
    # Require user input to choose to refuel or not.
    userInput = input()
    if userInput == '1':
        print("The aircraft is refueling at city B airport.")
        # Will call the function for refueling.
    elif userInput == '2':
        print("The aircraft is not refueling at city B airport.")
        # Will call the function for not refueling.

# Function for choosing flight destination. Will be expanded upon later.
def chooseDestination():
    global atCityAAirport
    global atCityBAirport
    print("Choose a destination.")
    # Require user input to choose a destination. Currently only able to travel to one destination. Checks where the
    #  aircraft is currently located by using the variables for where it were last. Modular for future expansion.
    userInput = input()
    if atCityAAirport:
        if userInput == '1':
            print("The aircraft is flying to city B.")
            # Will call the function for flying to city B.
            atCityBAirport = True
        else:
            print("The aircraft is staying at city A.")
            # Will call the function for flying to city A.
            chooseDestination()
    elif atCityBAirport:
        if userInput == '1':
            print("The aircraft is flying to city A.")
            # Will call the function for flying to city A.
            atCityAAirport = True
        else:
            print("The aircraft is staying at city B.")
            chooseDestination()



# Function for when the aircraft diverts to a closer airport.
def divertToCloserAirport():
    print("The aircraft has diverted to a closer airport.")
    # Adjust the simulation based on the decision.


# Function for when the aircraft encounters a technical issue.
def technicalIssue():
    issues = ['landing gear malfunction', 'electrical system failure', 'navigation equipment issue']
    if chosenCraft.leftEngine.engineCondition < 50:
        current_issue = random.choice(issues)
        print(f"Left engine has a technical Issue: {current_issue}.")
    if chosenCraft.rightEngine.engineCondition < 50:
        current_issue = random.choice(issues)
        print(f"Right engine has a technical Issue: {current_issue}.")
    # Adjust the simulation based on the issue
