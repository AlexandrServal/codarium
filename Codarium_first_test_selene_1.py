from selene import have, driver
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

# Arrange
browser.config.hold_browser_open = True # Задержка браузера
browser.open("https://www.google.com/")

# Act
s('[ class="gLFyf gsfi" ]').type('yashaka selene').press_enter() # Поиск Элемента по ID class href
s('[class="LC20lb DKV0Md"]').click()
# s('[href="https://pypi.org/project/selene/2.0.0a33/" ]').click()
# <input placeholder="Search the web to plant trees..." aria-label="Search Form" type="search" name="q" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" autofocus="autofocus" required="required" data-test-id="search-form-input" value="" class="input" data-v-b22df982="">
# __layout > div > section > div.content > form > div.input-wrapper > input
# //*[@id="__layout"]/div/section/div[1]/form/div[1]/input




ss(' [href="https://pypi.org/project/selene/2.0.0a33/" ] li')

print('Ссылок на странице =', len(ss('[ href="/yashaka/selene"]')))