import tkinter as tk

# Создаем окно приложения

win = tk.Tk()
win.geometry(f'240x260+600+200')
win['bg'] = '#909090'
win.title('Калькулятор')
faw_icon = tk.PhotoImage(file='fawicon.png')
win.iconphoto(False, faw_icon)

# Создаем поле для ввода цифр

calc = tk.Entry(win).grid(row=0, column=0, columnspan=3)

# Создаем кнопки для цифр

tk.Button(text='1').grid(row=1, column=0)
tk.Button(text='2').grid(row=1, column=1)
tk.Button(text='3').grid(row=1, column=2)
tk.Button(text='4').grid(row=2, column=0)
tk.Button(text='5').grid(row=2, column=1)
tk.Button(text='6').grid(row=2, column=2)
tk.Button(text='7').grid(row=3, column=0)
tk.Button(text='8').grid(row=3, column=1)
tk.Button(text='9').grid(row=3, column=2)
tk.Button(text='0').grid(row=4, column=0)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)

win.mainloop()

