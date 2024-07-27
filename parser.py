from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from config.py import *


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)  # вместо Chrome, вставляем название вашего браузера


def logining(url_main):
    global driver

    driver.get(url_main)
    driver.implicitly_wait(10)
    
    login = driver.find_element(By.NAME, "login")
    login.clear()
    login.send_keys(str(username))
    login.send_keys(Keys.RETURN)

    passwd = driver.find_element(By.NAME, "passwd")
    passwd.clear()
    passwd.send_keys(str(password))
    passwd.send_keys(Keys.RETURN)


def download(baze):
    legend, name = baze
    symbols = ['/', '\\', '|', '<', '>', '"', '?', '*', ':']
    for symbol in symbols:
        name = name.replace(symbol, '')
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

    if structure()[0]:
        download(structure())
    else:
        button_uslovie = driver.find_elements(By.CLASS_NAME, 'nav-tab__inner')
        button_uslovie[1].click()
        download(structure())

    escape = driver.find_element(By.CLASS_NAME, 'nav-tab__inner')
    escape.click()


def pars_one_lesson(number_of_lesson):
    works = driver.find_elements(By.CLASS_NAME, "link-list__link")
    work = works[number_of_lesson]
    work.click()

    uroks = driver.find_elements(By.CLASS_NAME, 'Accordion-Item')
    for num_of_work in range(len(uroks)):
        pars_one_work(num_of_work)

    escape = driver.find_element(By.CLASS_NAME, 'nav-tab__inner')
    escape.click()


if __name__ == '__main__':
    logining(URL)
    for num_of_les in range(col_of_lessons):
        pars_one_lesson(num_of_les)
