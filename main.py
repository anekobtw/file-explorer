import ctypes
import os
import string
import webbrowser

import customtkinter as ctk
import keyboard


# functions
def file_is_hidden(filepath: str):
    if os.name != "nt":
        return os.path.basename(filepath).startswith(".")
    return ctypes.windll.kernel32.GetFileAttributesW(filepath) & 2


# the window
class App(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("File Explorer")

        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, pady=20, padx=20, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.draw_sidebar()
        self.get_drives()

    def draw_sidebar(self):
        ctk.CTkLabel(self.sidebar_frame, text="Quick File Explorer v1.0.0", font=ctk.CTkFont(size=20, weight="bold")).grid(row=0, column=0, padx=20, pady=(20, 0))
        ctk.CTkLabel(self.sidebar_frame, text="© anekobtw, 2024").grid(row=1, column=0, padx=20, pady=(0, 20))
        ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:").grid(row=5, column=0, padx=20)

        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=lambda x: ctk.set_appearance_mode(x))
        self.appearance_mode_optionmenu.set("System")
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(0, 10))

        ctk.CTkButton(self.sidebar_frame, text="Tutorial", fg_color="transparent", border_width=2, command=lambda: webbrowser.open("https://github.com/anekobtw/file-explorer?tab=readme-ov-file#tutorial"), text_color=("gray15", "#DCE4EE")).grid(row=7, column=0, pady=(0, 10))

    def get_drives(self):
        self.path = ""
        self.selected_index = -1
        self.file_buttons = []
        self.main_frame = ctk.CTkScrollableFrame(self, label_text="Select Drive")
        self.main_frame.grid(row=0, column=1, pady=20, padx=20, sticky="nsew")

        drives = [f"{d}:/" for d in string.ascii_uppercase if os.path.exists(f"{d}:/")]
        for drive in drives:
            button = ctk.CTkButton(self.main_frame, text=drive, command=lambda d=drive: self.open_folder(d))
            button.grid(pady=3, padx=3, sticky="nsew")
            self.file_buttons.append(button)

    def open_folder(self, path: str):
        self.path = path
        self.selected_index = -1
        self.file_buttons = []
        self.main_frame = ctk.CTkScrollableFrame(self, label_text=path)
        self.main_frame.grid(row=0, column=1, pady=20, padx=20, sticky="nsew")

        for file in (i for i in os.listdir(path) if not file_is_hidden(f"{path}/{i}")):
            button = ctk.CTkButton(self.main_frame, text=file, command=lambda f=file: self.prepare_opening(f"{self.path}/{f}"))
            button.grid(pady=3, padx=3, sticky="nsew")
            self.file_buttons.append(button)

    def open_file(self):
        try:
            if os.name == "nt":
                os.startfile(self.path)
            else:
                os.system(f'xdg-open "{self.path}"')
        except Exception as e:
            self.main_frame.configure(label_text=f"Failed to open file: {e}")

    def prepare_opening(self, path: str):
        try:
            self.open_folder(path)
        except PermissionError:
            self.main_frame.configure(label_text="Permission denied")
        except NotADirectoryError:
            self.open_file()
        except Exception as e:
            self.main_frame.configure(label_text=str(e))

    def back(self):
        if self.state != "withdrawn":
            p = self.path.split("/")
            p.pop(-1)
            new_path = "/".join(p)
            if new_path and not new_path.endswith(":"):
                try:
                    self.open_folder(new_path)
                except FileNotFoundError:
                    self.get_drives()
            else:
                self.get_drives()

    # keyboard interactions
    def open_close(self):
        if self.state == "withdrawn":
            self.deiconify()
            self.state = "normal"
        else:
            self.withdraw()
            self.state = "withdrawn"

    def select_next(self):
        if self.selected_index >= 0:
            self.file_buttons[self.selected_index].configure(fg_color="#1f6aa5")
        self.selected_index = (self.selected_index + 1) % len(self.file_buttons)
        self.file_buttons[self.selected_index].configure(fg_color="blue")

    def select_previous(self):
        if self.selected_index >= 0:
            self.file_buttons[self.selected_index].configure(fg_color="#1f6aa5")
        self.selected_index = (self.selected_index - 1) % len(self.file_buttons)
        self.file_buttons[self.selected_index].configure(fg_color="blue")

    def open_selected(self):
        self.file_buttons[self.selected_index].invoke()


if __name__ == "__main__":
    app = App()
    keyboard.add_hotkey("esc", app.back)  # go one directory back
    keyboard.add_hotkey("o", app.open_file)  # open the directory you're in
    keyboard.add_hotkey("win+z", app.open_close)  # open/close the window
    keyboard.add_hotkey("down", app.select_next)  # select next file/folder
    keyboard.add_hotkey("up", app.select_previous)  # select previous file/folder
    keyboard.add_hotkey("enter", app.open_selected)  # open the selected file/folder
    app.mainloop()
