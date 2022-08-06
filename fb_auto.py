import os
import wget
import random
import warnings
import pyautogui
from time import sleep
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def open_browser():
    option1 = Options()
    option1.add_argument("--disable-notifications")
    warnings.simplefilter("ignore")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option1)

    try:
        driver.get('https://www.facebook.com')
        sleep(1)
        return driver
    except:
        print("Your internet is not working properly.")
        temp = True
        
    if temp:   
        exit()
        driver.quit()

def login(driver, u_name, password):

    username_box = driver.find_element_by_id('email')
    username_box.send_keys(u_name)
    sleep(1)

    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(password)
    sleep(1)

    password_box.send_keys(Keys.RETURN)
    sleep(10)


def search_target(diver):
    sleep(3)
    target_link = 'https://www.facebook.com/StartupPakistanSP'
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    driver.get(target_link)
    sleep(5)
    

def find_post(driver):
    target_post = 0
    
    try:                                      
        links = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[8]/div/div[3]/div[2]/div[1]/div/a/div[1]/div/div/div/img')
        target_post = links.get_attribute('src')
    except:
        pass

    try:                                      
        links = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[3]/div[3]/div[1]/div/a/div[1]/div/div/div/img')
        target_post = links.get_attribute('src')
    except:
        pass

    try:
        links = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[3]/div/div/div/div[1]/div[1]/a/div[1]/div/div/div/img')
        target_post = links.get_attribute('src')
    except:
        pass

    try:
        links = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[3]/div/div[1]/div/a/div[1]/div/div/div/img')
        target_post = links.get_attribute('src')
    except:
        pass
    
    return target_post

    
def download_post(target_post):
    path = os.getcwd()

    save_as = os.path.join(path,'Post'+'.jpg')
    wget.download(target_post, save_as)
    print("\nYour Post save At :", save_as)
    return path


def clear_cookie(driver):
    driver.switch_to.window(driver.window_handles[0])
    driver.delete_all_cookies()
    driver.refresh()
    sleep(2)
    driver.get('https://www.facebook.com')
    sleep(10)
    

def locate_upload(driver):
    photo = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/span[2]/span') 
    photo.click()
    sleep(10)

    get_photo = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div') 
    get_photo.click()
    sleep(3)


def select_post(path):
    res = pyautogui.locateCenterOnScreen("search.png", confidence=0.8)
    pyautogui.moveTo(res)
    pyautogui.click()
    print("Moved to Download folder")
    sleep(2)

    pyautogui.write(path)
    pyautogui.hotkey("enter")
    print("Locate directory")
    sleep(2)

    res = pyautogui.locateCenterOnScreen("Picture.png", confidence=0.8)
    pyautogui.moveTo(res)
    pyautogui.click(clicks=2)
    print("Target post selected")
    sleep(2)


def click_upload():
    get_photo = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div') 
    get_photo.click()
    print("Post uploaded")
    sleep(10)


def generate_num():
    numbers = random.sample(range(10), 6)
    gen_number = ''.join(map(str, numbers))
    return gen_number


def move_post():
    path = os.getcwd()
    dir_path = os.path.join(path,'POSTS')
    isExist = os.path.exists(dir_path)

    if not isExist:
        os.makedirs(dir_path)
        print("The new directory is created!")
    
    gen_number = generate_num()

    while True:
        save_as = os.path.join(path,'POSTS','Post_'+str(gen_number)+'.jpg')
        isFileExist = os.path.exists(save_as)
        if isFileExist:
            gen_number = generate_num()
        else:
            break
    save = os.path.join(path,'Post'+'.jpg')
    os.replace(save, save_as)

u_name = input("Enter Your Facebook username : ")
password = getpass("Enter your Facebook password : ")    

driver = open_browser()
login(driver, u_name, password)
search_target(driver)
target_post = find_post(driver)
if target_post == 0:
    print("Post not found! May be it's a video or text post")
    exit()
    driver.quit()
path = download_post(target_post)
clear_cookie(driver)
login(driver, u_name, password)
locate_upload(driver)
select_post(path)
click_upload()
move_post()
driver.quit()

