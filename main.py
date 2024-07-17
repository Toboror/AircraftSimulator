import aircraft
import character
import events
import pygame
import pygame_gui
import GUI

def main():
    window_surface = GUI.initialize_pygame()
    background = GUI.create_background()
    manager = GUI.create_ui_manager()
    buttons = GUI.create_buttons(manager)
    dropdown = GUI.create_dropdown(manager)
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
        time_delta = clock.tick(GUI.FPS) / 1000.0
        for event in pygame.event.get():
            is_running = GUI.handle_events(event, buttons, dropdown, manager, label, text_box)
            if not is_running:
                break

        manager.update(time_delta)

        bg_image = pygame.image.load('pictures/blackball.jpg')

        window_surface.blit(bg_image, (0, 0))
        manager.draw_ui(window_surface)

        # If the game has started, create the character.
        if GUI.game_started:
            character.create_character(window_surface, GUI.window_width, GUI.window_height)

        # If player has taken off, they can move.
        if events.hasTakenOff:
            character.player_can_move = True

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

