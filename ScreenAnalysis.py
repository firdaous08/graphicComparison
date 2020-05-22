
from PIL import Image, ImageDraw
from selenium import webdriver
import os
import sys

class ScreenAnalysis:

    STAGING_URL = 'https://pp.lahalle.com'
    PRODUCTION_URL = 'https://www.lahalle.com'
    driver = None

    def __init__(self):
        self.set_up()
        self.capture_screens()
        self.analyze()
        self.clean_up()

    def set_up(self):
        self.driver = webdriver.Chrome()

    def clean_up(self):
        self.driver.close()

    def capture_screens(self):
        self.screenshot(self.STAGING_URL, 'test2.png')
        self.screenshot(self.PRODUCTION_URL, 'maquette.png')

    def screenshot(self, url, file_name):
        print("Capturing", url, "screenshot as", file_name, "...")
        self.driver.get("https://pp.lahalle.com")
        self.driver.implicitly_wait(10)
        #self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath("C:\Robot\ImageMagick-20200513T143214Z-001\ImageMagick\PythonTest")), 'screenshots', file_name))
        #self.driver.get_screenshot_as_png()
        self.driver.get_screenshot_as_file("test2.png")
        print("Done.")

    def analyze(self):
        screenshot_staging = Image.open("C:\\robotProjects\\ImageMagick\\PythonTest\\test2.png")
        screenshot_production = Image.open("C:\\robotProjects\\ImageMagick\\PythonTest\\maquette.png")
        columns = 60
        rows = 80
        screen_width, screen_height = screenshot_staging.size

        block_width = ((screen_width - 1) // columns) + 1 # this is just a division ceiling
        block_height = ((screen_height - 1) // rows) + 1

        for y in range(0, screen_height, block_height+1):
            for x in range(0, screen_width, block_width+1):
                region_staging = self.process_region(screenshot_staging, x, y, block_width, block_height)
                region_production = self.process_region(screenshot_production, x, y, block_width, block_height)

                if region_staging is not None and region_production is not None and region_production != region_staging:
                    draw = ImageDraw.Draw(screenshot_staging)
                    draw.rectangle((x, y, x+block_width, y+block_height), outline = "red")

        screenshot_staging.save("result.png")

    def process_region(self, image, x, y, width, height):
        region_total = 0

        # This can be used as the sensitivity factor, the larger it is the less sensitive the comparison
        factor = 100

        for coordinateY in range(y, y+height):
            for coordinateX in range(x, x+width):
                try:
                    pixel = image.getpixel((coordinateX, coordinateY))
                    region_total += sum(pixel)/4
                except:
                    return

        return region_total/factor

ScreenAnalysis()
