# Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії
import turtle
import math


def draw_tree(length, level):
    if level == 0:
        return

    # Малюємо стовбур
    turtle.forward(length)

    # Зберігаємо позицію та кут
    pos = turtle.pos()
    angle = turtle.heading()

    # Ліва гілка
    turtle.left(30)
    draw_tree(length * 0.7, level - 1)

    # Повертаємося до стовбура
    turtle.penup()
    turtle.setpos(pos)
    turtle.setheading(angle)
    turtle.pendown()

    # Права гілка
    turtle.right(30)
    draw_tree(length * 0.7, level - 1)

    # Повертаємося назад
    turtle.penup()
    turtle.setpos(pos)
    turtle.setheading(angle)
    turtle.pendown()


def main():
    depth = int(input("Введіть рівень рекурсії (наприклад, 6–12): "))

    turtle.speed(0)
    turtle.left(90)  # Повертаємо вгору
    turtle.penup()
    turtle.goto(0, -250)  # Початкова точка — низ екрана
    turtle.pendown()
    turtle.color("saddlebrown")

    draw_tree(100, depth)
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
