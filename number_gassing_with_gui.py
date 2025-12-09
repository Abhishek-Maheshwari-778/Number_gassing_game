import tkinter as tk
from tkinter import messagebox
import random
import pygame 

pygame.mixer.init()
SOUNDS = {
    "click": "sounds/click.wav",
    "win": "sounds/win.wav",
    "lose": "sounds/lose.wav",
    "bg_music": "sounds/background.mp3"
}


def play_sound(sound):
    pygame.mixer.Sound(SOUNDS[sound]).play()

pygame.mixer.music.load(SOUNDS["bg_music"])
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) 


class NumberGuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("900x700")
        self.root.configure(bg="white")
        self.username = None
        self.current_number = None
        self.attempts_left = None
        self.max_attempts = None
        self.number_range = None

        
        # Sound control
        self.sound_enabled = True
        self.create_sound_controls()

        # Start with the main menu
        self.main_menu()

    def main_menu(self):
        self.clear_window()

        tk.Label(self.root, text="Number Guessing Game", font=("Arial", 30, "bold"), bg="white").pack(pady=20)

        tk.Label(
            self.root,
            text=f"Welcome, {self.username or 'Player'}!",
            font=("Arial", 16),
            fg="#4CAF50",
            bg="white"
        ).pack(pady=10)

        self.create_button("Play", self.start_single_player).pack(pady=10)


        self.create_button("Quit", self.root.quit).pack(pady=10)

    def create_button(self, text, command):
        button = tk.Button(
            self.root,
            text=text,
            font=("Arial", 18),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            command=lambda: [self.play_click_sound(), command()],
        )
        button.bind("<Enter>", lambda e: button.config(bg="#45a049"))
        button.bind("<Leave>", lambda e: button.config(bg="#4CAF50"))
        return button

    def create_sound_controls(self):
        sound_button = tk.Button(
            self.root,
            text="🔊 Sound ON",
            font=("Arial", 12),
            bg="#FFC107",
            fg="black",
            command=self.toggle_sound
        )
        sound_button.place(x=20, y=20, width=120)

    def toggle_sound(self):
        if self.sound_enabled:
            pygame.mixer.music.pause()
            self.sound_enabled = False
        else:
            pygame.mixer.music.unpause()
            self.sound_enabled = True

    def play_click_sound(self):
        if self.sound_enabled:
            play_sound("click")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def get_username(self):
        self.username = None

        def submit():
            self.username = entry.get().strip()
            if not self.username:
                messagebox.showerror("Error", "Username cannot be empty!")
            else:
                username_window.destroy()

        username_window = tk.Toplevel(self.root)
        username_window.title("Enter Username")
        username_window.geometry("400x200")
        username_window.config(bg="white")

        tk.Label(username_window, text="Enter your username:", font=("Arial", 14), bg="white").pack(pady=10)
        entry = tk.Entry(username_window, font=("Arial", 14))
        entry.pack(pady=10)
        tk.Button(username_window, text="Submit", font=("Arial", 14), command=submit).pack(pady=10)

        username_window.grab_set()
        self.root.wait_window(username_window)
        return self.username

    def setup_game(self, number_range, max_attempts):
        self.current_number = random.randint(*number_range)
        self.number_range = number_range
        self.attempts_left = max_attempts
        self.max_attempts = max_attempts

        self.clear_window()
        tk.Label(self.root, text=f"Guess the number between {number_range[0]} and {number_range[1]}!",
                 font=("Arial", 20), bg="white").pack(pady=10)
        tk.Label(self.root, text=f"All Attempts : {self.attempts_left}", font=("Arial", 16), bg="white", fg="blue").pack(pady=10)

        guess_entry = tk.Entry(self.root, font=("Arial", 16))
        guess_entry.pack(pady=10)

        def submit_guess():
            try:
                guess = int(guess_entry.get())
                guess_entry.delete(0, tk.END)
                self.process_guess(guess)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number!")

        self.create_button("Submit Guess", submit_guess).pack(pady=20)

    def process_guess(self, guess):
        if guess == self.current_number:
            if self.sound_enabled:
                play_sound("win")
            messagebox.showinfo("Congratulations!", f"You guessed the correct number: {self.current_number}")
            self.main_menu()
        else:
            if self.sound_enabled:
                play_sound("lose")
            self.attempts_left -= 1
            if self.attempts_left == 0:
                messagebox.showerror("Game Over", f"You've run out of attempts! The correct number was {self.current_number}")
                self.main_menu()
            else:
                hint = "Try a higher number!" if guess < self.current_number else "Try a lower number!"
                messagebox.showinfo("Incorrect", f"{hint}\nAttempts left: {self.attempts_left}")

    def start_single_player(self):
        self.username = self.get_username()
        if self.username:
            self.setup_game((1, 100), 8)

    def start_two_player(self):
        self.setup_game((1, 100), 10)

    def start_time_attack(self):
        self.setup_game((1, 50), 5)


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGameGUI(root)
    root.mainloop()
