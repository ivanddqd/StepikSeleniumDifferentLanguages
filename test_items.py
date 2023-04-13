from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_page_contain_button(browser):
    browser.get(url)
    #time.sleep(30)
    elements = browser.find_elements(By.CSS_SELECTOR, "div div div div form button")
    assert len(elements) > 0 and elements[0].is_enabled(), "Button not found!"

