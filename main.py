import tkinter as tk
import random


class Game():
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed App")
        self.root.geometry("600x600")
        self.root.configure(height=600, width=600)
        self.timer = 60
        self.wpm = 0
        self.word_list = [
                        "cat", "pancake", "friday", "moon", "tree", "car", "book", "chair", "water", "food",
                        "house", "ball", "shoe", "cloud", "rain", "bird", "fish", "star", "fire", "earth", "air",
                        "rock", "bridge", "key", "door", "window", "table", "computer", "phone", "plant", "education",
                        "swim", "shirt", "pants", "sock", "glove", "clock", "bed", "mirror", "brush", "knife",
                        "fork", "spoon", "plate", "yellow", "building", "carrot", "apple", "banana", "orange",
                        "grapes", "document", "madagaskar", "explosion", "planning", "wonderful", "amazing",
                        "gorgeous", "fantasy", "painting", "happiness", "exciting", "adorable", "innovation",
                        "leadership", "refreshing", "children", "journey", "motivated", "optimistic", "imagination"
                         ]
        self.failed_words = {}
        self.create_gui()

    def set_timer(self):
        # Function to set timer and update remaining time
    
        if self.timer > 0:
            self.timer -= 1
            self.time_label.config(text=f"Time: {self.timer}s")
            self.root.after(1000, self.set_timer)
        else:
            self.word_label.config(text=f"Time expired your wpm score is: {self.wpm}", font=("Arial", 20))
            self.word_label.place(x=120, y=140)

            self.type_entry.unbind("<Return>")
            self.type_entry.place_forget()
            self.text_label.place_forget()
            # Output list of wrong typed words
            self.wrong_label = tk.Label(text="Incorrectly typed words: ", font=("Arial", 15))
            self.wrong_label.place(x=120, y=260)
            y_position = 275
            for n in self.failed_words:
                value = self.failed_words[n]
                key = n
                new_label = tk.Label(text=f"{key}:{value}", font=("Arial", 15))
                y_position += 30
                new_label.place(x=120, y=y_position)

    def enter(self, event):
        # Function called when user enters text and press enter
        if self.type_entry.get() == self.word:
            self.wpm += 1
            self.wpm_label.config(text=f"Wpm: {self.wpm}", font=20)
        else:
            self.failed_words[self.word] = self.type_entry.get()
        self.type_entry.delete(0, tk.END)

        self.word = random.choice(self.word_list)
        self.word_label.config(text=f"Word: {self.word}", font=("Arial", 40))
        self.word_list.remove(self.word)

    def play(self):
        # Set up window for game and initiate a timer
        self.play_label.place_forget()
        self.play_button.place_forget()
        self.word = random.choice(self.word_list)

        self.time_label = tk.Label(text=f"Time: {self.timer}", font=20, bg="lightblue")
        self.time_label.place(x=50, y=50)

        self.word_label = tk.Label(text=f"Word: {self.word}", font=("Arial", 40))
        self.word_label.place(x=130, y=100)

        self.text_label = tk.Label(text="Type word hier", font=("Arial", 15))
        self.text_label.place(x=200, y=200)

        self.type_entry = tk.Entry(width=30)
        self.type_entry.place(x=200, y=230)

        self.wpm_label = tk.Label(text=f"Wpm: {self.wpm}", font=20, bg="lightblue")
        self.wpm_label.place(x=500, y=50)
        self.type_entry.bind("<Return>", self.enter)
        self.type_entry.focus()
        self.set_timer()

    def start_game(self):
        # Functions triggered to start a game, displays instructions
        self.welcome_label.place_forget()
        self.read_label.place_forget()
        self.start_button.place_forget()

        self.play_label = tk.Label(text="Type word that shows on screen and press enter.\n"
                                   "Time starts after you press 'play' button. You have 60 seconds.", font="30")
        self.play_label.place(x=80, y=100)

        self.play_button = tk.Button(text="Play", width=15, command=self.play)
        self.play_button.place(x=250, y=150)

    def create_gui(self):
        # Set up gui
        self.welcome_label = tk.Label(text="Welcome to Typing Speed Test", font=("arial", 25))
        self.welcome_label.place(x=60, y=40)

        self.read_label = tk.Label(text="Are you Ready to type? ", font=("arial", 15), height=2, width=90)
        self.read_label.place(x=-210, y=100)

        self.start_button = tk.Button(text="Start Test", command=self.start_game)
        self.start_button.place(x=400, y=115)


def main():
    root = tk.Tk()
    Game(root)
    root.mainloop()


if __name__ == '__main__':
    main()
