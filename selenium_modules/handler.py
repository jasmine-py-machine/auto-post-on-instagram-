import os
import sys

try:
    from selenium import webdriver
    from rich.console import Console
    
    from selenium.webdriver.support.ui import WebDriverWait
    import time,sys,traceback,os
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver import ActionChains
    
   
except ImportError as e:
    os.system(f"pip install -r requirements.txt")
from .settings import *  
options=Options()

console=Console()
if EXTENSION.lower()=="yes":
    path1=os.getcwd().split("/")
    path1.pop()
    extensionpath=f'{"/".join(path1)}/extensions'
    for i in os.listdir(extensionpath):
        
        if os.path.isfile(f"{extensionpath}/{i}"):
           
            if i.split(".")[1].lower()=="crx":
                options.add_extension(f"{extensionpath}/{i}")
                console.log(f"[green bold]Adding Extension..[/green bold] {i} [blue bold]Done[/blue bold]")
                
if HEADLESS.lower()=="yes":
    options.add_argument("--headless")

driver=webdriver.Chrome(options=options)  
driver.maximize_window()
class Handler: 
    def __init__(self) -> None:
        super().__init__()

    def countdown(self,t:int):
        """your time should be in secs """
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
    def wait(self,by,element,time=15):
        "WAIT FOR ELEMENT TO BE VISIBLE"
        try:
            wait=WebDriverWait(driver,time)
            return wait.until(EC.visibility_of_element_located((by,element)))
        except Exception as e:
            self.log(e)
    def waits(self,by,element,time=15):
        "WAIT FOR MUTILPLE ELEMENT TO BE VISIBLE"
        try:
            wait=WebDriverWait(driver,time)
            return wait.until(EC.visibility_of_all_elements_located((by,element)))
        except  Exception as e:
            self.log(e)
    def notvisible(self,by,element,time=150):
        "WAIT TILL ELEMENT IS NOT VISIBLE"
        try:
            wait=WebDriverWait(driver,time)
            return wait.until(EC.invisibility_of_element_located((by,element)))
        except  Exception as e:
            self.log(e)
    def error(self):
        "ERROR LOG"
        traceback_template = '''Traceback (most recent call last):
        File "%(filename)s", \nline %(lineno)s, in %(name)s
        %(type)s: %(message)s\n'''
        exc_type, exc_value, exc_traceback = sys.exc_info() 
        traceback_details = {
                                'filename': exc_traceback.tb_frame.f_code.co_filename,
                                'lineno'  : exc_traceback.tb_lineno,
                                'name'    : exc_traceback.tb_frame.f_code.co_name,
                                'type'    : exc_type.__name__,
                                'message' : exc_value,
                                }

        del(exc_type, exc_value, exc_traceback) # So we don't leave our local labels/objects dangling
        r=f"{traceback.format_exc()},{traceback_template % traceback_details}"
        return str(r)
    def exit(self):
        "EXIT "
        driver.quit()
        sys.exit()
    def log(self,txt):
        "WRITE ERROR LOG TO THE FILE"
        with open('logs.txt',"a+") as file:
            file.write(f"[{time.ctime()}]==>{txt}\n")
        file.close()