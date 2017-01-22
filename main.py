#!/usr/bin/env python3

import RPi.GPIO as GPIO
import picamera
import time
from omxplayer import OMXPlayer

FILE_PATH_26 = '/home/pi/video26.mp4'
FILE_PATH_19 = '/home/pi/video19.mp4'
FILE_PATH_13 = '/home/pi/video13.mp4'
FILE_PATH_6 = '/home/pi/video6.mp4'
FILE_PATH_5 = '/home/pi/video5.mp4'
FILE_PATH_10 = '/home/pi/video10.mp4'
FILE_PATH_9 = '/home/pi/video9.mp4'
FILE_PATH_11 = '/home/pi/video11.mp4'

def main():
    try:
        camera = picamera.PiCamera()
    except:
        print('')

    GPIO.setmode(GPIO.BCM)

    for i in range(2, 27):
        GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    counter = [0] * 27
    input_state = [True] * 27

    is_recording = False
    is_previewing = False

    player = OMXPlayer(FILE_PATH_26)
    length = player.duration()
    ratio = 5 / length
    player.pause()

    while True:
        for i in range(2, 27):
            input_state[i] = GPIO.input(i)

        if not input_state[26]:
            player.pause()
            player.load(FILE_PATH_26)
            player.play()

        if not input_state[19]:
            player.pause()
            player.load(FILE_PATH_19)
            player.play()

        if not input_state[13]:
            player.pause()
            player.load(FILE_PATH_13)
            player.play()

        if not input_state[6]:
            player.pause()
            player.load(FILE_PATH_6)
            player.play()

        if not input_state[5]:
            player.pause()
            player.load(FILE_PATH_5)
            player.play()

        if not input_state[10]:
            player.pause()
            player.load(FILE_PATH_10)
            player.play()

        if not input_state[9]:
            player.pause()
            player.load(FILE_PATH_9)
            player.play()

        if not input_state[11]:
            player.pause()
            player.load(FILE_PATH_11)
            player.play()

        if not input_state[20]:
            player.play_pause()
            time.sleep(0.125)

        if not input_state[16]:
            player.seek(5)

        if not input_state[21]:
            player.seek(-5)

        if not input_state[12]:
            player.quit()

        if not input_state[2]:
            camera.start_preview()
            time.sleep(5)
            camera.stop_preview()

        if not input_state[3]:
            camera.capture(time.strftime('./pictures/%a, %d-%b-%Y %H:%M:%S', time.gmtime()) + '.jpg')

        if not input_state[4]:
            '''
            if is_recording:
                camera.stop_recording()
                is_recording = False
            else:
                camera.start_recording(time.strftime('./videos/%a, %d-%b-%Y %H:%M:%S', time.gmtime()) + '.h264')
                is_recording = True
                time.sleep(0.1)
            '''
            camera.start_recording(time.strftime('./videos/%a, %d-%b-%Y %H:%M:%S', time.gmtime()) + '.h264')
            time.sleep(15)
            camera.stop_recording()

if __name__ == '__main__':
    main()
