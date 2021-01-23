from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from time import sleep
import os


# Credentials
user = ''
password = ''

# Preparation Navigateur

# Cache le navigateur
os.environ['MOZ_HEADLESS'] = '1'
options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
# Où le navigateur est rangé sur votre pc
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox"

driver = webdriver.Firefox(
    executable_path='selenium/geckodriver.exe', service_log_path='selenium/geckodriver.log')

# Connexion
driver.get('https://www.lms.7speaking.com/newsite/controlnew/newlogin.cfm')

sleep(2)

# Username
text_area = driver.find_element_by_id('username')
text_area.send_keys(user)

# Password
text_area = driver.find_element_by_id('password')
text_area.send_keys(password)

# Connection
submit_button = button = driver.find_element_by_xpath("//input[@type='button']")
submit_button.click()

sleep(5)

# Le bot est sur la page d'acceuil
print("Connexion réussi")

# Lien d'une vidéo au pif pour faire des heures
driver.get("https://www.lms.7speaking.com/newsite/assist/index.cfm?docID=12832")

btn_play_pause = driver.find_element_by_id('playpause')

# Lancement vidéo
print("Vidéo lancée")
btn_play_pause.click()

# On coupe le son comme un porc
print("Coupe le son")
btn_no_sound = driver.find_element_by_id('voldec')

for i in range(0, 20):
    btn_no_sound.click()
    sleep(0.2)

# Joue la vidéo en boucle
while 1:
    # Si la vidéo est fini ou en pause, la relance
    if btn_play_pause.get_attribute('data-state') == 'play':
        print("Vidéo relancée")
        btn_play_pause.click()
    else:
        sleep(5)











