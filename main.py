# Python program to create a basic form
# GUI application using the customtkinter module
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

# Sets the appearance of the window
# Supported modes : Light, Dark, System
# "System" sets the appearance mode to
# the appearance mode of the system
ctk.set_appearance_mode("System")

# Sets the color of the widgets in the window
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("blue")

# Dimensions of the window
appWidth, appHeight = 800, 700

# App Class


class App(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets the title of the window to "App"
        self.title("GUI Application")
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{appWidth}x{appHeight}")
        self.style = ttk.Style()
        self.tar = ctk.StringVar()
        self.style.theme_use('clam')  # -> uncomment this line if the styling does not work
        self.style.configure('my.DateEntry',
                             # fieldbackground='lightblue',
                             background=ctk.ThemeManager.theme["CTkButton"]["fg_color"][1],
                             foreground=ctk.ThemeManager.theme["CTkEntry"]["text_color"],
                             # arrowcolor=ctk.ThemeManager.theme["CTkButton"]["fg_color"],
                             headersbackground=ctk.ThemeManager.theme["CTkButton"]["fg_color"],
                             selectbackground='lightblue')

        self.tarikhLabel = ctk.CTkLabel(self,
                                        text="Tarikh")
        self.tarikhLabel.grid(row=0, column=0,
                              padx=20, pady=20,
                              sticky="ew")

        # Name Entry Field
        self.tarikh = DateEntry(style='my.DateEntry', locale='ms_MY', textvariable=self.tar)
        # self.tarikh.pack(padx=20)
        # self.tarikh = ctk.CTkEntry(self,
        #                               placeholder_text="Teja")
        self.tarikh.grid(row=0, column=1,
                         padx=20, pady=20, sticky="ew")

        # Age Label
        self.noxrayLabel = ctk.CTkLabel(self, text="No. X-Ray")
        self.noxrayLabel.grid(row=0, column=2,
                              padx=10, pady=20,
                              sticky="ew")

        # Age Entry Field
        self.noxray = ctk.CTkEntry(self,
                                   placeholder_text="18")
        self.noxray.grid(row=0, column=3,
                         columnspan=3, padx=20,
                         pady=20, sticky="ew")

        # Gender Label
        self.genderLabel = ctk.CTkLabel(self,
                                        text="Gender")
        self.genderLabel.grid(row=2, column=0,
                              padx=20, pady=20,
                              sticky="ew")

        # Gender Radio Buttons
        self.genderVar = tk.StringVar(value="Prefer not to say")

        self.maleRadioButton = ctk.CTkRadioButton(self,
                                                  text="Male",
                                                  variable=self.genderVar,
                                                  value="He is")
        self.maleRadioButton.grid(row=2, column=1,
                                  padx=20, pady=20,
                                  sticky="ew")

        self.femaleRadioButton = ctk.CTkRadioButton(self,
                                                    text="Female",
                                                    variable=self.genderVar,
                                                    value="She is")
        self.femaleRadioButton.grid(row=2, column=2,
                                    padx=20, pady=20,
                                    sticky="ew")

        self.noneRadioButton = ctk.CTkRadioButton(self,
                                                  text="Prefer not to say",
                                                  variable=self.genderVar,
                                                  value="They are")
        self.noneRadioButton.grid(row=2, column=3, padx=20,
                                  pady=20, sticky="ew")

        # Choice Label
        self.choiceLabel = ctk.CTkLabel(self,
                                        text="Choice")
        self.choiceLabel.grid(row=3, column=0,
                              padx=20, pady=20,
                              sticky="ew")

        # Choice Check boxes
        self.checkboxVar = tk.StringVar(value="Choice 1")

        self.choice1 = ctk.CTkCheckBox(self,
                                       text="choice 1",
                                       variable=self.checkboxVar,
                                       onvalue="choice1", offvalue="c1")
        self.choice1.grid(row=3, column=1,
                          padx=20, pady=20,
                          sticky="ew")

        self.choice2 = ctk.CTkCheckBox(self,
                                       text="choice 2",
                                       variable=self.checkboxVar,
                                       onvalue="choice2",
                                       offvalue="c2")
        self.choice2.grid(row=3, column=2,
                          padx=20, pady=20,
                          sticky="ew")

        # Occupation Label
        self.occupationLabel = ctk.CTkLabel(self,
                                            text="Occupation")
        self.occupationLabel.grid(row=4, column=0,
                                  padx=20, pady=20,
                                  sticky="ew")

        # Occupation combo box
        self.occupationOptionMenu = ctk.CTkOptionMenu(self,
                                                      values=["Student",
                                                              "Working Professional"])
        self.occupationOptionMenu.grid(row=4, column=1,
                                       padx=20, pady=20,
                                       columnspan=2, sticky="ew")

        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                                   text="Generate Results",
                                                   command=self.generateResults)
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=2, padx=20,
                                        pady=20, sticky="ew")

        # Text Box
        self.displayBox = ctk.CTkTextbox(self,
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
