"""
    The Game of Tic Tac Toe
    Author: Israel Dryer
    Modified: 2020-05-12
"""
from math import sqrt
from random import choice
import tkinter as tk
from PIL.ImageTk import PhotoImage


class Gameboard:
    """The Game of Tic Tac Toe"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x800")

        # images
        self.img_bg = PhotoImage(file='images/board.png')
        self.img_x = [PhotoImage(file='images/'+file) for file in ['blue_X1.png', 'blue_X2.png', 'blue_X3.png']]
        self.img_o = [PhotoImage(file='images/'+file) for file in ['green_O1.png', 'green_O2.png', 'green_O3.png']]
        self.img_wins = [PhotoImage(file='images/'+file) for file in ['h_win.png', 'v_win.png', 'c1_win.png', 'c2_win.png']]

        # canvas used to draw all images
        self.canvas = tk.Canvas(self.root)
        self.canvas.create_image(0, 0, image=self.img_bg, anchor=tk.NW)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.canvas.bind("<Button-1>", self.on_move)

        # game variables
        self.move_count = 0
        self.game_moves = list(False for _ in range(9))
        self.player = 'x'

        # playable position coordinates
        self.center_xy = (
            (130, 115), (392, 115), (650, 115),
            (130, 355), (392, 355), (650, 355),
            (130, 636), (392, 636), (650, 636))

    def collect_win_combos(self):
        """Collect and return all possible winning combinations from existing moves"""
        winning_combos = (
            # horizontal wins
            (self.game_moves[0:3], 'H1'),
            (self.game_moves[3:6], 'H2'),
            (self.game_moves[6:10], 'H3'),

            # vertical wins
            (list([self.game_moves[0], self.game_moves[3], self.game_moves[6]]), 'V1'),
            (list([self.game_moves[1], self.game_moves[4], self.game_moves[7]]), 'V2'),
            (list([self.game_moves[2], self.game_moves[5], self.game_moves[8]]), 'V3'),

            # corner wins
            (list([self.game_moves[0], self.game_moves[4], self.game_moves[8]]), 'C1'),
            (list([self.game_moves[6], self.game_moves[4], self.game_moves[2]]), 'C2'))

        return winning_combos

    def check_for_winner(self):
        """Check for winner and draw win pictures"""
        winning_combos = self.collect_win_combos()

        # display appropriate slash depending on the column/row of win
        for combo, win_type in winning_combos:
            if all(map(lambda x: x == 'x', combo)) or all(map(lambda o: o == 'o', combo)):
                if win_type == 'H1':
                    x, y = self.center_xy[1]
                    self.canvas.create_image(x, y, image=self.img_wins[0])
                elif win_type == 'H2':
                    x, y = self.center_xy[4]
                    self.canvas.create_image(x, y, image=self.img_wins[0])
                elif win_type == 'H3':
                    x, y = self.center_xy[7]
                    self.canvas.create_image(x, y, image=self.img_wins[0])
                elif win_type == 'V1':
                    x, y = self.center_xy[3]
                    self.canvas.create_image(x, y, image=self.img_wins[1])
                elif win_type == 'V2':
                    x, y = self.center_xy[4]
                    self.canvas.create_image(x, y, image=self.img_wins[1])
                elif win_type == 'V3':
                    x, y = self.center_xy[5]
                    self.canvas.create_image(x, y, image=self.img_wins[1])
                elif win_type == 'C2':
                    x, y = self.center_xy[4]
                    self.canvas.create_image(x, y, image=self.img_wins[2])
                elif win_type == 'C1':
                    x, y = self.center_xy[4]
                    self.canvas.create_image(x, y, image=self.img_wins[3])
            else:
                continue

    def on_move(self, event):
        """Callback when mouse is clicked on play"""

        # find playable location nearest to click
        index = self.find_nearest_location(event)

        # check if move has already occured
        print(self.game_moves)
        if not self.game_moves[index]:
            self.move_count += 1
            self.game_moves[index] = self.player
            x, y = self.center_xy[index]

            # draw the players token on the canvas
            if self.player == 'x':
                self.canvas.create_image(x, y, image=choice(self.img_x))
            else:
                self.canvas.create_image(x, y, image=choice(self.img_o))

            self.check_for_winner()
            self.player = 'x' if self.player == 'o' else 'o'
        else:
            return

    def find_nearest_location(self, event):
        """Find the playable location nearest to the point clicked"""
        distances = []
        for x, y in self.center_xy:
            distances.append(sqrt((x - event.x)**2 + (y - event.y)**2))

        # find the index number of the closes grid (center_xy)
        index = distances.index(min(distances))
        return index


if __name__ == '__main__':

    game = Gameboard()
    game.root.mainloop()
