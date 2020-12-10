import tkinter as tk
import tkmacosx as tkmac
import pygame


class AlarmApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill="none", expand=1)
        self.time = 0
        self.minute_time = 0
        self.second_time = 0
        self.flag = False
        pygame.mixer.init()
        self.create_widget()


    def create_widget(self):
        self.label = tk.Label(self, bg='light grey', fg='black', height=1, width=10, font=("Helvetica",32))
        self.label.grid(row=0, column=0, columnspan=4, padx=(50, 50), pady=(0,10))
        self.__update_time__()

        self.min = tkmac.Button(self, bg='pink', borderless=True)
        self.min['text'] = 'minute'
        self.min.grid(row=1, column=0)
        self.min['command'] = self.min_clicked

        self.sec = tkmac.Button(self, bg='pink', borderless=True)
        self.sec['text'] = 'second'
        self.sec.grid(row=1, column=1)
        self.sec['command'] = self.sec_clicked

        self.start = tkmac.Button(self, bg='#b4e5fa', borderless=True)
        self.start['text'] = 'start/stop'
        self.start.grid(row=1, column=2)
        self.start['command'] = self.start_clicked

        self.clear = tkmac.Button(self, bg='#b4e5fa', borderless=True)
        self.clear['text'] = 'clear'
        self.clear.grid(row=1, column=3)
        self.clear['command'] = self.clear_clicked

    def min_clicked(self):
        if not self.flag:
            if self.minute_time < 99:
                self.minute_time += 1
            else:
                self.minute_time = 0
            self.__update_time__()

    def sec_clicked(self):
        if not self.flag:
            if self.second_time < 59:
                self.second_time += 1
            else:
                self.second_time = 0
            self.__update_time__()

    def start_clicked(self):
        if not self.flag:
            self.__format_sec__()
            if self.time:
                self.__countdown__()
        else:
            self.__stop_countdown__()

    def clear_clicked(self):
        if not self.flag:
            self.minute_time = 0
            self.second_time = 0
            self.__update_time__()

    def __countdown__(self):
        if self.time:
            self.time -= 1
            self.__format_min_and_sec()
            self.__update_time__()
            self.flag = self.after(1000, self.__countdown__)
        else:
            self.__stop_countdown__()
            self.__play__()

    def __stop_countdown__(self):
        self.after_cancel(self.flag)
        self.flag = False

    def __update_time__(self):
        self.label.configure(text=f'{self.minute_time:0>2}:{self.second_time:0>2}')

    def __format_sec__(self):
        self.time = self.second_time + self.minute_time * 60

    def __format_min_and_sec(self):
        self.second_time = self.time % 60
        self.minute_time = self.time // 60

    def __play__(self):
        pygame.mixer.music.load("/Users/qianshameng/Documents/Media/Music/clips/countdown.mp3")
        pygame.mixer.music.play(loops=0)

if __name__ == "__main__":
    root = tk.Tk()
    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("400x250+{}+{}".format(positionRight, positionDown))
    root.title("Alarm")
    app = AlarmApp(parent=root)
    app.mainloop()