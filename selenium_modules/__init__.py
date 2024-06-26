
__all__=["dropfile","handler","settings"]
import os

try:
    import time
    from rich.console import Console
    import mimetypes
    import random
    from selenium.webdriver import ActionChains
    from selenium.webdriver.remote.webelement import WebElement
    import selenium_modules.dropfile as dropfile
    import mimetypes
    from colorama import Fore,Back,Style
    from tkinter import Tk
    from selenium.webdriver import ActionChains
except:
    os.system("pip install -r selenium_modules/requiretments.txt")
from .settings import *
from selenium.webdriver.common.by import By
from .handler import Handler,driver

WebElement.drop_files = dropfile.drop_files
console=Console()

"""
DON'T CHANGE THIS FILE 
PROGRAMMED BY PYJOSHTECH 

"""