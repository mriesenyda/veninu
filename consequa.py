from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Find the close button using XPath
close_btn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, close_btn_xpath))
)

# Click the close button
close_btn.click()
