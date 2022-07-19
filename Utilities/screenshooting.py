import time
import os
from traceback import print_stack


def screen_shot(self, result_message):
    """
    Takes screenshot of the current open web page
    """
    fileName = result_message + "." + str(round(time.time() * 1000)) + ".png"
    screenshotDirectory = "../screenshots/"
    relativeFileName = screenshotDirectory + fileName
    currentDirectory = os.path.dirname(__file__)
    destinationFile = os.path.join(currentDirectory, relativeFileName)
    destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

    try:
        if not os.path.exists(destinationDirectory):
            os.makedirs(destinationDirectory)
        self.driver.save_screenshot(destinationFile)
        print("Screenshot save to directory: " + destinationFile)
    except:
        print("### Exception Occurred when taking screenshot")
        print_stack()
