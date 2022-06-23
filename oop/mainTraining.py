import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = "hello world")
label2 = tkinter.Label(main_window, text = "Label2")

label1.pack()
label2.pack()

main_window.mainloop()
