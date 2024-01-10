from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to your webdriver executable
webdriver_path = '/path/to/chromedriver'  # Replace with the actual path

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Open the URL
url = "https://jqueryui.com/droppable/"
driver.get(url)

try:
    # Switch to the iframe containing the draggable elements
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

    # Locate the draggable element
    draggable_element = driver.find_element(By.ID, "draggable")

    # Locate the droppable element
    droppable_element = driver.find_element(By.ID, "droppable")

    # Perform the drag-and-drop operation using ActionChains
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable_element, droppable_element).perform()

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Switch back to the default content (outside the iframe)
    driver.switch_to.default_content()

    # Close the browser after completion
    driver.quit()
