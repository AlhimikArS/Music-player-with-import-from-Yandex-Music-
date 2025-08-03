from PySide6 import QtWidgets,QtCore,QtGui,QtMultimedia
from pygame import mixer
from PySide6.QtWidgets import QMainWindow
import interface
import sys
import os
import YMimport as YM
class Player(QMainWindow,interface.Ui_MainWindow):
    def __init__(self):
        super(Player,self).__init__()
        self.setupUi(self)
        
        self.setFixedSize(self.size())
        
        self.playbtn.clicked.connect(self.play_sound)
        self.prevbtn.clicked.connect(self.prev_sound)
        self.nextbtn.clicked.connect(self.next_sound)
        self.addbtn.clicked.connect(self.add_sound)
        self.removebtn.clicked.connect(self.remove_sound)
        self.Yandex_importbtn.clicked.connect(self.yandex_import)
        self.listWidget.clicked.connect(self.play_sound)
        self.updatebtn.autoRepeatInterval()
        self.updatebtn.setAutoRepeatInterval(100)
        self.updatebtn.setAutoRepeatDelay(100)
        self.updatebtn.clicked.connect(self.update_sound)
        
        self.play = False
        self.dir = ""
        self.sound_mixer = mixer
        self.sound_mixer.init()
    
    def update_sound(self):
        self.listWidget.clear()
        if self.dir:
            # Получаем список файлов с информацией о дате изменения
            files = []
            for filename in os.listdir(self.dir):
                if filename.endswith(('.wav', '.mp3')):
                    filepath = os.path.join(self.dir, filename)
                    # Получаем время последнего изменения файла (в секундах)
                    mtime = os.path.getmtime(filepath)
                    files.append((mtime, filename))
            
            # Сортируем файлы по дате изменения (новые сначала)
            files.sort(key=lambda x: x[0])
            
            # Добавляем отсортированные файлы в список
            for mtime, filename in files:
                self.listWidget.addItem(filename)
            
        
    def play_sound(self, n_or_p=False):
        if not self.listWidget.currentItem():
            self.listWidget.setCurrentRow(0)
            self.play_sound()

        filename = os.path.join(self.dir, self.listWidget.currentItem().text())

        if not self.play:
            # Запуск нового трека
            self.sound_mixer.music.load(filename)
            self.sound_mixer.music.play()
            self.playbtn.setText("||")  # Установите текст паузы сразу
            self.play = True
        else:
            if n_or_p:
                # Переключение на другой трек — сброс состояния
                self.sound_mixer.music.stop()
                self.sound_mixer.music.load(filename)
                self.sound_mixer.music.play()
                self.playbtn.setText("||")  # Обновление текста
            elif self.sound_mixer.music.get_busy() and not n_or_p:
                # Пауза текущего трека
                self.sound_mixer.music.pause()
                self.playbtn.setText("|>")
            elif not self.sound_mixer.music.get_busy() and not n_or_p:
                # Возобновление после паузы
                self.sound_mixer.music.unpause()
                self.playbtn.setText("||")

        
        
    def prev_sound(self):
        try:
            row = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(row -1)
            self.play_sound(True)
        except TypeError:
            if row == self.listWidget.count():
                self.listWidget.setCurrentRow(0)
                self.play_sound(True)

    def next_sound(self):
        row = self.listWidget.currentRow()
        if row < self.listWidget.count() - 1:
            self.listWidget.setCurrentRow(row + 1)
            self.play_sound(True)
        else:
            self.listWidget.setCurrentRow(0)
            self.play_sound(True)

        
    def add_sound(self):
        self.listWidget.clear()
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        
        if dir:
            # Получаем список файлов с информацией о дате изменения
            files = []
            for filename in os.listdir(dir):
                if filename.endswith(('.wav', '.mp3')):
                    filepath = os.path.join(dir, filename)
                    # Получаем время последнего изменения файла (в секундах)
                    mtime = os.path.getmtime(filepath)
                    files.append((mtime, filename))
            
            # Сортируем файлы по дате изменения (новые сначала)
            files.sort(key=lambda x: x[0])
            
            # Добавляем отсортированные файлы в список
            for mtime, filename in files:
                self.listWidget.addItem(filename)
            
            self.dir = dir

    def remove_sound(self):
        self.listWidget.clear()
        self.sound_mixer.music.stop()
    
    def yandex_import(self):
        YM.start()        

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    player = Player()
    player.show()
    
    app.exec()
    