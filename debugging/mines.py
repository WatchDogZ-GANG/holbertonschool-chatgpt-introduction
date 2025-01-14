#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set()
        self.generate_mines(mines)
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.flags = set()

    def generate_mines(self, mines):
        while len(self.mines) < mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.mines.add((x, y))

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2} ", end="")
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (x, y) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('■', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in self.mines:
                    count += 1
        return count

    def reveal(self, x, y):
        if (x, y) in self.mines:
            return False
        to_reveal = [(x, y)]
        while to_reveal:
            cx, cy = to_reveal.pop()
            if not self.revealed[cy][cx]:
                self.revealed[cy][cx] = True
                if self.count_mines_nearby(cx, cy) == 0:
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < self.width and 0 <= ny < self.height:
                                to_reveal.append((nx, ny))
        return True

    def is_win(self):
        revealed_count = sum(sum(row) for row in self.revealed)
        return revealed_count == (self.width * self.height - len(self.mines))

    def play(self):
        while True:
            self.print_board()
            if self.is_win():
                print("Congratulations! You cleared the minefield!")
                break
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds. Try again.")
                    continue
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
