import sys
from configparser import ConfigParser
from utils.pretty_print import prettyPrint

def closeBrowserAndExit(self):
    prettyPrint('warning', 'Exiting Zagreus, Goodbye master!')
    self.browser.close()
    sys.exit()