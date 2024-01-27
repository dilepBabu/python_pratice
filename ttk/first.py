import tkinter as tk
from tkinter import ttk

def calculate_cost():
    global result_label
    square_footage = float(entry_square_footage.get())
    material_cost = float(entry_material_cost.get())
    labor_cost = float(entry_labor_cost.get())

    total_cost = square_footage * (material_cost + labor_cost)

    result_label.config(text=f"Estimated Cost: Rs {total_cost:,.2f}",font=('times new romen',15,'bold'))


# Create the main window
root = tk.Tk()
root.title("Construction Cost Estimator")

# Create and pack widgets
productframe = tk.Frame(root, padx=10, pady=10)
productframe.pack()
frame=tk.LabelFrame(productframe,text="Estimator",font=('times new romen',15,'bold')
                                    ,bg='thistle',bd=8,relief='groove')
frame.grid(row=0,column=0)

label_square_footage = tk.Label(frame, text="Square Footage:",font=('times new romen',15,'bold'),bg='sky blue')
label_square_footage.grid(row=0, column=0, padx=5, pady=5)

entry_square_footage = ttk.Entry(frame,font=('times new romen',15,'bold'))
entry_square_footage.grid(row=0, column=1, padx=5, pady=5)

label_material_cost = tk.Label(frame, text="Material Cost per sq. ft:",font=('times new romen',15,'bold'),bg='sky blue')
label_material_cost.grid(row=1, column=0, padx=5, pady=5)

entry_material_cost = ttk.Entry(frame,font=('times new romen',15,'bold'))
entry_material_cost.grid(row=1, column=1, padx=5, pady=5)

label_labor_cost = tk.Label(frame, text="Labor Cost per sq. ft:",font=('times new romen',15,'bold'),bg='sky blue')
label_labor_cost.grid(row=2, column=0, padx=5, pady=5)

entry_labor_cost = ttk.Entry(frame,font=('times new romen',15,'bold'))
entry_labor_cost.grid(row=2, column=1, padx=5, pady=5)

calculate_button = tk.Button(frame, text="Calculate Cost",font=('times new romen',15,'bold'),bg='sky blue', command=calculate_cost)
calculate_button.grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(frame, text="",bg='thistle')
result_label.grid(row=4, columnspan=2)

# Run the Tkinter event loop
root.mainloop()