from selenium import webdriver
from selenium.webdriver.common.by import By

#выпадающее меню в хедере (наведение на него)
def header_menu(selenium):
    profile_hover = selenium.find_element(By.CLASS_NAME, "upper-case__profile-user")
    action_chains = webdriver.ActionChains(selenium)
    action_chains.move_to_element(profile_hover).perform()

#переключение аккаунта на физлицо
def profile_change_user(selenium):
    header_menu(selenium)
    profile_change_user = selenium.find_element(By.CLASS_NAME, "upper-case__profile-return")
    selenium.execute_script("arguments[0].click();", profile_change_user)

# Выход из аккаунта
def logout(selenium):
    header_menu(selenium)
    selenium.find_element(By.ID, "profile-logout").click()