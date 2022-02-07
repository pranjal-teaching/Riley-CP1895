import sys
import pickle
import turtle
import shapes
from turtle import *


def print_graphic(graphic, current_shape):
    if isinstance(current_shape, shapes.Circle):
        graphic.goto(current_shape.center_position)
        graphic.pendown()
        graphic.circle(current_shape.radius)
    elif isinstance(current_shape, shapes.Rectangle):
        graphic.goto(current_shape.top_left_corner_position)
        graphic.pendown()
        graphic.forward(current_shape.width)
        graphic.right(90)
        graphic.forward(current_shape.length)
        graphic.right(90)
        graphic.forward(current_shape.width)
        graphic.right(90)
        graphic.forward(current_shape.length)
        graphic.right(90)
    graphic.hideturtle()


def graphical_display(current_shape):
    print("1. Draw current shape")
    print("2. Change color for shape")
    print("3. Clear screen")
    print()
    graphic = Turtle()
    graphic.penup()
    option = int(input("Choose an option: "))
    print()
    if option == 1:
        print_graphic(graphic, current_shape)
    elif option == 2:
        try:
            pen_color = input("Enter a color: ")
            graphic.color(pen_color)
            choice = input("Print shape? (y/n): ")
            if choice.lower() == 'y':
                print_graphic(graphic, current_shape)
        except turtle.TurtleGraphicsError:
            print("Invalid color.")
    elif option == 3:
        clearscreen()
        choice = input("Print shape? (y/n): ")
        if choice.lower() == 'y':
            graphic = Turtle()
            print_graphic(graphic, current_shape)
    else:
        print("Invalid option.")


def load_shapes():
    try:
        with open("shapes.bin", "rb") as file:
            shapes_list = pickle.load(file)
    except FileNotFoundError:
        shapes_list = []
    except OSError:
        print("Error reading file - closing program.")
        sys.exit()
    return shapes_list


def save_shapes(shapes_list):
    try:
        with open("shapes.bin", "wb") as file:
            pickle.dump(shapes_list, file)
    except OSError:
        print("Error saving file - closing program.")


def menu():
    print("1. View shapes")
    print("2. Add shape to list")
    print("3. Exit")
    print()


def add_shape(new_shape, shapes_list):
    try:
        if new_shape.lower() == "circle":
            radius = float(input("Enter radius of circle: "))
            x_axis = float(input("Enter the x-axis position of the center: "))
            y_axis = float(input("Enter the y-axis position of the center: "))
            axis = (x_axis, y_axis)
            new_circle = shapes.Circle(radius, axis)
            shapes_list.append(new_circle)
            save_shapes(shapes_list)
        elif new_shape.lower() == "rectangle":
            length = float(input("Enter length of rectangle: "))
            rectangle_width = float(input("Enter width of rectangle: "))
            x_axis = float(input("Enter the x-axis position of the top-left corner: "))
            y_axis = float(input("Enter the y-axis position of the top-left corner: "))
            axis = (x_axis, y_axis)
            rectangle = shapes.Rectangle(length, rectangle_width, axis)
            shapes_list.append(rectangle)
            save_shapes(shapes_list)
        else:
            print("Invalid shape.\n")
        print()
        menu()
    except ValueError:
        print("Invalid data for shape.")
        print()


def view_shapes(shapes_list):
    index = 0
    while len(shapes_list) > index:
        print(f"{index + 1}. {shapes_list[index]}")
        index += 1
    print()
    try:
        shape_number = int(input("Enter shape number: "))
        graphical_display(shapes_list[shape_number - 1])
    except (IndexError, ValueError):
        print()
        print("Invalid shape number.")


def main():
    print("Shapes Program - Riley Burke\n")
    shapes_list = load_shapes()
    menu()
    while True:
        option = int(input("Choose an option: "))
        if option == 1 and len(shapes_list) > 0:
            print()
            view_shapes(shapes_list)
            print()
            menu()
        elif option == 1 and len(shapes_list) == 0:
            print("\nEmpty list, please add a shape.\n")
        elif option == 2:
            print()
            shape_type = input("Enter type of shape: ")
            add_shape(shape_type, shapes_list)
        elif option == 3:
            break
        else:
            print("Invalid option (1-3)")


if __name__ == "__main__":
    main()
