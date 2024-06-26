import os
import re,random
import sys,time
path=os.getcwd().split("/")
path.pop()
sys.path.insert(1,"/".join(path))
from selenium_modules  import By,driver,is_video,console,Fore,Back
from selenium_modules.dropfile import *
from selenium_modules.handler import Handler
from selenium_modules.is_video import _is_video
from selenium_modules.settings import *
from selenium.webdriver import ActionChains



