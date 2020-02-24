import socket
import numpy as np
import go_vncdriver
import time
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import cv2
import pickle
STATE_W = 1024
STATE_H = 768
#STATE_W = 128 , 256
#STATE_H = 96 , 192
class SlitherioEnv(gym.Env):
    """
    Description:

    Source:

    Observation:

    Actions:
        Type: Discrete(2)
        Num     Actions
        0       Move Left
        1       Move Right
        3       Increase Velocity
        4       Do Nothing

    Reward:

    Starting State:

    Episode Termination:

    """


    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.seed()
        self.session = go_vncdriver.VNCSession()
        self.session.connect("conn1", address="localhost:5900",password="secure", encoding="tight", subscription=[(0, 1920, 0, 1080)])
        self.tcpconnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpconnection.connect(('localhost', 5005))
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=255, shape=(192,256,3), dtype=np.uint8)
        self.last_length = 10
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    def step(self, action):
        print('step')
        done = True
        self.tcpconnection.send("state".encode('utf-8'))
        done, new_length= pickle.loads(self.tcpconnection.recv(1024))
        #time.sleep(5)
        if action == 0:
            observations, infos, errors = self.session.step({"conn1": [('KeyEvent', 65361 , 1)]})
            time.sleep(0.1)
            observations, infos, errors = self.session.step({"conn1": [('KeyEvent', 65361 , 0)]})
        elif action == 1:
            observations, infos, errors = self.session.step({"conn1": [('KeyEvent', 65363 , 1)]})
            time.sleep(0.1)
            observations, infos, errors = self.session.step({"conn1": [('KeyEvent', 65363 , 0)]})
        elif action == 2:
            observations, infos, errors = self.session.step({"conn1": [('KeyEvent', 65362 , 1)]})
            time.sleep(0.1)
            observations, infos, errors = self.session.step({"conn1": [('KeyEvent', 65362 , 0)]})
        else:
            observations, infos, errors = self.session.step({})
            time.sleep(0.1)
            observations, infos, errors = self.session.step({})

        observation = np.fromstring(observations['conn1'], dtype=np.uint8, sep='')
        observation = observation.reshape(STATE_H,STATE_W, 3)
        #observation = observation[::-1, :, 0:3]
        #cv2.imshow('image',observation)
        #cv2.waitKey(0)  
        #cv2.destroyAllWindows() 
        #observation = observation[::-1, :, 0:3]
        observation = observation[118:, :, 0:3]
        #cv2.imwrite("img.png", observation)
        observation = cv2.resize(observation, dsize=(256, 192), interpolation=cv2.INTER_CUBIC)
        #cv2.imwrite("img1.png", observation)
        if not done:
            self.tcpconnection.send("isalive".encode('utf-8'))
            if self.tcpconnection.recv(1024) == "no":
                self.reset()
            reward = new_length - self.last_length
        else:
            reward = -50
        print("****State of current espidoe: ",done)
        print("****New Length: ",new_length)
        print("****Last Length: ",self.last_length)
        print("****Collected Reward: ",reward)
        self.last_length = new_length
        return observation, reward, done, {} 
    def reset(self):
        self.tcpconnection.send("reset".encode('utf-8'))
        print("reset")
        if self.tcpconnection.recv(1024).decode('utf-8') == "ok":
            observations, infos, errors = self.session.step({})
            #print(observations['conn1'])
            observation = np.fromstring(observations['conn1'], dtype=np.uint8, sep='')
            observation = observation.reshape(STATE_H,STATE_W,  3)
            #observation = observation[::-1, :, 0:3]
            observation = observation[118:, :, 0:3]
            observation = cv2.resize(observation, dsize=(256, 192), interpolation=cv2.INTER_CUBIC)
            #observation = np.array(observations['conn1'])
            return observation
    '''
        self.tcpconnection.send("reset")
        if self.tcpconnection.recv(1024) == "ok":
            observations, infos, errors = self.session.step({"conn1": []})
            observation = np.asarray(observations['conn1'])
            return observation
    '''      
    def render(self, mode='human'):
         print('render')
    def close(self):
         print('close')
