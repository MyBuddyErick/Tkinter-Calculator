import tkinter as tk

field_text = ""

def add_to_field(sth):
    global field_text
    field_text = field_text + str(sth)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)

def add_parentheses():
    field.insert("1.0", "()")

def calculate():
    global field_text
    try:
        result = str(eval(field_text))
        field.delete("1.0", "end")
        field.insert("1.0", result)
    except:
        field.delete("1.0", "end")
        field.insert("1.0", "Error")

def add_parentheses():
    global field_text
    open_parentheses = field_text.count("(")
    close_parentheses = field_text.count(")")
    
    if open_parentheses == close_parentheses:
        field_text += "("
    elif open_parentheses > close_parentheses:
        field_text += ")"
    
    field.delete("1.0", "end")
    field.insert("1.0", field_text)

def clear():
    global field_text
    field_text = ""
    field.delete("1.0", "end")

def delete():
    global field_text
    field_text = field_text[:-1]
    field.delete("1.0", "end")
    field.insert("1.0", field_text)

window = tk.Tk()
window.geometry("300x300")
field = tk.Text(window, height=2, width=21, font=("Arial", 20), state="normal")
field.grid(row=1, column=1, columnspan=4)

# Number buttons
btn_1 = tk.Button(window, text="1", command=lambda: add_to_field(1), width=5, font=("Arial"))
btn_1.grid(row=5, column=1)

btn_2 = tk.Button(window, text="2", command=lambda: add_to_field(2), width=5, font=("Arial"))
btn_2.grid(row=5, column=2)

btn_3 = tk.Button(window, text="3", command=lambda: add_to_field(3), width=5, font=("Arial"))
btn_3.grid(row=5, column=3)

btn_4 = tk.Button(window, text="4", command=lambda: add_to_field(4), width=5, font=("Arial"))
btn_4.grid(row=4, column=1)

btn_5 = tk.Button(window, text="5", command=lambda: add_to_field(5), width=5, font=("Arial"))
btn_5.grid(row=4, column=2)

btn_6 = tk.Button(window, text="6", command=lambda: add_to_field(6), width=5, font=("Arial"))
btn_6.grid(row=4, column=3)

btn_7 = tk.Button(window, text="7", command=lambda: add_to_field(7), width=5, font=("Arial"))
btn_7.grid(row=3, column=1)

btn_8 = tk.Button(window, text="8", command=lambda: add_to_field(8), width=5, font=("Arial"))
btn_8.grid(row=3, column=2)

btn_9 = tk.Button(window, text="9", command=lambda: add_to_field(9), width=5, font=("Arial"))
btn_9.grid(row=3, column=3)

btn_0 = tk.Button(window, text="0", command=lambda: add_to_field(0), width=5, font=("Arial"))
btn_0.grid(row=6, column=2)

# Operation buttons
btn_plus = tk.Button(window, text="+", command=lambda: add_to_field("+"), width=5, font=("Arial"))
btn_plus.grid(row=5, column=4)

btn_minus = tk.Button(window, text="-", command=lambda: add_to_field("-"), width=5, font=("Arial"))
btn_minus.grid(row=4, column=4)

btn_times = tk.Button(window, text="*", command=lambda: add_to_field("*"), width=5, font=("Arial"))
btn_times.grid(row=3, column=4)

btn_div = tk.Button(window, text="/", command=lambda: add_to_field("/"), width=5, font=("Arial"))
btn_div.grid(row=2, column=4)

# Special buttons

btn_clear = tk.Button(window, text="AC", command=lambda: clear(), width=5, font=("Arial"))
btn_clear.grid(row=2, column=1)

btn_parenthesis = tk.Button(window, text="(  )", command=add_parentheses, width=5, font=("Arial"))
btn_parenthesis.grid(row=2, column=2)

btn_sqrt = tk.Button(window, text="sqrt", command=lambda: add_to_field("sqrt"), width=5, font=("Arial"))
btn_sqrt.grid(row=2, column=3)

btn_decimal = tk.Button(window, text=".", command=lambda: add_to_field("."), width=5, font=("Arial"))
btn_decimal.grid(row=6, column=1)

btn_delete = tk.Button(window, text="DEL", command=delete, width=5, font=("Arial"))
btn_delete.grid(row=6, column=3)

btn_equal = tk.Button(window, text="=", command=lambda: add_to_field(""), width=5, font=("Arial"))
btn_equal.grid(row=6, column=4)

window.mainloop()