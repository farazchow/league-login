import subprocess
from pynput.keyboard import Controller, Key
import time
import tkinter as tk
import tkinter.ttk as ttk

keyboard = Controller()

def tab(): keyboard.tap(Key.tab)

logins = {}

def createWindow():
    """
    A function that creates our main window
    :return:
    """
    # Init Window
    window = tk.Tk()
    text_frame = tk.Frame(master=window, height=20, width=40)
    text_frame.grid(row=0, column=1, padx=5, pady=5)
    greeting = tk.Label(master=text_frame, text="What Role Would You like to Play?")
    greeting.pack()

    # Images for Roles
    image_mid = tk.PhotoImage(file='images/Position_Challenger-Mid.png')
    image_adc = tk.PhotoImage(file='images/Position_Challenger-Bot.png')
    image_sup = tk.PhotoImage(file='images/Position_Challenger-Support.png')

    # Button Frames
    mid_frame = tk.Frame(master=window)
    mid_frame.grid(row=1, column=0)
    adc_frame = tk.Frame(master=window)
    adc_frame.grid(row=1, column=1)
    sup_frame = tk.Frame(master=window)
    sup_frame.grid(row=1, column=2)

    # Logging Window
    log = tk.Text(window, state="disabled", width=60, height=20, wrap='none')

    ys = ttk.Scrollbar(window, orient="vertical", command=log.yview)
    xs = ttk.Scrollbar(window, orient="horizontal", command=log.xview)
    log['yscrollcommand'] = ys.set
    log['xscrollcommand'] = xs.set
    log.grid(column=0, row=2, columnspan=3, sticky='nwes', padx=10, pady=10)
    xs.grid(column=0, row=3, columnspan=3, sticky='we')
    ys.grid(column=3, row=2, sticky='ns')

    def printToWindow(line: str):
        log['state'] = 'normal'
        log.insert('end', f'{line}\n')
        log['state'] = 'disabled'

    # Buttons for roles
    button_mid = tk.Button(master=mid_frame, text="MID", image=image_mid, compound="top",
                           command=lambda: chooseAccount("mid", printToWindow, window.destroy))
    button_adc = tk.Button(master=adc_frame, text="ADC", image=image_adc, compound="top",
                           command=lambda: chooseAccount("adc", printToWindow, window.destroy))
    button_sup = tk.Button(master=sup_frame, text="SUP", image=image_sup, compound="top",
                           command=lambda: chooseAccount("sup", printToWindow, window.destroy))

    # Finalize and Create
    button_mid.pack()
    button_adc.pack()
    button_sup.pack()

    window.mainloop()

def chooseAccount(acct: str, debug_func, destroy_func):
    if acct in logins:
        subprocess.run("C:\Riot Games\League of Legends\LeagueClient.exe")
        keyboard.type(logins[acct][0])
        tab()
        keyboard.type(logins[acct][1])
        for i in range(6):
            tab()
        keyboard.tap(Key.enter)
        time.sleep(15)
        subprocess.call("taskkill /F /IM RiotClientUx.EXE")
        debug_func("end")
        destroy_func()
    else:
        debug_func("Sorry that account doesn't exist currently")

if __name__ == "__main__":
    createWindow()