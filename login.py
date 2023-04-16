import subprocess
from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

def tab(): keyboard.tap(Key.tab)

logins = {"main": ["Vampiregamer7", "Fairytail743"],
          "sup": ["Garbagedude2", "Chrissexy6969"]}

if __name__ == "__main__":
    while(True):
        acct = input("Which account?\n")
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
            print("end")
            break
        else:
            print("Sorry that account doesn't exist currently")