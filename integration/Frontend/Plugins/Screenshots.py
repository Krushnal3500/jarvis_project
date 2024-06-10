from PIL import ImageGrab
import datetime
import py
import os

class Screenshot:
    @staticmethod
    def takeScreenshot(output_filename):
        
        screenshot = ImageGrab.grab()
        
        screenshot.save(screenshot.png)
        
        no = str(datetime.datetime.now())
        no = no.replace("-", "_")
        no = no.replace(":", "_")
        no = no.replace(".", "_")
        no = no.replace(" ", "_")
        screenshot_path = Config.get('Screenshots')
        file_path = "{}{}.png".format(screenshot_path, no)

        # py.screenshot(file_path)
        # os.system(file_path)

# Example of using the Screenshot class
Config = {'Screenshots': '/path/to/screenshots/'}
Screenshot.takeScreenshot()
