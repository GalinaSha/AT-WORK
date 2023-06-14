import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='class')
def selenium(pytestconfig):
    options = Options()
    browser_name = pytestconfig.getini("browser_name")
    logging.info(f'Prepare {browser_name} browser...')

    if pytestconfig.getini("headless") == "True" and browser_name == "chrome":
        options.add_argument("--headless")

    # Дожидаемся загрузки элемента, без ожидания загрузки всей страницы
    #  options.page_load_strategy = 'eager'

    # Заменяем создание удаленного веб-драйвера на создание локального драйвера Chrome
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)  # добавить неявное ожидание в 15 секунд

    logging.info(f'Browser {browser_name} has been started.')
    yield driver
    logging.info(f'Close {browser_name} browser...')
    driver.quit()



#Код для запуска с селенойдом

# import logging
# import pytest
# from selenium.webdriver import Remote
# from selenium.webdriver.chrome.options import Options
#
#
# @pytest.fixture(scope='class')
# def selenium(pytestconfig):
#     options = Options()
#     browser_name = pytestconfig.getini("browser_name")
#     logging.info(f'Prepare {browser_name} browser...')
#
#     if pytestconfig.getini("headless") == "True" and browser_name == "chrome":
#         options.add_argument("--headless")
#     driver = Remote(
#         desired_capabilities={
#             "browserName": pytestconfig.getini("browser_name"),
#             "browserVersion": pytestconfig.getini("browser_version")
#         },
#         command_executor=pytestconfig.getini("selenium_url"),
#         options=options
#     )
#     driver.implicitly_wait(15)  # добавить неявное ожидание в 15 секунд
#     logging.info(f'Browser {browser_name} has been started.')
#     yield driver
#     logging.info(f'Close {browser_name} browser...')
#     driver.quit()
#