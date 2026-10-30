
import tkinter as tk
from tkinter import ttk, messagebox
import math

BG = "#101827"
PANEL = "#1B263B"
CARD = "#24334D"
BLUE = "#5798FF"
CYAN = "#43D9D0"
WHITE = "#F1F5F9"
MUTED = "#9BAEC8"
RED = "#FF6B81"

root = tk.Tk()
root.title("Graph Studio — редактор графов")
root.geometry("1100x700")
root.minsize(900, 600)
root.configure(bg=BG)

vertices = {}
edges = set()
selected = []
next_id = 1
mode = tk.StringVar(value="Добавить вершину")
R = 22

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background=CARD,
    foreground=WHITE,
    fieldbackground=CARD,
    rowheight=34,
    font=("Segoe UI", 11),
    borderwidth=0
)

style.configure(
    "Treeview.Heading",
    background=PANEL,
    foreground=CYAN,
    font=("Segoe UI", 10, "bold"),
    padding=10,
    relief="flat"
)

style.map(
    "Treeview",
    background=[("selected", BLUE)],
    foreground=[("selected", "white")]
)

header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=24, pady=(20, 14))

tk.Label(
    header, text="GRAPH STUDIO",
    bg=BG, fg=CYAN,
    font=("Segoe UI", 11, "bold")
).pack(anchor="w")

tk.Label(
    header, text="Конструктор неориентированных графов",
    bg=BG, fg=WHITE,
    font=("Segoe UI", 22, "bold")
).pack(anchor="w", pady=(4, 2))

tk.Label(
    header,
    text="Создавайте вершины, соединяйте рёбра и проверяйте лемму о рукопожатиях",
    bg=BG, fg=MUTED,
    font=("Segoe UI", 10)
).pack(anchor="w")

body = tk.Frame(root, bg=BG)
body.pack(fill="both", expand=True, padx=24, pady=(0, 20))

left = tk.Frame(body, bg=PANEL)
left.pack(side="left", fill="both", expand=True, padx=(0, 14))

right = tk.Frame(body, bg=PANEL, width=300)
right.pack(side="right", fill="y")
right.pack_propagate(False)

tk.Label(
    left, text="  Рабочая область",
    bg=PANEL, fg=WHITE,
    font=("Segoe UI", 13, "bold")
).pack(anchor="w", pady=(14, 8))

canvas = tk.Canvas(
    left, bg="#F4F7FC",
    highlightthickness=0
)
canvas.pack(fill="both", expand=True, padx=12, pady=(0, 12))

tk.Label(
    right, text="УПРАВЛЕНИЕ",
    bg=PANEL, fg=CYAN,
    font=("Segoe UI", 10, "bold")
).pack(anchor="w", padx=16, pady=(18, 10))

buttons = [
    ("＋  Добавить вершину", "Добавить вершину", BLUE),
    ("⟷  Добавить ребро", "Добавить ребро", "#287D91"),
    ("−  Удалить вершину", "Удалить вершину", "#A94E68"),
    ("×  Удалить ребро", "Удалить ребро", "#7D567E")
]

for text, value, color in buttons:
    tk.Button(
        right, text=text,
        command=lambda v=value: mode.set(v),
        bg=color, fg="white",
        activebackground=BLUE,
        activeforeground="white",
        relief="flat", bd=0,
        font=("Segoe UI", 10, "bold"),
        cursor="hand2",
        pady=9
    ).pack(fill="x", padx=14, pady=3)

mode_label = tk.Label(
    right, text="Режим: Добавить вершину",
    bg=PANEL, fg=MUTED,
    font=("Segoe UI", 9),
    wraplength=260
)
mode_label.pack(anchor="w", padx=16, pady=(8, 12))

def update_mode(*args):
    mode_label.config(text="Режим: " + mode.get())

mode.trace_add("write", update_mode)

tk.Label(
    right, text="СТАТИСТИКА",
    bg=PANEL, fg=CYAN,
    font=("Segoe UI", 10, "bold")
).pack(anchor="w", padx=16, pady=(4, 8))

stats = tk.Frame(right, bg=CARD)
stats.pack(fill="x", padx=14)

def stat_card(title):
    frame = tk.Frame(stats, bg=CARD)
    frame.pack(fill="x", padx=12, pady=7)

    tk.Label(
        frame, text=title,
        bg=CARD, fg=MUTED,
        font=("Segoe UI", 9)
    ).pack(anchor="w")

    value = tk.Label(
        frame, text="0",
        bg=CARD, fg=WHITE,
        font=("Segoe UI", 18, "bold")
    )
    value.pack(anchor="w")
    return value

v_count = stat_card("Количество вершин")
e_count = stat_card("Количество рёбер")
d_sum = stat_card("Сумма степеней")
e_double = stat_card("Удвоенное число рёбер")

tk.Label(
    right, text="СТЕПЕНИ ВЕРШИН",
    bg=PANEL, fg=CYAN,
    font=("Segoe UI", 10, "bold")
).pack(anchor="w", padx=16, pady=(14, 7))

table = ttk.Treeview(
    right, columns=("v", "d"),
    show="headings", height=5
)
table.heading("v", text="Вершина")
table.heading("d", text="Степень")
table.column("v", width=130, anchor="center")
table.column("d", width=100, anchor="center")
table.pack(fill="x", padx=14)

check = tk.Label(
    right, text="● Лемма ещё не проверена",
    bg=PANEL, fg=MUTED,
    font=("Segoe UI", 10, "bold"),
    wraplength=260
)
check.pack(anchor="w", padx=16, pady=12)

tk.Button(
    right, text="Очистить граф",
    command=lambda: clear_graph(),
    bg="#34445F", fg=WHITE,
    activebackground="#455B7D",
    activeforeground=WHITE,
    relief="flat", bd=0,
    font=("Segoe UI", 10, "bold"),
    cursor="hand2", pady=9
).pack(fill="x", padx=14, pady=(0, 14))

def degree(v):
    return sum(v in edge for edge in edges)

def update_info():
    for item in table.get_children():
        table.delete(item)

    for v in sorted(vertices):
        table.insert(
            "", "end",
            values=(f"Вершина {v}", degree(v))
        )

    total = sum(degree(v) for v in vertices)
    doubled = 2 * len(edges)

    v_count.config(text=str(len(vertices)))
    e_count.config(text=str(len(edges)))
    d_sum.config(text=str(total))
    e_double.config(text=str(doubled))

    if total == doubled:
        check.config(
            text="✓ Лемма о рукопожатиях выполнена",
            fg=CYAN
        )
    else:
        check.config(text="✗ Проверка не пройдена", fg=RED)

def draw_graph():
    canvas.delete("all")

    for a, b in edges:
        x1, y1 = vertices[a]
        x2, y2 = vertices[b]

        canvas.create_line(
            x1, y1, x2, y2,
            fill="#8296B3", width=3
        )

    for v, (x, y) in vertices.items():
        canvas.create_oval(
            x-R, y-R, x+R, y+R,
            fill=BLUE, outline="#2868C8", width=2
        )
        canvas.create_text(
            x, y, text=str(v),
            fill="white",
            font=("Segoe UI", 11, "bold")
        )

    update_info()

def find_vertex(x, y):
    for v, (vx, vy) in vertices.items():
        if math.hypot(x-vx, y-vy) <= R + 5:
            return v
    return None

def click(event):
    global next_id, selected

    x, y = event.x, event.y
    action = mode.get()
    v = find_vertex(x, y)

    if action == "Добавить вершину":
        if v is not None:
            return
        if len(vertices) >= 100:
            messagebox.showwarning("Лимит", "Максимум 100 вершин")
            return

        vertices[next_id] = (x, y)
        next_id += 1

    elif action == "Добавить ребро":
        if v is None:
            return

        if v in selected:
            selected = []
            return

        selected.append(v)

        if len(selected) == 2:
            a, b = selected
            edge = tuple(sorted((a, b)))

            if edge not in edges and a != b:
                if len(edges) < 500:
                    edges.add(edge)
                else:
                    messagebox.showwarning("Лимит", "Максимум 500 рёбер")

            selected = []

    elif action == "Удалить вершину":
        if v is not None:
            del vertices[v]
            edges_copy = set(edges)

            for edge in edges_copy:
                if v in edge:
                    edges.remove(edge)

            selected = []

    elif action == "Удалить ребро":
        nearest = None
        min_distance = 12

        for a, b in edges:
            x1, y1 = vertices[a]
            x2, y2 = vertices[b]
            dx, dy = x2-x1, y2-y1
            length = dx*dx + dy*dy

            if length == 0:
                continue

            t = max(0, min(1,
                ((x-x1)*dx + (y-y1)*dy) / length))

            px, py = x1+t*dx, y1+t*dy
            distance = math.hypot(x-px, y-py)

            if distance < min_distance:
                min_distance = distance
                nearest = (a, b)

        if nearest:
            edges.remove(nearest)

    draw_graph()

def clear_graph():
    global next_id, selected
    vertices.clear()
    edges.clear()
    selected = []
    next_id = 1
    draw_graph()

canvas.bind("<Button-1>", click)
draw_graph()
root.mainloop()