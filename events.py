import random
import main
import time
import aircraft

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
                                                                                               '\nTotal fuel consumption rate: ' + str(
              chosenCraft.totalFuelBurnRate()) + ' litres per hour',
          '\nTotal engine condition: ' + str(chosenCraft.totalCondition()) + '%')


# Function for when the aircraft is taking off.
def takeOff():
    global hasTakenOff
    global leftEngineOn
    global rightEngineOn
    print('Checking if everything works...')
    time.sleep(1)
    checkEngine()
    if leftEngineWorks and rightEngineWorks:
        print('Alright, taking off!')
        hasTakenOff = True
        leftEngineOn = True
        rightEngineOn = True
    elif not leftEngineWorks or not rightEngineWorks:
        print('There seems to be a problem with one of the engines. We are not able to take off!')
        exit()

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
          '\n1. Spitfire'
          '\n2. Exit')
    userInput = input()
    if userInput == '1':
        chosenCraft = main.spitfire
    else:
        exit()


secondRound = False


# Function asking the user what to do next.
def whatToDo():
    global secondRound
    if hasTakenOff:
        if secondRound and checkEngine():
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
        else:
            checkEngine()
            flying()
            secondRound = True
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


def checkEngine():
    global leftEngineWorks
    global rightEngineWorks
    if chosenCraft.leftEngine.engineCondition <= 91:
        print('Your left engine has encountered a critical failure and is no longer working.')
        leftEngineWorks = False
    elif chosenCraft.rightEngine.engineCondition <= 86:
        print('Your right engine has encountered a critical failure and is no longer working.')
        rightEngineWorks = False

    if not leftEngineWorks and not rightEngineWorks:
        print('Both your engines are out. You are going down.')
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


def flying():
    global hasTakenOff
    global leftEnoughFuel
    global rightEnoughFuel
    global leftEngineOn
    global rightEngineOn
    checkedEngine = False
    # Record the start time
    start_time = time.time()
    print('You are flying through the skies.')
    encounterWeather()
    elapsed_time = 0
    while elapsed_time < 5:
        secondRound
        checkFuel()
        if leftEnoughFuel and rightEnoughFuel:
            # Reduces fuel + condition for every loop.
            if checkedEngine:
                checkEngine()
                checkedEngine = True
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


def fuelManagement():
    print("Fuel is running low. Choose to divert to a closer airport or attempt to reach the planned destination.")
    # User makes a choice affecting the outcome


def technicalIssue():
    issues = ['landing gear malfunction', 'electrical system failure', 'navigation equipment issue']
    current_issue = random.choice(issues)
    print(f"Technical Issue: {current_issue}.")
    # Adjust the simulation based on the issue
