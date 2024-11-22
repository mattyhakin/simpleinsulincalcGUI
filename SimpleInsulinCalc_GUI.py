import tkinter as tk

# Ratios for different meal types
breakfast = 2
lunch = 1.5
dinner = 1.5
snack = 1.5
correctional = 1

# Function to process the input and calculate the dose
def calculate():
    try:
        dose_type = input_display.get().lower()
        carbs = float(carbs_display.get())
        correction_needed = correctional_question.get()
        correction_units = correction_display.get()

        if dose_type == "breakfast":
            ratio = breakfast
        elif dose_type == "lunch":
            ratio = lunch
        elif dose_type == "dinner":
            ratio = dinner
        elif dose_type == "snack":
            ratio = snack
        else:
            result_display.set("Invalid Dose Type")
            return

        dose = ratio * carbs / 10

        if correction_needed.lower() == "yes":
            if correction_units.isdigit():
                correction = float(correction_units) * correctional
                total_dose = dose + correction
                result_display.set(f"You Need {total_dose:.1f} Units of Insulin")
            else:
                result_display.set("Invalid Correction Units")
        else:
            result_display.set(f"You Need {dose:.1f} Units of Insulin")

    except ValueError:
        result_display.set("Invalid Input")

# Function to clear all inputs and results
def clear_inputs():
    input_display.set("")
    carbs_display.set("")
    correctional_question.set("")
    correction_display.set("")
    result_display.set("")

# Create the main window
root = tk.Tk()
root.title("Insulin Dose Calculator")

# Display variables
input_display = tk.StringVar()
carbs_display = tk.StringVar()
correctional_question = tk.StringVar()
correction_display = tk.StringVar()
result_display = tk.StringVar()

# Input fields and labels
tk.Label(root, text="Type of Dose:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=input_display).grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Carbs (g):").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=carbs_display).grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Need Correction? (yes/no):").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=correctional_question).grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Correction Units (if yes):").grid(row=3, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=correction_display).grid(row=3, column=1, padx=5, pady=5)

# Result display
tk.Label(root, text="Result:").grid(row=4, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=result_display, state="readonly").grid(row=4, column=1, padx=5, pady=5)

# Buttons
tk.Button(root, text="Calculate", command=calculate).grid(row=5, column=0, pady=10)
tk.Button(root, text="Clear", command=clear_inputs).grid(row=5, column=1, pady=10)

# Run the application
root.mainloop()
