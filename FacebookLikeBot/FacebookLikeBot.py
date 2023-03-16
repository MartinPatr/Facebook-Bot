from selenium import webdriver

# Receiving the Email and Passwords
email = input("Enter your email: ")
password = input("Enter your password: ")

# Set up drivers
driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")

# Find the email or phone field and enter the email or phone number
email_field = driver.find_element_by_id("email")
email_field.send_keys(email)

# Find the password field and enter the password
password_field = driver.find_element_by_id("pass")
password_field.send_keys(password)

# Find the login button and click it
login_button = driver.find_element_by_id("loginbutton")
login_button.click()

# Wait for the page to load
driver.implicitly_wait(10)

# Scroll down to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(2) 

# Find all the like buttons on the page
like_buttons = driver.find_elements_by_css_selector("div[data-pagelet^='FeedUnit'] div[data-testid='fb-ufi-likelink'] a")

# Loop through the like buttons and click the next one that you haven't already liked
for button in like_buttons:
    if button.get_attribute("aria-pressed") == "false":
        button.click()
        break

# Close the browser
driver.quit()