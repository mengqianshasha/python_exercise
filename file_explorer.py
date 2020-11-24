import tkinter as tk
import tkinter.ttk as ttk
import os
import shutil
import datetime


class FileInfo:
    def __init__(self, name, stat):
        self.name = name
        self.last_modified = datetime.datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d-%H:%M:%S')
        self.type = stat.st_mode
        self.size = stat.st_size


class FileManager:
    def __init__(self):
        self.currentDirectory = "\\"
        self.back_history = []
        self.next_history = []
        self.files = self.list_of_file_info()

    def list_of_file_info(self):
        return [FileInfo(i, os.stat(self.currentDirectory + i)) for i in os.listdir(self.currentDirectory)]

    def go_to_directory(self, directory):
        self.back_history.append(self.currentDirectory)
        self.currentDirectory = directory
        self.next_history.clear()
        self.files = self.list_of_file_info()

    def back(self):
        if self.can_back():
            result = self.back_history.pop()
            self.next_history.append(result)
            return result

    def can_back(self):
        return len(self.back_history) > 0

    def can_next(self):
        return len(self.next_history) > 0

    def next(self):
        if self.can_next():
            return self.next_history.pop()


class FileExplorerApp(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.pack()
        self.file_manager = FileManager()
        self.create_widgets()

    def create_widgets(self):
        self.location_frame = tk.Frame(self, background="grey")
        self.location_frame.pack(side="top", fill="x", expand=1)
        self.location = tk.Text(self.location_frame, height=1, width=96, bg="white")
        self.location.insert('end', self.file_manager.currentDirectory)
        self.location.pack()
        self.tree_frame = tk.Frame(self, background="white")
        self.tree_frame.pack(side="left", expand=1)
        self.file_frame = tk.Frame(self, background="white")
        self.file_frame.pack(side="right", expand=1)
        self.tree = ttk.Treeview(self.file_frame, columns=("Name", "DateModified", "Type", "Size"))
        self.tree.heading('#0', text='Name')
        self.tree.heading('#1', text='DateModified')
        self.tree.heading('#2', text='Type')
        self.tree.heading('#3', text='Size')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#3', stretch=tk.YES)

        for i in self.file_manager.files:
            self.tree.insert('', 'end', text=i.name, values=(i.last_modified, i.type, i.size))

        self.tree.pack(side="right", fill="y")


if __name__ == "__main__":
    root = tk.Tk()
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("800x600+{}+{}".format(positionRight, positionDown))
    root.title("File Explorer")
    app = FileExplorerApp(parent=root)
    app.mainloop()