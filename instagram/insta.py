from  __init__ import *
import json
from alive_progress import alive_bar
from multiprocessing import Process as Thread
class Instagram(Handler):
    def __init__(self):
        self.actions=ActionChains(driver)
        driver.get("https://www.instagram.com/")
        self.cookies=False
        if USECOOKIES:
            try:
                open("igcookies.json","r+")
                pass
            except FileNotFoundError:
                self.login()
            self.cookies=True
        else:
            self.login()
            
            
        
        
        ...
    def saveCookies(self,driver=driver):
        cookies = driver.get_cookies()
        with open('igcookies.json', 'w') as file:
            json.dump(cookies, file)
    def loadCookies(self,driver=driver):
        driver.get("https://www.instagram.com/")
        try:
            with open('igcookies.json', 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)

        except FileNotFoundError:
            print("checking")
        driver.refresh()
    def login(self):
        ##open url
        #driver.get("https://www.instagram.com/")
        #login
        self.wait(By.XPATH,"//input[@name='username']").send_keys(IG_USERNAME)
        self.wait(By.XPATH,'//input[@name="password"]').send_keys(IG_PASSWORD)
        self.wait(By.XPATH,'//button[@type="submit"]').submit()
        
        #check if show save info then click not now
        if HEADLESS.lower()=="no":
            try:
                console.print(f"{Fore.MAGENTA}Successfully Login{Fore.RESET}....")
                self.wait(By.XPATH,'//div[contains(text(),"Not now")]',60).click()
            except:
                pass
            #click on not receiving notfication
            try:
               self.wait(By.XPATH,'//button[contains(text(),"Not Now")]',60).click()
            except:
                pass
        self.saveCookies()
    def postcontent(self,file:str,captions=None):
        #click on create post
        
        if USECOOKIES:
            self.loadCookies()

        if HEADLESS.lower()=="no":
            try:
                self.wait(By.XPATH,'//button[contains(text(),"Not Now")]',10).click()
            except:
                pass
        try:
           self.waits(By.XPATH,'//div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a',10)[0].click()
        except:
            self.waits(By.XPATH,'//div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a',10)[0].click()
        try:
           self.wait(By.XPATH,'//div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/div/div/div[1]/a[1]',3).click()
        except:
            pass
        start = time.time()
        ##drag and drop file
        drag_drop=self.wait(By.XPATH,'//div//*[contains(text(),"Drag photos and videos here")]',60)
        drag_drop.drop_files(file)

        #  next button
        
        
        #click it
        
        if is_video._is_video(file):
            try:
                self.wait(By.XPATH,'//button[contains(text(),"OK")]',15).click()
            except:
                pass
        if is_video._is_video(file):
            f_type="Video"
        else:
            f_type="Image"
        try:
           self.wait(By.XPATH,f'//div[contains(text(),"Next")]',60).click()
        except:
            self.wait(By.XPATH,f'//div[contains(text(),"Next")]',60).click()
            pass
        try:
           self.wait(By.XPATH,f'//div[contains(text(),"Next")]',30).click()
        except:
            self.wait(By.XPATH,f'//div[contains(text(),"Next")]',30).click()
            pass
        if captions !=None:
            try:
               self.wait(By.XPATH,"//div[@aria-label='Write a caption...']").send_keys(captions)
            except:
               self.wait(By.XPATH,f'//div[contains(text(),"Next")]',60).click()
               self.wait(By.XPATH,"//div[@aria-label='Write a caption...']").send_keys(captions)
        
        

        #next_share("Share")
        try:
           self.wait(By.XPATH,f'//div[contains(text(),"Share")]',100).click()
        except:
           self.wait(By.XPATH,f'//div[contains(text(),"Share")]',100).click()
        ##check if post has been postedd
        self.wait(By.XPATH,'//img[@alt="Animated checkmark"]',6*60)
        console.log(f"\n[cyan bold]Posted: [/cyan bold][magenta bold]{file.split("/")[-1]} [cyan bold]captions: [/cyan bold]{captions} ([/magenta bold][blue bold]Time Taken:[/blue bold]{round(time.time()-start,2)}secs,[blue bold]File Size:[/blue bold]{round(os.stat(file).st_size/(1024 * 1024),2)}mb,[blue bold]Type:[/blue bold]{f_type}[magenta bold])[/magenta bold] ✅")
        if REMOVE_FILE.lower()=="yes":
            os.remove(file)
        driver.close()
       
    def _random_captions(self):
        f=open("captions.txt","r+").readlines()
        return str(random.choice(f).strip("\n"))
    
       
x=os.listdir(FOLDER_NAME)
n=int(THREAD)
l = [ x [i:i + n] for i in range(0, len(x),n) ]
#l = [ x [i:i + 6] for i in range(0, len(x), 2) ]    
#scrape(urls[1])
processes = [] 
def main(filee):

    if is_video.check_file(filee):

        Instagram().postcontent(filee)
    else:
        console.log(f"[red bold] file not supported {filee}[/red bold]")

for i in l:
    if __name__=="__main__":
        start=time.time()
        with alive_bar(len(x)) as bar:
            for j in i:
                fileee=f"{FOLDER_NAME}/{j}"
                p = Thread(target=main,args=(fileee,)) 
                p.start() 
                processes.append(p) 
            for f in processes: 
                f.join()
                bar()
    

                    
    

        
        
        





