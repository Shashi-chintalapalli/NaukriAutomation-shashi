from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Your Naukri credentials
username = "sample@gmail.com"
password = "Sample@123"


# Set up the Chrome driver (Make sure chromedriver is in your PATH or specify path)
driver = webdriver.Chrome()

try:
    # Step 1: Open Naukri login page
    driver.get("https://www.naukri.com/nlogin/login")

    wait = WebDriverWait(driver, 5)

    # Step 2: Enter username and password
    wait.until(EC.presence_of_element_located((By.ID, "usernameField"))).send_keys(username)
    driver.find_element(By.ID, "passwordField").send_keys(password)

    # Step 3: Click Login button
    driver.find_element(By.XPATH, '//button[text()="Login"]').click()

    # Step 4: Wait until login is successful - wait for some element on dashboard/profile page or just wait fixed time
    time.sleep(10)  # waiting for redirect after login

    # Step 5: Navigate to your profile page directly by URL
    profile_url = "https://www.naukri.com/mnjuser/profile?id=&altresid"
    driver.get(profile_url)

    # Wait for the profile page to load
    time.sleep(5)

    # Step 6: Click the Edit button for Resume Headline (the pencil icon or edit span)
    # This selector may need to be adjusted if the site changes. Here we use the span with class "edit icon"
    edit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.edit.icon")))
    edit_button.click()

    # Step 7: Wait for the textarea to be visible and then append a dot or space
    textarea = wait.until(EC.visibility_of_element_located((By.ID, "resumeHeadlineTxt")))
    current_text = textarea.get_attribute("value")

    # Append a dot or space to force update
    new_text = current_text + " ."
    textarea.clear()
    textarea.send_keys(new_text)

    # Step 8: Click Save button
    save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-dark-ot[type='submit']")))
    save_button.click()

    # Step 9: Wait a bit to ensure save is done
    time.sleep(5)

    print("Profile headline updated successfully!")

finally:
    # Close the browser
    driver.quit()
