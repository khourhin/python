# --------------------------------------------------------------------------------
# Automatically download formation videos
# --------------------------------------------------------------------------------

from selenium import webdriver
import urllib

unow_url = "https://auth.unow.fr/"
user = "etienne.kornobis@pasteur.fr"
pwd = "pol78lux"


driver = webdriver.Firefox()

# Necessary for the driver to "follow the change of url after
# specifying the email address". Otherwise, driver cannot find the
# element with name password
driver.implicitly_wait(5)

driver.get(unow_url)

elem = driver.find_element_by_name("email")
elem.send_keys(user)

submit = driver.find_element_by_tag_name("button")
submit.click()

elem2 = driver.find_element_by_name("password")
elem2.send_keys(pwd)

# Selecting button by its type
submit = driver.find_element_by_xpath("//button[@type='submit']")
submit.click()

driver.find_element_by_link_text('Voir le mur de la session').click()
driver.find_element_by_link_text('Téléchargements').click()

# Get all links with mp4 videos
videos = driver.find_elements_by_xpath("//a[@download[contains(.,'mp4')]]")

# TODO: replace by a for loop to get all videos from the website
urllib.request.urlretrieve(videos[0].get_attribute('href'), 'test_video.mp4')
