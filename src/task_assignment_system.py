from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import random
from datetime import date, datetime , time
from tkinter import messagebox


TITLE_FONT = ("Verdana",26)
LARGE_FONT = ("Verdana",20)             #defining constants for font sizes to be used multiple times throughout the code
MEDIUM_FONT = ("Verdana",16)
SMALL_FONT = ("Verdana",14)
MINI_FONT = ("Verdana",12)
TINY_FONT = ("Verdana",10)

date_today = date.today()
str_date_today = date_today.strftime("%d/%m/%y")


class window(tk.Tk):                    #creating a super class to initialise all windows to be used within the code

     def __init__(self):

         tk.Tk.__init__(self)

         #tk.Tk.config(self,bg='black')

         tk.Tk.wm_title(self, "Issa's Project")
         tk.Tk.geometry(self,"800x600")
         tk.Tk.resizable(self,False,False)


         container = Frame(self)          #creating a variable called container which is a frame for the window
         container.pack(side="top", fill="both", expand=False)         #packing container to cover the whole window and expand as the window is enlarged
         container.grid_rowconfigure(0, weight=1)
         container.grid_columnconfigure(0, weight=1)

         self.create_database()
            

         self.frames = {}                         #creating an empty dictionary to store all frames for all pages            

         for F in (StartPage, ManagerLogin, WorkerLogin, ManagerPage,WorkerPage):

              frame = F(container,self)

              self.frames[F] = frame

              frame.grid(row = 0, column = 0, sticky="nesw")

         self.show_frame(StartPage)

         
         self.SetUpMenubar(container)
             
         self.display_date()

     def quit(self):
         get_exit = messagebox.askyesno(title="Quit",message="Are you sure you want to quit?")
         if get_exit > 0:
            tk.Tk.destroy(self)
               

     def SetUpMenubar(self,container):
         self.menubar = tk.Menu(container)
         self.filemenu = tk.Menu(self.menubar, tearoff = False)
         self.filemenu.add_command(label="Close Program",command= self.quit)
         self.menubar.add_cascade(label="File",menu = self.filemenu)
         tk.Tk.config(self,menu = self.menubar)

         
     def show_frame(self,PageName):               #method to show a frame
         frame = self.frames[PageName]             #assigns the page name which gets passed in to the variable called frame so it can be shown
         frame.tkraise()                           #built in function which raises the chosen frame to the top so only that frame is in use
         

     def create_database(self):
         new_path = "Project Database.db"
         connection = sqlite3.connect(new_path)
         data = connection.cursor()
         data.execute("""CREATE TABLE IF NOT EXISTS "Managers"(
         "ManagerID" TEXT PRIMARY KEY NOT NULL,
         "Username" TEXT,
         "Password" TEXT
    );""")
         data.execute("""CREATE TABLE IF NOT EXISTS "Workers"(
         "WorkerID" TEXT PRIMARY KEY NOT NULL,
         "Username" TEXT,
         "Password" TEXT
    );""")
         data.execute("""CREATE TABLE IF NOT EXISTS "Tasks"(
         "TaskID" TEXT PRIMARY KEY NOT NULL,
         "TaskType" TEXT,
         "Object" TEXT,
         "Quantity" TEXT,
         "Info" TEXT,
         "DateAssigned" DATETIME,
         "DateCompleted" DATETIME,
         "WorkerID" TEXT,
         "ManagerID" TEXT,
         FOREIGN KEY("WorkerID") REFERENCES "Workers"("WorkerID"),
         FOREIGN KEY("ManagerID") REFERENCES "Managers"("ManagerID")
    );""")
           
         data.execute("""CREATE TABLE IF NOT EXISTS "Details"(
         "WorkerID" TEXT PRIMARY KEY NOT NULL,
         "FirstName" TEXT,
         "LastName" TEXT,
         "Age" INTEGER,
         "YearsWorked" INTEGER,
         "JobRole" TEXT,
         FOREIGN KEY("WorkerID") REFERENCES "Workers"("WorkerID")
    );""")
         connection.commit()

         data.execute("""SELECT * FROM Managers""")
         my_list = data.fetchall()

         if len(my_list) == 0:

             data.execute("""INSERT INTO Managers(ManagerID,Username,Password)
     Values("001","Manager_1","password")  
     """)                                                                                  #8_x4zAFBg
             data.execute("""INSERT INTO Managers(ManagerID,Username,Password)
     Values("002","Manager_2","Password")                                               
     """)                                                                                  #{Cy:2?MC>
             data.execute("""INSERT INTO Managers(ManagerID,Username,Password)
     Values("003","Manager_3","L4#g)tsD&")  
     """)

             data.execute("""INSERT INTO Workers(WorkerID,Username,Password)
     Values("001","Worker_1","password")""")                                              
                                                                                          #md7P@F)7
             data.execute("""INSERT INTO Workers(WorkerID,Username,Password)
     Values("002","Worker_2","{mz&4=P&")""")

             data.execute("""INSERT INTO Workers(WorkerID,Username,Password)
     Values("003","Worker_3","6^Te{`7D")""")

             data.execute("""INSERT INTO Workers(WorkerID,Username,Password)
     Values("004","Worker_4","J>w$5Gjy")""")

             data.execute("""INSERT INTO Workers(WorkerID,Username,Password)
     Values("005","Worker_5","Q#e<2Dda")""")

             data.execute("""INSERT INTO Workers(WorkerID,Username,Password)
     Values("006","Worker_6","$Dw4vcC@")""")

             data.execute("""INSERT INTO Workers(WorkerID,Username,Password)
     Values("007","Worker_7","E(;5x*6K")""")

             data.execute("""INSERT INTO Workers(WorkerID,Username,Password)
     Values("008","Worker_8",".8UW#mb4")""")
                 
             connection.commit()



     def display_date(self):
         date_label = Label(self, text = str_date_today, font = MEDIUM_FONT)
         date_label.place(x=6,y=3)
        
        

class StartPage(tk.Frame):                        #class for the starting page

    def __init__(self, parent, controller):       #method to initialise the class
        Frame.__init__(self,parent)            #creates the frame

        self.SetCurrentWorkerID()
        
        self.DefineWidgets(controller)
                                                  #creating a label as a title for the page and setting the font to the constant already defined at the start
        self.TitleLabel.place(y=25,x=305)                                      #creating a button to access the managers login page

        DetailsComplete = self.CheckDetails()
        if DetailsComplete == False:
            self.DetailsButton.pack(pady=90)
        else:
             self.ManagerButton.place(x=330,y=175)                                                                                        #creating a button to access the workers login page
             self.WorkerButton.place(x=330,y=275)

        

    def DefineWidgets(self,controller):
        self.TitleLabel = Label(self, text="Home Page", font=TITLE_FONT)
        self.DetailsButton = ttk.Button(self, text="Input Worker Details",width = "20", command =lambda: self.GetDetails())
        self.ManagerButton = ttk.Button(self, text="Managers",width = "20", command =lambda: controller.show_frame(ManagerLogin))
        self.WorkerButton = ttk.Button(self, text="Workers",width = "20", command =lambda: controller.show_frame(WorkerLogin))

        FirstName = ""                                                          #creating the variables and assigning them empty strings
        LastName = ""
        Age = ""
        YearsWorked = ""
        JobRole = ""

        self.EnterDetailsLabel = Label(self, text="Enter Details Below:", font=MEDIUM_FONT)

        self.FirstNameLabel = Label(self, text="First Name", font=SMALL_FONT)
        self.FirstNameEntry = ttk.Entry(self, textvariable = FirstName)

        self.LastNameLabel = Label(self, text="Last Name", font=SMALL_FONT)
        self.LastNameEntry = ttk.Entry(self, textvariable = LastName)

        self.AgeLabel = Label(self, text="Age", font=SMALL_FONT)
        self.AgeEntry = ttk.Entry(self, textvariable = Age)

        self.YearsWorkedLabel = Label(self, text="Years Worked", font=SMALL_FONT)
        self.YearsWorkedEntry = ttk.Entry(self, textvariable = YearsWorked)

        self.JobRoleLabel = Label(self, text="Job Role", font=SMALL_FONT)
        self.JobRoleEntry = ttk.Entry(self, textvariable = JobRole)

        self.SaveButton = ttk.Button(self, text="Save", command =lambda: self.SaveDetails())

        self.ErrorLabel = Label(self, text="All Fields Must Be Filled In ",font=MINI_FONT, fg = "red")

        self.WidgetList = [self.EnterDetailsLabel,self.FirstNameLabel,self.FirstNameEntry,self.LastNameLabel,
                  self.LastNameEntry,self.AgeLabel,self.AgeEntry,self.YearsWorkedLabel,self.YearsWorkedEntry,
                  self.JobRoleLabel,self.JobRoleEntry,self.SaveButton]

    def ResetPage(self):
        for x in self.WidgetList:
              x.forget()
               

    def GetDetails(self):
        DetailsComplete = self.CheckDetails()
        if DetailsComplete == False:
           self.EnterDetails()
        else:
             self.ResetPage()
             self.DetailsButton.forget()
             self.ManagerButton.place(x=330,y=175)                                                                                        #creating a button to access the workers login page
             self.WorkerButton.place(x=330,y=275)

    def CheckDetails(self):
        Complete = True
        try:
            new_path = "Project Database.db"
            connection = sqlite3.connect(new_path)
            data = connection.cursor()
            data.execute("""SELECT * FROM Details WHERE WorkerID LIKE "008" """)
            details = data.fetchall()
            for i in range(0,6):
                  if details[0][i] == None:
                     Complete = False
        except:
               Complete = False
                 
        return Complete


    def EnterDetails(self):
        self.IDLabel = Label(self, text="WorkerID: "+self.CurrentWorkerID,font=MINI_FONT, fg = "blue")
        self.IDLabel.place(x=338,y=180)
        for x in self.WidgetList:
              x.pack()


    def SaveDetails(self):
        FirstName = self.FirstNameEntry.get()                                                        #creating the variables and assigning them empty strings
        LastName = self.LastNameEntry.get() 
        Age = self.AgeEntry.get() 
        YearsWorked = self.YearsWorkedEntry.get() 
        JobRole = self.JobRoleEntry.get()

        self.FirstNameEntry.delete(0,20)
        self.LastNameEntry.delete(0,20)
        self.AgeEntry.delete(0,20)
        self.YearsWorkedEntry.delete(0,20)
        self.JobRoleEntry.delete(0,20)

        Valid = True

        if FirstName == "" or LastName == "" or Age ==  "" or YearsWorked ==  "" or JobRole == "":
           Valid = False
              
        if Valid == False:
           self.ErrorLabel.pack()
        else:
             self.ErrorLabel.forget()
             self.IDLabel.place_forget()
             self.StoreDetails(FirstName,LastName,Age,YearsWorked,JobRole)


    def SetCurrentWorkerID(self):
        try:
             NewPath = "Project Database.db"
             connection = sqlite3.connect(NewPath)
             data = connection.cursor()
             data.execute("""SELECT WorkerID FROM Details ORDER BY WorkerID DESC LIMIT 1""")
             self.CurrentWorkerID = str(data.fetchall())
             self.CurrentWorkerID = self.CurrentWorkerID[3] + self.CurrentWorkerID[4] + self.CurrentWorkerID[5]
             self.CurrentWorkerID = int(self.CurrentWorkerID) + 1
             self.CurrentWorkerID = str(self.CurrentWorkerID)
             if len(self.CurrentWorkerID) == 1:
                self.CurrentWorkerID = "00" + self.CurrentWorkerID
             elif len(self.CurrentWorkerID) == 2:
                  self.CurrentWorkerID = "0" + self.CurrentWorkerID  
        except:
             self.CurrentWorkerID = "001"

             
    def IncrementCurrentWorkerID(self):
        self.CurrentWorkerID = (int(self.CurrentWorkerID)+1)
        self.CurrentWorkerID = str(self.CurrentWorkerID)
        if len(self.CurrentWorkerID) == 1:
           self.CurrentWorkerID = "00" + self.CurrentWorkerID
        elif len(self.CurrentWorkerID) == 2:
             self.CurrentWorkerID = "0" + self.CurrentWorkerID

    def StoreDetails(self,FirstName,LastName,Age,YearsWorked,JobRole):
        NewPath = "Project Database.db"
        connection = sqlite3.connect(NewPath)
        data = connection.cursor()
        data.execute("""INSERT INTO Details(WorkerID,FirstName,LastName,Age,YearsWorked,JobRole) Values(?,?,?,?,?,?)"""
                 ,(self.CurrentWorkerID,FirstName,LastName,Age,YearsWorked,JobRole,))
        connection.commit()

        self.IncrementCurrentWorkerID()
        self.GetDetails()
         
             

class ManagerLogin(tk.Frame):                                                                           #class for the manager login page

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        
        self.DefineWidgets(controller)
        
        self.TitleLabel.pack(pady=10,padx=10)

                                                               #button to go back to start page
        self.BackToStartButton.pack()

        Label(self, text= " ").pack()                        #empty labels to create space
        Label(self, text= " ").pack()
        Label(self, text= " ").pack()
        
        self.LoginLabel.pack()

        Label(self, text= " ").pack()

       
        self.UsernameLabel.pack()
        self.UsernameEntry.pack()

        self.PasswordLabel.pack()
        self.PasswordEntry.pack()

        Label(self, text= " ").pack()

        self.LoginButton.pack()

        Label(self, text = "").pack()


    def DefineWidgets(self,controller):
        self.TitleLabel = ttk.Label(self, text="Managers Login Page", font=TITLE_FONT)

        self.BackToStartButton = ttk.Button(self, text="Back To Home Page", command =lambda: self.BackToStart(controller))    #button to go back to start pag
        
        self.LoginLabel = Label(self, text="Enter login details below: ", font=MEDIUM_FONT) 

        username = ""
        password = ""
          
        self.UsernameLabel = Label(self, text="Username ", font=MEDIUM_FONT)  #label and entry box for username
        self.UsernameEntry = ttk.Entry(self, textvariable = username)

        self.PasswordLabel = Label(self, text="Password ", font=MEDIUM_FONT)  #label and entry box for password
        self.PasswordEntry = ttk.Entry(self, textvariable = password)

        self.ErrorLabel = Label(self, text="Incorrect Login Details ",font=MINI_FONT, fg = "red")   #error label to be displayed when login details are incorrect

        self.LoginButton = ttk.Button(self, text = "Login",command =lambda: self.Login(controller))
         
    def BackToStart(self,controller):
        self.ErrorLabel.forget()
        controller.show_frame(StartPage)
         

    def Login(self,controller):   #method to check the login details and allow the user to login if they are corrcet
        username =  self.UsernameEntry.get()                 #fetches the login details that the user entered
        password = self.PasswordEntry.get()
        Valid = self.CheckLoginDetails(username,password)                             #if the previous condition is met valid will be set to True else it is left as False
        if Valid == True:                               
           self.ErrorLabel.pack_forget()                      #remove error label
           controller.show_frame(ManagerPage)               #if valid is True after checking it will display the next page
           global CurrentManagerID
           CurrentManagerID = "00" + str(username[8])
        else:
             self.ErrorLabel.pack()                           #if valid is still False after checking, the error message label is displayed
        self.UsernameEntry.delete(0,10)                       #the entries are deleted
        self.PasswordEntry.delete(0,10)


    def CheckLoginDetails(self,username,password):
        Valid =  False                                #boolean variable to show whether or not the user details are valid  
        try:
             NewPath = "Project Database.db"
             connection = sqlite3.connect(NewPath)
             data = connection.cursor()
             data.execute("""SELECT Username, Password FROM Managers WHERE Username LIKE ? """,(username,))
             Login = data.fetchall()
             CheckUsername = Login[0][0]
             CheckPassword = Login[0][1]
             if CheckUsername == username and CheckPassword == password:    #condition to check that the details are valid and match each other
                Valid = True 
        except:
             Valid =  False
        return Valid

     
class WorkerLogin(tk.Frame):                                                #class for the worker login page

    def __init__(self, parent, controller):            
        Frame.__init__(self,parent)

        self.DefineWidgets(controller)
        
        self.TitleLabel.pack(pady=10,padx=10)

                                                               #button to go back to start page
        self.BackToStartButton.pack()

        Label(self, text= " ").pack()                        #empty labels to create space
        Label(self, text= " ").pack()
        Label(self, text= " ").pack()
        
        self.LoginLabel.pack()

        Label(self, text= " ").pack()

       
        self.UsernameLabel.pack()
        self.UsernameEntry.pack()

        self.PasswordLabel.pack()
        self.PasswordEntry.pack()

        Label(self, text= " ").pack()

        self.LoginButton.pack()

        Label(self, text = "").pack()


    def DefineWidgets(self,controller):
        self.TitleLabel = ttk.Label(self, text="Workers Login Page", font=TITLE_FONT)

        self.BackToStartButton = ttk.Button(self, text="Back To Home Page", command =lambda: self.BackToStart(controller))    #button to go back to start pag
        
        self.LoginLabel = Label(self, text="Enter login details below: ", font=MEDIUM_FONT) 

        username = ""
        password = ""
          
        self.UsernameLabel = Label(self, text="Username ", font=MEDIUM_FONT)  #label and entry box for username
        self.UsernameEntry = ttk.Entry(self, textvariable = username)

        self.PasswordLabel = Label(self, text="Password ", font=MEDIUM_FONT)  #label and entry box for password
        self.PasswordEntry = ttk.Entry(self, textvariable = password)

        self.ErrorLabel = Label(self, text="Incorrect Login Details ",font=MINI_FONT, fg = "red")   #error label to be displayed when login details are incorrect

        self.LoginButton = ttk.Button(self, text = "Login",command =lambda: self.Login(controller))
         

    def BackToStart(self,controller):
        self.ErrorLabel.forget()
        controller.show_frame(StartPage)


    def Login(self,controller):   #method to check the login details and allow the user to login if they are corrcet
        username =  self.UsernameEntry.get()                 #fetches the login details that the user entered
        password = self.PasswordEntry.get()
        Valid = self.CheckLoginDetails(username,password)                             #if the previous condition is met valid will be set to True else it is left as False
        if Valid == True:                               
           self.ErrorLabel.pack_forget()                      #remove error label
           controller.show_frame(WorkerPage)               #if valid is True after checking it will display the next page
           global CurrentWorkerID
           CurrentWorkerID = "00" + str(username[7])
        else:
             self.ErrorLabel.pack()                           #if valid is still False after checking, the error message label is displayed
        self.UsernameEntry.delete(0,10)                       #the entries are deleted
        self.PasswordEntry.delete(0,10)


    def CheckLoginDetails(self,username,password):
        Valid =  False                                #boolean variable to show whether or not the user details are valid  
        try:
             NewPath = "Project Database.db"
             connection = sqlite3.connect(NewPath)
             data = connection.cursor()
             data.execute("""SELECT Username, Password FROM Workers WHERE Username LIKE ? """,(username,))
             Login = data.fetchall()
             CheckUsername = Login[0][0]
             CheckPassword = Login[0][1]
             if CheckUsername == username and CheckPassword == password:    #condition to check that the details are valid and match each other
                Valid = True 
        except:
             Valid =  False
        return Valid

     
class ManagerPage(tk.Frame):                            #class for the main page for managers

     def __init__(self, parent, controller):            

         Frame.__init__(self,parent)

         self.DefineWidgets(controller)

         self.CreateQueue()

         self.CreateTasksTreeview()

         self.SetCurrentTaskID()
        
         self.TitleLabel.pack(pady=10,padx=10)
                                                                                       #button to go back to login page
         self.BackToLoginButton.pack()
                                                                                  #button to create a task which runs the CreateTask method
         self.CreateTaskButton.place(x=362,y=92)
                                                                                        #success label to show that a task has been assigned
         self.ShowTasksListButton.place(x=352,y=150)


     def DefineWidgets(self,controller):
         self.TitleLabel = Label(self, text="Manager Page", font=TITLE_FONT)

         self.BackToLoginButton = ttk.Button(self, text="Logout ", command =lambda: self.LogOut(controller))  #button to go back to login page

         self.CreateTaskButton = ttk.Button(self, text="Create Task", command = lambda: self.CreateTask(controller))  #button to create a task which runs the CreateTask method

         self.SuccessLabel = Label(self,text="Task Assigned! ",font = MEDIUM_FONT,fg="green")   #success label to show that a task has been assigned

         TaskType = ""                                                          #creating the variables and assigning them empty strings
         Object = ""
         Quantity = ""
         Info = ""
         
         self.EnterTaskDetailsLabel = Label(self, text="Enter Task Details Below:", font=MEDIUM_FONT)

         self.TaskTypeLabel = Label(self, text="Task Type ", font=SMALL_FONT)
         self.TaskTypeEntry = ttk.Entry(self, textvariable = TaskType)

         self.ObjectLabel = Label(self, text="Object (Optional) ", font=SMALL_FONT)
         self.ObjectEntry = ttk.Entry(self, textvariable = Object)

         self.QuantityLabel = Label(self, text="Quantity (Optional) ", font=SMALL_FONT)
         self.QuantityEntry = ttk.Entry(self, textvariable = Quantity)

         self.InfoLabel = Label(self, text="Extra Information (Optional) ", font=SMALL_FONT)
         self.InfoEntry = ttk.Entry(self, textvariable = Info)

         self.AutomaticButton = ttk.Button(self, text = "Assign Task", command =lambda: self.ManageTask("A"))

         self.ManualButton = ttk.Button(self, text = "Assign Task Manually", command =lambda: self.ManageTask("M"))

         self.ErrorLabel1 = Label(self, text="Task Type cannot be left blank", font = MINI_FONT,fg="red") 

         self.MyTree = ttk.Treeview(self)

         self.ShowTasksListButton = ttk.Button(self, text = "Show Tasks Lists", command = lambda: self.ShowTasksList())

         self.HideTasksListButton = ttk.Button(self,text="Hide Tasks List", command = lambda: self.HideTasksList())          


     def ResetPage(self):
         WidgetList = [self.EnterTaskDetailsLabel,self.TaskTypeLabel,self.ObjectLabel,self.QuantityLabel,self.InfoLabel,
                  self.AutomaticButton,self.ManualButton,
                  self.TaskTypeEntry,self.ObjectEntry,self.QuantityEntry,self.InfoEntry,
                  self.SuccessLabel,self.ErrorLabel1,self.MyTree]
         for x in WidgetList:
              x.forget()
               
         self.HideTasksListButton.place_forget()
         self.SuccessLabel.place_forget()
         self.CreateTaskButton.place(x=362,y=92)
         self.ShowTasksListButton.place(x=352,y=150)
         try:
             self.IDLabel.forget()
             self.ConfirmButton.forget()
             self.dropmenu.forget()
             self.SelectWorkerIDLabel.forget()
         except:
                return None
     
     def LogOut(self,controller):
         Confirm = messagebox.askyesno(title="Log Out",message="Are you sure you want to log out?")
         if Confirm > 0:
            controller.show_frame(ManagerLogin)
            self.ResetPage()

     def SetCurrentTaskID(self):
         try:
             NewPath = "Project Database.db"
             connection = sqlite3.connect(NewPath)
             data = connection.cursor()
             data.execute("""SELECT TaskID FROM Tasks ORDER BY TaskID DESC LIMIT 1""")
             self.CurrentTaskID = str(data.fetchall())
             self.CurrentTaskID = self.CurrentTaskID[3] + self.CurrentTaskID[4] + self.CurrentTaskID[5]
             self.CurrentTaskID = int(self.CurrentTaskID) + 1
             self.CurrentTaskID = str(self.CurrentTaskID)
             if len(self.CurrentTaskID) == 1:
                self.CurrentTaskID = "00" + self.CurrentTaskID
             elif len(self.CurrentTaskID) == 2:
                  self.CurrentTaskID = "0" + self.CurrentTaskID  
         except:
                self.CurrentTaskID = "001"          


     
     def CreateTask(self,controller):                        #method to create a task

         self.IDLabel = Label(self, text="ManagerID: "+CurrentManagerID, font=MEDIUM_FONT,fg="blue")
         self.IDLabel.pack()
          
         self.CreateTaskButton.place_forget()

         self.ShowTasksListButton.place_forget()
         self.HideTasksListButton.place_forget()
         self.MyTree.forget()
         
         
         self.SuccessLabel.place_forget()                                               #removces the success label

         TaskType = ""                                                          #creating the variables and assigning them empty strings
         Object = ""
         Quantity = ""
         Info = ""

         self.EnterTaskDetailsLabel.pack()

         self.TaskTypeLabel.pack()
         self.TaskTypeEntry.pack()
                                                              #labels and entries to input the required information about the task
         self.ObjectLabel.pack()
         self.ObjectEntry.pack()

         self.QuantityLabel.pack()
         self.QuantityEntry.pack()

         self.InfoLabel.pack()
         self.InfoEntry.pack()

                                                                       #button to assign the task automatically
         self.AutomaticButton.pack()
                                                                       #button to assign the task manually
         self.ManualButton.pack()


                                                                              #error label for if the TaskType entry is left blank

     def ManageTask(self,AutomaticOrManual):   #method to assign the task automatically
         self.ErrorLabel1.forget()
         self.TaskType = self.TaskTypeEntry.get()         #fetch the data inputted into the entry boxes
         self.Object = self.ObjectEntry.get()
         self.Quantity = self.QuantityEntry.get()
         self.Info = self.InfoEntry.get()

         self.TaskTypeEntry.delete(0,20)             #clear the entry boxes
         self.ObjectEntry.delete(0,20)
         self.QuantityEntry.delete(0,20)
         self.InfoEntry.delete(0,100)         

         if self.TaskType == "" or self.TaskType == " " or self.TaskType == "  ":                                   #if TaskType is left blank the error label for it is displayed
             self.ErrorLabel1.pack()
         else:
             self.ErrorLabel1.forget()

             self.ResetPage()

             if AutomaticOrManual == "A":
                  WorkerID = self.Algorithm()
                  self.AssignTask(WorkerID)
                  self.SuccessLabel.place(x=312,y=185)
             else:
                  self.CreateTaskButton.place_forget()
                  self.ShowTasksListButton.place_forget()
                  self.ManualChoice()

             
     def ManualChoice(self):   #method to assign the task automatically
         self.SelectWorkerIDLabel = Label(self,text = "Select WorkerID of worker to assign the task to:",font=SMALL_FONT)
         self.SelectWorkerIDLabel.pack()
        
         options = ["001", "002", "003", "004", "005", "006", "007", "008"]
         
         ID = StringVar()
         ID.set(options[0])
    
         self.dropmenu = ttk.OptionMenu(self,ID,*options)
         self.dropmenu.pack()
         
         self.ConfirmButton = ttk.Button(self,text="Assign",command = lambda: self.ConfirmChoice(ID.get()))
         self.ConfirmButton.pack()

         


     def ConfirmChoice(self,WorkerID):
         Confirm = messagebox.askyesno(title="Confirm Choice",message=("Assign to Worker?"))
         if Confirm > 0:
            self.SelectWorkerIDLabel.forget()
            self.dropmenu.forget()
            self.ConfirmButton.forget()
            self.ResetPage()
            self.SuccessLabel.place(x=312,y=185)
            self.AssignTask(WorkerID)

     def AssignTask(self,WorkerID):
         self.WorkerBusy = self.CheckIfBusy(WorkerID)
         if self.WorkerBusy == True:
            self.AddToQueue(self.CurrentTaskID)
         self.StoreTask(WorkerID)

     def IncrementCurrentTaskID(self):
         self.CurrentTaskID = (int(self.CurrentTaskID)+1)
         self.CurrentTaskID = str(self.CurrentTaskID)
         if len(self.CurrentTaskID) == 1:
            self.CurrentTaskID = "00" + self.CurrentTaskID
         elif len(self.CurrentTaskID) == 2:
              self.CurrentTaskID = "0" + self.CurrentTaskID
          
     def CheckIfBusy(self,WorkerID):
         try:
             NewPath = "Project Database.db"
             connection = sqlite3.connect(NewPath)
             data = connection.cursor()          
             data.execute("""SELECT TaskID FROM Tasks WHERE WorkerID LIKE ? AND DateCompleted IS NULL ORDER BY TaskID DESC LIMIT 1""",(WorkerID,))
             ID = data.fetchall()
             if ID[0][0] == "":
                self.WorkerBusy = False
             else:
                  self.WorkerBusy = True
         except:
                self.WorkerBusy = False
         return self.WorkerBusy
                           

     def Algorithm(self):
         NewPath = "Project Database.db"
         connection = sqlite3.connect(NewPath)
         data = connection.cursor()
         data.execute("""SELECT YearsWorked FROM Details""")
         Years = data.fetchall()
         YearsWorkedList = []
         for i in range(0,8):
             Years1 = str(Years[i])
             if len(Years1) == 4:
                Years1 = Years1[1]
             elif len(Years1) == 5:
                  Years1 = Years1[1] + Years1[2]
             Years1 = int(Years1)
             YearsWorkedList.append(Years1)

         SortedYearsWorkedList = self.MergeSort(YearsWorkedList)

         most = len(SortedYearsWorkedList) - 1
         found = False
         count = 0

         while found == False:
               if count > 8:
                  WorkerID = "00" + str(random.randint(1,8))
                  found = True
               count += 1
               data.execute("""SELECT WorkerID FROM Details WHERE YearsWorked LIKE ?""",(SortedYearsWorkedList[most],))
               ID = str(data.fetchall())
               WorkerID = ID[3] + ID[4] + ID[5]
               busy = self.CheckIfBusy(WorkerID)
               if busy == False:
                  found = True
               else:
                    most = most - 1
         return WorkerID
          
                                                                                      
             

 
     def StoreTask(self,WorkerID):                              #method which stores the current task into the database in the task table
         NewPath = "Project Database.db"
         connection = sqlite3.connect(NewPath)
         data = connection.cursor()
         data.execute("""INSERT INTO Tasks(TaskID,TaskType,Object,Quantity,Info,DateAssigned,WorkerID,ManagerID)
  Values(?,?,?,?,?,?,?,?)  
  """,(self.CurrentTaskID,self.TaskType,self.Object,self.Quantity,self.Info,str_date_today,WorkerID,CurrentManagerID,))
         connection.commit()

         self.MyTree.insert(parent='',index='end',text="",values=(self.CurrentTaskID,self.TaskType,self.Object,self.Quantity,self.Info,
                                                                str_date_today,"None",WorkerID,CurrentManagerID))
         self.IncrementCurrentTaskID()

         
     def CreateTasksTreeview(self):
         self.MyTree = ttk.Treeview(self)
         NewPath = "Project Database.db"
         connection = sqlite3.connect(NewPath)
         data = connection.cursor()
         data.execute("""SELECT * FROM Tasks""")
         TasksList = data.fetchall()

            
         self.MyTree['columns'] = ("TaskID","TaskType","Object","Quantity","Info","DateAssigned","DateCompleted","WorkerID","ManagerID")  #define columns

             
         self.MyTree.column("#0", width=0,minwidth=0)
         self.MyTree.column("TaskID",anchor=CENTER,width=50)
         self.MyTree.column("TaskType",anchor=W,width=100)
         self.MyTree.column("Object",anchor=W,width=100)
         self.MyTree.column("Quantity",anchor=CENTER,width=60)
         self.MyTree.column("Info",anchor=W,width=100)
         self.MyTree.column("DateAssigned",anchor=W,width=100)
         self.MyTree.column("DateCompleted",anchor=W,width=100)              #format columns
         self.MyTree.column("WorkerID",anchor=CENTER,width=60)
         self.MyTree.column("ManagerID",anchor=CENTER,width=50)

            
         self.MyTree.heading("#0",text="", anchor=W)
         self.MyTree.heading("TaskID",text="TaskID", anchor=CENTER)
         self.MyTree.heading("TaskType",text="TaskType", anchor=W)
         self.MyTree.heading("Object",text="Object", anchor=W)
         self.MyTree.heading("Quantity",text="Quantity", anchor=CENTER)
         self.MyTree.heading("Info",text="Info", anchor=W)                             #create headings
         self.MyTree.heading("DateAssigned",text="DateAssigned", anchor=W)
         self.MyTree.heading("DateCompleted",text="DateCompleted", anchor=W)
         self.MyTree.heading("WorkerID",text="WorkerID", anchor=CENTER)
         self.MyTree.heading("ManagerID",text="ManagerID", anchor=CENTER)

         for record in TasksList:                  #add data
              self.MyTree.insert(parent='',index='end',text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]))


     def ShowTasksList(self):                    
         self.SuccessLabel.place_forget()
         self.ShowTasksListButton.place_forget()
         self.HideTasksListButton.place(x=352,y=150)
         self.MyTree.pack(pady=100)


     def HideTasksList(self):
         self.MyTree.forget()
         self.HideTasksListButton.place_forget()
         self.ShowTasksListButton.place(x=352,y=150)            
          
     def CreateQueue(self):
         self.Queue = []

     def AddToQueue(self,item):
         self.Queue.append(item)

     def RemoveFromQueue(self,item):
         self.Queue.remove(item)

     def MergeSort(self,List):
         if len(List) > 1:
             mid = len(List) // 2
             LeftList = List[:mid]
             RightList = List[mid:]
             self.MergeSort(LeftList)
             self.MergeSort(RightList)
             #add elements from right and left into merged list in order
             i = 0
             j = 0
             k = 0
             while i < len(LeftList) and j < len(RightList):
                 if LeftList[i] < RightList[j]:
                     List[k] = LeftList[i]
                     i = i + 1
                 else:
                     List[k] = RightList[j]
                     j = j + 1
                 k = k + 1
                 #check if left list has elements not merged
             while i < len(LeftList):
                     List[k] = LeftList[i]
                     i = i + 1
                     k = k + 1
                 #check if right list has elements not merged
             while j < len(RightList):
                     List[k] = RightList[j]
                     j = j + 1
                     k = k + 1
             return(List)

     def BinarySearch(self,List,item,count,left,right):
         mid = (1+left+right)//2
         if count > (len(List)//2):
             return False
         if left < 0:
             return False
         if List[mid] == item:
             return mid + 1
         elif item <List[mid]:
             return self.BinarySearch(List,item,(count+1),left,mid-1)
         elif item> List[mid]:
             return self.BinarySearch(List,item,(count+1),mid+1,right)
          
                  

class WorkerPage(tk.Frame):                 #class for the workers main page

     def __init__(self, parent, controller):
         Frame.__init__(self,parent)

         self.DefineWidgets(controller)
        
         self.TitleLabel.pack(pady=10,padx=10)
                                                                             
         self.BackToLoginButton.pack()

         self.CurrentTaskButton.place(x=345,y=220)


     def DefineWidgets(self,controller):
         self.TitleLabel = Label(self, text="Worker Page", font=TITLE_FONT)

         self.BackToLoginButton = ttk.Button(self, text="Logout", command =lambda: self.LogOut(controller))   
 
         self.CurrentTaskButton = ttk.Button(self, text = "Show Current Task", command = lambda: self.ShowTask())

         self.NoTasksLabel = Label(self, text = "No tasks have been currently assigned", font = SMALL_FONT, fg="red")
 
         self.HideButton = ttk.Button(self, text = "Hide", command = lambda: self.HideTask())

         self.CompleteButton = ttk.Button(self, text = "Mark Task As Complete", command = lambda: self.CompleteTask())

         self.SuccessLabel = Label(self, text = "Task Completed!", font = MINI_FONT,fg = "green")
          

     def LogOut(self,controller):
         Confirm = messagebox.askyesno(title="Log Out",message="Are you sure you want to log out?")
         if Confirm > 0:
            self.ResetPage()
            controller.show_frame(WorkerLogin)

     def ResetPage(self):
         WidgetList1 = [self.CompleteButton,self.HideButton,self.NoTasksLabel,self.SuccessLabel]
         WidgetList2 = [self.HideButton,self.NoTasksLabel]
         try:
            self.IDLabel.forget()
            self.TaskTypeLabel.forget()
            self.ObjectLabel.forget()
            self.InfoLabel.forget()
            self.QuantityLabel.place_forget()
            self.QuantityValueLabel.place_forget()
            for x in WidgetList1:
                 x.pack_forget()
         except:
                for x in WidgetList1:
                    x.pack_forget()
         for x in WidgetList2:
             x.place_forget()
         self.CurrentTaskButton.place(x=345,y=220)
          

     def ShowTask(self):
         self.IDLabel = Label(self, text="WorkerID: "+CurrentWorkerID, font=MEDIUM_FONT,fg="blue")
         self.IDLabel.pack()
         self.NoTasksLabel.place_forget()
         self.CurrentTaskButton.place_forget()
         self.SuccessLabel.forget()
         self.HideButton.place(x=358,y=220)
         try:
             NewPath = "Project Database.db"
             connection = sqlite3.connect(NewPath)
             data = connection.cursor()
             data.execute("""SELECT TaskID,TaskType,Object,Quantity,Info FROM Tasks WHERE WorkerID LIKE ? AND DateCompleted IS NULL ORDER BY TaskID ASC LIMIT 1""",(CurrentWorkerID,))
             task = data.fetchall()

             self.CurrentTaskID = task[0][0]
             
             self.TaskTypeLabel = Label(self, text = "Task Type: "+task[0][1], font = MINI_FONT)
             self.TaskTypeLabel.pack()
             
             self.ObjectLabel = Label(self, text = "Object: "+task[0][2], font = MINI_FONT)
             self.ObjectLabel.pack()

             self.QuantityLabel = Label(self, text = "Quantity: ", font = MINI_FONT)
             self.QuantityLabel.place(x=350,y=172)
             
             self.QuantityValueLabel = Label(self, text = task[0][3], font = MINI_FONT)
             self.QuantityValueLabel.place(x=432,y=172)
             
             self.InfoLabel = Label(self, text = "Info: "+task[0][4], font = MINI_FONT)
             self.InfoLabel.pack(pady=20)

             self.CompleteButton.pack(pady=70)        

         except:
               self.NoTasksLabel.place(x=220,y=145)
             
     def HideTask(self):
         try:
             self.TaskTypeLabel.forget()
             self.ObjectLabel.forget()                  
             self.QuantityLabel.place_forget()
             self.QuantityValueLabel.place_forget()
             self.InfoLabel.forget()
             self.CompleteButton.forget()
         except:
                self.NoTasksLabel.forget()
         self.IDLabel.forget()
         self.NoTasksLabel.place_forget()
         self.HideButton.place_forget()
         self.CurrentTaskButton.place(x=345,y=220)
          


     def CompleteTask(self):
         Confirm = messagebox.askyesno(title="Mark Task as Complete",message="Confirm the task has been completed")
         if Confirm > 0:
            self.UpdateTasksTable()
            self.UpdateQueue()
            self.ResetPage()
            self.SuccessLabel.pack(pady=30)
          

                    
     def UpdateTasksTable(self):
         NewPath = "Project Database.db"
         connection = sqlite3.connect(NewPath)
         data = connection.cursor()
         data.execute("""UPDATE Tasks SET DateCompleted = ? WHERE TaskID LIKE ?""",(str_date_today,self.CurrentTaskID,))
         connection.commit()



     def UpdateQueue(self):
         busy = ManagerPage.CheckIfBusy(ManagerPage,CurrentWorkerID)
         if busy == False:
              try:
                   NewPath = "Project Database.db"
                   connection = sqlite3.connect(NewPath)
                   data = connection.cursor()          
                   data.execute("""SELECT TaskID FROM Tasks WHERE WorkerID LIKE ? AND DateCompleted IS NULL ORDER BY TaskID ASC LIMIT 1""",(CurrentWorkerID,))
                   ID = data.fetchall()
                   ManagerPage.RemoveFromQueue(ManagerPage,ID[0])
                   self.StoreInTasksTable(ManagerPage,ID[0])
              except:
                     return None
          
          
    


app = window()                     #creating an instance of the window class called app
app.mainloop()                     #runs app



           
    
                      
         
     
