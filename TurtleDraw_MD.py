import turtle
import math

def main():
    # Set up the screen and turtle
    screen = turtle.Screen()
    screen.setup(450, 450)
    screen.title("TurtleDraw")
    
    t = turtle.Turtle()
    t.speed(0)  # Set turtle to maximum speed
    t.penup()   # Start with the pen up
    total_distance = 0  # Initialize the total distance to 0

    # Ask user for the input file
    input_file = input("Please enter the name of the input file: ")

    try:
        with open(input_file, "r") as file:
            last_x, last_y = 0, 0  # Starting coordinates at the origin

            for line in file:
                # Strip whitespace and process each line
                line = line.strip()
                
                if line == "stop":
                    t.penup()  # Lift the pen to stop drawing
                    continue
                
                # Split the line into parts
                parts = line.split()
                color = parts[0]
                
                # If the line has a color, move the turtle accordingly
                if len(parts) == 3:
                    x = int(parts[1])
                    y = int(parts[2])
                    
                    # Move to the new point, first without drawing
                    if last_x == 0 and last_y == 0:
                        t.goto(x, y)
                    else:
                        # Calculate distance from the last point
                        distance = math.sqrt((x - last_x) ** 2 + (y - last_y) ** 2)
                        total_distance += distance
                        t.pendown()
                        t.color(color)
                        t.goto(x, y)

                    # Update the last position
                    last_x, last_y = x, y

                # If it's a "stop", lift the pen
                if line == "stop":
                    t.penup()

            # Display the total distance in the bottom right corner
            t.penup()
            t.goto(180, -180)
            t.color("black")
            t.write(f"Total Distance: {total_distance:.2f} units", font=("Arial", 12, "normal"))
        
        # Wait for user to press Enter before closing the window
        turtle.done()

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return

if __name__ == "__main__":
    main()
