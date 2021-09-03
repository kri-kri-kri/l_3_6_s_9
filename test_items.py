import pytest
from selenium import webdriver

class TestMainPage1():
    def add_to_basket_btn_seen(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
          
        browser.get(link)
       

        correct_text_elt = browser.find_element_by_css_selector("button.btn-add-to-basket")
        correct_text = correct_text_elt.text
        assert correct_text, \
        f"Wrong message, got no button instead of {correct_text}"
