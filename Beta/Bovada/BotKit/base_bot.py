
import configparser

class Base_Bot:
    def __init__(self, webdriver_import, CONFIG=None):
        #Base Config
        self.BASE_CONFIG_PATH = '/home/human/Kevin/Betting/BotKit/config.ini'
        self.base_config = Base_Bot.init_config(self.BASE_CONFIG_PATH)
        
        #Drivers
        self.webdriver = webdriver_import
        self.driver = None

        #Pages
        self.base_url = self.base_config['BASE_URLS']['BASE']
        self.access_url = None

        #Status
        self.page_accessed = False

        #Errors
        self.ERROR = False
        self.ERROR_Count = 0


    def init_config(config_file_path):
        # asserting configuration file has the correct extension
        path = config_file_path.split('.')
        assert(path[len(path)-1] == 'ini')

        config = configparser.ConfigParser()
        config.read(config_file_path)
        return config

        

    def Handle_Error(self, msg):
        if (self.ERROR == True):
            self.ERROR_Count = self.ERROR_Count + 1
            print("[ERROR]: Problem with class: {}".format(msg))
            self.ERROR = False


    def Perform_Action(self):
        self.actions = self.webdriver.ActionChains(self.driver)
        try:
            self.actions.move_to_element(self.Action)
            self.actions.click(self.Action).perform()
        except:
            self.ERROR = True
            self.Handle_Error("Perform_Action")

        
    def Driver_Setup(self, option):
        try:
            if (option == 'Firefox'):
                self.driver = self.webdriver.Firefox(executable_path=self.base_config['ENVIRONMENT']['FIREFOX_PATH'])
            elif (option == 'Chrome'):
                self.driver = self.webdriver.Chrome(self.base_config['ENVIRONMENT']['CHROMEDRIVER_PATH'])
        except:
            self.ERROR = True
            self.Handle_Error("Driver_Setup")


    def Access_URL(self, url=None):
        if (url == None):
            self.url = self.base_url
        else:
            self.url = url
        try:
            self.driver.get(self.url)
            self.page_accessed = True
        except:
            self.page_accessed = False
            self.ERROR = True
            self.Handle_Error("Access_URL")


    def Switch_Frame(self):
        try:
            iframe = self.driver.find_element_by_tag_name('iframe')
            self.driver.switch_to.frame(iframe)
        except:
            self.ERROR = True
            self.Handle_Error("Switch_Frame")
        


    def Switch_Default_Frame(self):
        try:
            self.driver.switch_to.default_content()
        except:
            self.ERROR = True
            self.Handle_Error("Switch_Default_Frame")
       
        

    def Shutdown_Driver(self):
        self.driver.close()
        quit()
