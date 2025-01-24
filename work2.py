import turtle
import sys

def koch_curve(t, order, size):
 
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)
        t.right(120)
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)

def snowflake(t, order, size):

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():

    try:
        if len(sys.argv) > 1:
            order = int(sys.argv[1]) 
        else:
            order = int(input("Введіть рівень рекурсії (ціле число): "))
    except ValueError:
        print("Невірне введення. Використовується рівень 3 за замовчуванням.")
        order = 3

   
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  

    size = 300  


    t.penup()
    t.goto(-size/2, size/3)
    t.pendown()

    snowflake(t, order, size)

    screen.exitonclick()

if __name__ == "__main__":
    main()

