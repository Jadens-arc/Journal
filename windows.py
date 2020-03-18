import tkinter as tk
from tkinter import END, INSERT
from journal import Journal

journal = Journal() # declared new Journal from Journal file 

# Sylesheet for managing fonts, background colors, and the alike
style = {
    # window and widget styling
    'background': 'white',
    'foreground': 'light grey',

    # text styling
    'title': ('Helvetica', 30),
    'body': ('Helvetica', 12)
}

# gets data from all text entries and write to journal file
def publish():
    title = titleEnt.get()
    body = bodyEnt.get('1.0', END)
    journal.newEntry(title, body)

def seeJournal():
    journalWin = tk.Tk()
    journalWin.title('Jadens Journal')
    journalWin.geometry('550x320')

    menu = tk.Menu(journalWin)
    menu.add_command(label='Save Changes')

    body = tk.Text(journalWin, bg=style['foreground'])
    body.insert(INSERT, str(journal))
    body.place(relx=0, rely=0, relwidth=1, relheight=1)

    journalWin.config(menu=menu)
    journalWin.mainloop()

root = tk.Tk()
root.title('New Entry')
root.geometry('550x320')
root.config(bg=style['background'])

menu = tk.Menu(root)
menu.add_command(label='Publish', command=publish)
menu.add_command(label='See Journal', command=seeJournal)

titleEnt = tk.Entry(root, bg=style['foreground'])
titleEnt.config(font=style['title'])
titleEnt.insert(0, 'Today Something Happened...')
titleEnt.place(relx=0, rely=0, relwidth=1, relheight=0.15)

bodyEnt = tk.Text(root, bg=style['foreground'])
bodyEnt.config(font=style['body'])
bodyEnt.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)

root.config(menu=menu)
root.mainloop()