import tkinter as tk

def get_text():
    text = txt_edit.get('1.0',tk.END)
    print(text)

class GuiWindow:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.start_txt_editor()
        self.window.mainloop()

    def _get_text(self):
        text = self.txt_edit.get('1.0',tk.END)
        print(text)

    def start_txt_editor(self):
        self.txt_edit = tk.Text(self.window)
        frm_buttons = tk.Frame(self.window, relief=tk.RAISED, bd=2)

        btn_open = tk.Button(frm_buttons, text="Open")
        btn_save = tk.Button(frm_buttons, text="Save As...",command=self._get_text)

        btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_save.grid(row=1, column=0, sticky="ew", padx=5)

        frm_buttons.grid(row=0, column=0, sticky="ns")
        self.txt_edit.grid(row=0, column=1, sticky="nsew")






