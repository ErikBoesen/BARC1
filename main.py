#!/usr/bin/env python

import RPi.GPIO as GPIO
import picamera
import time
from omxplayer import OMXPlayer

def main():
	try:
		camera = picamera.PiCamera()
	except:
		print('')
	
	GPIO.setmode(GPIO.BCM)
	filepath26 = '/home/pi/video26.mp4'
	filepath19 = '/home/pi/video19.mp4'
	filepath13 = '/home/pi/video13.mp4'
	filepath6 = '/home/pi/video6.mp4'
	filepath5 = '/home/pi/video5.mp4'
	filepath10 = '/home/pi/video10.mp4'
	filepath9 = '/home/pi/video9.mp4'
	filepath11 = '/home/pi/video11.mp4'
	
	for i in range(2,27):
		GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	counter = [0] * 27
	input_state = [ True ] * 27
	
	is_recording = False
	is_previewing = False
	
	
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
			
		if input_state[10] == False:
			player.pause()
			player.load(filepath10)
			player.play()
			
		if input_state[9] == False:
			player.pause()
			player.load(filepath9)
			player.play()
			
		if input_state[11] == False:
			player.pause()
			player.load(filepath11)
			player.play()
	
		
		if input_state[20] == False:
			player.play_pause()
			time.sleep(0.125)
			
		if input_state[16] == False:
			player.seek(5)
			
		if input_state[21] == False:
			player.seek(-5)
			
		if input_state[12] == False:
			player.quit()
			
		if input_state[2] == False:
			camera.start_preview()
			time.sleep(5)
			camera.stop_preview()
			
		if input_state[3] == False:
			camera.capture(time.strftime('./pictures/%a, %d-%b-%Y %H:%M:%S', time.gmtime()) + '.jpg')
		
		if input_state[4] == False:
			'''if is_recording == True:
				camera.stop_recording()
				is_recording = False
			else:
				camera.start_recording(time.strftime('./videos/%a, %d-%b-%Y %H:%M:%S', time.gmtime()) + '.h264')
				is_recording = True
				time.sleep(0.1)'''
			camera.start_recording(time.strftime('./videos/%a, %d-%b-%Y %H:%M:%S', time.gmtime()) + '.h264')
			time.sleep(15)
			camera.stop_recording()
		

if __name__ == '__main__':
	main()

