from waveshare_epd import epd2in13_V2

class rassPaper:
    def __init__(self):
        self.display = epd2in13_V2.EPD()
        self.clearScreen()

    def clearScreen(self):
        self.display.init(self.display.FULL_UPDATE)
        display.Clear(0xFF)

if(__name__=='__main__'):
    rassPaper = rassPaper()