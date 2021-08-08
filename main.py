import tkinter


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Lable
my_label = tkinter.Label(text="Welcome")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)


def change_text():
    my_label["text"] = input_text.get()


#Button
button = tkinter.Button(text="Click", command=change_text)
button.grid(column=1, row=1)
button.config(padx=20, pady=20)


#Entry
input_text = tkinter.Entry(width=10)
input_text.grid(column=3, row=2)
input_text.grid(padx=10, pady=10)



#New Button
new_button = tkinter.Button(text="Click")
new_button.grid(column=2, row=0)









window.mainloop()