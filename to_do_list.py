import tkinter
from tkinter import *
root=Tk()
root.title("TO DO List")
root.geometry("400x630+450+0")
root.resizable(False,False)
task_list=[]

#Add Task by button--------------------->
def add_task():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        list_box.insert(END,task) 
        c+=1

#delete tasks ------------------------->
def delete_task():
    task=str(list_box.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        list_box.delete(ANCHOR)                   

#file opretions------------------------->
def open_task_file():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task!='\n':
                task_list.append(task)
                list_box.insert(END,task)
    except:
        new_file=open("tasklist.txt","w")
        new_file.close()    

#Heading ------------------------------->
heading=Label(root,text="ALL TASKS",font="arial 30 bold",fg="black",bg='#009AC4')
heading.place(x=0,y=0,height=70,width=400)

# Text Input --------------------------->
frame=Frame(root,bg='#C0C0C0')
frame.place(x=0,y=90,height=50,width=400)
task=StringVar()
task_entry=Entry(frame,width=22,font='arial 20',bd=0,bg='#C0C0C0')
task_entry.place(x=3,y=8)
task_entry.focus()

# Add Button---------------------------->
add=Button(frame,text='ADD',font='arial 25 bold',width=4,bg='#6DB800',fg='black',bd=0,command=add_task)
add.place(x=313,y=0)

# display Box------------------------------>
frame1=Frame(root,bd=3,width=700,height=300,bg='black')
frame1.pack(pady=(145,0))
list_box=Listbox(frame1,font=('arial',12),width=40,height=20,bg='#8AD2D8')
list_box.pack(side=LEFT,fill=BOTH,padx=2)

open_task_file()
# Delete Button--------------------------->
delete=Button(root,text='Delete',font='arial 25 bold',bg='red',fg='black',command=delete_task)
delete.place(x=150,y=550,height=50,width=110)


root.mainloop()
