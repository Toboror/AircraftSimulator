import pygame
import pygame_gui

import events
import aircraft
import main

# Constants for configuration
window_height = 600
window_width = 800
window_size = (window_width, window_height)  # Defines the size of the window as a tuple (width, height)
FPS = 60  # Defines the frames per second (FPS) for the game loop


def initialize_pygame():
    """
    Initializes the Pygame library, sets the window caption, and creates the window surface.

    Returns:
        pygame.Surface: The main window surface where all elements will be drawn.
    """
    pygame.init()
    pygame.display.set_caption('Aircraft Simulation')
    window_surface = pygame.display.set_mode(window_size)
    return window_surface


def create_background():
    """
    Creates a background surface with the specified window_size and fills it with the BACKGROUND_COLOR.

    Returns:
        pygame.Surface: The background surface.
    """
    background = pygame.Surface(window_size)
    return background


def create_ui_manager():
    """
    Creates and returns a UIManager object which is responsible for managing UI elements in the window.

    Returns:
        pygame_gui.UIManager: The UI manager for the window.
    """
    return pygame_gui.UIManager(window_size)


def create_buttons(manager):
    """
    Creates a dictionary of buttons for the simulation using the provided UI manager.

    Args:
        manager (pygame_gui.UIManager): The UI manager to which the buttons will be added.

    Returns:
        dict: A dictionary containing the created buttons, keyed by their intended functionality.
    """
    buttons = {
        'start': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (125, 50)),
                                              text='Start Simulation',
                                              manager=manager),
        'exit': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 425), (125, 50)),
                                             text='Exit',
                                             manager=manager),
        'back_button': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 425), (125, 50)),
                                                    text='Back',
                                                    manager=manager,
                                                    visible=False),
        'settings_confirm': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (125, 50)),
                                                         text='Done',
                                                         manager=manager,
                                                         visible=False),
        'toggle_fullscreen': pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 325), (125, 50)),
                                                          text='Toggle fullscreen',
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

# Checks if the "start sim" button has been pressed. If it has, the player char will be created.
game_started = False

def handle_events(event, buttons, dropdown, manager, label, text_box):
    global chosenCraft
    global game_started

    if event.type == pygame.QUIT:
        return False

    if event.type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == buttons['start']:
            print('Start Simulation button pressed')
            buttons['start'].hide()
            buttons['exit'].hide()
            buttons['back_button'].show()


            game_started = True

            # Assuming `set_relative_position()` is available and preferred
            buttons['back_button'].set_relative_position((650, 500))
            buttons['back_button'].rebuild()

            buttons['settings'].hide()
            label.show()
            # Show the text box. Currently, it is hidden because it will be replaced by a tileset.
            text_box.hide()
            # Start simulation logic here,
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
            buttons['exit'].hide()
            dropdown.show()
            buttons['toggle_fullscreen'].show()
            buttons['back_button'].show()
            buttons['settings_confirm'].show()

        elif event.ui_element == buttons['back_button']:
            print('back button pressed')
            start_screen(buttons, dropdown, text_box)

            game_started = False

        elif event.ui_element == buttons['settings_confirm']:
            print('Settings Confirm button pressed')
            start_screen(buttons, dropdown, text_box)

        elif event.ui_element == buttons['toggle_fullscreen']:
            print('toggle_fullscreen button pressed')
            pygame.display.toggle_fullscreen()

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
            chosenCraft = aircraft.aircraftList[0]
            events.hasChosenAircraft = True
            buttons['takeOff'].enable()
            buttons['takeOff'].show()
            buttons['StateOfTheAircraft'].enable()
            buttons['StateOfTheAircraft'].show()
            buttons['chooseAircraft'].show()
            buttons['Spitfire'].hide()
            buttons['SuperConsumer'].hide()
            buttons['SuperSpeed'].hide()
            events.append_to_text_box(text_box, 'You have chosen the Spitfire.\n')
        elif event.ui_element == buttons['SuperConsumer']:
            chosenCraft = aircraft.aircraftList[2]
            events.hasChosenAircraft = True
            buttons['takeOff'].enable()
            buttons['takeOff'].show()
            buttons['StateOfTheAircraft'].enable()
            buttons['StateOfTheAircraft'].show()
            buttons['chooseAircraft'].show()
            buttons['Spitfire'].hide()
            buttons['SuperConsumer'].hide()
            buttons['SuperSpeed'].hide()
            events.append_to_text_box(text_box, 'You have chosen the SuperConsumer.\n')
        elif event.ui_element == buttons['SuperSpeed']:
            chosenCraft = aircraft.aircraftList[3]
            events.hasChosenAircraft = True
            buttons['takeOff'].enable()
            buttons['takeOff'].show()
            buttons['StateOfTheAircraft'].enable()
            buttons['StateOfTheAircraft'].show()
            buttons['chooseAircraft'].show()
            buttons['Spitfire'].hide()
            buttons['SuperConsumer'].hide()
            buttons['SuperSpeed'].hide()
            events.append_to_text_box(text_box, 'You have chosen the SuperSpeed.\n')

        elif event.ui_element == buttons['StateOfTheAircraft']:
            events.stateOfTheCraft(text_box)

    if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
        if event.ui_element == dropdown:
            resolution = tuple(map(int, event.text.split('x')))
            pygame.display.set_mode(resolution)
            print('Resolution changed to:', event.text)

    manager.process_events(event)
    return True

def create_dropdown(manager):
    dropdown = pygame_gui.elements.UIDropDownMenu(options_list=['800x600', '1024x768', '1280x720'],
                                                  starting_option='800x600',
                                                  relative_rect=pygame.Rect((350, 200), (100, 30)),
                                                  manager=manager,
                                                  visible=False)
    return dropdown


def hide_all_buttons(buttons, dropdown, text_box):
    for button in buttons.values():
        button.hide()
    dropdown.hide()
    text_box.hide()


# Function for going back to the start screen. Shows all start screen buttons and hide all others.
def start_screen(buttons, dropdown, text_box):
    hide_all_buttons(buttons, dropdown, text_box)  # Hide all buttons
    # Then show only the buttons needed for the start screen
    buttons['start'].show()
    buttons['exit'].show()
    buttons['settings'].show()