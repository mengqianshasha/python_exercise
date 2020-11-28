import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd
import os
import shutil
import datetime
from enum import Enum
import stat


class FileType(Enum):
    Folder = 0
    File = 1
    Link = 2


class FileInfo:
    size_level = ['KB', 'MB', 'GB']

    def __init__(self, name, stat_result):
        self.name = name
        self.last_modified = datetime.datetime.fromtimestamp(stat_result.st_mtime).strftime('%Y-%m-%d-%H:%M:%S')
        if stat.S_ISDIR(stat_result.st_mode):
            self.type = FileType.Folder
        elif stat.S_ISREG(stat_result.st_mode):
            self.type = FileType.File
        elif stat.S_ISLINK(stat_result.st_mode):
            self.type = FileType.Link
        self.size = FileInfo.format_size(self.type, stat_result.st_size)

    @staticmethod
    def format_size(file_type, size):
        if file_type == FileType.Folder:
            return ''
        if size < 1024:
            return '0KB'
        index = -1
        while size > 1024:
            size = size / 1024
            index += 1

        return str(int(size)) + FileInfo.size_level[index]


class FolderNode:
    def __init__(self, name, location=None, children={}, is_top_level=False):
        self.id = None
        self.name = name
        self.location = location
        self.children = children
        self.is_top_level = is_top_level


class FileManager:
    def __init__(self):
        self.back_history = []
        self.next_history = []
        self.desktop_node = FolderNode('Desktop', 'C:\\Users\\mijian\\Desktop')
        self.quick_access_node = FolderNode('Quick Access', children={'Desktop': self.desktop_node}, location='Quick Access', is_top_level=True)
        self.root_node = FolderNode('C Drive', 'C:\\')
        self.this_pc = FolderNode('This PC', children={'C Drive': self.root_node}, location='This PC', is_top_level=True)
        self.dictionary = {}
        self.current_node = self.quick_access_node
        self.folders = self.list_of_folder_node()

    def add_node(self, id, node):
        self.dictionary[id] = node

    def get_node(self, id):
        return self.dictionary[id]

    def list_of_file_info(self):
        return [FileInfo(i, os.stat(os.path.join(self.current_node.location, i))) for i in os.listdir(self.current_node.location)]

    def list_of_folder_node(self):
        return self.current_node.children

    def go_to_directory(self, node):
        self.back_history.append(self.current_node)
        self.current_node = node
        self.next_history.clear()
        self.notify_current_node_update()

    def notify_current_node_update(self):
        if not self.current_node.is_top_level:
            self.files = self.list_of_file_info()
        else:
            self.folders = self.list_of_folder_node()

    def back(self):
        if self.can_back():
            result = self.back_history.pop()
            self.next_history.append(self.current_node)
            self.current_node = result
            self.notify_current_node_update()

    def can_back(self):
        return len(self.back_history) > 0

    def can_next(self):
        return len(self.next_history) > 0

    def next(self):
        if self.can_next():
            result = self.next_history.pop()
            self.back_history.append(self.current_node)
            self.current_node = result
            self.notify_current_node_update()

class FileExplorerApp(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill="none", expand=1)
        self.file_manager = FileManager()
        self.create_widgets()
        self.is_tree_initialized = False
        self.is_folders_initialized = False
        self.is_open_close = False

    def create_widgets(self):
        self.location_frame = tk.Frame(self)
        self.location_frame.pack(side="top", fill="x", expand=1)

        self.back = tk.Button(self.location_frame)
        self.back["text"] = "<-"
        self.back["command"] = self.click_back
        self.back.grid(row=0, column=0, padx=(10, 0), pady=10)

        self.next = tk.Button(self.location_frame)
        self.next["text"] = "->"
        self.next["command"] = self.click_next
        self.next.grid(row=0, column=1, padx=(10, 0), pady=10)

        self.location = tk.Text(self.location_frame, height=1, width=115, bg="white")
        self.location.grid(row=0, column=2, padx=10, pady=10, sticky="EW")
        self.location.insert('end', self.file_manager.current_node.location)
        self.file_frame = tk.Frame(self, background="white")
        self.file_frame.pack(side="bottom", fill="both", expand=1)

        self.folder_tree = ttk.Treeview(self.file_frame, selectmode='extended', height=25, show="tree", padding=(0,10,0,0))
        folder_tree_scrollbar = ttk.Scrollbar(orient="vertical", command=self.folder_tree.yview)
        self.folder_tree.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="SN")
        self.folder_tree.configure(yscrollcommand=folder_tree_scrollbar.set)
        self.folder_tree.heading('#0', text='Name')
        self.folder_tree.column('#0', stretch=tk.YES)

        self.file_manager.quick_access_node.id = self.folder_tree.insert('', 'end', text=self.file_manager.quick_access_node.name)
        self.file_manager.add_node(self.file_manager.quick_access_node.id, self.file_manager.quick_access_node)
        for k in self.file_manager.quick_access_node.children.values():
            k.id = self.folder_tree.insert(self.file_manager.quick_access_node.id, 'end', text=k.name)
            self.file_manager.add_node(k.id, k)
        self.folder_tree.item(self.file_manager.quick_access_node.id, open=True)
        self.file_manager.this_pc.id = self.folder_tree.insert('', 'end', text=self.file_manager.this_pc.name)
        self.file_manager.add_node(self.file_manager.this_pc.id, self.file_manager.this_pc)
        for k in self.file_manager.this_pc.children.values():
            k.id = self.folder_tree.insert(self.file_manager.this_pc.id, 'end', text=k.name)
            self.file_manager.add_node(k.id, k)

        self.folder_tree.bind('<<TreeviewSelect>>', self.folder_tree_clicked)
        self.folder_tree.bind('<<TreeviewOpen>>', self.folder_tree_openclose)
        self.folder_tree.bind('<<TreeviewClose>>', self.folder_tree_openclose)

        self.update_button_status()

        if not self.file_manager.current_node.is_top_level:
            self.set_up_file_list()
        else:
            self.set_up_folder_list()

    def set_up_file_list(self):
        self.tree = ttk.Treeview(self.file_frame, columns=("DateModified", "Type", "Size"), selectmode='extended',
                                 height=25)
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        self.tree.grid(row=0, column=1, padx=10, pady=10, sticky="EWSN")
        self.tree.configure(yscrollcommand=vsb.set)
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
            file_id = self.tree.insert('', 'end', text=i.name, values=(i.last_modified, str(i.type), i.size))

        self.is_tree_initialized = True

        self.tree.bind("<Button-3>", self.popup)
        self.tree.bind("<Control-a>", self.select_all)
        self.tree.bind("<Double-1>", self.double_lick)

        self.context_menu_on_file = tk.Menu(self, tearoff=0)
        self.context_menu_on_file.add_command(label="Move",
                                    command=self.move)
        self.context_menu_on_file.add_command(label="Copy",
                                    command=self.copy)

        self.context_menu_on_file.add_separator()

        self.context_menu_on_file.add_command(label="Create Shortcut",
                                      command=self.shortcut)

        self.context_menu_on_file.add_command(label="Delete",
                                      command=self.delete)

        self.context_menu_on_file.add_command(label="Rename",
                                      command=self.rename)

    def popup(self, event):
        node = self.tree.selection()
        if len(node) > 0:
            iid = self.tree.identify_row(event.y)
            if iid in node:
                self.context_menu_on_file.post(event.x_root, event.y_root)

    def select_all(self, event):
        pass

    def double_lick(self, event):
        iid = self.tree.identify_row(event.y)
        file = self.tree.item(iid)['text']
        file_type = self.tree.item(iid)['values'][1]
        if file_type == str(FileType.Folder):
            if file not in self.file_manager.current_node.children:
                self.file_manager.current_node.children[file] = FolderNode(file, os.path.join(self.file_manager.current_node.location, file))
                new_id = self.folder_tree.insert(self.file_manager.current_node.id, 'end', text=file)
                self.file_manager.add_node(new_id, self.file_manager.current_node.children[file])

            self.file_manager.go_to_directory(self.file_manager.current_node.children[file])
            self.update_button_status()
            self.update_files()

    def move(self):
        name = fd.askdirectory()
        if name != "":
            for node in self.tree.selection():
                file = self.tree.item(node)['text']
                shutil.move(os.path.join(self.file_manager.current_node.location, file), os.path.join(name, file))
            self.file_manager.notify_current_node_update()
            self.update_files()

    def copy(self):
        name = fd.askdirectory()
        if name != "":
            for node in self.tree.selection():
                file = self.tree.item(node)['text']
                shutil.copyfile(os.path.join(self.file_manager.current_node.location, file), os.path.join(name, file))
            self.file_manager.notify_current_node_update()
            self.update_files()

    def shortcut(self):
        pass

    def delete(self):
        for node in self.tree.selection():
            file = self.tree.item(node)['text']
            file_type = self.tree.item(node)['values'][1]
            if file_type == str(FileType.File) or file_type == str(FileType.Link):
                os.remove(os.path.join(self.file_manager.current_node.location, file))
            else:
                os.rmdir(os.path.join(self.file_manager.current_node.location, file))
        self.file_manager.notify_current_node_update()
        self.update_files()

    def rename(self):
        pass

    def set_up_folder_list(self):
        pass

    def folder_tree_openclose(self, event):
        self.is_open_close = True

    def folder_tree_clicked(self, event):
        if self.is_open_close:
            self.is_open_close = False
            return
        node_id = self.folder_tree.selection()[0]
        node = self.file_manager.get_node(node_id)
        self.file_manager.go_to_directory(node)
        self.update_button_status()
        self.update_files()

    def update_button_status(self):
        if self.file_manager.can_back():
            self.back["state"] = tk.NORMAL
        else:
            self.back["state"] = tk.DISABLED

        if self.file_manager.can_next():
            self.next["state"] = tk.NORMAL
        else:
            self.next["state"] = tk.DISABLED

    def click_back(self):
        self.file_manager.back()
        self.update_button_status()
        self.update_files()

    def click_next(self):
        self.file_manager.next()
        self.update_button_status()
        self.update_files()

    def update_files(self):
        self.location.delete('1.0', "end")
        self.location.insert('end', self.file_manager.current_node.location)
        if not self.file_manager.current_node.is_top_level:
            if not self.is_tree_initialized:
                self.set_up_file_list()
            for item in self.tree.get_children():
                self.tree.delete(item)
            for i in self.file_manager.files:
                self.tree.insert('', 'end', text=i.name, values=(i.last_modified, str(i.type), i.size))


if __name__ == "__main__":
    root = tk.Tk()
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("1100x600+{}+{}".format(positionRight, positionDown))
    root.title("File Explorer")
    app = FileExplorerApp(parent=root)
    app.mainloop()