#!/usr/bin/env python3

import anki_vector
from anki_vector.util import degrees
import time
import sys

hours_to_sleep = 8

with anki_vector.AsyncRobot() as robot:
    robot.conn.release_control()
    while True:
        if robot.touch.last_sensor_reading.is_being_touched:
            robot.conn.request_control()
            time.sleep(2)
            robot.behavior.say_text("Good night, I am going home")
            robot.behavior.drive_on_charger()
            time.sleep(10)
            robot.audio.stream_wav_file("../Sounds/truck_reversing.wav", 25)
            robot.behavior.set_head_angle(degrees(-22.0))

            duration_s = (hours_to_sleep * 3600)
            time.sleep(13)
            robot.screen.set_screen_to_color(anki_vector.color.Color(rgb=[0, 0, 0]), duration_sec=duration_s)
            robot.behavior.say_text("Commencing {} hour deep sleep".format(hours_to_sleep))
            time.sleep(duration_s)
            sys.exit()

