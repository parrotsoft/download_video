import customtkinter
from core import youtube


class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Youtube Downloader")
        self.geometry("320x160")
        self.resizable(False, False)

        label = customtkinter.CTkLabel(self, text='URl Youtube')
        label.grid(row=0, column=0, pady=10)

        self.entry_link = customtkinter.CTkEntry(self, width=300, placeholder_text='Pega la URL del video de YouTube')
        self.entry_link.grid(row=1, column=0, padx=10, sticky=customtkinter.EW)

        self.button = customtkinter.CTkButton(self, text='Download', command=self.download_video)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.status_label = customtkinter.CTkLabel(self, text='')
        self.status_label.grid(row=4, column=0, pady=5)

    def download_video(self):
        try:
            url = self.entry_link.get()
            if not url:
                self.status_label.configure(text="Por favor, ingresa una URl")
                return

            self.status_label.configure(text="Downloading...")
            self.button.configure(state='disabled')

            success = youtube.download_video(self.entry_link.get())

            if success:
                self.status_label.configure(text="Descarga completada!")
            else:
                self.status_label.configure(text="Error en la descarga")

        except Exception as e:
            self.status_label.configure(text=f'Error: {str(e)}')
        finally:
            self.button.configure(state='normal')


app = Window()
app.mainloop()
