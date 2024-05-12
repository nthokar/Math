import customtkinter as CTk

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title("EN/DE/CODER")
        self.resizable(False, False)

        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20,20), sticky="nseew")

        self.entry_password = CTk.CTkEntry(master=self, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

if __name__ == "__main__":
    app = App()
    app.mainloop()