import tkinter

window = tkinter.Tk()
window.title('Mile to kilometers converter')
window.minsize(width=300, height=500)
window.config(padx=20, pady=20)

def button_clicked():
  result = input.get()

  result = float(result)*1.6
  label3.config(text=result)

#Label
my_label = tkinter.Label(text='Miles', font=('Arial',15, "italic"))
my_label.grid(column=2, row=0)

label2 = tkinter.Label(text='is equal to', font=('Arial',15, "italic"))
label2.grid(column=0, row=1)

label4 = tkinter.Label(text='Km', font=('Arial',15, "italic"))
label4.grid(column=2, row=1)

label3 = tkinter.Label(text='0', font=('Arial',15, "italic"))
label3.grid(column=1, row=1)

#Button
button = tkinter.Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()