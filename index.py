#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Tk, RIGHT, LEFT, BOTH, RAISED, CENTER
from tkinter.ttk import Frame, Button, Style, Label
import json
import requests
import subprocess


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.quote = "I was supposed to be a cool quote . But then internet abandoned me !"
        self.author = "Alisha"
        #self.getQuote()
        self.initUI()

    def initUI(self):

        self.parent.title("Wola!!! I automate")
        self.style = Style()
        self.style.theme_use("alt")

        # Styling
        self.style.configure('.', font=('Helvetica', 12), background="#300A24")
        self.style.configure(
            "PW.TLabel", foreground="#fff", background="#300A24", padding=20, justify=CENTER, wraplength="350")
        self.style.configure(
            "Medium.TButton", foreground="#300A24", background="#fff", borderwidth=0, padding=8, font=('Helvetica', 9))
        # Styling Ends

        quoteLabel = Label(self, text=self.quote, style="PW.TLabel")
        quoteLabel.pack()
        authorLabel = Label(self, text=self.author, style="PW.TLabel")
        authorLabel.pack()

        self.pack(fill=BOTH, expand=True)

        closeButton = Button(self, text="Close This",
                             style="Medium.TButton", command=self.parent.quit)
        closeButton.pack(side=RIGHT)
        okButton = Button(
            self, text="GitHub", style="Medium.TButton", command=self.btnOneFn)
        okButton.pack(side=RIGHT)
        okButton = Button(self, text="Open Project List",
                          style="Medium.TButton", command=self.btnTwoFn)
        okButton.pack(side=RIGHT)
        okButton = Button(self, text="Login to CET Wifi",
                          style="Medium.TButton", command=self.btnThreeFn)
        okButton.pack(side=RIGHT)
        okButton = Button(self, text="Saavn",
                          style="Medium.TButton", command=self.btnFourFn)
        okButton.pack(side=RIGHT)

    def hello(self):
        print("Print Hello")

    def getQuote(self):
        j = json.loads(requests.get(
            "http://quotes.stormconsultancy.co.uk/random.json").text)
        self.quote = j["quote"]
        self.author = j["author"]

    def btnOneFn(self):
        subprocess.Popen(
            ['firefox', "https://www.github.com"])

    def btnTwoFn(self):
        subprocess.Popen(
            ['nautilus', "/home/alisha/project"])

    def btnThreeFn(self):
        subprocess.call("python /home/alisha/project/Automating-Working-Env/cet_logn.py", shell="True")

    def btnFourFn(self):
        subprocess.Popen(
            ['firefox', "https://www.saavn.com/"])

def main():

    root = Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()