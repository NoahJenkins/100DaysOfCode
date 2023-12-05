import tkinter as tk
import random

# Constants
WIDTH = 600
HEIGHT = 400
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 30
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 15
ENEMY_ROWS = 4
ENEMY_COLS = 8
ENEMY_PADDING = 10
ENEMY_SPEED = .1
PLAYER_SPEED = 4
BULLET_SPEED = 5

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Invaders")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.game_over = False
        self.enemies = []
        self.player_id = None
        self.bullet_id = None
        self.ENEMY_SPEED = 1  # Define as a class variable
        self.create_enemies()
        self.create_player()
        self.bind_keys()
        self.animate()

    def create_enemies(self):
        x_offset = 50
        y_offset = 50
        for row in range(ENEMY_ROWS):
            for col in range(ENEMY_COLS):
                x = x_offset + col * (ENEMY_WIDTH + ENEMY_PADDING)
                y = y_offset + row * (ENEMY_HEIGHT + ENEMY_PADDING)
                enemy = self.canvas.create_rectangle(x, y, x + ENEMY_WIDTH, y + ENEMY_HEIGHT, fill="red")
                self.enemies.append(enemy)

    def create_player(self):
        x = (WIDTH - PLAYER_WIDTH) // 2
        y = HEIGHT - PLAYER_HEIGHT - 20
        self.player_id = self.canvas.create_rectangle(x, y, x + PLAYER_WIDTH, y + PLAYER_HEIGHT, fill="blue")

    def move_player_left(self, event):
        self.canvas.move(self.player_id, -PLAYER_SPEED, 0)

    def move_player_right(self, event):
        self.canvas.move(self.player_id, PLAYER_SPEED, 0)

    def fire_bullet(self, event):
        if not self.game_over and not self.bullet_id:
            x1, y1, x2, y2 = self.canvas.coords(self.player_id)
            x = x1 + (PLAYER_WIDTH / 2)
            y = y1
            self.bullet_id = self.canvas.create_rectangle(x, y, x + 2, y - 10, fill="yellow")
            self.move_bullet()

    def move_bullet(self):
        if self.bullet_id and not self.game_over:
            self.canvas.move(self.bullet_id, 0, -BULLET_SPEED)
            x1, y1, x2, y2 = self.canvas.coords(self.bullet_id)
            for enemy in self.enemies:
                ex1, ey1, ex2, ey2 = self.canvas.coords(enemy)
                if x1 >= ex1 and x2 <= ex2 and y1 >= ey1 and y2 <= ey2:
                    self.canvas.delete(enemy)
                    self.enemies.remove(enemy)
                    self.canvas.delete(self.bullet_id)
                    self.bullet_id = None
                    break
            if y1 <= 0:
                self.canvas.delete(self.bullet_id)
                self.bullet_id = None
            else:
                self.root.after(10, self.move_bullet)
    
    def animate(self):
        if not self.game_over:
            for enemy in self.enemies:
                self.canvas.move(enemy, self.ENEMY_SPEED, 0)  # Use self.ENEMY_SPEED here
                x1, y1, x2, y2 = self.canvas.coords(enemy)
                if x2 >= WIDTH or x1 <= 0:
                    self.ENEMY_SPEED *= -1  # Update self.ENEMY_SPEED
                    for e in self.enemies:
                        self.canvas.move(e, 0, ENEMY_HEIGHT)
                    break
            if self.enemies and self.canvas.coords(self.enemies[-1])[3] >= HEIGHT:
                self.game_over = True
                self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 30))
            self.root.after(10, self.animate)

    def bind_keys(self):
        self.root.bind("<Left>", self.move_player_left)
        self.root.bind("<Right>", self.move_player_right)
        self.root.bind("<space>", self.fire_bullet)

def main():
    root = tk.Tk()
    game = Game(root)
    root.mainloop()

if __name__ == "__main__":
    main()