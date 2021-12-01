import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    """Функция добавления цифр в окно ввода"""
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)


def add_operations(operations):
    """Функция добавления знаки операций в окно ввода"""
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' or value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value+operations)


def make_digit_buttons(digit):
    """Функция создает кнопки с цифрами"""
    return tk.Button(text=digit, bd=5, font=('Arial', 15), command=lambda: add_digit(digit))


def make_operations_buttons(operations):
    """Функция создания знаков операций"""
    return tk.Button(text=operations, bd=5, font=('Arial', 15), fg='red', command=lambda: add_operations(operations))


def make_calc_buttons(operations):
    """Функция создает кнопку равно"""
    return tk.Button(text=operations, bd=5, font=('Arial', 15), fg='red', command=calculate)


def make_clear_buttons(operations):
    """Функция создает кнопку очистить"""
    return tk.Button(text=operations, bd=5, font=('Arial', 15), fg='red', command=clear)


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)


def calculate():
    """Функция для подсчета значений"""
    value = calc.get()
    if value[-1] in '+-*/':
        operation = value[-1]
        value = value[:-1] + operation + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Введите цифры' )
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя')
        calc.insert(0, 0)


def press_key(event):
    """Функция обработки событий клавиатуры"""
    print(event.char)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operations(event.char)
    elif event.char == '\r':
        calculate()


win = tk.Tk()
win.geometry(f'240x270+850+400')
win['bg'] = '#909090'
win.title('Калькулятор')
faw_icon = tk.PhotoImage(file='fawicon.png')
win.iconphoto(False, faw_icon)

win.bind('<Key>', press_key)

# Создаем поле для ввода цифр

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

# Создаем кнопки

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
make_clear_buttons('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()



