import tkinter as tk

class Snake(tk.Tk):
    width = 10
    height = 10

    def __init__(self):
        self.x = 10
        self.y = 10
        self.currentDirection = "Right"
        self.targetDirection = "Right"
        self.targetX = 20
        self.targetY = 20
    def draw(self, mainCanvas):
        self.tkObject = mainCanvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, outline="#0f0", fill="#0f0")

class SnakeChain():
    def __init__(self):
        self.snakeList = []
    
    def __getitem__(self, key):
        return self.snakeList[key]

    def addBlock(self, mainCanvas):
        snake = Snake()
        snake.x = self.snakeList[-1].x - 15
        snake.y = self.snakeList[-1].y
        self.snakeList.append(snake)
        snake.draw(mainCanvas)