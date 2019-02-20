try:
    import unzip_requirements
except ImportError:
    pass
import logging
import json
import os
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger(__name__)


class Head:
    """
    Class to create a headless chrome driver and collect data
    from www.scopus.com
    """
    DOWNLOAD_DIR = os.getcwd()    
        
    def __init__(self, headless=True):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--disable-extensions')
        if headless:
            self.options.add_argument('--headless')
            self.options.add_argument('--disable-gpu')
            self.options.add_argument('--no-sandbox')
            self.options.add_argument('--disable-dev-shm-usage')
            self.options.add_argument('--window-size=1280x1696')
            self.options.add_argument('--user-data-dir=/tmp/user-data')
            self.options.add_argument('--hide-scrollbars')
            self.options.add_argument('--enable-logging')
            self.options.add_argument('--log-level=0')
            self.options.add_argument('--v=99')
            self.options.add_argument('--single-process')
            self.options.add_argument('--data-path=/tmp/data-path')
            self.options.add_argument('--ignore-certificate-errors')
            self.options.add_argument('--homedir=/tmp')
            self.options.add_argument('--disk-cache-dir=/tmp/cache-dir')
            self.options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
            self.options.binary_location = os.getcwd() + "/bin/headless-chromium"

        self.driver = webdriver.Chrome(chrome_options=self.options)
