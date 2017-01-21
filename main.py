#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from omxplayer import OMXPlayer

def main():
	GPIO.setmode(GPIO.BCM)
	filepath26 = '/home/pi/entertained.mp4'
	filepath19 = '/home/pi/darkness.mp4'
	filepath6 = '/home/pi/jericho.mp4'
	filepath13 = '/home/pi/no_one_cared.mp4'
	filepath5 = '/home/pi/matter.mp4'
	
	for i in range(2,27):
		GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	counter = [0] * 27
	input_state = [ True ] * 27
	
	player = OMXPlayer(filepath26)
	length = player.duration()
	ratio = 5 / length
	player.pause()
	
	while True:
		for i in range(2,27):
			input_state[i] = GPIO.input(i)
		
		
		if input_state[26] == False:
			player.pause()
			player.load(filepath26)
			player.play()
			
		if input_state[19] == False:
			player.pause()
			player.load(filepath19)
			player.play()
				
		if input_state[13] == False:
			player.pause()
			player.load(filepath13)
			player.play()
			
		if input_state[6] == False:
			player.pause()
			player.load(filepath6)
			player.play()
			
		if input_state[5] == False:
			player.pause()
			player.load(filepath5)
			player.play()
	
		
		if input_state[20] == False:
			player.play_pause()
			
		if input_state[16] == False:
			player.seek(5)
			
		if input_state[21] == False:
			player.seek(-5)
			
		if input_state[12] == False:
			player.quit()
		

if __name__ == '__main__':
	main()

