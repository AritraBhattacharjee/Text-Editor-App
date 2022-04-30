"""
    Author: Aritra Bhattacharjee
    Date of Working: 29.04.2022 to 02.05.2022
    Tech Stack: Python, Tkinter.
    About: A python based text editor application
"""
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
class TextEditor(Tk):

    def __init__(self):
        super().__init__()
        self.title("Text Editor")
        self.geometry("644x688")
        self.iconbitmap("icon2.ico")

        # Adding text area
        self.TextArea = Text(self, font="lucida 13")
        self.TextArea.pack(fill=BOTH,expand=True)
        self.file = None
        # adding Icon
        photo = PhotoImage(file="icon2.ico")
        # photo = PhotoImage(file="icon.png")
        self.iconphoto(False,photo)
        # Menu Bar
        MenuBar = Menu(self)
        #File Meny
        FileMenu = Menu(MenuBar,tearoff=0)
        FileMenu.add_command(label = "New",command=self.newFile)
        FileMenu.add_command(label="Open",command=self.openFile)
        FileMenu.add_command(label="Save",command=self.saveFile)
        FileMenu.add_separator()
        FileMenu.add_command(label="Exit",command=self.quitApp)
        MenuBar.add_cascade(label="File",menu=FileMenu)
        self.config(menu=MenuBar)
    
        # Edit Menu
        EditMenu = Menu(MenuBar,tearoff=0)
        EditMenu.add_command(label="Cut",command=self.cut)
        EditMenu.add_command(label="Copy",command=self.copy)
        EditMenu.add_command(label="Paste",command=self.paste)
        MenuBar.add_cascade(label="Edit",menu=EditMenu)
        self.config(menu=MenuBar)

        # help Menu
        HelpMenu = Menu(MenuBar,tearoff=0)
        HelpMenu.add_command(label="About",command=self.about)
        MenuBar.add_cascade(label="Help",menu=HelpMenu)
        self.config(menu=MenuBar)

        # Adding Scrool Bar
        Scroll = Scrollbar(self.TextArea)
        Scroll.pack(side=RIGHT,fill=Y)
        Scroll.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=Scroll.set)

    def newFile(self):
        # global file
        self.title("Untitled - Text Editor")
        self.file = None
        self.TextArea.delete(1.0,END)


    def openFile(self):
        # global file
        self.file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.file == "":
            self.file = None
        else:
            self.title(os.path.basename(self.file)+ " - Text Editor")
            self.TextArea.delete(1.00,END)
            f = open(self.file,"r")
            self.TextArea.insert(1.0,f.read())
            f.close()

    def saveFile(self):
        # global file
        if self.file == None:
            
            self.file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            if self.file =="":
                self.file = None
            else:
                # save a new file
                f = open(self.file,"w")
                f.write(self.TextArea.get(1.0,END))
                f.close()

                self.title(os.path.basename(self.file)+"-Text Editor")
                # print("File Saved")
        else:
            # save the file
            f = open(self.file,"w")
            f.write(self.TextArea.get(1.0,END))
            f.close()

    def quitApp(self):
        self.destroy()
    def cut(self):
        self.TextArea.event_generate(("<<Cut>>"))

    def copy(self):
        self.TextArea.event_generate(("<<Copy>>"))
        
    def paste(self):
        self.TextArea.event_generate(("<<Paste>>"))
        
    def about(self):
        showinfo("Text Editor","A Text Editor  by Aritra Bhattacharjee")


if __name__ == '__main__':
    
    obj = TextEditor()
    obj.mainloop()
    