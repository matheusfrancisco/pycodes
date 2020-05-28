from selenium import webdriver


class DuckDcukGo:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://duckduckgo.com/'
        self.search_bar = 'search_form_input_homepage'
        self.btn_search = 'search_button_homepage'

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_id(self.search_bar).send_keys(word)
        self.driver.find_element_by_id(self.btn_search).click()


ff = webdriver.Chrome()
dd = DuckDcukGo(ff)
dd.navigate()
dd.search("Live de Python")
#ff.quit()
