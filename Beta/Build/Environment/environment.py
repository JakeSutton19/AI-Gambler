import numpy as np
import pygame as pg

class Snake():

    def __init__(self, waitTime): #waitime variable is used in order to be able to play the game

        self.width = 400
        self.height = 400
        self.nRows = 10
        self.nColumns = 10
        self.defReward = -0.02 #living penalty
        self.negReward = -1. #penalty for loosing
        self.posReward = 2. #reward when eating an apple
        self.waitTime = waitTime

        #Addition - Time Reward
        self.steps_alive_count = 0


        if self.initSnakeLen > self.nRows / 2:
            self.initSnakeLen = int(self.nRows / 2)

        self.screen = pg.display.set_mode((self.width, self.height))

        self.snakePos = list()
        self.screenMap = np.zeros((self.nRows, self.nColumns))

        for i in range(self.initSnakeLen):
            self.snakePos.append((int(self.nRows / 2) + i, int(self.nColumns / 2)))
            self.screenMap[int(self.nRows / 2) + i][int(self.nColumns / 2)] = 0.5

        self.applePos = self.placeApple()

        self.drawScreen()
        self.collected = False

        self.lastMove = 0

    def step(self, action):
        # action = 0 -> up
        # action = 1 -> down
        # action = 2 -> right
        # action = 3 -> left
        gameOver = False
        reward = self.defReward
        self.collected = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        snakeX = self.snakePos[0][1]
        snakeY = self.snakePos[0][0]

        if action == 1 and self.lastMove == 0:
            action = 0
        if action == 0 and self.lastMove == 1:
            action = 1
        if action == 3 and self.lastMove == 2:
            action = 2
        if action == 2 and self.lastMove == 3:
            action = 3

        if action == 0:
            if snakeY > 0:
                if self.screenMap[snakeY - 1][snakeX] == 0.5:
                    gameOver = True
                    reward = self.negReward
                elif self.screenMap[snakeY - 1][snakeX] == 1:
                    reward = self.posReward
                    self.moveSnake((snakeY - 1, snakeX), True)
                elif self.screenMap[snakeY - 1][snakeX] == 0:
                    self.moveSnake((snakeY - 1, snakeX), False)
            else:
                gameOver = True
                reward = self.negReward

        elif action == 1:
            if snakeY < self.nRows - 1:
                if self.screenMap[snakeY + 1][snakeX] == 0.5:
                    gameOver = True
                    reward = self.negReward
                elif self.screenMap[snakeY + 1][snakeX] == 1:
                    reward = self.posReward
                    self.moveSnake((snakeY + 1, snakeX), True)
                elif self.screenMap[snakeY + 1][snakeX] == 0:
                    self.moveSnake((snakeY + 1, snakeX), False)
            else:
                gameOver = True
                reward = self.negReward

        elif action == 2:
            if snakeX < self.nColumns - 1:
                if self.screenMap[snakeY][snakeX + 1] == 0.5:
                    gameOver = True
                    reward = self.negReward
                elif self.screenMap[snakeY][snakeX + 1] == 1:
                    reward = self.posReward
                    self.moveSnake((snakeY, snakeX + 1), True)
                elif self.screenMap[snakeY][snakeX + 1] == 0:
                    self.moveSnake((snakeY, snakeX + 1), False)
            else:
                gameOver = True
                reward = self.negReward

        elif action == 3:
            if snakeX > 0:
                if self.screenMap[snakeY][snakeX - 1] == 0.5:
                    gameOver = True
                    reward = self.negReward
                elif self.screenMap[snakeY][snakeX - 1] == 1:
                    reward = self.posReward
                    self.moveSnake((snakeY, snakeX - 1), True)
                elif self.screenMap[snakeY][snakeX - 1] == 0:
                    self.moveSnake((snakeY, snakeX - 1), False)
            else:
                gameOver = True
                reward = self.negReward

        self.drawScreen()

        self.lastMove = action

        pg.time.wait(self.waitTime)

        if (reward == self.defReward):
            self.steps_alive_count += 1
        elif (reward == self.posReward):
            if (self.steps_alive_count >= 10):
                reward += .5
            elif (self.steps_alive_count >= 5 and self.steps_alive_count < 10):
                reward += .1
            else:
                reward -= .01
        else:
            self.steps_alive_count = 0

        return self.screenMap, reward, gameOver


    def reset(self):
        self.screenMap  = np.zeros((self.nRows, self.nColumns))
        self.snakePos = list()

        for i in range(self.initSnakeLen):
            self.snakePos.append((int(self.nRows / 2) + i, int(self.nColumns / 2)))
            self.screenMap[int(self.nRows / 2) + i][int(self.nColumns / 2)] = 0.5

        self.screenMap[self.applePos[0]][self.applePos[1]] = 1

        self.lastMove = 0

        self.drawScreen()

if __name__ == '__main__':
     env = Environment(100)
     gameOver = False
     start = False
     action = 0
     while True:
          for event in pg.event.get():
               if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE and not start:
                         start = True
                    elif event.key == pg.K_SPACE and start:
                         start = False
                    if event.key == pg.K_UP:
                         action = 0
                    elif event.key == pg.K_DOWN:
                         action = 1
                    elif event.key == pg.K_RIGHT:
                         action = 2
                    elif event.key == pg.K_LEFT:
                         action = 3

          if start:
               _, _, gameOver = env.step(action)

          if gameOver:
               start = False
               gameOver = False
               env.reset()
               action = 0
