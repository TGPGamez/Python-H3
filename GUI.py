import re
from tkinter import *
import SSH as ssh
import threading
import SNMP as snmp

class Application(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.grid()
        self.master.title("Cisco manager")
        for r in range(6):
            self.master.rowconfigure(r, weight=1)
        for c in range(5):
            self.master.columnconfigure(c, weight=1)

        info_frame = Frame(master, borderwidth=1, relief=RIDGE, bg="gray")
        info_frame.grid(row=0, column=0, rowspan=1, columnspan=1, sticky=NSEW)
        info_frame.rowconfigure((0, 1, 2), weight=1)
        info_frame.columnconfigure((0, 1), weight=1)

        info_hostname_title_lbl = Label(info_frame, text="Hostname:", font="Arial 14 bold", bg="gray")
        info_hostname_title_lbl.grid(row=1, column=0, sticky=E)
        info_hostname_title_lbl = Label(info_frame, text=ssh.Get_Hostname(), font="Arial 12", bg="gray")
        info_hostname_title_lbl.grid(row=1, column=1, sticky=W)

        info_version_title_lbl = Label(info_frame, text="Version:", font="Arial 14 bold", bg="gray")
        info_version_title_lbl.grid(row=2, column=0, sticky=E)
        info_version_title_lbl = Label(info_frame, text=snmp.Get_Config_Version(), font="Arial 12", bg="gray")
        info_version_title_lbl.grid(row=2, column=1, sticky=W)

        up_time_frame = Frame(master, borderwidth=1, relief=RIDGE, bg="gray")
        up_time_frame.rowconfigure((0, 1), weight=1)
        up_time_frame.columnconfigure((0, 1), weight=1)
        up_time_frame.grid(row=0, column=2, rowspan=1, columnspan=1, sticky=NSEW)
        info_up_time_title_lbl = Label(up_time_frame, text="Uptime:", font="Arial 14 bold", bg="gray")
        info_up_time_title_lbl.grid(row=0, column=0, rowspan=2, sticky=E)
        info_up_time_lbl = Label(up_time_frame, font="Arial 12", bg="gray")
        info_up_time_lbl.grid(row=0, column=1, rowspan=2, sticky=W)

        # test = Label(master, text="Testing here")
        # test.grid(row=1, column=2)

        def set_up_time():
            info_up_time_lbl.config(text=snmp.Get_Up_Time())
            threading.Timer(1, set_up_time).start()

        set_up_time()

        show_cmd_frame = Frame(master)
        show_cmd_frame.grid(row=2, column=0, columnspan=5, sticky=W + E + N + S)

        show_cmd_lbl = Label(show_cmd_frame, text="Skriv show-cmd:")
        show_cmd_lbl.grid(row=0, column=0)

        show_cmd_entry = Entry(show_cmd_frame)
        show_cmd_entry.grid(row=0, column=1)

        show_cmd_text = Text(master, state="disabled")
        show_cmd_text.grid(row=4, column=0, columnspan=3, sticky=W + E)

        scroll_bar = Scrollbar(master, orient="vertical", command=show_cmd_text.yview)
        scroll_bar.grid(row=4, column=3, sticky=NS)

        show_cmd_text['yscrollcommand'] = scroll_bar.set

        def Show_Cmd():
            matches = re.finditer(r"^[^\s]+", show_cmd_entry.get(), re.MULTILINE)
            text = ""
            matches = show_cmd_entry.get().split(' ')
            if matches[0].lower() != "show":
                text = "Dette var ikke en show-cmd."
            else:
                text = ssh.Show_Cmd(show_cmd_entry.get())
            show_cmd_text.configure(state='normal')
            show_cmd_text.delete('1.0', END)
            show_cmd_text.insert(INSERT, text)
            show_cmd_text.configure(state='disabled')

        show_cmd_btn = Button(show_cmd_frame, text="Send", command=Show_Cmd)
        show_cmd_btn.grid(row=0, column=2, padx=5)

#main = Tk()
#main.geometry("700x500")
#app = Application(master=main)
#app.mainloop()

