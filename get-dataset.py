import os, requests, json, pickle, re
import os.path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def load_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--start-maximized")
    options.add_argument('log-level=3')

    driver = webdriver.Chrome(executable_path="C:\\Users\\chromedriver.exe", options=options)

    return driver

def get_user_followers(driver, username):
    user_link = "https://open.spotify.com/user/{}/followers".format(username)
    driver.get(user_link)
    driver.implicitly_wait(5)

    users_element = driver.find_elements_by_class_name("f7ebc3d96230ee12a84a9b0b4b81bb8f-scss")
    users_id = []

    for el in users_element:
        user_link = el.get_attribute("href")
        user_id = user_link.split("/")[-1]
        users_id.append(user_id)

    return users_id

def get_playlists_id(driver, username):
    user_link = "https://open.spotify.com/user/{}/playlists".format(username)
    driver.get(user_link)
    
    playlist_element = driver.find_elements_by_class_name("f7ebc3d96230ee12a84a9b0b4b81bb8f-scss")
    playlists_id = []

    for el in playlist_element:
        playlist_link = el.get_attribute("href")
        playlist_id = playlist_link.split("/")[-1]
        playlists_id.append(playlist_id)

    return playlists_id


if __name__ == '__main__':
    driver = load_driver()
    users_id = get_user_followers(driver, "rachelvennya")

    playlists_id = []
    for user in users_id:
        user_playlists = get_playlists_id(driver, user)
        playlists_id += user_playlists