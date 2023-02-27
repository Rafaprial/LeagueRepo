from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import random
import string
import pyautogui
from selenium.webdriver.common.keys import Keys

def randomEmailAddress():
    listOfLetters = list(string.ascii_lowercase)
    name = ""
    for i in range(8):
        name += random.choice(listOfLetters)
    return name



def generatePassword(length):
    # Generate a string of letters, digits, and symbols with the specified length
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits 
    password = ''.join(random.choices(characters, k=length))
    
    return password
    # Example usage: generate a password with length 8

def saveAccountsOnFile(account, password):
    with open("my_file.txt", "a") as f:
        f.write(account+"||"+password+"\n")

def listFile():
    with open("my_file.txt", "r") as f:
        lines = f.read().splitlines()
        return (lines)

def createProtonMailAccount(email, password):
    # # Set the path to the Firefox driver executable
    geckodriver_path = "path/to/geckodriver"
    # Create a new instance of the Firefox browser
    driver = webdriver.Firefox(executable_path=geckodriver_path)
    # Navigate to a website
    driver.get("https://account.proton.me/signup?plan=free&billing=12&ref=prctbl&minimumCycle=12&currency=EUR&product=mail&language=en")
    time.sleep(5)
    pyautogui.write(email)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(5)
    pyautogui.write(password)
    pyautogui.press('tab')
    time.sleep(5)
    pyautogui.write(password)
    pyautogui.press('enter')
    time.sleep(3)
    emailCaptcha = driver.find_element(By.ID, "label_1")
    emailCaptcha.click()
    pyautogui.write(getNonUsedEmail()+"@proton.me")
    pyautogui.press('enter')
    driver.get("https://account.proton.me/login?product=generic&language=en")
    driver.execute_script("window.open('about:blank','secondtab')")
    # It is switching to second tab now
    driver.switch_to.window("secondtab")
    # In the second tab, it opens geeksforgeeks
    driver.get("https://account.proton.me/login")

    # emailInput = driver.find_element(By.ID, "email")
    # emailInput.send_keys(email)
    # passwordInput = driver.find_element(By.ID, "password")
    # passwordInput.send_keys(password)
    # repasswordInput = driver.find_element(By.ID, "repeat-password")
    # repasswordInput.send_keys(password)
    # driver.find_element(By.ID, "submit").click()
# def createLeagueAccount():

def getNonUsedEmail():
    listOfEmails = listFile()
    if listOfEmails is not None:
        value = listOfEmails[-1].split("|")
        return(value[0])

    else:
        print("Error")

