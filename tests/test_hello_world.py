from selenium.webdriver.common.keys import Keys

from chromehead.driver import Head


def test_driver(event, driver):
    search_term = "headless chrome"

    h = Head(headless=False)

    h.driver.get("http://www.google.com")
    search_bar = h.driver.find_element_by_xpath("//input[@title='Search']")
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.ENTER)

    result_elements = h.driver.find_elements_by_xpath(
        "//div[@class='r']/a[@ping]")
    results_links = [x.get_attribute("href") for x in result_elements]
    print(results_links)
    
    assert results_links, "No links extracted"
