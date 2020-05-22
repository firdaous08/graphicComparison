def process_region(self, image, x, y, width, height):
    region_total = 0

    # This is the sensitivity factor, the larger it is the less sensitive the comparison
    factor = 10

    for coordinateY in range(y, y+height):
        for coordinateX in range(x, x+width):
            try:
                pixel = image.getpixel((coordinateX, coordinateY))
                region_total += sum(pixel)/4
            except:
                return
            
    return region_total/factor