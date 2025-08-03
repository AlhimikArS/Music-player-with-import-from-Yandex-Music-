from yandex_music import ClientAsync
import asyncio
import webbrowser
import os
import re
import customtkinter as ctk
import time
import concurrent.futures
def sanitize_filename(filename):
    # Удаляем запрещённые символы
    filename = re.sub(r'[<>:"/\\|?*#]', '', filename)
    # Заменяем пробелы на подчёркивания
    filename = filename.replace(' ', '_')
    return filename



class PathEntryFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,fg_color="transparent")
        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=0)
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter path to save")
        self.entry.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "ew")
        
        self.button = ctk.CTkButton(self, text="Browse", command=self.browse)
        self.button.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "ew")
        
        
        
    def browse(self):
        path = ctk.filedialog.askdirectory()
        if path:
            self.entry.delete(0, 'end')
            self.entry.insert(0, path)
        
            
        
class YandexMusicImporter(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("Yandex Music Import")
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.grid_columnconfigure((0), weight=1)
        
        self.label = ctk.CTkLabel(self,text='Enter your yandex music token',font=('Arial', 16))
        self.label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "ew")
        
        self.weblabel = ctk.CTkLabel(
            self,
            text="How get?",
            text_color="blue",              # Синий цвет текста
            cursor="hand2",                  # Курсор в виде руки
            font=("Arial", 14, "underline")  # Подчёркнутый шрифт
        )
        self.weblabel.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "ew")
        self.weblabel.bind("<Button-1>", lambda e: webbrowser.open_new("https://yandex-music.readthedocs.io/en/main/token.html"))
        
        self.entryToken = ctk.CTkEntry(self, placeholder_text="Enter your token here")
        self.entryToken.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "ew")
        
        self.entryPath = PathEntryFrame(self)
        self.entryPath.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "ew")
        self.btn = ctk.CTkButton(self, text="Import",command=self.button_clicked)
        self.btn.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "ew")
        
        
        
    def button_clicked(self):
        if self.btn.cget("text") == "Stop":
            if self.executor:
                self.executor.shutdown(wait=False)
                self.stop_flag = True  # Устанавливаем флаг "Stop"
                self.executor = None
                self.btn.configure(text='Import')
                self.textbox.insert("end", "Остановлено пользователем.\n")
            return
                
        
        elif self.entryToken.get() and  self.entryPath.entry.get():
            self.geometry("450x500")
            self.grid_rowconfigure((0,1,2,3,4,5), weight=1)
            
            self.btn.configure(True,text = 'Stop')
            
            self.stop_flag = False  # Сбрасываем флаг
            
            self.textbox = ctk.CTkTextbox(self)
            self.textbox.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
            self.textbox.insert("1.0", "Importing...\n")
            
            # Запуск асинхронной задачи в отдельном потоке
            self.executor = concurrent.futures.ThreadPoolExecutor()
            future = self.executor.submit(self.run_async_task, self.entryToken.get(), self.entryPath.entry.get())
            future.add_done_callback(self.on_task_complete)
        else:pass   

    def run_async_task(self, token, path_to_save):
        asyncio.run(self.yandex_music_import(token, path_to_save))

    def on_task_complete(self, future):
        if future.exception() is not None:
            self.textbox.insert("end", f"Произошла ошибка: {future.exception()}\n")
        else:
            self.textbox.insert("end", "Импорт завершён.\n")
        self.btn.configure(True,text = 'Import')


    async def yandex_music_import(self, token, path_to_save):
        try:
            client = ClientAsync(token=token)
            await client.init()
            
            liked_tracks = await client.users_likes_tracks()
            
            if not liked_tracks or not liked_tracks.tracks:
                self.textbox.insert("end", "No liked tracks found.\n")
                return
            
            os.makedirs(path_to_save, exist_ok=True)
            existing_files = os.listdir(path_to_save)
            
            for track_short in liked_tracks.tracks:
                if self.stop_flag:  # Проверяем флаг
                    self.textbox.insert("end", "Загрузка остановлена.\n")
                    return
                try:
                    full_track = await track_short.fetch_track_async()
                    clean_title = sanitize_filename(full_track.title)
                    filename = f"{clean_title}.mp3"
                    
                    if filename in existing_files:
                        self.textbox.insert("end", f"Трек {clean_title} уже скачан.\n")
                        continue
                    
                    self.textbox.insert("end", f"Скачиваем: {clean_title}\n")
                    await full_track.download_async(f'{path_to_save}/{filename}')
                    self.textbox.insert("end", f"Успешно скачан: {clean_title}\n")
                    self.textbox.see("end")   
                except Exception as e:
                    self.textbox.insert("end", f"Ошибка при обработке трека {clean_title}: {e}\n")
                        
        except Exception as e:
            self.textbox.insert("end", f"Произошла ошибка: {e}\n")

def start():
    ctk.set_appearance_mode("dark")
    app = YandexMusicImporter()
    
        
    app.mainloop()
    app.executor.shutdown(wait=False)
    app.stop_flag = True
    

if __name__ == "__main__":
    start()