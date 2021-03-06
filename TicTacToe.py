# -*- coding:UTF-8 -*- 
import pygame
import random
import time
from pygame.locals import *

global board
global score
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
score = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
m, n = 'X', 'O'
pygame.init()
BOX_SIZE = 50
BOX_GAP = 5
BORDER_GAP = 20
SCREEN_SIZE = BOX_SIZE * 3 + BOX_GAP * 2 + BORDER_GAP * 2
TEXT_HEIGHT  = int(BOX_SIZE * 0.35)
BLACK = pygame.color.THECOLORS['black']
WHITE = pygame.color.THECOLORS['white']
RED = pygame.color.THECOLORS['red']
GREEN = pygame.color.THECOLORS['green']

def display():
	print('{0:3} {1:3} {2:3}'.format(board[0][0], board[0][1], board[0][2]))
	print('{0:3} {1:3} {2:3}'.format(board[1][0], board[1][1], board[1][2]))
	print('{0:3} {1:3} {2:3}'.format(board[2][0], board[2][1], board[2][2]))

def init():
	global screen
	screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE), 0, 32)
	pygame.display.set_caption("TicTacToe")

def drawBox():
	x, y = BORDER_GAP, BORDER_GAP
	size = BOX_SIZE * 3 + BOX_GAP * 2
	pygame.draw.rect(screen, BLACK, (BORDER_GAP, BORDER_GAP, size, size))
	for i in range(3):
		for j in range(3):
			idx = board[i][j]
			if idx == 0:
				text = ''
			# elif idx == 1:
			# 	text = 'X'
			# elif idx == -1:
			# 	text = 'O'
			else:
				text = idx
			pygame.draw.rect(screen, WHITE, (x, y, BOX_SIZE, BOX_SIZE))
			my_font = pygame.font.SysFont("arial", 64)
			text_surface = my_font.render(text, True, RED)
			text_rect = text_surface.get_rect()
			text_rect.center = (x + BOX_SIZE / 2, y + BOX_SIZE /2)
			screen.blit(text_surface, text_rect)
			x += BOX_SIZE + BOX_GAP
		x = BORDER_GAP
		y += BOX_SIZE + BOX_GAP

def write(x, y):
	if 20 < x < 70 and 20 < y < 70 and board[0][0] == 0:
		board[0][0] = m
	if 75 < x < 125 and 20 < y < 70 and board[0][1] == 0:
		board[0][1] = m
	if 130 < x < 180 and 20 < y < 70 and board[0][2] == 0:
		board[0][2] = m
	if 20 < x < 70 and 75 < y < 125 and board[1][0] == 0:
		board[1][0] = m
	if 75 < x < 125 and 75 < y < 125 and board[1][1] == 0:
		board[1][1] = m
	if 130 < x < 180 and 75 < y < 125 and board[1][2] == 0:
		board[1][2] = m
	if 20 < x < 70 and 130 < y < 180 and board[2][0] == 0:
		board[2][0] = m
	if 75 < x < 125 and 130 < y < 180 and board[2][1] == 0:
		board[2][1] = m
	if 130 < x < 180 and 130 < y < 180 and board[2][2] == 0:
		board[2][2] = m

def ai():
	if check():
		max_score = -1
		pos = (0, 0)
		for i in range(3):
			for j in range(3):
				if board[i][j] == 0:
					score[i][j] = -1
					# row
					score[i][j] += calcScore(board[i])
					# col
					line = [board[k][j] for k in range(3)]
					score[i][j] += calcScore(line)
					# left-top to right-bottom
					if i == j:
						line = [board[k][k] for k in range(3)]
						score[i][j] += calcScore(line)
					# right-top to left-bottom
					if i + j == 2:
						line = [board[k][2 - k] for k in range(3)]
						score[i][j] += calcScore(line)
					# center
					if i == 1:
						score[i][j] += 1
					if j == 1:
						score[i][j] += 1
					if score[i][j] > max_score:
						max_score = score[i][j]
						pos = (i, j)
		board[pos[0]][pos[1]] = n
	drawBox()

def calcScore(line):
	score = 0
	if line.count('X') == 2:
		score += 1000
	if line.count('O') == 2:
		score += 900
	if line.count('X') == 1 and line.count('O') == 0:
		score += 100
	if line.count('X') == 0 and line.count('O') == 1:
		score += 90
	if line.count(0) == 3:
		score += 10
	return score

def check():
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2] != 0:
			print board[i][0] + 'win'
			return False
		if board[0][i] == board[1][i] == board[2][i] != 0:
			print board[0][i] + 'win'
			return False
	if board[0][0] == board[1][1] == board[2][2] != 0:
		print board[0][0] + 'win'
		return False
	if board[2][0] == board[1][1] == board[0][2] != 0:
		print board[2][0] + 'win'
		return False
	if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
		print 'Draw'
		return False
	return True

def main():
	init()
	drawBox()
	while check():
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.display.quit()
			if event.type == MOUSEBUTTONUP:
				x, y = pygame.mouse.get_pos()
				write(x, y)
				ai()
		pygame.display.update()


if __name__ == "__main__":
    main()