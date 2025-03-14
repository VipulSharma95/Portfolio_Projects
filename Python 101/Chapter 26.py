import math
import tkinter as tk

class App:

    def __init__(self, parent):
        frame = tk.Frame(parent)
        frame.pack()

        btn22 = tk.Button(frame, text="22",command = lambda: self.printNum(22))
        btn22.pack(side=tk.LEFT)
        btn66 = tk.Button(frame,text="66",command = lambda: self.printNum(66))
        btn66.pack(side=tk.LEFT)

        quitBtn = tk.Button(frame,text="QUIT",fg="Red",command=frame.quit)
        quitBtn.pack(side=tk.LEFT)

    def printNum(self,num):
        print("You pressed the %s button" % num)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()


# = lambda x: math.sqrt(x)
#print(square_rt(64))
