import tkinter as tk
from tkinter import scrolledtext

class AdventureGame:
    def __init__(self, root):
        self.root = root
        root.title("The Lost Treasure Adventure")
        root.geometry("600x500")
        root.configure(bg="#f0f0f0")

        # Header
        self.header = tk.Label(root, text="The Lost Treasure", font=("Arial", 16, "bold"),
                               bg="#4a7abc", fg="white", pady=10)
        self.header.pack(fill=tk.X)

        # Story display
        self.story_area = scrolledtext.ScrolledText(root, width=70, height=20, wrap=tk.WORD,
                                                    font=("Arial", 12), state=tk.DISABLED, bg="#e6e6e6")
        self.story_area.pack(padx=10, pady=10)

        # Button frame
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=5)

        self.start_game()

    def clear_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def print_text(self, text):
        self.story_area.config(state=tk.NORMAL)
        self.story_area.insert(tk.END, text + "\n\n")
        self.story_area.see(tk.END)
        self.story_area.config(state=tk.DISABLED)

    def start_game(self):
        # Clear story and buttons
        self.story_area.config(state=tk.NORMAL)
        self.story_area.delete(1.0, tk.END)
        self.story_area.config(state=tk.DISABLED)
        self.clear_buttons()

        # Intro
        self.print_text("Welcome to The Lost Treasure adventure!")
        self.print_text("You are an explorer searching for a hidden treasure in an ancient temple.")

        # First choice
        self.root.after(500, self.first_choice)

    def first_choice(self):
        self.print_text("You reach the entrance of the temple. There are two paths:")
        self.print_text("1. Enter through the dark cave.")
        self.print_text("2. Walk along the narrow bridge over a chasm.")

        self.clear_buttons()
        tk.Button(self.button_frame, text="Dark Cave", width=15, command=self.dark_cave).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame, text="Narrow Bridge", width=15, command=self.narrow_bridge).pack(side=tk.LEFT, padx=10)

    def dark_cave(self):
        self.print_text("You enter the dark cave. A wild creature appears!")
        self.clear_buttons()
        tk.Button(self.button_frame, text="Fight", width=15, command=lambda: self.treasure_room(has_key=True)).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame, text="Run", width=15, command=self.first_choice).pack(side=tk.LEFT, padx=10)

    def narrow_bridge(self):
        self.print_text("You carefully walk along the narrow bridge. A storm starts!")
        self.clear_buttons()
        tk.Button(self.button_frame, text="Run Across", width=15, command=lambda: self.treasure_room(has_key=False)).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame, text="Wait", width=15, command=self.game_over).pack(side=tk.LEFT, padx=10)

    def treasure_room(self, has_key):
        self.print_text("You enter the treasure room. Glittering gold and jewels are everywhere!")
        if has_key:
            self.print_text("Using the golden key, you unlock the grand treasure chest filled with ancient riches!")
            self.print_text("CONGRATULATIONS! You found the lost treasure!")
        else:
            self.print_text("The grand chest is locked. Without a key, you can't open it.")
            self.print_text("You collect some scattered coins and leave the temple. GAME OVER")
        self.clear_buttons()
        tk.Button(self.button_frame, text="Play Again", width=15, command=self.start_game).pack(side=tk.LEFT, padx=10)

    def game_over(self):
        self.print_text("The storm grows stronger, and the bridge collapses! You fall and lose the adventure. GAME OVER")
        self.clear_buttons()
        tk.Button(self.button_frame, text="Play Again", width=15, command=self.start_game).pack(side=tk.LEFT, padx=10)


# Run the game
root = tk.Tk()
game = AdventureGame(root)
root.mainloop()

