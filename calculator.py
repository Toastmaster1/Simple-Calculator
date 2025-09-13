import tkinter as tk

displayText = ""
resultShowing = False
lastInput = ""

def create_layout():

    # subroutines
    def editDisplay(input):
        global displayText
        global resultShowing
        global lastInput
        if input == "enter" and lastInput not in ["+", "-", "/", "*"]:
            displayText = eval(displayText)
            resultShowing = True
        elif input == "clear":
            displayText = ""
        else:
            if resultShowing:
                displayText = ""
                resultShowing = False
            if lastInput not in ["+", "-", "/", "*"] or input not in ["+", "-", "/", "*", "enter"]:
                displayText += input
                lastInput = input
        
        display.config(text=displayText)

    root = tk.Tk()
    root.title("Calculator")
    root.geometry("400x500")

    # Display
    display = tk.Label(root, text="", font=("Arial", 30), anchor="e", bg="white", relief="sunken")
    display.pack(fill="x", padx=10, pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Row 0
    b00 = tk.Button(button_frame, text="7", font=("Arial", 14), command=lambda:editDisplay("7"))
    b01 = tk.Button(button_frame, text="8", font=("Arial", 14), command=lambda:editDisplay("8"))
    b02 = tk.Button(button_frame, text="9", font=("Arial", 14), command=lambda:editDisplay("9"))
    b03 = tk.Button(button_frame, text="+", font=("Arial", 14), bg="lightgray", command=lambda:editDisplay("+"))

    # Row 1
    b10 = tk.Button(button_frame, text="4", font=("Arial", 14), command=lambda:editDisplay("4"))
    b11 = tk.Button(button_frame, text="5", font=("Arial", 14), command=lambda:editDisplay("5"))
    b12 = tk.Button(button_frame, text="6", font=("Arial", 14), command=lambda:editDisplay("6"))
    b13 = tk.Button(button_frame, text="-", font=("Arial", 14), bg="lightgray", command=lambda:editDisplay("-"))

    # Row 2
    b20 = tk.Button(button_frame, text="1", font=("Arial", 14), command=lambda:editDisplay("1"))
    b21 = tk.Button(button_frame, text="2", font=("Arial", 14), command=lambda:editDisplay("2"))
    b22 = tk.Button(button_frame, text="3", font=("Arial", 14), command=lambda:editDisplay("3"))
    b23 = tk.Button(button_frame, text="*", font=("Arial", 14), bg="lightgray", command=lambda:editDisplay("*"))

    # Row 3
    b30 = tk.Button(button_frame, text="0", font=("Arial", 14), command=lambda:editDisplay("0"))
    b31 = tk.Button(button_frame, text="clear", font=("Arial", 10), bg="lightgray", command=lambda:editDisplay("clear"))
    b32 = tk.Button(button_frame, text="enter", font=("Arial", 10), bg="lightgray", command=lambda:editDisplay("enter"))
    b33 = tk.Button(button_frame, text="/", font=("Arial", 14), bg="lightgray", command=lambda:editDisplay("/"))

    # Grid placement
    b00.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    b01.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
    b02.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
    b03.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)

    b10.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
    b11.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
    b12.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
    b13.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)

    b20.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
    b21.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
    b22.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
    b23.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)

    b30.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
    b31.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
    b32.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
    b33.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)

    # Expand rows and columns evenly
    for i in range(4):
        button_frame.grid_rowconfigure(i, weight=1)
        button_frame.grid_columnconfigure(i, weight=1)
        display.pack(fill="both", expand=True)

    root.mainloop()

create_layout()
