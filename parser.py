from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from bs4 import BeautifulSoup as bs
import time
import os

username = None
password = None

driver = webdriver.Chrome()  # вместо Chrome, вставляем название вашего браузера
URL = 'URL'  # вставляем адресс главной страницы курса
col_of_lessons = 1  # вставляем колличество уроков в курсе


def log_pas_init():
    global username, password
    load_dotenv('password.env')
    username = os.getenv('name')
    password = os.getenv('password')


def logining(url_main):
    global driver

    log_pas_init()

    driver.get(url_main)
    driver.implocotly_wait(10)
    
    login = driver.find_element(By.NAME, "login")
    login.clear()
    login.send_keys(str(username))
    login.send_keys(Keys.RETURN)
    driver.implocotly_wait(10)

    passwd = driver.find_element(By.NAME, "passwd")
    passwd.clear()
    passwd.send_keys(str(password))
    passwd.send_keys(Keys.RETURN)
    driver.implocotly_wait(10)


def download(baze):
    legend, name = baze
    name = name.replace('/', '')
    name = name.replace('\\', '')
    name = name.replace('|', '')
    name = name.replace('<', '')
    name = name.replace('>', '')
    name = name.replace('"', '')
    name = name.replace('?', '')
    name = name.replace('*', '')
    name = name.replace(':', '')
    with open(str(name) + '.html', 'w+', encoding="utf-8") as file:
        file.write(str(legend))
        print(str(legend))
        file.write('\n')


def structure():
    source_data = driver.page_source
    soup = bs(source_data, 'lxml')
    legend = soup.find_all('div', {'class': ['problem-statement']})
    soup_name = soup.find('h1', {'class': ['heading heading_level_1 yde1c4--task-header__heading']})
    soup_name = soup_name.get_text(strip=True) if soup_name else ''
    print(soup_name)

    return legend, soup_name


def pars_one_work(number_of_work):
    uroks = driver.find_elements(By.CLASS_NAME, 'Accordion-Item')
    urok = uroks[number_of_work]
    urok.click()
    driver.implocotly_wait(10)

    if structure()[0]:
        download(structure())
    else:
        button_uslovie = driver.find_elements(By.CLASS_NAME, 'nav-tab__inner')
        button_uslovie[1].click()
        driver.implocotly_wait(10)
        download(structure())

    escape = driver.find_element(By.CLASS_NAME, 'nav-tab__inner')
    escape.click()

    driver.implocotly_wait(10)


def pars_one_lesson(number_of_lesson):
    works = driver.find_elements(By.CLASS_NAME, "link-list__link")
    work = works[number_of_lesson]
    work.click()
    driver.implocotly_wait(10)

    uroks = driver.find_elements(By.CLASS_NAME, 'Accordion-Item')
    for num_of_work in range(len(uroks)):
        pars_one_work(num_of_work)

    escape = driver.find_element(By.CLASS_NAME, 'nav-tab__inner')
    escape.click()

    driver.implocotly_wait(10)


if __name__ == '__main__':
    logining(URL)
    for num_of_les in range(col_of_lessons):
        pars_one_lesson(num_of_les)
