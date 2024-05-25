import turtle
import math

def draw_branch(t, length, angle, level):
    if level == 0:
        return
    
    t.forward(length)
    t.left(angle)
    draw_branch(t, length * math.cos(math.radians(angle)), angle, level - 1)
    t.right(2 * angle)
    draw_branch(t, length * math.cos(math.radians(angle)), angle, level - 1)
    t.left(angle)
    t.backward(length)

def draw_pythagoras_tree(t, length, level):
    angle = 45
    t.left(90)  
    draw_branch(t, length, angle, level)

def setup_turtle():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed("fastest")
    return t

def main():
    level = int(input("Введіть рівень рекурсії: "))
    t = setup_turtle()
    draw_pythagoras_tree(t, 100, level)
    turtle.done()

if __name__ == "__main__":
    main()

