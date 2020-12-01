from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

# Arrange
browser.config.hold_browser_open = True # Задержка браузера
browser.open("http://todomvc.com/examples/emberjs/")

# Act
s('[id="new-todo"]').type('listen lesson').press_enter() # Поиск Элемента по ID
s('[id="new-todo"]').type('have a rest').press_enter() # Ввод текста
s('[id="new-todo"]').type('do home work').press_enter()

# Assert
ss('[id="todo-list"] li').should(have.exact_texts('listen lesson', 'have a rest', 'do home work'))
# Подсчет элементов

s('[id="todo-list"] li:nth-child(2) .toggle').click()
browser.element('[id="todo-list"] li:nth-child(2)').should(have.css_class('completed'))
browser.element('[id="todo-list"] li:nth-child(1)').should(have.no.css_class('completed'))
browser.element('[id="todo-list"] li:nth-child(2)').should(have.no.css_class('completed'))
