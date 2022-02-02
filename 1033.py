from tkinter import *

X = 400
Y = 100
WIDTH = 400
HEIGHT = 340
RESIZABLE = FALSE

root = Tk()

def save():
    name.insert(0, "Корнилов И.С.")
    date.insert(0, "06/09/2007")

     # сохранение данных
    save_name = name.get()
    save_date = date.get()





root.title("регистрационный лист")
root.geometry(f"{WIDTH}x{HEIGHT}+{X}+{Y}")
root.resizable(RESIZABLE, RESIZABLE)


frame_name_date = Frame(pady=10, padx=10)
frame_name_date.pack()

Label(master=frame_name_date, text="введите ФИО:").grid(sticky=E, row=0, column=0)
name = Entry(master=frame_name_date, width=40)
name.grid(row=0, column=1)

Label(master=frame_name_date, text="введите дату рождения:").grid(sticky=E, row=1, column=0)
date = Entry(master=frame_name_date, width=40)
name.grid(row=1, column=1)



frame_gender = Frame(pady=0, padx=10)
frame_gender.pack(anchor=W)


Label(master=frame_gender, text="выберите пол").pack(anchor=W)

gender_value = BooleanVar(value=True)
Radiobutton(master=frame_gender, text="Мужской", value=True, variable=gender_value).pack(side=LEFT)
Radiobutton(master=frame_gender, text="Женский", value=True, variable=gender_value).pack(side=LEFT)

frame_intrests = Frame(padx=10, pady=10)
frame_intrests.pack(anchor=W)

Label(master=frame_intrests, text="Выберите интересы:").pack(anchore=W)

intrests_names = ["игры, програмированние, другое"]
intrests_values = []


for i in intrests_names:
    i_value = BooleanVar()
    Checkbutton(master=frame_intrests, text=i, variable=i_value).pack(anchor=W)
    intrests_values.append(i_value)

    frame_button = Frame(padx=20)
    frame_button.pack(anchor=E)

root.mainloop()