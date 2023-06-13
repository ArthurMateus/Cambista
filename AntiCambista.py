from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from threading import Thread

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


class tokenFinder():

    def token():
        url = 'https://t4fcombr.queue-it.net/afterevent.aspx?c=t4fcombr&e=taylorswiftrjgeral'
        browser = webdriver.Chrome()
        for c in range(1,10):
            browser.get(url)
        while True:
            token = browser.find_element(By.XPATH, '//*[@id="hlLinkToQueueTicket2"]').text
            if token == '':
                pass
            else: 
                return token
            
class transcriptor():
    
    def transcript():
        word = tokenFinder.token()
        print(word)
        with open('Tokens.txt', 'a') as txtfile:
            txtfile.write(word)
            txtfile.write('\n')

def main():
    transcriptor.transcript()


if __name__ == '__main__':
    while True:
        Thread(target=main()).start()