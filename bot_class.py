"""Класс работы бота"""
import os
import pyautogui as root
from tqdm import tqdm
from time import sleep
from loguru import logger

class UM_bot:
    def __init__(self,wagon: str = None,
                 way_type: str = None,
                 fault: str = None,
                 speed:int = None,
                 wheel_profile:str = None):
        
        self.wagon = wagon
        self.way_type = way_type
        self.fault = fault
        self.speed = speed
        self.wheel_profile = wheel_profile
        self.railway_eqipaje_position = (548,602)
        
        if self.wagon == "empty":
            self.path_to_save = r"C:/Users/Daniil/Desktop/simulation_results/empty"  #/empty/newwagonw
            logger.info("путь сохранения: empty")
        
        elif self.wagon == "loaded":
            self.path_to_save = r"C:/Users/Daniil/Desktop/simulation_results/loaded"
            logger.info("путь сохранения: loaded")

        self.name = (str(self.wagon)+"_"+str(self.way_type)+"_"+str(self.fault)+  # название файла сразу с типом вагона и т.д.
                "_"+str(self.speed)+"_"+str(self.wheel_profile))
        
        if "curve" in self.way_type: #ограничение скорости в кривой 
            if self.speed > 80:
                self.speed = 80

    def sleep_time(self):
        """
        Выбор времени на которое бот будет застывать, пока идет расчет
        """

        # Выбор времени при расчете в прямой
        if self.way_type == "straight":    
            if round(self.speed/3.6, 2) <= 11.11: # до 40 км/ч ждем 21 секунду
                self.wait_status_bar(21)          # время интеграции с запасом
            
            elif 11.11 < round(self.speed/3.6, 2) <= 22.22: # от 40 до 80 км/ч ждем 21 секунду
                self.wait_status_bar(21)          # время интеграции с запасом

            elif 22.22 < round(self.speed/3.6, 2) <= 33.34: # от 80 до 120 км/ч ждем 21 секунду
                self.wait_status_bar(21)          # время интеграции с запасом
            else:
                raise ValueError("Что-то не то с вводимой скоростью")

        # Выбор времени при расчете в кривой 350 м
        elif self.way_type == "curve_350":
            if round(self.speed/3.6, 2) <= 11.11: # до 40 км/ч ждем 300 секунд
                self.wait_status_bar(440)         # время интеграции с запасом
            
            elif 11.11 < round(self.speed/3.6, 2) <= 22.22: # от 40 до 80 км/ч ждем 150 секунд
                self.wait_status_bar(115)         # время интеграции с запасом

            else:
                raise ValueError("Что-то не то с вводимой скоростью, возможно она превышает задуманную")
        
        # Выбор времени при расчете в кривой 650 м
        elif self.way_type == "curve_650":
            if round(self.speed/3.6, 2) <= 11.11: # до 40 км/ч ждем  секунд
                self.wait_status_bar(550)         # время интеграции с запасом
            
            elif 11.11 < round(self.speed/3.6, 2) <= 22.22: # от 40 до 80 км/ч ждем 120 секунд
                self.wait_status_bar(120)         # время интеграции с запасом

            else:
                raise ValueError("Что-то не то с вводимой скоростью, возможно она превышает задуманную")



    def start_integration (self, v:float):
        """
        Функция начинает выполнение расчета вагона в Универсальном механизме
        """

        button_start_integration = (148, 1000) #кнопка 'интегрирование'
        button_ok_integration = (1056, 600) # кнопка ок после интеграции
        results_button = (976, 186)
        save_file_button = (1070, 448)

        path_position = (659,87)
        filename_position = (602, 604)
        extention_position = (578, 629)
        csv_button_position = (363,692)
        save_button = (788, 672)
        end_integration_position = (477, 908)             

        root.moveTo(button_start_integration) # кнопка начать интеграцию
        root.click()

        self.sleep_time()

        root.moveTo(button_ok_integration,duration=v) # завершить интеграцию
        root.click()

        root.moveTo(results_button,duration=v) # переменная с графика, которую надо сохранить
        root.click(button="RIGHT")

        root.moveTo(save_file_button,duration=v) # кнопка сохранить файл
        root.click()

        root.moveTo(path_position,duration=v) # навелся на строку пути в проводнике
        root.click()
        root.typewrite(self.path_to_save) # НЕПРАВИЛЬНО ИДЕТ К ЯЧЕЙКЕ ПУТИ ДО ФАЙЛА И ДАЛЕЕ ТОЖЕ
        root.press("enter") # тут возможно намудил

        root.moveTo(filename_position,duration=v) # пишу название файла
        root.click()
        root.typewrite(message=self.name) # название файла

        root.moveTo(extention_position,duration=v) # кнопка выбора расширения
        root.click()
        root.moveTo(csv_button_position,duration=v) # выбрать csv разрешение
        root.click()

        root.moveTo(save_button,duration=v) # сохранить файл в выбранной папке
        root.click()

        root.moveTo(end_integration_position,duration=v) # прервать интеграцию
        root.click()


    def change_speed(self):
        """
        Смена параметра скорости, перменную передавать в км/ч,
        внутри будет перевод в м/с
        """
        self.speed_position = (145,732)
        idetificators_position = (185,603)
        ok_button = (916,662)

        logger.info(f"скорость: {self.speed}")

        std_v = round((self.speed/3.6), 2)

        root.moveTo(idetificators_position)
        root.click()

        root.moveTo(self.speed_position)
        root.click()

        root.typewrite("{}".format(std_v))
        root.press("enter")
        
        root.moveTo(ok_button)
        root.click()


    def clear_speed (self):
        """
        Стираю введеное число функцией `change_speed()`
        """

        # speed_position = (133,732)
        idetificators_position = (185,603)

        root.moveTo(idetificators_position)
        root.click()

        root.moveTo(self.speed_position)
        root.click()
        self.backspace()
        self.backspace()
    
    @staticmethod
    def ctr_a():
        """
        Ctr+a
        """
        root.keyDown("ctrl")
        root.keyDown("a")

        root.keyUp("ctrl")
        root.keyUp("a")
    
    @staticmethod
    def backspace():
        root.press("backspace")
        root.press("backspace")
        root.press("backspace")

    def change_time_integration(self):
        """
        Смена количества времени интеграции, в секундах
        """
        integration_button_position = (79,599)
        seconds_window_position = (253,764)

        root.moveTo(integration_button_position) # вкладка интегратор
        root.click()

        root.moveTo(seconds_window_position) # ячейка секунд
        root.click()

        self.ctr_a()

        self.backspace()

        if self.way_type == "straight":
            time = 5

        elif self.way_type == "curve_350":
            if round(self.speed/3.6, 2) <= 11.11: # до 40 км/ч модельное время будет 120 с
                time = 105 # время интеграции с запасом
            
            elif 11.11 < round(self.speed/3.6, 2) <= 22.22: # от 40 до 80 км/ч модельное время будет 30 с
                time = 32 # время интеграции с запасом

        elif self.way_type == "curve_650":
            if round(self.speed/3.6, 2) <= 11.11: # до 40 км/ч модельное время будет 120 с
                time = 120 # время интеграции с запасом
            
            elif 11.11 < round(self.speed/3.6, 2) <= 22.22: # от 40 до 80 км/ч модельное время будет 30 с
                time = 30 # время интеграции с запасом
        
        else:
            raise ValueError("Что-то не так с типом прямой")

        root.typewrite("{}".format(time))

        root.press("enter")
    

    def change_way_type(self):
        """
        Выбор макрогеометрии пути, есть развилка на  прмяую и две кривых
        """

        way_window_position = (38,657)
        way_makrogeometry_position = (179,680)
        straight_position = (36,714)
        curve_position = (35,734)
        curve_radius_position = (79,838)
        ok_button_position = (1032,605) # подтвердить изменения радиуса

        # Иду по вкладкам до выбора геомерии пути
        root.moveTo(self.railway_eqipaje_position)
        root.click()

        root.moveTo(way_window_position)
        root.click()

        root.moveTo(way_makrogeometry_position)
        root.click()

        # Развилка для кривых и прямой
        if self.way_type == "curve_350" :
            
            logger.info(f"геометрия пути: {self.way_type}")

            root.moveTo(curve_position,duration=0)
            root.click()

            root.moveTo(curve_radius_position,duration=0)
            root.click()
            self.ctr_a()
            self.backspace()
            self.backspace()
            
            root.typewrite(str(350),0)

            root.press("enter")
            
            root.moveTo(ok_button_position,duration=0)
            root.click()

            sleep(1)

        elif self.way_type == "curve_650":
            
            logger.info(f"геометрия пути: {self.way_type}")

            root.moveTo(curve_position)
            root.click()

            root.moveTo(curve_radius_position)
            root.click()
            self.ctr_a()
            self.backspace()
            self.backspace()
            
            root.typewrite(str(650),0)
            root.press("enter")
            
            root.moveTo(ok_button_position)
            root.click()

            sleep(1)

        elif self.way_type == "straight":

            logger.info(f"геометрия пути: {self.way_type}")

            root.moveTo(straight_position)
            root.click()

            sleep(1)
        
        else:
            raise ValueError("нет такой макрогеометрии пути")
    

    def get_number_from_name(self):
        """Функция достает число из названия неисправности
        'polzun12' -> '1.2'
        """

        if "polzun" in self.fault:

            l = len("polzun")
            num = self.fault[l:]

            return f"{num[0]}.{num[1]}"
        
        elif "ellips" in self.fault:

            l = len("ellips")
            num = self.fault[l:]

            return f"{num}.{0}"
        
        else:
            raise ValueError("нет такого типа неисправности")


    def change_fault(self, new:bool):
        """
        Измененеие параметра неиспранвости (колеса)
        Неисправности есть 3 видов = `normal`, `polzun`, `elips`
        После названий `polzun` и `elips` можно вводить цифры, тем самым задавая размер
        неисправности.
        Например `polzun15` -> ползун равный 1,5 мм
        """
        wheel_rail_position = (98,649)
        wheels_window_position = (45,672)
        fault_types_position = (125,697)
        
        no_fault = (120,734)
        
        polzun = (121,752)
        d_polzun = (247, 899)
        
        ellips = (120,768)
        a_ellips = (168,859)

        root.moveTo(self.railway_eqipaje_position)
        root.click()

        root.moveTo(wheel_rail_position)
        root.click()

        root.moveTo(wheels_window_position)
        root.click()

        root.moveTo(fault_types_position)
        root.click()

        if self.fault == "normal":

            logger.info(f"Неисправность: {self.fault}")

            root.moveTo(no_fault)
            root.click()

        elif "polzun" in self.fault:

            logger.info(f"Неисправность: {self.fault}")

            num = self.get_number_from_name()
            logger.info(f"polzun {num}")
            
            root.moveTo(polzun)
            root.click()

            if new == True:
                pos_new = (121,869)
                root.moveTo(pos_new)
                root.click()
            
            elif new == False:
                pos_used = (512,869)
                root.moveTo(pos_used)
                root.click()
            
            else:
                raise ValueError("Указан неверный формат параметра `new`")

            root.moveTo(d_polzun)
            root.click()

            self.ctr_a()
            self.backspace()
            self.backspace()
            root.typewrite(message=num)
            root.press("enter")
        
        elif "ellips" in self.fault:

            logger.info(f"Неисправность: {self.fault}")

            num = self.get_number_from_name()
            logger.info(f"ellips {num}")

            root.moveTo(ellips)
            root.click()

            root.moveTo(a_ellips)
            root.click()

            self.ctr_a()
            self.backspace()
            self.backspace()
            root.typewrite(message=num)
            root.press("enter")
        
        else:
            raise ValueError(f"нет такого типа неисправности {self.fault}")


    def change_wheel_profile(self): 
        """Смена профиля колеса"""
        
        if self.wheel_profile == None:
            return None
        
        wheel_rail_position = (98,649)
        wheels_window_position = (45,672)
        wheels_profiles = (51,697)
        newwagon_wheel = (457,738) # -> moveRel(64,58)
        greb_26_wheel = (433,749)
        gost_wheel = (448,761)
        greb_28_5_wheel = (452,775)
        greb_30_wheel = (453,787)
        greb_24_wheel = (556,808)

        set_for_all = (64,58)

        root.moveTo(self.railway_eqipaje_position)
        root.click()

        root.moveTo(wheel_rail_position)
        root.click()

        root.moveTo(wheels_window_position)
        root.click()

        root.moveTo(wheels_profiles)
        root.click()

        if self.wheel_profile == "newwagonw":

            logger.info(f"Профиль колеса: {self.wheel_profile}")

            root.moveTo(newwagon_wheel)
            root.click()
            root.click(button="RIGHT")
            root.moveRel(set_for_all)
            root.click()
        
        elif self.wheel_profile == "greb_26":

            logger.info(f"Профиль колеса: {self.wheel_profile}")
            
            root.moveTo(greb_26_wheel)
            root.click()
            root.click(button="RIGHT")
            root.moveRel(set_for_all)
            root.click()

        elif self.wheel_profile == "gost":

            logger.info(f"Профиль колеса: {self.wheel_profile}")

            root.moveTo(gost_wheel)
            root.click()
            root.click(button="RIGHT")
            root.moveRel(set_for_all)
            root.click()
        
        elif self.wheel_profile == "greb_28":

            logger.info(f"Профиль колеса: {self.wheel_profile}")

            root.moveTo(greb_28_5_wheel)
            root.click()
            root.click(button="RIGHT")
            root.moveRel(set_for_all)
            root.click()

        elif self.wheel_profile == "greb_30":

            logger.info(f"Профиль колеса: {self.wheel_profile}")

            root.moveTo(greb_30_wheel)
            root.click()
            root.click(button="RIGHT")
            root.moveRel(set_for_all)
            root.click()
        
        elif self.wheel_profile == "greb_24":
            
            logger.info(f"Профиль колеса: {self.wheel_profile}")

            root.moveTo(greb_24_wheel)
            root.click()
            root.click(button="RIGHT")
            root.moveRel(set_for_all)
            root.click()

        else:
            raise ValueError(f"нет такого типа профиля {self.wheel_profile}, есть `greb_24`, `greb_26`, `greb_28`, `greb_30`, `gost`")            


    def choose_config(self):
        """Выбор конфига вагона: груженый или порожний"""
        open_folder = (25,64)
        config_empty = (791,489)
        config_loaded = (782,505)
        accept = (718,698)
        modeling = (131,63)

        root.moveTo(open_folder)
        root.click()

        if self.wagon == "empty":
            root.moveTo(config_empty)
            root.click()

            root.moveTo(accept)
            root.click()
        
        elif self.wagon == "loaded":
            
            root.moveTo(config_loaded)
            root.click()

            root.moveTo(accept)
            root.click()
        
        sleep(4)

        root.moveTo(modeling)
        root.click()
    

    def exit_model_integration(self):
        """Выход из режима интегрирования"""
        
        exit_button = (775,992)

        root.moveTo(exit_button)
        root.click()
    

    def if_result_exist(self):
        """Проверка наличия уже проведенных расчетов в папке сохранения"""

        raw_list_of_results = os.listdir(self.path_to_save)

        list_of_results = []

        for i in raw_list_of_results:
            l = len(i)
            name = i[:l-4]
            list_of_results.append(name)

        if self.name in list_of_results:
            return True
        
        elif self.name not in list_of_results:
            return False
        
        else:
            raise ValueError(f"Что-то не то с {self.name} и путем сохранения файла")
    
    def wait_status_bar(self,num:int):
        for i in tqdm(range(num),"Ожидание"):
            sleep(1)