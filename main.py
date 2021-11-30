import tkinter as tk

# Создаем функцию добавления цифр в окно ввода


def add_digit(digit):
    value = calc.get()
    if value[0] == '0':
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)

# Создаем функцию добавления знаки операций в окно ввода


def add_operations(operations):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value+operations)


# Создаем функцию создания кнопок цифр

def make_digit_buttons(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 15), command=lambda: add_digit(digit))


# Создаем функцию создания знаков операций


def make_operations_buttons(operations):
    return tk.Button(text=operations, bd=5, font=('Arial', 15), fg='red', command=lambda: add_operations(operations))


def make_calc_buttons(operations):
    return tk.Button(text=operations, bd=5, font=('Arial', 15), fg='red', command=lambda: add_digit(operations))



# Создаем окно приложения


win = tk.Tk()
win.geometry(f'240x270+600+200')
win['bg'] = '#909090'
win.title('Калькулятор')
faw_icon = tk.PhotoImage(file='fawicon.png')
win.iconphoto(False, faw_icon)

# Создаем поле для ввода цифр

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

# Создаем кнопки для цифр

make_digit_buttons('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_buttons('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_buttons('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_buttons('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_buttons('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_buttons('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_buttons('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_buttons('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_buttons('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_buttons('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operations_buttons('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operations_buttons('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operations_buttons('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operations_buttons('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_buttons('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)


win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()

