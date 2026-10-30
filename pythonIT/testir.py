
import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("500x500")
root.configure(bg="black")

# Верхняя часть — поле результата
top_frame = tk.Frame(root, height=150, bg="white", width=500)
top_frame.pack(fill="x")
top_frame.pack_propagate(False)

entry = tk.Entry(top_frame, font=("Arial", 22), justify="right")
entry.pack(fill="both", expand=True, padx=5, pady=5)

# Левая часть — цифры
left_frame = tk.Frame(root, height=150, bg="grey", width=200)
left_frame.pack(side="left", fill="both", expand=True)

# Правая часть — операции
right_frame = tk.Frame(root, height=150, bg="blue", width=200)
right_frame.pack(side="right", fill="both", expand=True)


# Добавление символа в поле
def add(value):
    entry.insert(tk.END, value)


# Очистка поля
def clear():
    entry.delete(0, tk.END)


# Вычисление результата
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


# Кнопки с цифрами
numbers = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0", ".", "C"
]

for i, number in enumerate(numbers):
    if number == "C":
        command = clear
    else:
        command = lambda n=number: add(n)

    tk.Button(
        left_frame,
        text=number,
        font=("Arial", 16),
        command=command
    ).grid(row=i // 3, column=i % 3, sticky="nsew",
           padx=2, pady=2)

# Кнопки математических операций
operations = [
    ("+", "+"),
    ("-", "-"),
    ("*", "*"),
    ("/", "/"),
    ("=", "=")
]

for i, (text, value) in enumerate(operations):
    if value == "=":
        command = calculate
    else:
        command = lambda v=value: add(v)

    tk.Button(
        right_frame,
        text=text,
        font=("Arial", 16),
        command=command
    ).grid(row=i, column=0, sticky="nsew",
           padx=2, pady=2)

# Растягивание кнопок
for i in range(4):
    left_frame.rowconfigure(i, weight=1)

for i in range(3):
    left_frame.columnconfigure(i, weight=1)

for i in range(5):
    right_frame.rowconfigure(i, weight=1)

right_frame.columnconfigure(0, weight=1)

root.mainloop()