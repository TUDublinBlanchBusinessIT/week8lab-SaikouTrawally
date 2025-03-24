from tkinter import *


class myFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A Simple GUI")

        self.label1 = Label(master, text="Firstname: ")
        self.label1.pack()

        self.entry1 = Entry()
        self.entry1.pack()

        self.label2 = Label(master, text="Surname: ")
        self.label2.pack()

        self.entry2 = Entry()
        self.entry2.pack()

        self.label3 = Label(master, text="Date of Birth: ")
        self.label3.pack()

        self.entry3 = Entry()
        self.entry3.pack()

        self.label4 = Label(master, text="Member Type: ")
        self.label4.pack()

        self.entry4 = Entry()
        self.entry4.pack()

        self.close_button = Button(master, text="Insert Into DB", command=self.hello)
        self.close_button.pack()

        self.close_button = Button(master, text="Print All Members", command=self.hello)
        self.close_button.pack()

        self.close_button = Button(master, text="Closer", command=self.hello)
        self.close_button.pack()
