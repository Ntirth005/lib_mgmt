#!!IMP!!
# Firstly split screen into two parts
# one for library window
# other for corresponding idle window

#Note :
#Do not click any bottom-most button more than once.
#it will cause irritating results or window not responding

from tkinter import ttk,Button,Frame,Tk,TRUE,RIGHT,LEFT,CENTER,TOP,BOTTOM,Scrollbar,Radiobutton
import csv
from lib_tasks import *
from os import getcwd

a='Shelf1'
var_shelf=[]
root=Tk()
root.geometry("1200x600+30+40")
root.title("Library")

frame=Frame(root,width=1000,height=400)
frame.place(x=60,y=60,relheight=0.8,relwidth=0.9)


def treeview_call():
    global var_shelf

    tv1=ttk.Treeview(frame)
    tv1.place(relheight=1,relwidth=1)#settheheightandwidthofthewidgetto100%ofitscontainer(frame).
    treescrolly=Scrollbar(frame,orient="vertical",command=tv1.yview)#commandmeansupdatetheyaxisviewofthewidget
    treescrollx=Scrollbar(frame,orient="horizontal",command=tv1.xview)#commandmeansupdatethexaxisviewofthewidge
    tv1.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)#assignthescrollbarstothetTreeviewWidget
    treescrollx.pack(side="bottom",fill="x")#makethescrollbarfillthexaxisofthetTreeviewwidget
    treescrolly.pack(side="right",fill="y")

    tv1["column"]=('SNo','BooksName','AuthorName','PubName','Genre','Quantity',)
    tv1["show"]="headings"
    tv1.column(0,width=40)
    tv1.column(5,width=120)
    for column in tv1["columns"]:
        tv1.heading(column,text=column)#letthecolumnheading=columnname
        
    for row in var_shelf:
        tv1.insert("","end",values=row)#insertseachlistintotheTreeview.Forparametersseehttps://docs.python.org/3/library/tkinter.thtml#
    ttk.Treeview.insert

# for working in windows
     
def read_shelf():
     f=open(str(getcwd())+'/Book Details//'+a+'.csv')
     csv_reader=csv.reader(f)
     global var_shelf
     var_shelf=[]
     for i in csv_reader:
        var_shelf.append(i)
     return var_shelf

#for wrorking in linux
'''
def read_shelf():
    global a
    global var_shelf
    f=open(a+'.csv')
    csv_reader=csv.reader(f)
    global var_shelf
    var_shelf=[]
    for i in csv_reader:
        var_shelf.append(i)
    return var_shelf
'''
read_shelf()    
treeview_call()

def refresh():
    global frame
    global a

    frame.destroy()

    frame=Frame(root,width=1000,height=400)
    frame.place(x=60,y=60,relheight=0.8,relwidth=0.9)
    read_shelf()
    treeview_call()

shelf_list=Frame(root,)
shelf_list.place(relwidth=0.8,relx=0.1,rely=0)

def assign(x):
    global a     
    a=x
    refresh()

def save2storage():
    global var_shelf
    # for working in windows
    
    with open(str(getcwd())+'/Book Details//'+a+'.csv', 'w',newline='') as f:
         csv.writer(f,delimiter=',').writerows(var_shelf)
    '''
    #for working in linux
    with open(a+'.csv', 'w',newline='') as f:
         csv.writer(f,delimiter=',').writerows(var_shelf)
   ''' 
def task01():
    print('under development')
    
def task02():
    global var_shelf
    var_shelf=newbook(var_shelf)
    save2storage()
    refresh()
    print('Done',end='\n\n')
    
def task03():
    global var_shelf
    global a
    a='find'
    var_shelf=find(var_shelf)
    save2storage()
    refresh()
    print('Done',end='\n\n')
    
def task04():
    global var_shelf
    var_shelf=remove(var_shelf)
    save2storage()
    refresh()
    print('Done',end='\n\n')
    
def task05():
    global var_shelf
    var_shelf=arng_alph(var_shelf)
    save2storage()
    refresh()
    print('Done',end='\n\n')

def task06():
    refresh()
    print('Done',end='\n\n')

def task07():
    global var_shelf
    var_shelf=edit(var_shelf)
    save2storage()
    refresh()
    print('Done',end='\n\n')

    
shelf1=Button(shelf_list,text="Shelf1",bd=0,bg="skyblue3",command=lambda:assign('Shelf1'))
shelf2=Button(shelf_list,text="Shelf2",bd=0,bg="skyblue3",command=lambda:assign('Shelf2'))
shelf3=Button(shelf_list,text="Shelf3",bd=0,bg="skyblue3",command=lambda:assign('Shelf3'))
shelf4=Button(shelf_list,text="Shelf4",bd=0,bg="skyblue3",command=lambda:assign('Shelf4'))
shelf5=Button(shelf_list,text="Shelf5",bd=0,bg="skyblue3",command=lambda:assign('Shelf5'))
shelf6=Button(shelf_list,text="Shelf6",bd=0,bg="skyblue3",command=lambda:assign('Shelf6'))
shelf7=Button(shelf_list,text="Shelf7",bd=0,bg="skyblue3",command=lambda:assign('Shelf7'))
shelf8=Button(shelf_list,text="Shelf8",bd=0,bg="skyblue3",command=lambda:assign('Shelf8'))
shelf9=Button(shelf_list,text="Shelf9",bd=0,bg="skyblue3",command=lambda:assign('Shelf9'))
shelf10=Button(shelf_list,text="Shelf10",bd=0,bg="skyblue3",command=lambda:assign('Shelf10'))


shelf1.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
shelf2.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
shelf3.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
shelf4.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
shelf5.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
shelf6.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
shelf7.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
shelf8.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
shelf9.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
shelf10.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)


workspace=Frame(root,width=1000)
workspace.place(relwidth=0.8,relx=0.1,rely=0.9)

task1=Button(workspace,text="Update borrowers",bd=0,bg="skyblue3",command=lambda:task01())
task2=Button(workspace,text="New book",bd=0,bg="skyblue3",command=lambda:task02())
task3=Button(workspace,text="Find",bd=0,bg="skyblue3",command=lambda:task03())
task4=Button(workspace,text="remove",bd=0,bg="skyblue3",command=lambda:task04())
task5=Button(workspace,text="Arrange Alpha",bd=0,bg="skyblue3",command=lambda:task05())
task6=Button(workspace,text="Refresh",bd=0,bg="skyblue3",command=lambda:task06())
task7=Button(workspace,text="Edit",bd=0,bg="skyblue3",command=lambda:task07())
#task8=Button(workspace,text="task8",bd=0,bg="skyblue3",)
#task9=Button(workspace,text="task9",bd=0,bg="skyblue3",)
task10=Button(workspace,text="Exit",bd=0,bg="red",command=lambda:root.destroy())

task1.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
task2.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
task3.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
task4.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
task5.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
task6.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
task7.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
#task8.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
#task9.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)
task10.pack(pady=10,padx=6,expand=TRUE,fill="x",side=LEFT)


root.mainloop()
