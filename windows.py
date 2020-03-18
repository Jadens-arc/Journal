import tkinter as tk
from tkinter import END
from journal import Journal

journal = Journal()

style = {
    'title': ('Helvetica', 30),
    'body': ('Helvetica', 12)
}

def publish():
    title = titleEnt.get()
    body = bodyEnt.get('1.0', END)
    journal.newEntry(title, body)

root = tk.Tk()
root.title('Jadens Journal')
root.geometry('550x320')
root.config(bg = 'white')

menu = tk.Menu(root)
menu.add_command(label = 'Publish', command = publish)
menu.add_command(label = 'Delete')
menu.add_command(label = 'See Journal')

titleEnt = tk.Entry(root, bg = 'light grey')
titleEnt.config(font=style['title'])
titleEnt.insert(0, 'Today Something Happened...')
titleEnt.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.15)

bodyEnt = tk.Text(root, bg = 'light grey')
bodyEnt.config(font=style['body'])
bodyEnt.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.8)

root.config(menu = menu)
root.mainloop()