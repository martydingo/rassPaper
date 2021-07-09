from waveshare_epd import epd2in13_V2

class rassPaper:
    def __init__(self):
        self.display = epd2in13_V2.EPD()
        self.clearScreen()

    def clearScreen(self):
        self.display.init(self.display.FULL_UPDATE)
        self.display.Clear(0xFF)

if(__name__=='__main__'):
    try:
        rassPaper = rassPaper()
        rassPaper.clearScreen()
        
    except KeyboardInterrupt:
        epd2in13_V2.epdconfig.module_exit()
        exit()