from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.edge.options import Options as edge_options


class WebdriverFactory:
    def __init__(self, browser, headless=False):
        self.browser = browser
        self.headless = headless
        self.drive = None


    def get_driver_instance(self):
        if self.browser.lower() == 'chrome':
            chr_opt = chrome_options()
            if self.headless:
                chr_opt.add_argument("--headless")
            self.driver = webdriver.Chrome(options=chr_opt)
        elif self.browser.lower() == 'firefox':
            fr_opt = firefox_options()
            if self.headless:
                fr_opt.add_argument("--headless")
            self.driver = webdriver.Firefox(options=fr_opt)

        elif self.browser.lower() == 'edge':
            edge_opt = edge_options()
            if self.headless:
                edge_opt.add_argument("--headless")
            self.driver = webdriver.Firefox(options=edge_opt)

        return self.driver

