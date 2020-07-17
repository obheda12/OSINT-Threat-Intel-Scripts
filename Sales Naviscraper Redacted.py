#Welcome to the Naviscraper
print("""
 _____       _             _   _             _
/  ___|     | |           | \ | |           (_)
\ `--.  __ _| | ___  ___  |  \| | __ ___   ___ ___  ___ _ __ __ _ _ __   ___ _ __
 `--. \/ _` | |/ _ \/ __| | . ` |/ _` \ \ / / / __|/ __| '__/ _` | '_ \ / _ \ '__|
/\__/ / (_| | |  __/\__ \ | |\  | (_| |\ V /| \__ \ (__| | | (_| | |_) |  __/ |
\____/ \__,_|_|\___||___/ \_| \_/\__,_| \_/ |_|___/\___|_|  \__,_| .__/ \___|_|
                                                                 | |
                                                                 |_|
""")

print("""

Author: Omar Bheda
Version: 1.0
Last Updated: 2/11/2020

The Sales Naviscraper utilizes LinkedIn Sales Navigator and the
'Sales Navigator Search Export' phantom from Phantombuster to scrape LinkedIn Profiles
to be used in Open Source Intelligence Gathering activities such as email guessing.

The Naviscraper can only scrape 2,500 profiles at a time. In order to obtain over
2,500 results, the usage of filtering is required. Filtering capabilities are built
into the scraper for clients larger than 2,500 profile results.

""")

#Drivers for Chrome Headless Browser
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
driver = webdriver.Chrome('.PATH/TO/CHROMEDRIVER)
driver.get('https://linkedin.com/sales')

#---Login into Sales Navigator---

#Username Input
username = driver.find_element_by_id('username')
username.send_keys('*REDACTED*')

#Password Input
password = driver.find_element_by_id('password')
password.send_keys("*REDACTED*")

#Logon
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
log_in_button.click()

#sleep to avoid race conditions
time.sleep(1.0)

#Get Session Cookie
session_cookie_dictionary = driver.get_cookie('li_at')
actual_session_cookie = session_cookie_dictionary['value']
print(actual_session_cookie)

#Search by Company Name
search = driver.find_element_by_name('keywords')
print("TEST")
print(search)
search_string = input('Company Name (enter full name of company): ')
print("")
search.send_keys(search_string)
search.send_keys(Keys.RETURN)

#sleep to avoid race conditions
time.sleep(3.0)

#Company Sales Navigator Page
all_employees_link = driver.find_element_by_xpath('//*[@data-control-name="hero_card_all_employees"]')
all_employees_link.click()

#Filter Results

#Filter Options

#Open Function Filter
open_function_filter = driver.find_element_by_xpath('//*[@data-test-filter-code="F"]')
open_function_filter.click()

#sleep to avoid race conditions
time.sleep(3.0)

#Set Function Filters
def SetFunctionFilters():
    filter_menu_list = []
    filter_function_list = []

    try:
        finance_filter = driver.find_element_by_xpath('//*[contains(@title, "Finance")]')
        filter_menu_list.append(finance_filter.get_attribute('innerHTML'))
        filter_function_list.append(finance_filter)
    except:
        pass

    try:
        engineering_filter = driver.find_element_by_xpath('//*[contains(@title, "Engineering")]')
        filter_menu_list.append(engineering_filter.get_attribute('innerHTML'))
        filter_function_list.append(engineering_filter)


    except:
        pass

    try:
        administrative_filter = driver.find_element_by_xpath('//*[contains(@title, "Administrative")]')
        filter_menu_list.append(administrative_filter.get_attribute('innerHTML'))
        filter_function_list.append(administrative_filter)


    except:
        pass

    try:
        healthcare_services_filter = driver.find_element_by_xpath('//*[contains(@title, "Healthcare Services")]')
        filter_menu_list.append(healthcare_services_filter.get_attribute('innerHTML'))
        filter_function_list.append(healthcare_services_filter)


    except:
        pass

    try:
        it_filter = driver.find_element_by_xpath('//*[contains(@title, "Information Technology")]')
        filter_menu_list.append(it_filter.get_attribute('innerHTML'))
        filter_function_list.append(it_filter)


    except:
        pass

    try:
        bus_dev_filter = driver.find_element_by_xpath('//*[contains(@title, "Business Development")]')
        filter_menu_list.append(bus_dev_filter.get_attribute('innerHTML'))
        filter_function_list.append(bus_dev_filter)


    except:
        pass

    try:
        sales_filter = driver.find_element_by_xpath('//*[contains(@title, "Sales")]')
        filter_menu_list.append(sales_filter.get_attribute('innerHTML'))
        filter_function_list.append(sales_filter)


    except:
        pass

    try:
        marketing_filter = driver.find_element_by_xpath('//*[contains(@title, "Marketing")]')
        filter_menu_list.append(marketing_filter.get_attribute('innerHTML'))
        filter_function_list.append(marketing_filter)


    except:
        pass

    try:
        operations_filter = driver.find_element_by_xpath('//*[contains(@title, "Operations")]')
        filter_menu_list.append(operations_filter.get_attribute('innerHTML'))
        filter_function_list.append(operations_filter)


    except:
        pass

    try:
        hr_filter = driver.find_element_by_xpath('//*[contains(@title, "Human Resources")]')
        filter_menu_list.append(hr_filter.get_attribute('innerHTML'))
        filter_function_list.append(hr_filter)


    except:
        pass

    try:
        pm_filter = driver.find_element_by_xpath('//*[contains(@title, "Product Management")]')
        filter_menu_list.append(pm_filter.get_attribute('innerHTML'))
        filter_function_list.append(pm_filter)


    except:
        pass

    try:
        support_filter = driver.find_element_by_xpath('//*[contains(@title, "Support")]')
        filter_menu_list.append(support_filter.get_attribute('innerHTML'))
        filter_function_list.append(support_filter)


    except:
        pass

    try:
        program_and_pm_filter = driver.find_element_by_xpath('//*[contains(@title, "Program and Project")]')
        filter_menu_list.append(program_and_pm_filter.get_attribute('innerHTML'))
        filter_function_list.append(program_and_pm_filter)


    except:
        pass

    try:
        consulting_filter = driver.find_element_by_xpath('//*[contains(@title, "Consulting")]')
        filter_menu_list.append(consulting_filter.get_attribute('innerHTML'))
        filter_function_list.append(consulting_filter)


    except:
        pass

    try:
        research_filter = driver.find_element_by_xpath('//*[contains(@title, "Research")]')
        filter_menu_list.append(research_filter.get_attribute('innerHTML'))
        filter_function_list.append(research_filter)


    except:
        pass

    try:
        legal_filter = driver.find_element_by_xpath('//*[contains(@title, "Legal")]')
        filter_menu_list.append(legal_filter.get_attribute('innerHTML'))
        filter_function_list.append(legal_filter)


    except:
        pass

    try:
        education_filter = driver.find_element_by_xpath('//*[contains(@title, "Education")]')
        filter_menu_list.append(pm_filter.get_attribute('innerHTML'))
        filter_function_list.append(education_filter)


    except:
        pass

    try:
        arts_desig_filter = driver.find_element_by_xpath('//*[contains(@title, "Arts and Design")]')
        filter_menu_list.append(arts_desig_filter.get_attribute('innerHTML'))
        filter_function_list.append(arts_desig_filter)

    except:
        pass

    try:
        media_communications = driver.find_element_by_xpath('//*[contains(@title, "Media and Communications")]')
        filter_menu_list.append(media_communications.get_attribute('innerHTML'))
        filter_function_list.append(media_communications)


    except:
        pass

    try:
        community_filter = driver.find_element_by_xpath('//*[contains(@title, "Community and")]')
        filter_menu_list.append(community_filter.get_attribute('innerHTML'))
        filter_function_list.append(community_filter)


    except:
        pass

    return filter_function_list


#TODO: TRY/EXCEPT handling of non-present filters and dynamic list creation
#TODO: Show dynamic filters output using a for loop and a list

total_results = driver.find_element_by_id('search-spotlight-tab-ALL').text
print("______________")
print("")
print(total_results)
print("______________")
print("")
print("--- FUNCTION FILTER OPTIONS ---")

#Show function menu
number = 1
filter_function_list = SetFunctionFilters()
print("0. Skip Function Filter")
for i in range(0, len(filter_function_list)):
    filter_function_list[i] = filter_function_list[i].text
    print(str(number) + ". " + filter_function_list[i])
    number = number + 1
filter_function_list = SetFunctionFilters()

#Filter Input
print("")
filter_flag = "Y"

#Filter Selection
while filter_flag == "Y" or filter_flag == "y":
    print("(NOTE: Only select a filter if total results are above 2500.)")
    print("")
    filter_input = input("To select a filter, enter its corresponding number: ")
    print("")

    #Tried to make cleaner code
    # filter_number = 1
    #
    # for i in range(0,len(filter_function_list):
    #     if filter_input = filter_number:
    #         filter_function_list[filter_number].click()

    if filter_input == "0":
        break;

    if filter_input == "1":
        filter_function_list[0].click()
        time.sleep(3.0)


    if filter_input == "2":
        filter_function_list[1].click()
        time.sleep(3.0)



    if filter_input == "3":
        filter_function_list[2].click()
        time.sleep(3.0)



    if filter_input == "4":
        filter_function_list[3].click()
        time.sleep(3.0)



    if filter_input == "5":
        filter_function_list[4].click()
        time.sleep(3.0)



    if filter_input == "6":
        filter_function_list[5].click()
        time.sleep(3.0)



    if filter_input == "7":
        filter_function_list[6].click()
        time.sleep(3.0)


    if filter_input == "8":
        filter_function_list[7].click()
        time.sleep(3.0)


    if filter_input == "9":
        filter_function_list[8].click()
        time.sleep(3.0)


    if filter_input == "10":
        filter_function_list[9].click()
        time.sleep(3.0)


    if filter_input == "11":
        filter_function_list[10].click()
        time.sleep(3.0)


    if filter_input == "12":
        filter_function_list[11].click()
        time.sleep(3.0)


    if filter_input == "13":
        filter_function_list[12].click()
        time.sleep(3.0)


    if filter_input == "14":
        filter_function_list[13].click()
        time.sleep(3.0)


    filter_function_list = SetFunctionFilters()

    total_results = driver.find_element_by_id('search-spotlight-tab-ALL').text
    print("______________")
    print(total_results)
    print("______________")
    print("")

    filter_flag = input("Would you like to select additional filters? 'Y' for Yes 'N' for No: ")

#Open Seniority Filter
open_seniority_filter = driver.find_element_by_xpath('//*[@data-test-filter-code="SE"]')
open_seniority_filter.click()

#Sleep to avoid race conditions
time.sleep(3.0)

#Set Seniority Filters
def SetSeniorityFilters():
    filter_menu_list_seniority = []
    filter_seniority_list = []

    try:
        owner_filter = driver.find_element_by_xpath('//*[contains(@title, "Owner")]')
        filter_menu_list_seniority.append(owner_filter.get_attribute('innerHTML'))
        filter_seniority_list.append(owner_filter)
    except:
        pass

    try:
        partner_filter = driver.find_element_by_xpath('//*[contains(@title, "Partner")]')
        filter_menu_list_seniority.append(partner_filter.get_attribute('innerHTML'))
        filter_seniority_list.append(partner_filter)


    except:
        pass

    try:
        cxo_filter = driver.find_element_by_xpath('//*[contains(@title, "CXO")]')
        filter_menu_list_seniority.append(cxo_filter.get_attribute('innerHTML'))
        filter_seniority_list.append(cxo_filter)


    except:
        pass

    try:
        director_filter = driver.find_element_by_xpath('//*[contains(@title, "Director")]')
        filter_menu_list_seniority.append(director_filter.get_attribute('innerHTML'))
        filter_seniority_list.append(director_filter)


    except:
        pass

    try:
        manager_filter = driver.find_element_by_xpath('//*[contains(@title, "Manager")]')
        filter_menu_list_seniority.append(manager_filter.get_attribute('innerHTML'))
        filter_seniority_list.append(manager_filter)


    except:
        pass

    try:
        senior_filter = driver.find_element_by_xpath('//*[contains(@title, "Senior")]')
        filter_menu_list_seniority.append(senior_filter.get_attribute('innerHTML'))
        filter_seniority_list.append(senior_filter)


    except:
        pass

    try:
        entry_filter = driver.find_element_by_xpath('//*[contains(@title, "Entry")]')
        filter_menu_list_seniority.append(entry_filter.get_attribute('innerHTML'))
        filter_seniority_list.append(entry_filter)


    except:
        pass

    try:
        training_filter = driver.find_element_by_xpath('//*[contains(@title, "Training")]')
        filter_menu_list_seniority.append(training_filter.get_attribute('innerHTML'))
        filter_seniority_list.append(training_filter)


    except:
        pass

    try:
        unpaid_filter = driver.find_element_by_xpath('//*[contains(@title, "Unpaid")]')
        filter_menu_list_seniority.append(unpaid_filter.get_attribute('innerHTML'))
        filter_seniority_list.append(unpaid_filter)


    except:
        pass

    return filter_seniority_list

#Show Seniority menu
number = 1
filter_seniority_list = SetSeniorityFilters()
print("")
print("--- SENIORITY FILTER OPTIONS ---")
print("0. Skip Seniority Filter")
for i in range(0, len(filter_seniority_list)):
    filter_seniority_list[i] = filter_seniority_list[i].text
    print(str(number) + ". " + filter_seniority_list[i])
    number = number + 1
filter_seniority_list = SetSeniorityFilters()


#Filter Input
print("")
filter_flag = "Y"

#Filter Selection
while filter_flag == "Y" or filter_flag == "y":
    print("NOTE: Only select a filter if total results are above 2500.")
    print("")
    filter_input = input("To select a filter, enter its corresponding number: ")
    print("")

    #Tried to make cleaner code
    # filter_number = 1
    #
    # for i in range(0,len(filter_function_list):
    #     if filter_input = filter_number:
    #         filter_function_list[filter_number].click()

    if filter_input == "0":
        break;

    if filter_input == "1":
        filter_seniority_list[0].click()
        time.sleep(3.0)


    if filter_input == "2":
        filter_seniority_list[1].click()
        time.sleep(3.0)



    if filter_input == "3":
        filter_seniority_list[2].click()
        time.sleep(3.0)



    if filter_input == "4":
        filter_seniority_list[3].click()
        time.sleep(3.0)



    if filter_input == "5":
        filter_seniority_list[4].click()
        time.sleep(3.0)



    if filter_input == "6":
        filter_seniority_list[5].click()
        time.sleep(3.0)



    if filter_input == "7":
        filter_seniority_list[6].click()
        time.sleep(3.0)


    if filter_input == "8":
        filter_seniority_list[7].click()
        time.sleep(3.0)


    if filter_input == "9":
        filter_seniority_list[8].click()
        time.sleep(3.0)


    if filter_input == "10":
        filter_seniority_list[9].click()
        time.sleep(3.0)

    total_results = driver.find_element_by_id('search-spotlight-tab-ALL').text
    print("______________")
    print(total_results)
    print("______________")
    print("")

    filter_seniority_list = SetSeniorityFilters()

    filter_flag = input("Would you like to select additional filters? 'Y' for Yes 'N' for No: ")


#Copy address to be used in Phantombuster
current_address = driver.current_url


current_date = (time.strftime("%m/%d/%Y"))
results_name_string = search_string + " - Employees - " + current_date

#Launch Sales Navigator Scrape
url = "*REDACTED*"

querystring = {"argument":"{ \"sessionCookie\": \""+actual_session_cookie+"\", \t\"searches\": \""+current_address+"\", \t\"csvName\": \""+results_name_string+"\",  \"removeDuplicateProfiles\": true }"}

headers = {
    'accept': "application/json",
    'x-phantombuster-key-1': "*REDACTED*"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

print("Beginning Scraping...")

#Abort Sales Navigator Scrape
#Sales Navigator Abort
abort_input = input("Would you like to abort? ('Y' to abort or 'N' to continue scraping)")
if abort_input == 'Y' or abort_input =='y':
    url = "*REDACTED*"

    headers = {
        'accept': "application/json",
        'x-phantombuster-key-1': "*REDACTED*"
    }

    response = requests.request("POST", url, headers=headers)

    print("Scrape Aborted...")

else:
    print("Continue scraping...")



















