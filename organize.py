import os
import tkinter as tk
from shutil import move

file_extension_map = {
    'pdf'   : 'Report',
    'doc'   : 'Report',
    'docx'  : 'Report',
    'txt'   : 'Report',
    'xlsx'  : 'Data',
    'csv'   : 'Data',
    'png'   : 'Images',
    'jpg'   : 'Images',
    'jpeg'  : 'Images',
    'v'     : 'Code',
    'py'    : 'Code',
    'c'     : 'Code'
}

def organize(folder_input):
    os.chdir(folder_input.get())
    folder_input.delete(0, tk.END)
    
    generate_folders()
    move_files()
    remove_unused_folders()

def generate_folders():
    for f in set(file_extension_map.values()):
        folder_path = f + '/'
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

def move_files():
    all_files = os.listdir()

    for f in all_files:
        if not os.path.isfile(f): 
            continue

        file_name, file_extension = f.split('.')
        if file_extension not in file_extension_map:
            continue

        folder_destination = file_extension_map[file_extension]
        move(f, folder_destination)

def remove_unused_folders():
    folders = [f for f in os.listdir() if os.path.isdir(f)]

    for dir in folders:
        if len(os.listdir(dir)) == 0:
            os.rmdir(dir)

root = tk.Tk()
root.title("Lab Folder Organizer")
root.geometry("400x200")

folder_path = tk.Label(root, text="Folder path")
folder_path.pack(pady=20)

folder_path_input = tk.Entry(root)
folder_path_input.pack(pady=10)

button = tk.Button(root, text="Organize", command=lambda: organize(folder_path_input))
button.pack(pady=10)

root.mainloop()