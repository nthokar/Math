import customtkinter as CTk
from Coder import Coder
from Coder import generate_key
from Coder import Alphabet
from hacker import hack_key
from CTkMessagebox import CTkMessagebox


class LeftFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.phrase = CTk.CTkTextbox(master=self)
        self.phrase.grid(sticky='nsew')
        self.phrase.insert("0.0", "ваша фраза для шифрования")

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        super().__init__()
        # self.grid_rowconfigure(0, weight=1)  # configure grid system
        # self.grid_columnconfigure(0, weight=1)
        #
        # self.frame_1 = CTk.CTkFrame(master=self)
        # self.frame_1.grid(sticky='nsew')
        #
        # self.textbox = CTk.CTkTextbox(master=self.frame_1, width=400, corner_radius=0)
        # self.textbox.grid(row=0, column=0, sticky="nsew")
        # self.textbox.insert("0.0", "Some example text!\n" * 50)

        self.coder = Coder()
        my_font = CTk.CTkFont(family="Ubuntu", size=14)

        self.geometry("1840x800")
        self.title("EN/DE/CODER")
        self.resizable(False, False)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.left_frame = CTk.CTkFrame(master=self)
        self.left_frame.grid(row=0, column=0, padx=4, pady=4)

        self.mid_frame = CTk.CTkFrame(master=self)
        self.mid_frame.grid(row=0, column=1, pady=4)

        self.right_frame = CTk.CTkFrame(master=self)
        self.right_frame.grid(row=0, column=2, padx=4, pady=4)


        self.phrase = CTk.CTkTextbox(master=self.left_frame, width=600, height=600, font=my_font)
        self.phrase.grid(sticky='nsew')
        self.phrase.insert("0.0", "ваша фраза для шифрования")


        self.btn_code = CTk.CTkButton(master=self.mid_frame, text="-> Зашифровать ->", command=self._validate_and_code, font=my_font)
        self.btn_code.grid(row=1, column=0, sticky='nsew')

        self.key = CTk.CTkTextbox(master=self.mid_frame, width=600, height=600, font=my_font)
        self.key.grid(row=2, column=0, sticky='nsew')
        self.key.insert("0.0", "ваш ключ шифрования")


        self.btn_generate_key = CTk.CTkButton(master=self.mid_frame, text="-- Сгенерировать ключ --", command=self._generate_key, font=my_font)
        self.btn_generate_key.grid(row=3, column=0, pady=4, sticky='nsew')

        self.btn_code = CTk.CTkButton(master=self.mid_frame, text="<- Расшифровать <-", command=self._validate_and_decode, font=my_font)
        self.btn_code.grid(row=4, column=0, sticky='nsew')


        self.code = CTk.CTkTextbox(master=self.right_frame, width=600, height=600, font=my_font)
        self.code.insert("0.0", "ваш шифр")
        self.code.grid(row=0, column=0, sticky='nsew')

        self.btn_hack = CTk.CTkButton(master=self.right_frame, text="--| Взлом |--", command=self._hack_key, font=my_font)
        self.btn_hack.grid(row=1, column=0, sticky='nsew')

    def _hack_key(self):
        code = self._get_code()

        if not self._validate(code):
            if not self.show_warning():
                return


        code = self.coder.preprocessing(code)
        self._set_code(code)

        keys = hack_key(code)
        keys = list(map(lambda x: x[0], keys))

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)
            self._set_key(choice)

        self.combo_keys = CTk.CTkComboBox(self, values=keys, command=combobox_callback)
        self.combo_keys.grid(row=1, column=1)


    def _generate_key(self):
        key = generate_key()
        self.key.delete("0.0", "end")
        self.key.insert("0.0", key)

    def _get_phrase(self) -> str:
        return self.phrase.get("0.0", "end")

    def _get_key(self) -> str:
        return self.key.get("0.0", "end")

    def _get_code(self) -> str:
        return self.code.get("0.0", "end")


    def _set_phrase(self, text: str):
        self.phrase.delete("0.0", "end")
        self.phrase.insert("0.0", self.__pretty_text(text))

    def _set_key(self, text: str):
        self.key.delete("0.0", "end")
        self.key.insert("0.0", text)

    def _set_code(self, text: str):
        self.code.delete("0.0", "end")
        self.code.insert("0.0", self.__pretty_text(text))

    def _validate(self, text: str) -> bool:
        txt = text[:-1].lower().replace(' ', '')
        for i in txt:
            if i not in Alphabet.alphabet:
                return False
        return True

    def _validate_and_code(self):
        phrase = self._get_phrase()
        key = self._get_key()


        if not self._validate(phrase) or not self._validate(key):
            if not self.show_warning():
                return


        key = self.coder.preprocessing(key)

        phrase = self.coder.preprocessing(phrase)


        code = self.coder.encode(phrase, key)
        print(code)

        self._set_code(code)
        self._set_phrase(phrase)
        self._set_key(key)


    def _validate_and_decode(self):
        key = self._get_key()
        decode = self._get_code()

        if not self._validate(decode) or not self._validate(key):
            if not self.show_warning():
                return

        key = self.coder.preprocessing(key)
        decode = self.coder.preprocessing(decode)



        phrase = self.coder.decode(decode, key)
        print(phrase)
        self._set_phrase(phrase)
        self._set_code(decode)
        self._set_key(key)


    def __pretty_text(self, text: str) -> str:
        n = 5
        return ' '.join([text[i:i+n] for i in range(0, len(text), n)])

    def show_warning(self):
        # Show some retry/cancel warnings
        # msg = CTkMessagebox(title="Ошибка!", message="Допустимо использовать только русские буквы",
        #                     icon="themes/orig.webp", icon_size=(150, 150), option_1="Отмена", option_2="Убрать не подходящие символы")
        msg = CTkMessagebox(title="Ошибка!", message="Допустимо использовать только русские буквы",
                            icon="warning", option_1="Отмена", option_2="Убрать не подходящие символы")

        if msg.get() == "Убрать не подходящие символы":
            key = self._get_key()
            key = self.coder.preprocessing(key)
            self._set_key(key)

            code = self._get_code()
            code = self.coder.preprocessing(code)
            self._set_code(code)

            phrase = self._get_phrase()
            phrase = self.coder.preprocessing(phrase)
            self._set_phrase(phrase)

            return True


if __name__ == "__main__":
    CTk.set_default_color_theme("themes/green.json")

    app = App()
    app.mainloop()