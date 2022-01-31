import sys
import pickle
import shapes


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
    print("2. Add shape")
    print("3. Exit")
    print()


def add_shape(shape, shapes_list):
    try:
        if shape.lower() == "circle":
            radius = float(input("Enter radius of circle: "))
            x_axis = float(input("Enter the x-axis position of the center: "))
            y_axis = float(input("Enter the y-axis position of the center: "))
            axis = (x_axis, y_axis)
            circle = shapes.Circle(radius, axis)
            shapes_list.append(circle)
            save_shapes(shapes_list)
        elif shape.lower() == "rectangle":
            length = float(input("Enter length of rectangle: "))
            width = float(input("Enter width of rectangle: "))
            x_axis = float(input("Enter the x-axis position of the top-left corner: "))
            y_axis = float(input("Enter the y-axis position of the top-left corner: "))
            axis = (x_axis, y_axis)
            rectangle = shapes.Rectangle(length, width, axis)
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
    for shape in shapes_list:
        print(shape)


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
