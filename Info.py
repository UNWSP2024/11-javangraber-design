# Programmer: Javan Graber
# Date: 4/17/26
# Program #2: Information Button

import tkinter
import tkinter.messagebox

# Create the Gui Class
class MYGUI:
    # Create the Initializer
    def __init__(self):
        # Create the main window, the title, the information button, and the quit button
        self.main_window = tkinter.Tk()

        self.main_window.title("Information")

        self.inf_button = tkinter.Button(self.main_window, text="Show Info", command=self.display_info,
                                         borderwidth=15, relief="raised")

        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy,
                                          borderwidth=15, relief="raised")

        # Call the pack method for both buttons and enter the loop
        self.inf_button.pack(ipadx=40, ipady=40, padx=40, pady=40)
        self.quit_button.pack(ipadx=40, ipady=40, padx=40, pady=40)

        tkinter.mainloop()

    # Create the function that displays the information
    def display_info(self):
        tkinter.messagebox.showinfo("Info Response", "Javan Graber, 58934 Random Avenue, Farmington,"
                                    " MN 55962")

if __name__ == "__main__":
    mygui = MYGUI()
