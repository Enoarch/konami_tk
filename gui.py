#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# code by Thomas RENAUD - 11/2018

from tkinter import *
from tkinter.messagebox import *

class Main_gui(Tk):
    """
    CLASS:  basic tkinter Interface with an hidden Konami code

    """

    def __init__(self):
        Tk.__init__(self)

        # Tkinter window definition
        w = 500
        h = 150

        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the tkinter windows and where it is placed on the screen
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(width=False, height=False)
        self.bind("<Any-KeyPress>",self.isKonami)

        #KONAMI DEF
        self.konami_code = [38,38,40,40,37,39,37,39,66,65] #Konami code in keykode numero
        self.keyevt_list = [0,0,0,0,0,0,0,0,0,0]

    def isKonami(self, evt):
        """
        Method witch scan key pressed and compare the ten last key pressed to the konami list
        If the result is true then we show a popup

        :param evt:
        :return: Nothing
        """
        self.keyevt_list.__delitem__(0) #we supp the firt element of the list
        self.keyevt_list.append(evt.keycode) #we add the new evt keykode at the end of the list

        #comparaison

        if self.keyevt_list == self.konami_code:
            showinfo("!! KONAMI SECRET !! ","Fine, you are a real Geek, you find my Konami secret O_o")


if __name__ == "__main__":
    app = Main_gui()
    app.mainloop()