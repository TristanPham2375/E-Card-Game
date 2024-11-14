import tkinter as tk
from random import randint
from tkinter import messagebox
from player_and_card_class import Card, Player


class KaijiGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaiji's Death Game")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(expand=True)

        self.instructions = tk.Label(
            root, text=("Welcome to Kaiji's death game!\n\n"
                        "Rules:\n"
                        "Two decks, 5 cards each\n"
                        "Slave side: slave and 4 citizens\n"
                        "Emperor side: emperor and 4 citizens.\n\n"
                        "Each player places a card each turn. Outcomes:\n"
                        "Citizen vs. Citizen: Draw\n"
                        "Citizen vs. Slave: Citizen wins - Emperor side wins\n"
                        "Emperor vs. Citizen: Emperor wins - Emperor side wins\n"
                        "Emperor vs. Slave: Slave wins - Slave side wins\n\n"
                        "Slave side has a lower chance of winning overall\n Play the Slave side if you want to play as Kaiji.\n"
                        ),
            justify="center"
        )
        self.instructions.pack(pady=10)

        self.side_var = tk.StringVar()
        self.side_var.set("E")
        self.choose_label = tk.Label(root, text="Choose your side (S/E):")
        self.choose_label.pack()
        self.choose_entry = tk.Entry(root, textvariable=self.side_var)
        self.choose_entry.pack()

        self.start_button = tk.Button(
            root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.player = None
        self.player2 = None
        self.turn = 1
        self.condition = True
        self.player_side = "E"
        self.card_buttons = []
        self.selected_card_index = None

        self.output = tk.Text(root, height=10, width=50)
        self.output.pack(pady=10)
        self.output.config(state=tk.DISABLED)

        self.card_buttons_frame = tk.Frame(root)
        self.card_buttons_frame.pack()

        self.play_button = tk.Button(
            root, text="Play Selected Card", command=self.play_turn, state=tk.DISABLED)
        self.play_button.pack(pady=10)

    def start_game(self):
        side = self.side_var.get().upper()
        self.player_side = side
        self.player = Player()
        self.player2 = Player()
        self.turn = 1
        self.condition = True

        if side == 'E':
            self.setup_emperor_side()
        else:
            self.setup_slave_side()

        self.play_button.config(state=tk.NORMAL)
        self.output.config(state=tk.NORMAL)
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, "Game started! Choose a card to play.\n")
        self.output.config(state=tk.DISABLED)
        self.display_hand()

    def setup_emperor_side(self):
        for _ in range(4):
            self.player.addcard(Card("citizen"))
        self.player.addcard(Card("emperor"))

        for _ in range(4):
            self.player2.addcard(Card("citizen"))
        self.player2.addcard(Card("slave"))

    def setup_slave_side(self):
        for _ in range(4):
            self.player.addcard(Card("citizen"))
        self.player.addcard(Card("slave"))

        for _ in range(4):
            self.player2.addcard(Card("citizen"))
        self.player2.addcard(Card("emperor"))

    def display_hand(self):
        for widget in self.card_buttons_frame.winfo_children():
            widget.destroy()
        self.card_buttons = []

        for i, card in enumerate(self.player._hand):
            card_button = tk.Button(self.card_buttons_frame, text=card.string(
            ), command=lambda i=i: self.select_card(i))
            card_button.grid(row=0, column=i)
            self.card_buttons.append(card_button)

        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, "\nCards on hand:\n")
        for i, card in enumerate(self.player._hand):
            self.output.insert(tk.END, f"{i} - {card.string()}\n")
        self.output.config(state=tk.DISABLED)

    def select_card(self, index):
        self.selected_card_index = index
        self.play_button.config(state=tk.NORMAL)

    def play_turn(self):
        if self.selected_card_index is None:
            return

        a1 = self.player.play_card(self.selected_card_index)
        random_index = randint(0, len(self.player2) - 1)
        a2 = self.player2.play_card_bot(random_index)
        compare_result = a1.compare(a2)

        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, f"\nYou played: {a1.string()}\n")
        self.output.insert(tk.END, f"Opponent played: {a2.string()}\n")

        self.card_buttons[self.selected_card_index].destroy()

        if compare_result == -1:
            self.player2.pop(random_index)
            self.player.pop(self.selected_card_index)
            self.output.insert(tk.END, f"You won round {self.turn}\n")
        elif compare_result == 0:
            self.player.pop(self.selected_card_index)
            self.player2.pop(random_index)
            self.output.insert(tk.END, f"Round {self.turn} was a draw\n")
        elif compare_result == 1:
            self.player.pop(self.selected_card_index)
            self.player2.pop(random_index)
            self.output.insert(tk.END, f"You lost round {self.turn}\n")

        self.selected_card_index = None
        self.play_button.config(state=tk.DISABLED)
        self.turn += 1
        self.output.config(state=tk.DISABLED)
        self.check_game_status()

    def check_game_status(self):
        self.output.config(state=tk.NORMAL)
        if self.player_side == 'E':
            if not self.player.has_emperor() and not self.player2.has_slave():
                self.output.insert(tk.END, "You lost the game!\n")
                self.end_game(player_won=False)
            elif (not self.player2.has_slave()) and (self.player.has_emperor()):
                self.output.insert(tk.END, "You won the game!\n")
                self.end_game(player_won=True)
            elif (self.player2.has_slave) and (not self.player.has_emperor()):
                self.output.insert(tk.END, "You won the game!\n")
                self.end_game(player_won=True)
            else:
                self.display_hand()
        elif self.player_side == 'S':
            if not self.player2.has_emperor() and not self.player.has_slave():
                self.output.insert(tk.END, "You won the game!\n")
                self.end_game(player_won=True)
            elif (not self.player.has_slave()) and (self.player2.has_emperor()):
                self.output.insert(tk.END, "You lost the game!\n")
                self.end_game(player_won=False)
            elif (self.player.has_slave) and (not self.player2.has_emperor()):
                self.output.insert(tk.END, "You lost the game!\n")
                self.end_game(player_won=False)
            else:
                self.display_hand()
        self.output.config(state=tk.DISABLED)

    def end_game(self, player_won):
        self.play_button.config(state=tk.DISABLED)
        for widget in self.card_buttons_frame.winfo_children():
            widget.destroy()

        if player_won:
            self.main_frame.config(bg="lightgreen")
            messagebox.showinfo("Congratulations!")
            self.output.config(state=tk.NORMAL)
            self.output.insert(tk.END, "\nCongratulations!")
        else:
            self.main_frame.config(bg="lightcoral")
            messagebox.showwarning("Game Over")
            self.output.config(state=tk.NORMAL)
            self.output.insert(tk.END, "\nBetter luck next time!\n")
        self.output.config(state=tk.DISABLED)


root = tk.Tk()
app = KaijiGameGUI(root)
root.mainloop()
