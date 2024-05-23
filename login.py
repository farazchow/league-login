import subprocess

# from pynput.keyboard import Controller, Key
import time
import tkinter as tk
import tkinter.ttk as ttk
import json

# keyboard = Controller()


def load_data():
    file = open("login.json")
    user_data = json.load(file)
    return user_data


# def tab():
#     keyboard.tap(Key.tab)


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
    image_mid = tk.PhotoImage(file="images/Position_Challenger-Mid.png")
    image_adc = tk.PhotoImage(file="images/Position_Challenger-Bot.png")
    image_sup = tk.PhotoImage(file="images/Position_Challenger-Support.png")

    # Button Frames
    mid_frame = tk.Frame(master=window)
    mid_frame.grid(row=1, column=0)
    adc_frame = tk.Frame(master=window)
    adc_frame.grid(row=1, column=1)
    sup_frame = tk.Frame(master=window)
    sup_frame.grid(row=1, column=2)

    # Logging Window
    log = tk.Text(window, state="disabled", width=60, height=20, wrap="none")

    ys = ttk.Scrollbar(window, orient="vertical", command=log.yview)
    xs = ttk.Scrollbar(window, orient="horizontal", command=log.xview)
    log["yscrollcommand"] = ys.set
    log["xscrollcommand"] = xs.set
    log.grid(column=0, row=2, columnspan=3, sticky="nwes", padx=10, pady=10)
    xs.grid(column=0, row=3, columnspan=3, sticky="we")
    ys.grid(column=3, row=2, sticky="ns")

    def printToWindow(line: str):
        log["state"] = "normal"
        log.insert("end", f"{line}\n")
        log["state"] = "disabled"

    # Buttons for roles
    button_mid = tk.Button(
        master=mid_frame,
        text="MID",
        image=image_mid,
        compound="top",
        command=lambda: chooseAccount("mid", printToWindow, window.destroy),
    )
    button_adc = tk.Button(
        master=adc_frame,
        text="ADC",
        image=image_adc,
        compound="top",
        command=lambda: chooseAccount("adc", printToWindow, window.destroy),
    )
    button_sup = tk.Button(
        master=sup_frame,
        text="SUP",
        image=image_sup,
        compound="top",
        command=lambda: chooseAccount("sup", printToWindow, window.destroy),
    )

    # Finalize and Create
    button_mid.pack()
    button_adc.pack()
    button_sup.pack()

    window.mainloop()


def createWindow1():
    """
    A function that creates our main window
    """

    def printToWindow(line: str):
        # Function to print to debugger
        log["state"] = "normal"
        log.insert("end", f"{line}\n")
        log["state"] = "disabled"

    # Init window
    root = tk.Tk()
    root.title("Choose your account!")

    mainframe = ttk.Frame(root)

    # Label
    label = ttk.Label(mainframe, text="Choose your account!")

    # Frames
    account_frame = ttk.Frame(mainframe, relief="ridge", width=200, height=400)
    option_frame = ttk.Frame(mainframe, relief="ridge", width=200, height=150)
    debug_frame = ttk.Frame(mainframe, relief="solid", width=200, height=300)

    # Logging/Debug Window
    character_width = 8
    character_height = 16

    log = tk.Text(
        debug_frame,
        state="disabled",
        wrap="none",
        width=debug_frame["width"] // character_width,
        height=debug_frame["height"] // character_height,
    )
    log.configure(font=("Terminal", 10))

    ys = ttk.Scrollbar(
        debug_frame,
        orient="vertical",
        command=log.yview,
    )
    xs = ttk.Scrollbar(debug_frame, orient="horizontal", command=log.xview)
    log["yscrollcommand"] = ys.set
    log["xscrollcommand"] = xs.set

    # Accounts
    account_holder = tk.Text(
        account_frame,
        state="disabled",
        width=account_frame["width"] // character_width,
        height=account_frame["height"] // character_height,
    )
    ays = ttk.Scrollbar(
        account_frame,
        orient="vertical",
        command=account_holder.yview,
    )
    account_holder["yscrollcommand"] = ays.set

    image = tk.PhotoImage(file="images/Position_Challenger-Mid.png")
    account = ttk.Button(
        account_holder,
        text="Username1",
        image=image,
        compound="left",
        command=lambda: printToWindow("pressed"),
    )
    account.pack()

    # Grid (Frames)
    mainframe.grid(column=0, row=0)
    label.grid(column=0, row=0, columnspan=2, rowspan=1, pady=15)

    account_frame.grid(
        column=0, row=1, columnspan=1, rowspan=2, padx=(25, 25), pady=(0, 20)
    )
    option_frame.grid(column=1, row=1, padx=(25, 5), pady=(5, 10))
    debug_frame.grid(
        column=1, row=2, columnspan=1, rowspan=1, padx=(25, 5), pady=(10, 5)
    )

    # Grid (Debugger)
    log.grid(column=0, row=0, columnspan=3, rowspan=3, padx=1, pady=1)
    xs.grid(column=0, row=3, columnspan=3, sticky="we")
    ys.grid(column=3, row=0, rowspan=3, sticky="ns")

    # Grid (Accounts)
    account_holder.grid(column=0, row=0, rowspan=3)
    ays.grid(column=1, row=0, rowspan=3, sticky="ns")

    root.mainloop()


def chooseAccount(acct: str, debug_func, destroy_func):
    # logins = load_data()
    # if acct in logins:
    #     subprocess.run(logins["league-path"])
    #     keyboard.type(logins[acct][0])
    #     tab()
    #     keyboard.type(logins[acct][1])
    #     for i in range(6):
    #         tab()
    #     keyboard.tap(Key.enter)
    #     time.sleep(15)
    #     subprocess.call("taskkill /F /IM RiotClientUx.EXE")
    #     debug_func("end")
    #     destroy_func()
    # else:
    #     debug_func("Sorry that account doesn't exist currently")
    debug_func("not implemented")


if __name__ == "__main__":
    # createWindow()
    createWindow1()
