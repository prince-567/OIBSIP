#Prince 
#          Task-2  BMI Calculator

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x400")
root.configure(bg="#c0b8b8")
root.title("BMI CALCULATOR")
font1 = ("Sans-serif", 12)

title_label = Label(root, text="BMI CALCULATOR", padx=30, pady=15, bg="#887a7a", font=font1)
weight_label = Label(root, text="Your weight(in Kgs): ", padx=13, pady=10, bg="#c0b8b8", font=font1)
height_label = Label(root, text="Your height(in mts): ", padx=13, pady=10, bg="#c0b8b8", font=font1)
bmi_label = Label(root, text="BMI Value: ", padx=13, pady=10, bg="#c0b8b8", font=font1)
bmi_msg = Label(root, text="BMI Category: ", padx=13, pady=10, bg="#c0b8b8", font=font1)

user_weight = Entry(root, width=20)
user_height = Entry(root, width=20)
bmi_entry = Entry(root, width=20, bg="#c0b8b8", font=font1)
cat_entry = Entry(root, width=30, bg="#c0b8b8", font=font1)

res = 0
msg = ''

def calculate_bmi():
    """ this function computes user's bmi """
    global res, msg
    msg = ""
    bmi_entry.delete(0, END)
    cat_entry.delete(0, END)
    try:
        weight = float(user_weight.get())
        height = float(user_height.get())
        if weight <= 0 or height <= 0:
            raise ZeroDivisionError
            
    except ValueError:
        messagebox.showerror("Error", "Values must be numeric")
        res = ''
    except ZeroDivisionError:
        messagebox.showerror("Error", "Height and(or)  weight value cannot be zero")
        res = ''
    else:
        user_bmi = weight/(height*height)
        user_bmi_res = round(user_bmi, 2)
        res = str(user_bmi_res)
        if user_bmi < 18.5:
            msg = " \t\tUnderweight\t\t"
            cat_entry.insert(0, msg)
        elif user_bmi < 25:
            msg = "Normal Healthy Weight"
        elif user_bmi < 30:
            msg = "\t\tOverweight\t\t"
        elif user_bmi < 35:
            msg = "\t\tObesity\t\t"
        else:
            msg = "\t\tSevere Obesity\t\t"

    bmi_entry.insert(0, res)
    cat_entry.insert(0, msg)


def clear_values():
    user_weight.delete(0, END)
    user_height.delete(0, END)
    bmi_entry.delete(0, END)
    cat_entry.delete(0, END)

compute_btn = Button(root, text="COMPUTE BMI", padx=5, pady=5, bg="#887a7a", font=font1, command=calculate_bmi)
reset_btn = Button(root, text="RESET", padx=5, pady=5, bg="#887a7a", font=font1, command=clear_values)


title_label.grid(row=0, column=0, columnspan=3)
weight_label.grid(row=1, column=0)
height_label.grid(row=2, column=0)
user_weight.grid(row=1, column=1)
user_height.grid(row=2, column=1)
compute_btn.grid(row=3, column=1)
reset_btn.grid(row=3, column=0)
bmi_label.grid(row=4, column=0)
bmi_entry.grid(row=4, column=1)
bmi_msg.grid(row=5, column=0)
cat_entry.grid(row=5, column=1)

root.mainloop()
