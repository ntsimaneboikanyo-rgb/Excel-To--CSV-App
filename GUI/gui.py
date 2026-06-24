import tkinter
from tkinter import *
import customtkinter
from customtkinter import filedialog
import os

def drop(event):
    drop_here_label.configure(text=event.data)

# make a basic block 
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk() 
app.grid_columnconfigure(0,weight=1)

app.title("Excel to CSV Converter")
app.geometry("500x500")

# I don't need a textbox, so I'm going to comment this out
# textbox = customtkinter.CTkTextbox(app, width=250, height=250)
# textbox.grid(row=0, column=0, padx=100,pady=100,sticky="nsew")

# Title
header_frame = customtkinter.CTkFrame(master=app, fg_color='#f2f2f2') # Defining our frame
header_frame.grid(row=0,column=0) # Placing our frame in the larger app

title_label = customtkinter.CTkLabel(master=header_frame, text="Excel to CSV Converter", text_color="black", bg_color='#f2f2f2') # defining a label
title_label.grid(row=0,column=0, padx=50, pady=20) # place the label in a specfic frame 




#Upload
upload_frame = customtkinter.CTkFrame(master=app, fg_color='#f2f2f2')
upload_frame.grid(row=1,column=0)

#drag&drop 
drag_drop_frame = customtkinter.CTkFrame(master=upload_frame,width=400, height=200, fg_color='#ffb3b3')
drag_drop_frame.grid(row=0,column=0)

# make it a dnd widget
drag_drop_frame.drop_target_register(DND_FILES)


drag_drop_frame.dnd_bind('<<Drop>>',drop)

# Label 
drop_here_label = customtkinter.CTkLabel(master=upload_frame, text="Drop your excel file here",font=("ariel",14,"bold"), bg_color="#ffb3b3")
drop_here_label.grid(row=0,column=0, pady=10)



# Button
button_frame = customtkinter.CTkFrame(master=app,fg_color='#f2f2f2')
button_frame.grid(row=2,column=0)

convert_button = customtkinter.CTkButton(master=button_frame, text="Convert", fg_color='black') # currently the button won't do anything, add functionality in the last argument 
# # convert_button.place(relx=0.5,rely=0.9,anchor=tkinter.CENTER)
convert_button.grid(row=1,column=1,pady=70)



app.mainloop()


# 23 June 2026
# Just finished the basic GUI and the file opening architecture. So now we need to bring it all together, link the gui to the architecture 
# also just realised i might have saved my stuff incorrectly by putting it in the venv folder, might be worth trying to actually check if they should be in there or not, otherwise i don't think they actually get saved to github