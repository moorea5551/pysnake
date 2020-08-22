import tkinter as tk
from tkinter import ttk
from Snake import Snake, SnakeChain

root = tk.Tk()

def move(event):
    global motion
    global snakeChain
    mainCanvas.after_cancel(motion)
    direction = event.keysym
    
    targetX = snakeChain[0].x
    targetY = snakeChain[0].y
    for snake in snakeChain:
        snake.targetDirection = direction

        if snake.targetX == targetX and snake.targetY == targetY:
            print("here")
            if direction == "Up":
                snake.y = snake.y - 5
            elif direction == "Down":
                snake.y = snake.y + 5
            elif direction == "Left":
                snake.x = snake.x - 5
            elif direction == "Right":
                snake.x = snake.x + 5
        else:
            print("there")
            snake.targetX = targetX
            snake.targetY = targetY

        print(mainCanvas.coords(snake))
        mainCanvas.coords(snake, snake.x, snake.y, snake.x+snake.width, snake.y+snake.height)
    motion = mainCanvas.after(500, move, event)
    
mainCanvas = tk.Canvas(root, bg="black")
mainCanvas.pack()

# bind key strokes for motion
root.bind("<Down>", move)
root.bind("<Left>", move)
root.bind("<Up>", move)
root.bind("<Right>", move)

# init first snake block and chain
snake = Snake()
snakeChain = SnakeChain()
snakeChain.snakeList.append(snake)
snake.draw(mainCanvas)
print(mainCanvas.coords(snake))

# create initial "after" event so that new motion afters can be cancelled
motion = mainCanvas.after(500, lambda: print("hacky hack"))
    
tk.mainloop()