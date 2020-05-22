from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


#class UntitledTestCase(unittest.TestCase):
  #def tunnel_Vente(self):
        #driver = self.driver
#driver = webdriver.Chrome()
#driver.get("https://pp.lahalle.com")
#assert "La Halle" in driver.title
#try:
   # element = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.XPATH, "categorie")))
#finally:
    #driver.quit()


#driver.implicitly_wait(10)
#driver.get_screenshot_as_file("test2.png")
#driver.quit()
#print("end...")





















class ScreenCapture:

    STAGING_URL = 'http://www.yahoo.com'
    PRODUCTION_URL = 'http://www.yahoo.com'
    driver = None
    i = 0
    path="C:/robotProjects/ImageMagick/PythonTest/"

    def __init__(self):
        self.set_up()
        self.capture_screens()
        self.clean_up()
    
    def renommer():
    for  filename in os.listdir(path)
      my_dest ="screenshot" + str(i) + ".png"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1



    def set_up(self):
        self.driver = webdriver.Chrome()

    def clean_up(self):
        self.driver.close()

    def capture_screens(self):
        self.screenshot(self.STAGING_URL, 'screen_staging.png')
        self.screenshot(self.PRODUCTION_URL, 'screen_production.png')

    def screenshot(self, url, file_name):
        print("Capturing", url, "screenshot as", file_name, "...")
        self.driver.get("https://pp.lahalle.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        #self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath("C:\Robot\ImageMagick-20200513T143214Z-001\ImageMagick\PythonTest")), 'screenshots', file_name))
        #self.driver.get_screenshot_as_png()
     self.driver.get_screenshot_as_file(rename(my_source, my_dest))
        print("Done.")
        #self.driver.quit()

   
ScreenCapture()