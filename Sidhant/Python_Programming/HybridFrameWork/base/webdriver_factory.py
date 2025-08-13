<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chr_option
from selenium.webdriver.edge.options import Options as edge_option
from selenium.webdriver.firefox.options import Options as firefox_option

class WebdriverFactory:
    def __init__(self, browser, headless): # this mean the test will run with a visible browser window.
=======
class WebdriverFactory:
    def __init__(self,browser,headless):
>>>>>>> origin/main
        self.browser = browser
        self.headless = headless

    def get_driver_instance(self):
<<<<<<< HEAD

        if self.browser.lower() == 'chrome':
            option1 = chr_option()
            if self.headless:
                option1.add_argument("--disable-headless-mode")  # enable headless mode
            driver = webdriver.Chrome(options=option1)
        elif self.browser.lower() == 'edge':
            option2 = edge_option()
            if self.headless:
                option2.add_argument("--headless")  # enable headless mode
            driver = webdriver.Edge(options=option2)
        elif self.browser.lower() == 'firefox':
            option3 = firefox_option()
            if self.headless:
                option3.add_argument("--headless")  # enable headless mode
            driver = webdriver.Firefox(options=option3)
        return driver
=======
        if self.browser.lower() == 'chrome':
            option1 = chr_option()
            if self.headless:
                option1.add_argument( "--headless" )  # enable headless mode
            driver = webdriver.Chrome( options=option1 )
        elif self.browser.lower() == 'edge':
            option2 = edge_option()
            if self.headless:
                option2.add_argument( "--headless" )  # enable headless mode
            driver = webdriver.Edge( options=option2 )
        elif self.browser.lower() == 'firefox':
            option3 = firefox_option()
            if self.headless:
                option3.add_argument( "--headless" )  # enable headless mode
            driver = webdriver.Firefox( options=option3 )
>>>>>>> origin/main
