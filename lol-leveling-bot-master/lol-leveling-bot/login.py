import pyautogui
import time
import subprocess
import globals
import os

lol_client_path = os.path.join("C:\Riot Games\League of Legends", "LeagueClient.exe")

try:
    subprocess.Popen(lol_client_path)
except Exception:
    print("Couldn't open league client")

time.sleep(10)
pyautogui.typewrite('Xannainienza')
pyautogui.press('tab')
pyautogui.typewrite('wXE8FEhZss')
pyautogui.press('enter')
