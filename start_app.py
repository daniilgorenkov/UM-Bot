from pywinauto.application import Application
import pyautogui as root

def get_model_path():
    """Получение полного пути до приложения"""
    path_question = input("Оставить старый путь к UM Simulation? Y/n: ")
    if path_question == "Y":
        APP_PATH = "C:\\Program Files\\UM Software Lab\\Universal Mechanism\\9\\bin\\umsimul.exe"
    
    elif path_question =="n":
        APP_PATH = input("Введите полный путь до файла: ")
    
    return APP_PATH

def start_app(PATH:str):
    """Запуск самого приложения"""
    app = Application(backend="uia").start(PATH)

def is_running():
    inp = input("Программа уже запущена? Y/n: ")

    if inp == "Y":
        return True
    
    elif inp == "n":
        return False