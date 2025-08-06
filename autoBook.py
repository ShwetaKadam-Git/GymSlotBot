from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Setup Chrome driver
service = Service("D:/STUTTGART/PROJECTS/autoBook/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Step 1: Open the calendar
calendar_url = "https://calendar.google.com/calendar/u/0/appointments/schedules/AcZssZ06yuRnqZ6BCkgtAJlU3dh3cWI0GINjEySTDjolrjWn3-rBAcE7MZNhSerTo7ziMJ7FSDHZ7Qwe?gv=true"
driver.get(calendar_url)
driver.maximize_window()
time.sleep(5)

# Step 2: Calculate the day after tomorrow
target_date = datetime.now() + timedelta(days=1)
target_day = target_date.strftime("%A, %B %d").replace(" 0", " ") # e.g., 'Thursday, August 7'
print("Target day:", target_day)

# Wait until the day section loads
time.sleep(5)

# Step 3: Find the section for the target day
day_section_xpath = f"//div[@role='list' and contains(@aria-label, '{target_day}')]"
day_section = driver.find_element(By.XPATH, day_section_xpath)

# Step 4: Get all slot buttons in that day
slot_buttons = day_section.find_elements(By.TAG_NAME, "button")

# Step 5: Filter for slots between 8:00am and 2:00pm
def is_time_in_range(time_str):
    # Convert time string like "9:30am" to 24-hour float
    time_obj = datetime.strptime(time_str, "%I:%M%p")
    time_float = time_obj.hour + time_obj.minute / 60
    return 8 <= time_float <= 18 # 8 AM to 2 PM

# Click the first available slot
for btn in slot_buttons:
    slot_time = btn.get_attribute("aria-label")  # e.g., '9:30am'
    if slot_time and is_time_in_range(slot_time):
        print("Booking slot at:", slot_time)
        btn.click()
        time.sleep(5)
        break
else:
    print("No suitable slot found.")

wait = WebDriverWait(driver, 20)  # instead of 10

# this was used to debug the button text in order to find the correct button
# buttons = driver.find_elements(By.XPATH, "//button")
# for b in buttons:
# print(b.text) -- 

try:
    book_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[contains(text(), 'Book')]]")
    ))
    # First Name
    first_name_input = wait.until(EC.visibility_of_element_located((By.ID, "c11")))
    first_name_input.clear()
    first_name_input.send_keys("Shweta")

    # Last Name
    last_name_input = wait.until(EC.visibility_of_element_located((By.ID, "c12")))
    last_name_input.clear()
    last_name_input.send_keys("Kadam")

    # Email
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "c13")))
    email_input.clear()
    email_input.send_keys("kadamshweta11111@gmail.com")
    
    book_button.click()
except:
    print("Could not find the 'Book' button.")



# Done
time.sleep(60)
driver.quit()



