from PIL import Image, ImageDraw

class Grid:

    def __init__(self):
        self.capture_image()

    def capture_image(self):
        screenshot = Image.open("C:\\robotProjects\\ImageMagick\\PythonTest\\test2.png")
        columns = 60
        rows = 80
        screen_width, screen_height = screenshot.size

        block_width = ((screen_width - 1) // columns) + 1 # this is just a division ceiling
        block_height = ((screen_height - 1) // rows) + 1

        for y in range(0, screen_height, block_height):
            for x in range(0, screen_width, block_width):
                draw = ImageDraw.Draw(screenshot)
                draw.rectangle((x, y, x+block_width, y+block_height), outline = "red")

        screenshot.save("grid.png")

Grid()