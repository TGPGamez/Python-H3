import math
import threading

import SNMP as snmp
import SSH as ssh
from tkinter import *

#Class to construct a Interface
class Interface:
    row = 0
    column = 0
    name = "Not set"
    status = 2
    oid = 0

    def __init__(self, r, c, n, s, o):
        self.row = r
        self.column = c
        self.name = n
        self.status = s
        self.oid = o

#Make a instance of Tkinter View
main = Tk()
#Set size of window
main.geometry("900x500")

switch_interface_List = []
statuses_config = {2: "green", 3: "orange", 4: "red"}

#Get interfaces from MIB
def Get_Interfaces():
    switch_interface_List.clear()
    ints = snmp.get_all('.1.3.6.1.2.1.2.2.1.2', '1.3.6.1.2.1.2.1.0')
    int_count = snmp.get_result('.1.3.6.1.2.1.2.1.0')
    #Define max columns per row
    max_column = round(math.sqrt(int_count))
    current_column = 0
    current_row = 0
    for index in range(int_count):
        int = ints[index]
        #Get first character of name
        port_char = list(int.values())[0][0]
        #Get interface port
        int_oid = (list(int.keys())[0]).split('.')[-1]
        if port_char == 'F' or port_char == 'G':
            #Get Admin status
            admin_status = snmp.get_result('.1.3.6.1.2.1.2.2.1.7.' + int_oid)
            #Get Operation status
            oper_status = snmp.get_result('.1.3.6.1.2.1.2.2.1.8.' + int_oid)
            switch_interface_List.append(
                Interface(current_row,
                                current_column,
                                list(int.values())[0],
                                admin_status+oper_status,
                                int_oid
                                ))
            if current_column >= max_column - 1:
                current_column = 0
                current_row += 1
            else:
                current_column += 1

def Gui():
    eval_click = lambda obj, obj2, x, y: (lambda p: click_event(obj, obj2, x, y))
    for idx, int in enumerate(switch_interface_List):
        background = statuses_config[int.status]
        frame = Frame(main, bg=background)
        frame.grid(row=int.row, column=int.column, sticky=NSEW, pady=5, padx=5)
        label = Label(frame, text=int.name, bg=background, fg="white", font="Arial 14")

        def click_event(fr, lbl, int, idx):
            Toggle_Status(idx, int.name, int.status)

            background = statuses_config[int.status]
            fr.config(bg=background)
            lbl.config(bg=background)

        label.bind("<Button-1>", eval_click(frame, label, int, idx))
        label.grid(row=0, column=0, pady=5, padx=5)
    main.mainloop()

def Toggle_Status(idx, name, status):
    ssh.Change_Interface_Status(int.name, int.status)
    if switch_interface_List[idx].status == 1:
        switch_interface_List[idx].status = 2
    else:
        switch_interface_List[idx].status = 1

def Start():
    Get_Interfaces()
    Gui()
    main.mainloop()
