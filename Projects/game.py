import pygame
import random
from abc import ABC, abstractmethod

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 959, 536
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHARKDLE")

font = pygame.font.Font(None, 60)
title_font = pygame.font.Font(None, 120)
win_font = pygame.font.Font(None, 90)

# --- Colors ---
CORRECT = (0, 120, 255)
MISPLACED = (255, 165, 0)
WRONG = (100, 100, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 200)
RED = (200, 0, 0)

# --- Layout ---
BOX_SIZE = 80
BOX_SPACING = 100
NUM_COLS = 5
ROW_SPACING = 90

# --- Word Classes ---
class Word(ABC):
    def __init__(self, text):
        self.text = text.upper()

    @abstractmethod
    def letters(self):
        pass

class SecretWord(Word):
    def letters(self):
        return list(self.text)

class GuessWord(Word):
    def letters(self):
        return list(self.text)

    def feedback(self, secret):
        colors = []
        for i, letter in enumerate(self.text):
            if secret.text[i] == letter:
                colors.append(CORRECT)
            elif letter in secret.text:
                colors.append(MISPLACED)
            else:
                colors.append(WRONG)
        return colors

# --- Renderer ---
class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw_guess(self, guess, colors, row, scroll_offset):
        margin_right = 40
        start_x = WIDTH - (NUM_COLS * BOX_SPACING) - margin_right

        for col, letter in enumerate(guess.letters()):
            rect = pygame.Rect(
                start_x + col * BOX_SPACING,
                50 + row * ROW_SPACING - scroll_offset,
                BOX_SIZE, BOX_SIZE
            )

            box = pygame.Surface((BOX_SIZE, BOX_SIZE), pygame.SRCALPHA)
            pygame.draw.rect(box, colors[col] + (200,),
                             box.get_rect(), border_radius=12)
            self.screen.blit(box, rect.topleft)

            text = font.render(letter, True, BLACK)
            self.screen.blit(text, text.get_rect(center=rect.center))

    def draw_end_message(self, message, color):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 140))
        self.screen.blit(overlay, (0, 0))

        text = win_font.render(message, True, color)
        self.screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

# --- Button ---
class Button:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = "SUBMIT"

    def set_text(self, text):
        self.text = text.upper()

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect, border_radius=12)
        label = font.render(self.text, True, WHITE)
        screen.blit(label, label.get_rect(center=self.rect.center))

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

# --- Game ---
class Game:
    def __init__(self):
        self.background = pygame.image.load("background.jpg").convert()
        self.renderer = Renderer(screen)

        button_w, button_h = 200, 60
        self.button = Button(
            (WIDTH - button_w) // 2,
            HEIGHT - button_h - 20,
            button_w, button_h
        )

        self.reset_game()

    def reset_game(self):
        self.secret = SecretWord(random.choice(["APPLE", "GRAPE", "PEARL", "STONE", "CHAIR"]))
        self.guesses = []
        self.current_guess = ""
        self.scroll_offset = 0
        self.max_attempts = 10
        self.game_over = False
        self.win = False
        self.button.set_text("SUBMIT")

    def submit_guess(self):
        if len(self.current_guess) == 5 and not self.game_over:
            guess = GuessWord(self.current_guess)
            self.guesses.append(guess)

            visible_height = HEIGHT - 120
            max_rows = visible_height // ROW_SPACING
            if len(self.guesses) > max_rows:
                self.scroll_offset = (len(self.guesses) - max_rows) * ROW_SPACING

            if guess.text == self.secret.text:
                self.win = True
                self.game_over = True
                self.button.set_text("RESTART")
            elif len(self.guesses) >= self.max_attempts:
                self.game_over = True
                self.button.set_text("RESTART")

            self.current_guess = ""

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and not self.game_over:
            if event.key == pygame.K_RETURN:
                self.submit_guess()
            elif event.key == pygame.K_BACKSPACE:
                self.current_guess = self.current_guess[:-1]
            elif event.unicode.isalpha() and len(self.current_guess) < 5:
                self.current_guess += event.unicode.upper()

        if self.button.is_clicked(event):
            if self.game_over:
                self.reset_game()
            else:
                self.submit_guess()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.scroll_offset = max(0, self.scroll_offset - ROW_SPACING)
            elif event.button == 5:
                self.scroll_offset += ROW_SPACING

    def draw(self):
        screen.blit(self.background, (0, 0))

        for row, guess in enumerate(self.guesses):
            self.renderer.draw_guess(
                guess,
                guess.feedback(self.secret),
                row,
                self.scroll_offset
            )

        margin_right = 40
        start_x = WIDTH - (NUM_COLS * BOX_SPACING) - margin_right
        y = 50 + len(self.guesses) * ROW_SPACING - self.scroll_offset

        for col in range(NUM_COLS):
            rect = pygame.Rect(start_x + col * BOX_SPACING, y, BOX_SIZE, BOX_SIZE)
            box = pygame.Surface((BOX_SIZE, BOX_SIZE), pygame.SRCALPHA)
            pygame.draw.rect(box, (255, 255, 255, 100),
                             box.get_rect(), border_radius=12)
            screen.blit(box, rect.topleft)

            if col < len(self.current_guess):
                letter = font.render(self.current_guess[col], True, BLACK)
                screen.blit(letter, letter.get_rect(center=rect.center))

        self.button.draw(screen)

        if self.game_over:
            if self.win:
                self.renderer.draw_end_message("YOU WIN!", CORRECT)
            else:
                self.renderer.draw_end_message("TRY AGAIN", RED)

        pygame.display.flip()

    def run(self):
        self.show_main_menu()
        running = True
        while running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.handle_input(event)
        pygame.quit()

    # --- MAIN MENU ---
    def show_main_menu(self):
        waiting = True
        while waiting:
            screen.fill(BLUE)
            title_text = title_font.render("SHARKDLE", True, WHITE)
            prompt_text = font.render("PRESS ANY KEY TO START", True, WHITE)

            screen.blit(title_text, title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
            screen.blit(prompt_text, prompt_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False  # Start the game

if __name__ == "__main__":
    Game().run()