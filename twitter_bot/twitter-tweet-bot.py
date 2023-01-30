import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from twitterUserinfo import username,password
# Start
class Twitter:
    def __init__(self,username,password):        
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages":"en,en_US"})
        self.browser = webdriver.Chrome("chromedriver.exe",chrome_options=self.browserProfile)
        self.username = username
        self.password = password
    # Sign in        
    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(10)
        # Username SignIn
        usernameInput = self.browser.find_element(By.XPATH,"")
        usernameInput.send_keys(self.username)

        sbmtbttn = self.browser.find_element(By.XPATH,"")
        sbmtbttn.click()
        time.sleep(3)
        # Password SignIn
        passwordInput = self.browser.find_element(By.XPATH,"")
        passwordInput.send_keys(self.password)

        sbmtbttnn = self.browser.find_element(By.XPATH,"")
        sbmtbttnn.click()
        time.sleep(3)
    # Search
    def search(self,hashtag):
        # Search Start
        searchInput = self.browser.find_element(By.XPATH,"")
        searchInput.send_keys(hashtag)
        time.sleep(4)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(4)

        results = []
 
        
        list = self.browser.find_elements(By.XPATH,"//div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div['data-testid=tweetText']")
        time.sleep(4)
        print("count: "+ str(len(list)))
        
        for i in list:
            results.append(i.text)
        
        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")        
        # Scroll Start
        while True:
            if loopCounter>5:
              break  
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
            time.sleep(5)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height==new_height:
                break
            last_height = new_height
            loopCounter+=1 
            #  Scroll Finish
        # Text Write

            list = self.browser.find_elements(By.XPATH,"//div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div['data-testid=tweetText']")
            time.sleep(4)
            print("count: "+ str(len(list)))

        for i in list:
            results.append(i.text)

            
        list = self.browser.find_elements(By.XPATH,"//div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div['data-testid=tweetText']")
        time.sleep(4)
        print("count: "+ str(len(list )))
        # count = 1
        # with open("tweet.txt","w",encoding="UTF-8") as file:
            # for item in results:
                # file.write(f"{count}-{item}\n")
                # count+=1


        count = 1
    
        for item in results:
            print(f"{count}-{item}")
            count+=1
            print("**************")
        # Text Write Finish
    

twit = Twitter(username,password)
twit.signIn()
twit.search("python") 