from tkinter import Tk, Label, Entry, Button, StringVar
from owlready2 import get_ontology, onto_path

# Load the ontology
onto_path.append(".")  # Directory containing the OWL file
ontology = get_ontology("geometry_shapes.owl").load()

# Define area calculation logic
def calculate_area():
    shape = shape_var.get().lower()
    try:
        if shape == "triangle":
            base = float(base_var.get())
            height = float(height_var.get())
            area = 0.5 * base * height
            result.set(f"Area of Triangle: {area:.2f}")
        elif shape == "rectangle":
            length = float(length_var.get())
            breadth = float(breadth_var.get())
            area = length * breadth
            result.set(f"Area of Rectangle: {area:.2f}")
        elif shape == "circle":
            radius = float(radius_var.get())
            area = 3.14159 * radius ** 2
            result.set(f"Area of Circle: {area:.2f}")
        else:
            result.set("Unsupported shape!")
    except ValueError:
        result.set("Invalid input! Please enter numeric values.")

# Create the GUI
root = Tk()
root.title("Geometry ITS")

# Input for shape selection
Label(root, text="Shape (Triangle, Rectangle, Circle):").grid(row=0, column=0)
shape_var = StringVar()
Entry(root, textvariable=shape_var).grid(row=0, column=1)

# Input for triangle dimensions
Label(root, text="Base:").grid(row=1, column=0)
base_var = StringVar()
Entry(root, textvariable=base_var).grid(row=1, column=1)

Label(root, text="Height:").grid(row=2, column=0)
height_var = StringVar()
Entry(root, textvariable=height_var).grid(row=2, column=1)

# Input for rectangle dimensions
Label(root, text="Length:").grid(row=3, column=0)
length_var = StringVar()
Entry(root, textvariable=length_var).grid(row=3, column=1)

Label(root, text="Breadth:").grid(row=4, column=0)
breadth_var = StringVar()
Entry(root, textvariable=breadth_var).grid(row=4, column=1)

# Input for circle dimensions
Label(root, text="Radius:").grid(row=5, column=0)
radius_var = StringVar()
Entry(root, textvariable=radius_var).grid(row=5, column=1)

# Output for results
result = StringVar()
Label(root, textvariable=result).grid(row=7, column=0, columnspan=2)

# Calculate button
Button(root, text="Calculate Area", command=calculate_area).grid(row=6, column=0, columnspan=2)

root.mainloop()
