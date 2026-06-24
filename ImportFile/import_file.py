import customtkinter
from customtkinter import filedialog


#file import 


def import_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Excel files", "*.xlsx"), ("Excel Binary Files", "*.xlsb")])
    print("File successfully imported: ", file_path)

    return file_path



