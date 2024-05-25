import subprocess
from pynput.keyboard import Controller, Key
import time
import tkinter as tk
import tkinter.ttk as ttk
import json
from PIL import Image, ImageTk
from pyWinActivate import win_wait_active

keyboard = Controller()
character_width = 8
character_height = 16
image_size = (64, 64)

tab_locations = {
    "username": 0,
    "password": 1,
    "stay_signed_in": 7,
    "login": 8,
    "league": 7,
    "val": 9,
    "enter_game": 9
}

def load_data():
    file = open("login.json")
    user_data = json.load(file)
    return user_data

def setup_debug(debug_frame):
    # Logging/Debug Window
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

    # Grid (Debugger)
    log.grid(column=0, row=0, columnspan=3, rowspan=3, padx=1, pady=1)
    xs.grid(column=0, row=3, columnspan=3, sticky="we")
    ys.grid(column=3, row=0, rowspan=3, sticky="ns")

    return log

def setup_accounts(account_frame):
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
    account_holder.grid(column=0, row=0, rowspan=3)
    ays.grid(column=1, row=0, rowspan=3, sticky="ns")

    return account_holder

def createWindow():
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
    option_frame = ttk.Frame(mainframe, width=400, height=150)
    debug_frame = ttk.Frame(mainframe, relief="solid", width=400, height=300)

    # Logging/Debug Window
    log = setup_debug(debug_frame)

    # Options
    # League or Val?
    game_label = ttk.Label(option_frame, text="What game to play?")
    game = tk.StringVar(root, "league")
    lol = ttk.Radiobutton(option_frame, text="League", variable=game, value="league", command=lambda: printToWindow("Will load League"), padding=10)
    val = ttk.Radiobutton(option_frame, text="Valorant", variable=game, value="val", command=lambda: printToWindow("Will load Valorant"), padding=10)
    game_label.grid(column=1, row=0)
    lol.grid(column=0, row=1)
    val.grid(column=0, row=2)

    # Stay signed in?
    signed_in = tk.BooleanVar(root, False)
    signed_in_box = ttk.Checkbutton(option_frame, text="Stay Signed In?", variable=signed_in, command= lambda: printToWindow("Will stay signed in"))
    signed_in_box.grid(column=2, row=1)

    # Populate Accounts
    image_paths = {
        "Top":      ImageTk.PhotoImage(Image.open("images\Position_Challenger-Top.png").resize(image_size)),
        "Jungle":   ImageTk.PhotoImage(Image.open("images\Position_Challenger-Jungle.png").resize(image_size)),
        "Mid":      ImageTk.PhotoImage(Image.open("images\Position_Challenger-Mid.png").resize(image_size)),
        "Bot":      ImageTk.PhotoImage(Image.open("images\Position_Challenger-Bot.png").resize(image_size)),
        "Support":  ImageTk.PhotoImage(Image.open("images\Position_Challenger-Support.png").resize(image_size)),
        "Fill":     ImageTk.PhotoImage(Image.open("images\icon-position-fill.png").resize(image_size))
    }

    account_holder = setup_accounts(account_frame)

    data = load_data()
    for account_data in data["Accounts"]:
        account = ttk.Button(
            account_holder,
            text=account_data["Username"],
            image=image_paths[account_data["role"]],
            compound="left",
            command=lambda a = account_data: chooseAccount(a, data["riot-path"], printToWindow, root.destroy, game.get(), signed_in.get()),
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

    root.mainloop()


def chooseAccount(acct, riot_path, debug_func, destroy_func, game, signed_in):
    # Start Riot Client
    subprocess.run(riot_path)
    win_wait_active(win_to_wait="Riot Client", message=True)
    time.sleep(3)

    # Input Info & Login
    print("Trying to type")
    keyboard.type(acct["Username"])
    keyboard.tap(Key.tab)
    keyboard.type(acct["Password"])

    for tabs in range(1, tab_locations["login"]):
        if tabs == tab_locations["stay_signed_in"] and signed_in:
            keyboard.tap(Key.enter)
        keyboard.tap(Key.tab)
    keyboard.tap(Key.enter)
    print("logged in?")
    time.sleep(5)

    # Choose Game
    for tabs in range(1, tab_locations[game]):
        keyboard.tap(Key.tab)
    keyboard.tap(Key.enter)
    time.sleep(5)

    # Enter game
    for tabs in range(1, tab_locations["enter_game"]):
        keyboard.tap(Key.tab)
    keyboard.tap(Key.enter)

    time.sleep(5)
    subprocess.call("taskkill /F /IM \"Riot Client.EXE\"")
    # debug_func("end")
    print("end")
    destroy_func()


if __name__ == "__main__":
    createWindow()
