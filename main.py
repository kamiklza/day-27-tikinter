import tkinter


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Lable
my_label = tkinter.Label(text="Welcome")
my_label.pack()


def change_text():
    my_label["text"] = input.get()
    

#Button
button = tkinter.Button(text="Click", command=change_text)
button.pack()


#Entry
input = tkinter.Entry(width=10)
input.pack()









window.mainloop()