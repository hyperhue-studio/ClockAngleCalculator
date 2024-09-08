import tkinter as tk
from math import radians, cos, sin

# Function to calculate the angle between the clock hands
def calculate_angle(hour, minute):
    # Convert the hour and minute to angles in degrees
    hour_angle = (hour % 12) * 30 + minute * 0.5
    minute_angle = minute * 6
    
    # Calculate the angle difference
    angle_difference = abs(hour_angle - minute_angle)
    
    # Adjust the difference if it's greater than 180 degrees
    if angle_difference > 180:
        angle_difference = 360 - angle_difference
    
    return angle_difference

# Function to draw the clock
def draw_clock(hour, minute):
    # Clear the canvas
    canvas.delete("all")
    
    # Calculate the angles of the clock hands
    hour_angle = radians((hour % 12) * 30 + minute * 0.5)
    minute_angle = radians(minute * 6)
    
    # Calculate the final positions of the hands
    x_center = 150
    y_center = 150
    hour_length = 50
    minute_length = 80
    x_hour = x_center + hour_length * sin(hour_angle)
    y_hour = y_center - hour_length * cos(hour_angle)
    x_minute = x_center + minute_length * sin(minute_angle)
    y_minute = y_center - minute_length * cos(minute_angle)
    
    # Draw the clock
    # Outer circle of the clock
    canvas.create_oval(50, 50, 250, 250)
    # Hour hand
    canvas.create_line(x_center, y_center, x_hour, y_hour, width=5, fill="blue")
    # Minute hand
    canvas.create_line(x_center, y_center, x_minute, y_minute, width=3, fill="red")

# Function to handle real-time input and update both the clock and angle
def update_clock_and_angle(*args):
    try:
        hour = int(entry_hour.get())
        minute = int(entry_minute.get())
        
        # Validate hour and minute
        if 0 <= hour <= 23 and 0 <= minute <= 59:
            draw_clock(hour, minute)
            angle = calculate_angle(hour, minute)
            label_result.config(text=f"Angle between the clock hands:\n{round(angle, 2)} degrees")
        else:
            label_result.config(text="Invalid time input.")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")

# Function to reset the input fields and result
def reset_inputs():
    entry_hour.delete(0, tk.END)
    entry_minute.delete(0, tk.END)
    label_result.config(text="")
    canvas.delete("all")

# Create the main window
window = tk.Tk()
window.title("Clock Angle Calculator")

# Instructions
label_instructions = tk.Label(window, text="Enter a time (24-hour format), and the angle between the clock hands will update automatically.")
label_instructions.grid(row=0, column=0, columnspan=2)

# Create the interface elements
label_hour = tk.Label(window, text="Hour (0-23):")
entry_hour = tk.Entry(window)
label_minute = tk.Label(window, text="Minute (0-59):")
entry_minute = tk.Entry(window)

# Add placeholders for the inputs
entry_hour.insert(0, "HH")
entry_minute.insert(0, "MM")

# Bind changes in the input fields to update the clock and angle automatically
entry_hour.bind("<KeyRelease>", update_clock_and_angle)
entry_minute.bind("<KeyRelease>", update_clock_and_angle)

# Create a reset button to clear the inputs
button_reset = tk.Button(window, text="Reset", command=reset_inputs)

# Create the label to display the result
label_result = tk.Label(window, text="")

# Create the canvas for the clock
canvas = tk.Canvas(window, width=300, height=300)

# Position the elements in the window
label_hour.grid(row=1, column=0)
entry_hour.grid(row=1, column=1)
label_minute.grid(row=2, column=0)
entry_minute.grid(row=2, column=1)
button_reset.grid(row=3, column=0, columnspan=2)
label_result.grid(row=4, column=0, columnspan=2)
canvas.grid(row=5, column=0, columnspan=2)

# Run the window
window.mainloop()
