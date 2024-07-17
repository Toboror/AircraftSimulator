import random
import time
import pygame

from aircraft import aircraftList, chosenCraft

# Global variables for the simulation
leftEnoughFuel = True
rightEnoughFuel = True
elapsed_time = 0
leftEngineWorks = True
rightEngineWorks = True
leftEngineOn = False
rightEngineOn = False
hasTakenOff = False
isFlying = False
atCityAAirport = True
atCityBAirport = False
reachedDestination = False
hasChosenAircraft = False
isOnSecondRound = False

cityAAirport = 'City A Airport'
cityBAirport = 'City B Airport'

# Engine fuel burn rate
leftEngineBurnRate = chosenCraft.leftEngine.calculateFuelBurnRate()
rightEngineBurnRate = chosenCraft.rightEngine.calculateFuelBurnRate()


def append_to_text_box(text_box, message):
    text_box.html_text += f'{message}<br>'
    text_box.rebuild()


def stateOfTheCraft(text_box):
    return append_to_text_box(text_box, f'The state of the aircraft is:\n'
                                        f'Left engine:\n'
                                        f'Fuel: {chosenCraft.leftEngine.engineFuel} Litres\n'
                                        f'Condition: {chosenCraft.leftEngine.engineCondition}%\n'
                                        f'Horsepower: {chosenCraft.leftEngine.engineHP}\n'
                                        f'Fuel consumption rate: {chosenCraft.leftEngine.calculateFuelBurnRate()} litres per hour\n'
                                        f'Right engine:\n'
                                        f'Fuel: {chosenCraft.rightEngine.engineFuel} Litres\n'
                                        f'Condition: {chosenCraft.rightEngine.engineCondition}%\n'
                                        f'Horsepower: {chosenCraft.rightEngine.engineHP}\n'
                                        f'Fuel consumption rate: {chosenCraft.rightEngine.calculateFuelBurnRate()} litres per hour\n'
                                        f'Total fuel amount: {chosenCraft.leftEngine.engineFuel + chosenCraft.rightEngine.engineFuel} litres\n'
                                        f'Total fuel consumption rate: {chosenCraft.totalFuelBurnRate()} litres per hour\n'
                                        f'Total engine condition: {chosenCraft.totalCondition()}%')


def takeOff(gui_elements):
    global hasTakenOff, leftEngineOn, rightEngineOn, takeOffStartTime, takeOffStep
    label, buttons, text_box = gui_elements  # Unpack correctly

    # Initialize the takeoff process if it hasn't started yet
    if not hasTakenOff:
        takeOffStartTime = pygame.time.get_ticks()  # Step 2: Record the start time
        takeOffStep = 0  # Initialize or reset the takeoff step counter
        hasTakenOff = True  # Mark the takeoff process as started

    # Calculate the elapsed time since the start of the takeoff process
    currentTime = pygame.time.get_ticks()  # Step 3: Get the current time
    elapsedTime = currentTime - takeOffStartTime  # Calculate the elapsed time

    # Step 4: Proceed through the takeoff steps based on the elapsed time
    if takeOffStep == 0 and elapsedTime >= 1000:  # After 1 second, check the left engine
        append_to_text_box(text_box, 'Checking if everything works...')
        takeOffStep += 1
        takeOffStartTime = currentTime  # Reset the start time for the next step
    if takeOffStep == 1 and elapsedTime >= 1000:  # After another second, check the right engine
        append_to_text_box(text_box, 'Left engine...')
        leftEngineOn = True
        takeOffStep += 1
        takeOffStartTime = currentTime
    if takeOffStep == 2 and elapsedTime >= 1000:  # After another second, finalize checks
        append_to_text_box(text_box, 'Right engine...')
        rightEngineOn = True
        takeOffStep += 1
        takeOffStartTime = currentTime
    if takeOffStep == 3 and elapsedTime >= 1000:  # After another second, take off
        append_to_text_box(text_box, 'Everything else...')
        takeOffStep += 1
        takeOffStartTime = currentTime
    if takeOffStep == 4 and elapsedTime >= 1000:  # Confirm takeoff
        append_to_text_box(text_box, 'Everything seems to be in order! Taking off...')
        takeOffStep += 1  # This marks the end of the takeoff process

    # Additional steps can be added here following the same pattern


def chooseAircraft(text_box):
    global hasChosenAircraft
    return append_to_text_box(text_box, 0)


def secondRound():
    return ''


def checkFuel():
    global leftEnoughFuel, rightEnoughFuel
    leftEnoughFuel = chosenCraft.leftEngine.engineFuel > chosenCraft.leftEngine.calculateFuelBurnRate()
    rightEnoughFuel = chosenCraft.rightEngine.engineFuel > chosenCraft.rightEngine.calculateFuelBurnRate()


def flying(text_box):
    global hasTakenOff, leftEnoughFuel, rightEnoughFuel, leftEngineOn, rightEngineOn, reachedDestination, elapsed_time
    start_time = time.time()
    append_to_text_box(text_box, 'You are flying through the skies.')
    encounterWeather(text_box)
    hasTakenOff = True
    while elapsed_time < 5:
        checkFuel()
        if leftEnoughFuel and rightEnoughFuel:
            if leftEngineOn:
                chosenCraft.leftEngine.engineCondition -= 2
                chosenCraft.leftEngine.engineFuel -= elapsed_time * chosenCraft.leftEngine.calculateFuelBurnRate()
            else:
                append_to_text_box(text_box, 'Your left engine is not on!')
            if rightEngineOn:
                chosenCraft.rightEngine.engineCondition -= 2
                chosenCraft.rightEngine.engineFuel -= elapsed_time * chosenCraft.rightEngine.calculateFuelBurnRate()
            else:
                append_to_text_box(text_box, 'Your right engine is not on!')
            time.sleep(2)
            end_time = time.time()
            elapsed_time = (end_time - start_time) / 2
            append_to_text_box(text_box, f'You have currently flown for {elapsed_time:.2f} hours')
        elif leftEnoughFuel and not rightEnoughFuel:
            rightEngineOn = False
            append_to_text_box(text_box, 'Your right engine has run out of fuel.')
        elif rightEnoughFuel and not leftEnoughFuel:
            leftEngineOn = False
            append_to_text_box(text_box, 'Your left engine has run out of fuel.')
        else:
            append_to_text_box(text_box, 'Both of your engines are out of fuel. You crash.')
            exit()


def encounterWeather(text_box):
    global leftEngineBurnRate, rightEngineBurnRate
    weather_conditions = ['clear', 'rainy', 'stormy', 'foggy', 'windy']
    current_weather = random.choice(weather_conditions)
    append_to_text_box(text_box, f"You are flying through {current_weather} weather.")
    if current_weather == 'clear':
        append_to_text_box(text_box, 'This has no effect on fuel consumption or engine condition.')
    elif current_weather == 'rainy':
        append_to_text_box(text_box, 'Fuel consumption +10% and engine condition reduced by -20%.')
        leftEngineBurnRate *= 1.1
        chosenCraft.leftEngine.engineCondition *= 0.8
        rightEngineBurnRate *= 1.1
        chosenCraft.rightEngine.engineCondition *= 0.8
    elif current_weather == 'stormy':
        append_to_text_box(text_box, 'Fuel consumption +30% and engine condition reduced by -50%.')
        leftEngineBurnRate *= 1.3
        chosenCraft.leftEngine.engineCondition *= 0.5
        rightEngineBurnRate *= 1.3
        chosenCraft.rightEngine.engineCondition *= 0.5
    elif current_weather == 'foggy':
        append_to_text_box(text_box, 'Fuel consumption +5% and engine condition is unaffected.')
        leftEngineBurnRate *= 1.05
        rightEngineBurnRate *= 1.05
    elif current_weather == 'windy':
        append_to_text_box(text_box, 'Fuel consumption +20% and engine condition reduced by -10%.')
        leftEngineBurnRate *= 1.2
        chosenCraft.leftEngine.engineCondition *= 0.9
        rightEngineBurnRate *= 1.2
        chosenCraft.rightEngine.engineCondition *= 0.9


def emergencySituation():
    emergencies = ['engine fire', 'system failure', 'medical emergency']
    current_emergency = random.choice(emergencies)
    print(f"Emergency: {current_emergency} has occurred.")


def fuelManagement():
    if chosenCraft.leftEngine.engineFuel < chosenCraft.leftEngine.engineFuel * 0.1 \
            and chosenCraft.rightEngine.engineFuel < chosenCraft.rightEngine.engineFuel * 0.1:
        print("Fuel is running low. Choose to divert to a closer airport or attempt to reach the planned destination.")
    userInput = input()
    if userInput == '1':
        print("The aircraft is diverting to a closer airport.")
        divertToCloserAirport()
    elif userInput == '2':
        print("The aircraft is attempting to reach the planned destination.")
    else:
        exit()


def refuelAtCityAirport():
    global atCityAAirport, atCityBAirport
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
            cityAFuelCosts()
        elif atCityBAirport:
            cityBFuelCosts()
    elif userInput == '2':
        if atCityAAirport:
            print("The aircraft is not refueling at city A airport.")
        elif atCityBAirport:
            print("The aircraft is not refueling at city B airport.")
    takeOff()


def cityAFuelCosts():
    print("The fuel costs at city A airport are 1.50€ per litre.")
    userInput = input()
    if userInput == '1':
        print("The aircraft is refueling at city A airport.")
    elif userInput == '2':
        print("The aircraft is not refueling at city A airport.")


def cityBFuelCosts():
    print("The fuel costs at city B airport are 1.60€ per litre.")
    userInput = input()
    if userInput == '1':
        print("The aircraft is refueling at city B airport.")
    elif userInput == '2':
        print("The aircraft is not refueling at city B airport.")


def chooseDestination():
    global atCityAAirport, atCityBAirport
    if atCityAAirport:
        print('Choose destination:\n1. City B')
    elif atCityBAirport:
        print('Choose destination:\n1. City A')
    userInput = input()
    if atCityAAirport:
        if userInput == '1':
            print("The aircraft is flying to city B.")
            atCityBAirport = True
        else:
            print("The aircraft is staying at city A.")
            chooseDestination()
    elif atCityBAirport:
        if userInput == '1':
            print("The aircraft is flying to city A.")
            atCityAAirport = True
        else:
            print("The aircraft is staying at city B.")
            chooseDestination()


def divertToCloserAirport():
    print("The aircraft has diverted to a closer airport.")


def technicalIssue():
    issues = ['landing gear malfunction', 'electrical system failure', 'navigation equipment issue']
    if chosenCraft.leftEngine.engineCondition < 50:
        current_issue = random.choice(issues)
        print(f"Left engine has a technical Issue: {current_issue}.")
    if chosenCraft.rightEngine.engineCondition < 50:
        current_issue = random.choice(issues)
        print(f"Right engine has a technical Issue: {current_issue}.")


def whatToDo(gui_elements):
    label, buttons, text_box = gui_elements  # Unpack correctly

    global isOnSecondRound, isFlying, reachedDestination, atCityAAirport, atCityBAirport, elapsed_time, hasTakenOff

    try:
        if hasTakenOff:
            if isOnSecondRound:
                label.set_text(secondRound())
                technicalIssue()
            else:
                flying(text_box)
                technicalIssue()
                isOnSecondRound = True
        elif not hasTakenOff:
            buttons['takeOff'].set_text('Take off')
            buttons['chooseAircraft'].set_text('Choose aircraft')
            buttons['StateOfTheAircraft'].set_text('Check aircraft')
            buttons['takeOff'].show()
            buttons['chooseAircraft'].show()
            buttons['StateOfTheAircraft'].show()
        elif isFlying:
            if elapsed_time >= 10:
                label.set_text('You have reached your destination.')
                reachedDestination = True
            elif not elapsed_time >= 10:
                buttons['option1'].set_text('Continue flying')
                buttons['option2'].set_text('Check aircraft')
                buttons['option3'].set_text('Exit')
                buttons['option1'].show()
                buttons['option2'].show()
                buttons['option3'].show()

        if reachedDestination:
            if atCityAAirport:
                label.set_text(f'You have reached {cityBAirport} airport.')
                atCityBAirport = True
                atCityAAirport = False
            elif atCityBAirport:
                label.set_text(f'You have reached {cityAAirport} airport.')
                atCityAAirport = True
                atCityBAirport = False
    except KeyboardInterrupt:
        print('Program stopped by user.')
        exit()
