#!/usr/bin/env python3

import anki_vector
from anki_vector.util import degrees
import time
import sys

#change to the number of hours your require
hours_to_sleep = 8

with anki_vector.Robot() as robot:
    robot.conn.release_control()
    while True:
        if robot.touch.last_sensor_reading.is_being_touched:
            robot.conn.request_control()
            time.sleep(2)
            robot.behavior.say_text("Good night, I am going home")
            robot.behavior.drive_on_charger()
            robot.behavior.set_head_angle(degrees(-22.0))

            duration_s = (hours_to_sleep * 3600)
            robot.screen.set_screen_to_color(anki_vector.color.Color(rgb=[0, 0, 0]), duration_sec=duration_s)
            robot.behavior.say_text("Commencing {} hour deep sleep".format(hours_to_sleep))
            time.sleep(duration_s)
            sys.exit()

