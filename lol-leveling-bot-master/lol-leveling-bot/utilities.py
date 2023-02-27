import shutil
import os

import pyautogui
import pywinauto.win32functions
import win32gui
from pywinauto.findwindows import find_window

import globals
# Pilla rutas de donde tenemos input.ini & game.cfg para cambiarlos 
# por los que tenemos en bot_settings
bot_settings_path = os.path.join(os.getcwd(), "bot_settings")
lol_settings_path = "C:\\Riot Games\\League of Legends\\Config"


def setup():
    globals.picture_path = os.path.join(os.getcwd(), "search_images") 
    # Busca el lol.
    find_league_location()
    # Cambia los archivos def como globals por los originales del launcher.
    set_bot_files()


def find_league_location():
    global lol_settings_path
    # print("Attempting to locate League of Legends...")
    # for r, d, f in os.walk("C:\\"):
    #     for files in f:
    #         if files == "LeagueClient.exe":
    #             print("Successfully found %s" % r)
    globals.lol_client_path = os.path.join("C:\Riot Games\League of Legends", "LeagueClient.exe")
    lol_settings_path = os.path.join("C:\Riot Games\League of Legends", "Config")
    return
    # for r, d, f in os.walk("D:\\"):
    #     for files in f:
    #         if files == "LeagueClient.exe":
    #             print("Successfully found %s" % r)
    #             globals.lol_client_path = os.path.join(r, files)
    #             lol_settings_path = os.path.join(r, "Config")
    #             return
    # print("Failed to locate League of Legends.")

# Cambia los archivos de config por los del bot.
def set_bot_files():
    for files in globals.files_to_replace:
        shutil.copy(os.path.join(bot_settings_path, files), os.path.join(lol_settings_path, files))
    print("Successfully loaded bot settings to %s" % lol_settings_path)




def get_client_coords():
    hwnd = win32gui.FindWindow(None, 'League of Legends')
    rect = win32gui.GetWindowRect(hwnd)
    return rect


def get_game_coords():
    hwnd = win32gui.FindWindow(None, 'League of Legends (TM) Client')
    rect = win32gui.GetWindowRect(hwnd)
    return rect


def get_riot_client_coords():
    hwnd = win32gui.FindWindow(None, 'Riot Client Main')
    rect = win32gui.GetWindowRect(hwnd)
    return rect


def is_league_in_game():
    try:
        find_window(title='League of Legends (TM) Client')
        return True
    except Exception:
        return False


def is_client_open():
    try:
        find_window(title='League of Legends')
        return True
    except Exception:
        return False


def is_riot_client_open():
    try:
        find_window(title='Riot Client')
        return True
    except Exception:
        return False


def set_status(status):
    globals.last_status = status
    print(status)


def move_windows():
    try:
        hwnd = win32gui.FindWindow(None, 'LoL Bot')
        win32gui.MoveWindow(hwnd, -8, 0, 655, 1050, True)
        # if is_client_open():
        #     hwnd = win32gui.FindWindow(None, 'League of Legends')
        #     win32gui.MoveWindow(hwnd, 640, 180, 1280, 720, True)
        # if is_league_in_game():
        #     hwnd = win32gui.FindWindow(None, 'League of Legends (TM) Client')
        #     win32gui.MoveWindow(hwnd, 640, 180, None, None, True)
    except Exception:
        print("Error: Could not move windows.")
        return


def focus_game_or_client():
    if is_league_in_game():
        win32gui.SetForegroundWindow(find_window(title='League of Legends (TM) Client'))
    elif is_client_open():
        win32gui.SetForegroundWindow(find_window(title='League of Legends'))

