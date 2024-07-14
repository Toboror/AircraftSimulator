import aircraft
import events
import pygame
import pygame_gui

# Constants for configuration
WINDOW_SIZE = (800, 600)
BACKGROUND_COLOR = 'black'
FPS = 60

# Global variables for the simulation
chosenCraft = aircraft.AircraftBlueprint('Spitfire', 3200, 100, 1000, 3200, 100, 1000)
aircraftList = [
    chosenCraft,
    aircraft.AircraftBlueprint('Test', 10, 10, 10, 10, 10, 10),
    aircraft.AircraftBlueprint('SuperConsumer', 10000, 100, 2000, 10000, 100, 2000),
    aircraft.AircraftBlueprint('SuperSpeed', 3200, 100, 10000, 3200, 100, 10000)
]


def initialize_pygame():
    pygame.init()
    pygame.display.set_caption('Aircraft Simulation')
    window_surface = pygame.display.set_mode(WINDOW_SIZE)
    return window_surface


def create_background():
    background = pygame.Surface(WINDOW_SIZE)
    background.fill(pygame.Color(BACKGROUND_COLOR))
    return background


def create_ui_manager():
    return pygame_gui.UIManager(WINDOW_SIZE)


def create_buttons(manager):
    buttons = {
        'start': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (125, 50)),
                                              text='Start Simulation',
                                              manager=manager),
        'exit': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 425), (125, 50)),
                                             text='Exit',
                                             manager=manager),
        'settings_confirm': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (125, 50)),
                                                         text='Done',
                                                         manager=manager,
                                                         visible=False),
        'settings': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 350), (125, 50)),
                                                 text='Settings',
                                                 manager=manager),
        'takeOff': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 500), (150, 50)),
                                                text='Option 1',
                                                manager=manager,
                                                visible=False),
        'chooseAircraft': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 500), (150, 50)),
                                                       text='Option 2',
                                                       manager=manager,
                                                       visible=False),
        'StateOfTheAircraft': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 500), (150, 50)),
                                                           text='Option 3',
                                                           manager=manager,
                                                           visible=False),
        'Spitfire': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 500), (150, 50)),
                                                 text='Spitfire',
                                                 manager=manager,
                                                 visible=False),
        'SuperConsumer': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 500), (150, 50)),
                                                      text='SuperConsumer',
                                                      manager=manager,
                                                      visible=False),
        'SuperSpeed': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 500), (150, 50)),
                                                   text='SuperSpeed',
                                                   manager=manager,
                                                   visible=False)
    }
    return buttons


def create_dropdown(manager):
    dropdown = pygame_gui.elements.UIDropDownMenu(options_list=['800x600', '1024x768', '1280x720'],
                                                  starting_option='800x600',
                                                  relative_rect=pygame.Rect((350, 200), (100, 30)),
                                                  manager=manager,
                                                  visible=False)
    return dropdown


def handle_events(event, buttons, dropdown, manager, label, text_box):
    global chosenCraft

    if event.type == pygame.QUIT:
        return False

    if event.type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == buttons['start']:
            print('Start Simulation button pressed')
            buttons['start'].hide()
            buttons['exit'].relative_rect = pygame.Rect((550, 500), (125, 50))
            buttons['exit'].rebuild()
            buttons['settings'].hide()
            label.show()
            text_box.show()
            # Start simulation logic here
            # If an aircraft has not been chosen, the 'take off' button is disabled.
            if not events.hasChosenAircraft:
                buttons['takeOff'].disable()
                buttons['StateOfTheAircraft'].disable()

            events.whatToDo((label, buttons, text_box))

        elif event.ui_element == buttons['exit']:
            print('Exit button pressed')
            return False

        elif event.ui_element == buttons['settings']:
            print('Settings button pressed')
            buttons['start'].hide()
            dropdown.show()
            buttons['settings_confirm'].show()

        elif event.ui_element == buttons['settings_confirm']:
            print('Settings Confirm button pressed')
            buttons['start'].show()
            dropdown.hide()
            buttons['settings_confirm'].hide()

        elif event.ui_element == buttons['takeOff']:
            events.takeOff((label, buttons, text_box))

        elif event.ui_element == buttons['chooseAircraft']:
            events.chooseAircraft(text_box)
            buttons['takeOff'].hide()
            buttons['chooseAircraft'].hide()
            buttons['StateOfTheAircraft'].hide()
            buttons['Spitfire'].show()
            buttons['SuperConsumer'].show()
            buttons['SuperSpeed'].show()

        elif event.ui_element == buttons['Spitfire']:
            chosenCraft = aircraftList[0]
            events.hasChosenAircraft = True
            buttons['takeOff'].enable()
            buttons['takeOff'].show()
            buttons['StateOfTheAircraft'].enable()
            buttons['StateOfTheAircraft'].show()
            buttons['chooseAircraft'].show()
            buttons['Spitfire'].hide()
            buttons['SuperConsumer'].hide()
            buttons['SuperSpeed'].hide()
        elif event.ui_element == buttons['SuperConsumer']:
            chosenCraft = aircraftList[2]
            events.hasChosenAircraft = True
            buttons['takeOff'].enable()
            buttons['StateOfTheAircraft'].enable()
            buttons['Spitfire'].hide()
            buttons['SuperConsumer'].hide()
            buttons['SuperSpeed'].hide()
        elif event.ui_element == buttons['SuperSpeed']:
            chosenCraft = aircraftList[3]
            events.hasChosenAircraft = True
            buttons['takeOff'].enable()
            buttons['StateOfTheAircraft'].enable()
            buttons['Spitfire'].hide()
            buttons['SuperConsumer'].hide()
            buttons['SuperSpeed'].hide()

        elif event.ui_element == buttons['StateOfTheAircraft']:
            events.stateOfTheCraft(text_box)

    if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
        if event.ui_element == dropdown:
            resolution = tuple(map(int, event.text.split('x')))
            pygame.display.set_mode(resolution)
            print('Resolution changed to:', event.text)

    manager.process_events(event)
    return True


def main():
    window_surface = initialize_pygame()
    background = create_background()
    manager = create_ui_manager()
    buttons = create_buttons(manager)
    dropdown = create_dropdown(manager)
    label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 500), (700, 50)),
                                        text='',
                                        manager=manager,
                                        visible=False)
    text_box = pygame_gui.elements.UITextBox(html_text='',
                                             relative_rect=pygame.Rect((50, 50), (700, 400)),
                                             manager=manager,
                                             visible=False)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            is_running = handle_events(event, buttons, dropdown, manager, label, text_box)
            if not is_running:
                break

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

# Creates different aircraft.
spitfire = aircraft.AircraftBlueprint('Spitfire', 3200, 100, 1000, 3200, 100, 1000)
test = aircraft.AircraftBlueprint('Test', 10, 10, 10, 10, 10, 10)

# This is a super consumer aircraft. It's fuel burn rate is 10 times higher than the Spitfire.
superConsumer = aircraft.AircraftBlueprint('SuperConsumer', 10000, 100, 2000, 10000, 100, 2000)

# SuperSpeed is a super-fast aircraft. Its HP is 10 times higher than the Spitfire.
superSpeed = aircraft.AircraftBlueprint('SuperSpeed', 3200, 100, 10000, 3200, 100, 10000)

aircraftList = [spitfire, test, superConsumer, superSpeed]

# Var for setting the chosen aircraft. Default is spitfire.
chosenCraft = spitfire
