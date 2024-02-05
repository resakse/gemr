# Python program to create a basic form
# GUI application using the customtkinter module
from datetime import datetime

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

now = datetime.now()

# Sets the appearance of the window
# Supported modes : Light, Dark, System
# "System" sets the appearance mode to
# the appearance mode of the system
ctk.set_appearance_mode("System")

# Sets the color of the widgets in the window
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("blue")

# Dimensions of the window
appWidth, appHeight = 800, 600

# App Class


class App(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        main_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.grid(row=0, column=0, padx=10, pady=10)
        # Sets the title of the window to "App"
        self.title("Pendaftaran Radiologi")
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{appWidth}x{appHeight}")
        self.style = ttk.Style()
        self.tar = ctk.StringVar()
        self.harini = tk.StringVar()
        self.harini.set(now.strftime('%d-%m-%Y %H:%M'))
        self.style.theme_use('clam')  # -> uncomment this line if the styling does not work
        self.style.configure('my.DateEntry',
                             # fieldbackground='lightblue',
                             background=ctk.ThemeManager.theme["CTkButton"]["fg_color"][1],
                             foreground=ctk.ThemeManager.theme["CTkEntry"]["text_color"],
                             # arrowcolor=ctk.ThemeManager.theme["CTkButton"]["fg_color"],
                             headersbackground=ctk.ThemeManager.theme["CTkButton"]["fg_color"],
                             selectbackground='lightblue')

        self.tarikhLabel = ctk.CTkLabel(master=main_frame,
                                        text="Tarikh")
        self.tarikhLabel.grid(row=0, column=0,
                              padx=20, pady=20,
                              sticky="ew")

        # Name Entry Field
        self.tarikh = ctk.CTkEntry(master=main_frame, textvariable=self.harini)
        # self.tarikh = DateEntry(master=main_frame, style='my.DateEntry', locale='ms_MY', textvariable=self.tar)
        self.tarikh.grid(row=0, column=1,
                          pady=20, sticky="ew")

        # Age Label
        self.noxrayLabel = ctk.CTkLabel(master=main_frame, text="No. X-Ray")
        self.noxrayLabel.grid(row=0, column=2,
                               pady=20,
                              sticky="ew")

        # Age Entry Field
        self.noxray = ctk.CTkEntry(master=main_frame,
                                   placeholder_text="KKP2400001")
        self.noxray.grid(row=0, column=3,
                         columnspan=1,
                         pady=20, sticky="ew")

        self.nricLabel = ctk.CTkLabel(master=main_frame, text="NRIC")
        self.nricLabel.grid(row=0, column=4,
                              pady=20,
                              sticky="ew")

        # Age Entry Field
        self.nric = ctk.CTkEntry(master=main_frame,
                                   placeholder_text="791113111111")
        self.nric.grid(row=0, column=5,
                         columnspan=1,
                         pady=20, sticky="ew")

        self.umurLabel = ctk.CTkLabel(master=main_frame, text="Umur")
        self.umurLabel.grid(row=2, column=0,
                            padx=10, pady=20,
                            sticky="ew")

        # Age Entry Field
        self.umur = ctk.CTkEntry(master=main_frame, placeholder_text="24")
        self.umur.grid(row=2, column=1,
                       columnspan=1,
                       pady=20, sticky="ew")
        # Gender Label
        self.genderLabel = ctk.CTkLabel(master=main_frame,
                                        text="Jantina")
        self.genderLabel.grid(row=2, column=2,
                              padx=20, pady=20,
                              sticky="ew")

        # Gender Radio Buttons
        self.genderVar = tk.StringVar(value="L")

        self.maleRadioButton = ctk.CTkRadioButton(master=main_frame,
                                                  text="Lelaki",
                                                  variable=self.genderVar,
                                                  value="L")
        self.maleRadioButton.grid(row=2, column=3,
                                  padx=20, pady=20,
                                  sticky="ew")

        self.femaleRadioButton = ctk.CTkRadioButton(master=main_frame,
                                                    text="Perempuan",
                                                    variable=self.genderVar,
                                                    value="P")
        self.femaleRadioButton.grid(row=2, column=4,
                                    padx=20, pady=20,
                                    sticky="ew")

        # Choice Label
        self.choiceLabel = ctk.CTkLabel(master=main_frame,
                                        text="Choice")
        self.choiceLabel.grid(row=3, column=0,
                              padx=20, pady=20,
                              sticky="ew")

        # Choice Check boxes
        self.checkboxVar = tk.StringVar(value="Choice 1")

        self.choice1 = ctk.CTkCheckBox(master=main_frame,
                                       text="choice 1",
                                       variable=self.checkboxVar,
                                       onvalue="choice1", offvalue="c1")
        self.choice1.grid(row=3, column=1,
                          padx=20, pady=20,
                          sticky="ew")

        self.choice2 = ctk.CTkCheckBox(master=main_frame,
                                       text="choice 2",
                                       variable=self.checkboxVar,
                                       onvalue="choice2",
                                       offvalue="c2")
        self.choice2.grid(row=3, column=2,
                          padx=20, pady=20,
                          sticky="ew")

        # Occupation Label
        self.occupationLabel = ctk.CTkLabel(master=main_frame,
                                            text="Ambulatori")
        self.occupationLabel.grid(row=4, column=0,
                                  padx=20, pady=20,
                                  sticky="ew")

        # Occupation combo box
        self.occupationOptionMenu = ctk.CTkOptionMenu(master=main_frame,
                                                      values=["Berjalan",
                                                              "Wheelchair",
                                                              "Troli"])
        self.occupationOptionMenu.grid(row=4, column=1,
                                       padx=20, pady=20,
                                       columnspan=2, sticky="ew")

        # Generate Button
        self.generateResultsButton = ctk.CTkButton(master=main_frame,
                                                   text="Generate Results",
                                                   command=self.generateResults)
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=2, padx=20,
                                        pady=20, sticky="ew")

        # Text Box
        self.displayBox = ctk.CTkTextbox(master=main_frame,
                                         width=200,
                                         height=100)
        self.displayBox.grid(row=6, column=0,
                             columnspan=4, padx=20,
                             pady=20, sticky="nsew")

    # This function is used to insert the
    # details entered by users into the textbox
    def generateResults(self):
        self.displayBox.delete("0.0", "200.0")
        text = self.createText()
        self.displayBox.insert("0.0", text)

    # This function is used to get the selected
    # options and text from the available entry
    # fields and boxes and then generates
    # a prompt using them
    def createText(self):
        checkboxValue = ""

        # .get() is used to get the value of the checkboxes and entryfields

        if self.choice1._check_state and self.choice2._check_state:
            checkboxValue += self.choice1.get() + " and " + self.choice2.get()
        elif self.choice1._check_state:
            checkboxValue += self.choice1.get()
        elif self.choice2._check_state:
            checkboxValue += self.choice2.get()
        else:
            checkboxValue = "none of the available options"

        # Constructing the text variable
        text = f"{self.tar.get()}\n"
        text += f"{self.genderVar.get()} currently a {self.occupationOptionMenu.get()}"

        return text


if __name__ == "__main__":
    app = App()
    # Used to run the application
    app.mainloop()
