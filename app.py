import customtkinter as CTk
from Coder import Coder
from Coder import generate_key
from Coder import Alphabet
from hacker import hack_key
from CTkMessagebox import CTkMessagebox

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.coder = Coder()
        self.my_font = CTk.CTkFont(family="Ubuntu", size=14)

        self.geometry("1200x800")
        self.title("EN/DE/CODER")
        self.resizable(False, False)
        self.cur_hack_frame=False
        self._decode_encode()

    def _hack(self):
        self.mid_frame.destroy()
        self.left_frame.destroy()
        self.right_frame.destroy()
        self.cur_hack_key=""
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        self.left_frame = CTk.CTkFrame(master=self)
        self.left_frame.grid(row=0, column=0, padx=4, pady=4)
        self.right_frame = CTk.CTkFrame(master=self)
        self.right_frame.grid(row=0, column=1, padx=4, pady=4)

        self.btn_decode_encode = CTk.CTkButton(master=self.left_frame, text="<-Кодирование/декодирование",
                                               command=self.__code_decode_switch, font=self.my_font)
        self.btn_decode_encode.grid(row=0, column=0, sticky='nsew')

        self.phrase = CTk.CTkTextbox(master=self.left_frame, width=600, height=600, font=self.my_font)
        self.phrase.grid(row = 1,column = 0,sticky='nsew')
        self.phrase.insert("0.0", "Взломанное сообщение")

        self.btn_decode_encode = CTk.CTkButton(master=self.left_frame, text="Очистить",
                                               command=self.__clear_phrase, font=self.my_font)
        self.btn_decode_encode.grid(row=2, column=0, sticky='sw')

        self.phrase_label = CTk.CTkTextbox(master=self.left_frame, width=150, height=50, font=self.my_font)
        self.phrase_label.insert("0.0", "Взломанное сообщение")
        self.phrase_label.grid(row=2, column=0,sticky='en')
        self.phrase_label.configure(state="disable",fg_color="#C0B3B0")

        self.btn_decode_encode = CTk.CTkButton(master=self.right_frame, text="--| Взлом |--",
                                      command=self._hack_key, font=self.my_font)
        self.btn_decode_encode.grid(row=0, column=1, sticky='new')

        self.code = CTk.CTkTextbox(master=self.right_frame, width=600, height=600, font=self.my_font)
        self.code.insert("0.0", "Шифрованное сообщение")
        self.code.grid(row=1, column=1,sticky='nsew')

        self.code_label = CTk.CTkTextbox(master=self.right_frame, width=150, height=50, font=self.my_font)
        self.code_label.insert("0.0", "Шифр")
        self.code_label.grid(row=2, column=1,sticky='wn')
        self.code_label.configure(state="disable",fg_color="#C0B3B0")

        self.btn_decode_encode = CTk.CTkButton(master=self.right_frame, text="Очистить",
                                               command=self.__clear_hack, font=self.my_font)
        self.btn_decode_encode.grid(row=2, column=1,sticky = "es")

        self.update()

    def __clear_hack(self):
        self.code.delete("0.0", "end")
        self.code.insert("0.0","")

    def  __clear_phrase(self):
        self.phrase.delete("0.0", "end")
        self.phrase.insert("0.0","")

    def _decode_encode(self):

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        self.left_frame = CTk.CTkFrame(master=self)
        self.left_frame.grid(row=0, column=0, padx=4, pady=4)

        self.mid_frame = CTk.CTkFrame(master=self)
        self.mid_frame.grid(row=0, column=1, pady=4)

        self.right_frame = CTk.CTkFrame(master=self)
        self.right_frame.grid(row=0, column=2, padx=4, pady=4)

        self.btn_hack_frame = CTk.CTkButton(master=self.left_frame, text="<-Взлом",
                                            command=self.__hack_switch, font=self.my_font)
        self.btn_hack_frame.grid(row=1, column=0, sticky="nsew")

        self.phrase = CTk.CTkTextbox(master=self.left_frame, width=600, height=600, font=self.my_font)
        self.phrase.grid(sticky='nsew')
        self.phrase.insert("0.0", "Ваша фраза для шифрования")

        self.phrase_label = CTk.CTkTextbox(master=self.left_frame, width=150, height=50, font=self.my_font)
        self.phrase_label.insert("0.0", "Ваша фраза для шифрования")
        self.phrase_label.grid(row=2, column=0,sticky='wn')
        self.phrase_label.configure(state="disable",fg_color="#C0B3B0")

        self.btn_code = CTk.CTkButton(master=self.mid_frame, text="-> Зашифровать ->", command=self._validate_and_code,
                                      font=self.my_font)
        self.btn_code.grid(row=1, column=0, sticky='nsew')

        self.key = CTk.CTkTextbox(master=self.mid_frame, width=600, height=600, font=self.my_font)
        self.key.grid(row=2, column=0, sticky='nsew')
        self.key.insert("0.0", "Ваш ключ")

        self.btn_generate_key = CTk.CTkButton(master=self.mid_frame, text="-- Сгенерировать ключ --",
                                              command=self._generate_key, font=self.my_font)
        self.btn_generate_key.grid(row=3, column=0, pady=4, sticky='nsew')

        self.btn_code = CTk.CTkButton(master=self.mid_frame, text="<- Расшифровать <-",
                                      command=self._validate_and_decode, font=self.my_font)
        self.btn_code.grid(row=4, column=0, sticky='nsew')

        self.code = CTk.CTkTextbox(master=self.right_frame, width=600, height=600, font=self.my_font)
        self.code.insert("0.0", "Ваш шифр")
        self.code.grid(row=0, column=0, sticky='nsew')


        self.update()

    def __hack_switch(self):
        self.cur_hack_frame=True
        self.left_frame.destroy()
        self.mid_frame.destroy()
        self.right_frame.destroy()
        self._hack()

    def __code_decode_switch(self):
        self.cur_hack_frame=False
        self.left_frame.destroy()
        self.mid_frame.destroy()
        self.right_frame.destroy()
        self._decode_encode()

    def _hack_key(self):
        code = self._get_code()

        if not self._validate(code):
            if not self.show_warning():
                return

        code = self.coder.preprocessing(code)

        try:
            keys = hack_key(code)
        except:
            self.show_error()
            return
        keys = list(map(lambda x: x[0], keys))
        if(len(keys)>0):
            self.cur_hack_key = keys[0]

        self._set_phrase(self.coder.decode(self._get_code(),self.cur_hack_key))


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
        key = self._get_key()
        if( key == "\n" or key == ""):
            if(not self.show_warning_without_key()):
                return

        phrase = self._get_phrase()

        if not self._validate(phrase) or not self._validate(key):
            if not self.show_warning():
                return

        key = self.coder.preprocessing(key)

        phrase = self.coder.preprocessing(phrase)
        try:
            code = self.coder.encode(phrase, key)
            print(code)

            self._set_code(code)
        except:
            self.show_error_wrong_key()

    def _validate_and_decode(self):
        key = self._get_key()

        if( key == ""):
            if(not self.show_warning_without_key()):
                return

        decode = self._get_code()

        if not self._validate(decode) or not self._validate(key):
            if not self.show_warning():
                return


        key = self.coder.preprocessing(key)
        decode = self.coder.preprocessing(decode)

        try:
            phrase = self.coder.decode(decode, key)
            print(phrase)
            self._set_phrase(phrase)
        except:
            self.show_error_wrong_key()
            return

    def __pretty_text(self, text: str) -> str:
        n = 5
        return ' '.join([text[i:i+n] for i in range(0, len(text), n)])

    def show_warning(self):
        msg = CTkMessagebox(title="Ошибка!", message="Допустимо использовать только русские буквы",
                            icon="warning", option_1="Отмена", option_2="Продолжить игнорируя эти символы")
        return msg.get() == "Продолжить игнорируя эти символы"

    def show_warning_without_key(self):
        msg = CTkMessagebox(title="Ошибка!", message="Вы не ввели ключ",
                            icon="warning", option_1="Ок")
        return True

    def show_error(self):
        msg = CTkMessagebox(title="Ошибка!", message="Неподходящее сообщение",
                            icon="warning", option_1="Ок")
        return True

    def show_error_wrong_key(self):
        msg = CTkMessagebox(title="Ошибка!", message="Ошибка!",
                            icon="warning", option_1="Ок")


if __name__ == "__main__":
    CTk.set_default_color_theme("themes/green.json")

    app = App()
    app.mainloop()