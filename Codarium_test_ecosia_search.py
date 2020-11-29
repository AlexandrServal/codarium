from selene import have
from selene.support.shared import browser

#Arrenge
browser.config.hold_browser_open = True
browser.open("https://www.ecosia.org/")

#Action
browser.element('[data-test-id="search-form-input"]').type('yashaka selene').press_enter()
browser.all('.result').first.click()

#Assert
browser.all('[href="/yashaka/selene"]').should(have.size(3))