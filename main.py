import pyautogui
import time
import keyboard
import sys
import threading
import tkinter as tk
from selenium import webdriver
import newMailAccount

# class App:
#     def __init__(self, master):
#         self.master = master
#         master.title("My App")

#         self.label = tk.Label(master, text="Hello, world!")
#         self.label.pack()

#         self.button = tk.Button(master, text="Open Firefox", command=self.open_firefox)
#         self.button.pack()

#         self.button = tk.Button(master, text="Quit", command=self.quit)
#         self.button.pack()

#         # Create a flag variable to signal to the background process to stop
#         self.should_stop = False

#         # Schedule the background process to run periodically
#         self.master.after(10000, self.background_process)

#     def open_firefox(self):
#         # Set the path to the Firefox driver executable
#         geckodriver_path = "path/to/geckodriver"

#         # Create a new instance of the Firefox browser
#         driver = webdriver.Firefox(executable_path=geckodriver_path)

#         # Navigate to a website
#         driver.get("https://www.google.com")

#     def quit(self):
#         # Set the flag variable to signal to the background process to stop
#         self.should_stop = True
#         self.master.quit()

#     def background_process(self):
#         if not self.should_stop:
#             # Open the Riot Games launcher
#             pyautogui.press('win')
#             pyautogui.typewrite('riot')
#             pyautogui.press('enter')

#             # Wait for the launcher to load
#             time.sleep(10)

#             # Type in the username and password fields and click the login button
#             pyautogui.typewrite('your_username')
#             pyautogui.press('tab')
#             pyautogui.typewrite('your_password')
#             pyautogui.press('enter')

#             # Schedule the background process to run again after 10 seconds
#             self.master.after(10000, self.background_process)

# root = tk.Tk()
# app = App(root)
# root.mainloop()


password = newMailAccount.generatePassword(8)
email = newMailAccount.randomEmailAddress()

newMailAccount.saveAccountsOnFile(email, password)
newMailAccount.createProtonMailAccount(email, password)
# print(newMailAccount.listFile())
newMailAccount.getNonUsedEmail()