#   @author: Mitchell Levesque                                                          #
#   @desc  : A file that listens for global key presses to handle pausing hotkeys       #

import threading

import pyWinhook
import pythoncom
import win32api
import win32con
import time

import globals
import robot
import utilities


def on_keyboard_event(event):
    # Si se pulsa F6 tecla especificada en las globals el robot se pausa
    if event.Key == globals.pause_key:
        robot.set_to_pause()
    # Si por el contrario se pulsa f7 se encarga de mover la ventana a una pos especifica
    elif event.Key == globals.move_windows_key:
        utilities.move_windows()
    # return True to pass the event to other handlers
    return True


def hook_keyboard():
    # coge el Id del thread y lo guarda.
    globals.listener_thread_id = threading.get_ident()

    # create a hook manager
    hm = pyWinhook.HookManager()
    # watch for all mouse events
    hm.KeyDown = on_keyboard_event
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()


def create_thread():
    # Llama al metodo hook_keyboard para escuchar todo lo que se escribe en el keyboard
    # Tambien el hacerlo con Thread es para que la app pueda seguir corriendo otros procesos
    # globalr.listener_thread se usa para poder parar la accion mas tarde.
    globals.listener_thread = threading.Thread(target=hook_keyboard)
    # Indirectamente llama al metodo hook_keyboard.
    globals.listener_thread.start() 



def stop():
    if globals.listener_thread_id is not None:
        win32api.PostThreadMessage(globals.listener_thread_id, win32con.WM_QUIT, 0, 0)
