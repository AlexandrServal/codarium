from selene import have
from selene.support.shared import browser

browser.config.hold_browser_open = True
browser.open("http://todomvc.com/examples/emberjs/")


browser.element('[id="new-todo"]').type('a').press_enter()
browser.element('[id="new-todo"]').type('b').press_enter()
browser.element('[id="new-todo"]').type('c').press_enter()

browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

browser.element('#todo-list>li:nth-child(2) .toggle').click()
browser.element('#todo-list>li:nth-child(2)').should(have.css_class('completed'))
browser.element('#todo-list>li:nth-child(1)').should(have.no.css_class('completed'))
browser.element('#todo-list>li:nth-child(3)').should(have.no.css_class('completed'))

#browser.close()