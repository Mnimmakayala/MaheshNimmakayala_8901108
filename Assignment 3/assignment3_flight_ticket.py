# Importing required libraries

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Aircanada homepage
driver.get("https://www.aircanada.com/ca/en/aco/home.html")
time.sleep(8)

#Select the flight type
trip_type = driver.find_element("xpath","//*[@id='bkmgFlights_tripTypeSelector_O']")
trip_type.click()

#Check the airmiles offer
trip_offer_selection= driver.find_element("xpath","//*[@id='bkmg-tab-content-flight']/ac-bkmg-flights-tab/div/form/fieldset/div/ac-search-type-toggle/div/abc-checkbox")
trip_offer_selection.click()

#Fill the from details
trip_from = driver.find_element("xpath","//*[@id='bkmgFlights_origin_trip_1']")
trip_from.clear()
trip_from.click()
trip_from.send_keys("Toronto")

#Fill the to details
trip_to = driver.find_element("xpath","//*[@id='bkmgFlights_destination_trip_1']")
trip_to.clear()
trip_to.click()
trip_to.send_keys("Vienna")

#Fill the travel date details
trip_date = driver.find_element("xpath","//*[@id='bkmgFlights_travelDates_1']")
trip_date.clear()
trip_date.click()
trip_date.send_keys("22/08/2024")
date_dropdown = driver.find_element("xpath","//*[@id='bkmgFlights_travelDates_1-date-2024-08-22']/div")
date_dropdown.click()
time.sleep(1)

Click on the submit button
trip_submit = driver.find_element("xpath","//*[@id='bkmgFlights_findButton']/abc-ripple/div")
trip_submit.click()
time.sleep(10)

#CLose the popup
close_popup = driver.find_element("xpath","//*[@id='mat-dialog-title-0']/span")
close_popup.click()

