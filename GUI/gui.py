import tkinter
from tkinter import *
import customtkinter
from ImportFile.import_file import import_file
from Excel_to_CSV.excel_to_csv import excel_to_csv
import os

# function to set up the initial gui state
def gui_setup():
# make a basic block 
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("dark-blue")

    app = customtkinter.CTk() 
    app.grid_columnconfigure(0,weight=1)

    app.title("Excel to CSV Converter")
    app.geometry("500x500")



    # Title
    header_frame = customtkinter.CTkFrame(master=app, fg_color='#f2f2f2') # Defining our frame
    header_frame.grid(row=0,column=0) # Placing our frame in the larger app

    title_label = customtkinter.CTkLabel(master=header_frame, text="Excel to CSV Converter", text_color="black", bg_color='#f2f2f2') # defining a label
    title_label.grid(row=0,column=0, padx=50, pady=20) # place the label in a specfic frame 



    #Upload
    upload_frame = customtkinter.CTkFrame(master=app, fg_color='#f2f2f2')
    upload_frame.grid(row=1,column=0)

    #file finder
    file_frame = customtkinter.CTkFrame(master=upload_frame,width=400, height=200, fg_color='#f2f2f2')
    file_frame.grid(row=0,column=0)

    file_button = customtkinter.CTkButton(master=file_frame,text="Click here to find your Excel doc in the File Explorer" \
    "", fg_color="#397031",hover_color= '#579e4d',text_color="white",width=200,height=200, command=excel_to_csv)
    file_button.grid(row=0,column=0)



    # Button
    button_frame = customtkinter.CTkFrame(master=app,fg_color='#f2f2f2')
    button_frame.grid(row=2,column=0)

    convert_button = customtkinter.CTkButton(master=button_frame, text="Convert", fg_color='black',width=200,height=50) # currently the button won't do anything, add functionality in the last argument 
    # # convert_button.place(relx=0.5,rely=0.9,anchor=tkinter.CENTER)
    convert_button.grid(row=1,column=1,pady=70)



    app.mainloop()






# 23 June 2026
# Just finished the basic GUI and the file opening architecture. So now we need to bring it all together, link the gui to the architecture 
# also just realised i might have saved my stuff incorrectly by putting it in the venv folder, might be worth trying to actually check if they should be in there or not, otherwise i don't think they actually get saved to github