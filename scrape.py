from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from bs4 import BeautifulSoup
from typing import Union
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Scrape:
    
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)    


    def scraper(self,website:str,page_down:int) -> str:
        try:
            self.driver.get(website)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            if page_down > 0:
                for _ in range(1,page_down+1):
                    ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
                    time.sleep(2)

            page_src = self.driver.page_source
            body_content = self.extract_body_content(page_src)
            cleaned_content = self.clean_body_content(body_content)
            return cleaned_content
        except Exception as e:
            print(e)
            print("In Except Block")
            return None

    def scrape_website(self,websites:Union[str,list],page_down:int) -> str:
        all_responses = "" # initlize empty string
        if isinstance(websites,list):
            for website in websites:
                response = self.scraper(website.strip())
                if response is not None:
                    all_responses += response
                else:
                    pass
        if isinstance(websites,str):
            response = self.scraper(websites.strip(),page_down)
            if response is not None:
                all_responses += response

        self.driver.quit()
        return all_responses
    
    def extract_body_content(self,html_content:str) -> None:
        soup = BeautifulSoup(html_content,"html.parser")
        body_content = soup.body
        if body_content:
            return str(body_content)
        return None

    def clean_body_content(self,body_content:str) ->None:
        soup = BeautifulSoup(body_content,"html.parser")
        
        for script_or_style in soup(["script","style"]):
            script_or_style.extract()

        cleaned_content = soup.get_text(separator="/n")
        cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
        cleaned_content = re.sub(r"/n+"," ",cleaned_content)
        cleaned_content = re.sub(r"\s+"," ",cleaned_content).strip()
        return cleaned_content
    