from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random as rand
import time
import socket
import pickle
'''
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
'''
class RemoteEnv:
    def __init__(self, tcp_ip='localhost', tcp_port=5005, buffer_size=20):
        self.buffer_size = buffer_size
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"
        options = webdriver.chrome.options.Options()
        #options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(desired_capabilities=caps,chrome_options=options)
        self.driver.maximize_window()
        tcpconnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpconnection.bind((tcp_ip, tcp_port))
        tcpconnection.listen(1)
        self.conn, self.addr = tcpconnection.accept()
        self.last_length = 10


    '''
    Initializing TCP connection; Initializing Chrome webkit;   
    '''


    def env_reset(self):
        self.driver.get("http://www.slither.io")
        time.sleep(8)
        self.driver.execute_script("window.stop()")
        assert "slither.io" in self.driver.title
        try:
            nickname = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "nick")))
            if nickname.is_displayed() and nickname.is_enabled():
                nickname.clear()
                nickname.send_keys("AI-BOT")
                nickname.send_keys(Keys.ENTER)
        finally:
            time.sleep(2)


    '''
    Reset enviroment;  
    '''


    def env_cmd(self):
        data = self.conn.recv(self.buffer_size)
        if data:
            print("received data:", data.decode('utf-8'))
            if data.decode('utf-8') == "state":
                try:
                    data=pickle.dumps([False,int(self.driver.execute_script("return Math.floor(15 * (fpsls[snake.sct] + snake.fam / fmlts[snake.sct] - 1) - 5) / 1"))])
                except:
                    data=pickle.dumps([True,0])
                self.conn.send(data)
            elif data.decode('utf-8') == "reset":
                self.env_reset()
                self.conn.send("ok".encode('utf-8'))
            elif data.decode('utf-8') == "isalive":
                if self.driver.execute_script("document.getElementById('login').style.display")=="block":
                    self.conn.send("no".encode('utf-8'))
                else:
                    self.conn.send("yes".encode('utf-8'))
            



