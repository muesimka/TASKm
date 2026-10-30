import tkinter as tk
from Frame import AppFrame
from Button import AppButton


class Interface(tk.Tk):
    def __init__(self, window_w=400, window_h=400):
        super().__init__()

        self.root_w = window_w
        self.root_h = window_h
        self.geometry(f"{self.root_w}x{self.root_h}")
        self.title("Task Manager")

        self.frames = {}
        self.buttons = {}

        self.create_interface() 

    def create_interface(self):
        self.create_frames(["menu", "tasks"])
        self.create_buttons()
        self.show_frame("menu")

    def create_frames(self, name_frame):
        for name in name_frame:
            frame = AppFrame(self,color="black",width=self.root_w,height=self.root_h)
            frame.place(x=0, y=0, relwidth=1, relheight=1)
            self.frames[name] = frame

        tk.Label(self.frames["tasks"],text="Все задачи",bg="black",fg="white",font=("Arial", 20)).pack(pady=30)

    def create_buttons(self):
        tk.Label(self.frames["menu"],text="Главное меню", bg="black", fg="white", font=("Arial", 22)).pack(pady=30)

        self.buttons["show_tasks"] = AppButton(self.frames["menu"], text="Посмотреть все задачи", command=lambda: self.show_frame("tasks") )
        self.buttons["show_tasks"].pack(pady=10)

        self.buttons["exit"] = AppButton( self.frames["menu"],text="Выход", command=self.destroy)
        self.buttons["exit"].pack(pady=10)

        self.buttons["back"] = AppButton(self.frames["tasks"], text="Вернуться в меню",command=lambda: self.show_frame("menu"))
        self.buttons["back"].pack(pady=10)

    def show_frame(self, name):
        self.frames[name].tkraise()




if __name__ == "__main__":
    interface = Interface(window_w=800, window_h=600)
    interface.mainloop()
