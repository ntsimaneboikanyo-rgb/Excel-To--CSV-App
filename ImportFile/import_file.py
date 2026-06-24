import customtkinter
from customtkinter import filedialog

def import_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Excel files", ".xlsx")])
    print(file_path)

    return file_path
    