"""
This handler will be deployed in the cloud and we'll do a simple 
requests on the service to see if it returns the links.
"""
try:
    import unzip_requirements # For the aws lambda
except ImportError:
    pass

from selenium.webdriver.common.keys import Keys

from chromehead.driver import Head


def handle(event, context):


    h = Head(headless=event.get("headless", True))

    print("crawling")
    h.driver.get("http://www.google.com")
    search_bar = h.driver.find_element_by_xpath("//input[@title='Search']")
    search_bar.send_keys("headless chrome")
    search_bar.send_keys(Keys.ENTER)

    result_elements = h.driver.find_elements_by_xpath(
        "//div[@class='r']/a[@ping]")
    results_links = [x.get_attribute("href") for x in result_elements]
    print(results_links)
    
    return {"statusCode": 200, "body": results_links}
