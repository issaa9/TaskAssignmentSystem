from tkinter import *
from tkinter import ttk


class tree:
    def __init__(self):
        root = Tk()
        root.geometry("500x500")


        self.my_tree = ttk.Treeview(root)

        #define columns
        self.my_tree['columns'] = ("Name","ID","Favourite pizza")

        #format columns
        self.my_tree.column("#0", width=120,minwidth=25)#set to 0
        self.my_tree.column("Name",anchor=W,width=120)
        self.my_tree.column("ID",anchor=CENTER,width=80)
        self.my_tree.column("Favourite pizza",anchor=W,width=120)

        #create headings
        self.my_tree.heading("#0",text="Label", anchor=W)
        self.my_tree.heading("Name",text="Name", anchor=W)
        self.my_tree.heading("ID",text="ID", anchor=CENTER)
        self.my_tree.heading("Favourite pizza",text="Favourite pizza", anchor=W)

        #add data
        self.my_tree.insert(parent='',index='end',iid=0,text="Parent",values=("John",1,"pepperoni"))

        self.my_tree.pack()
                   





app = tree()
app.mainloop()
