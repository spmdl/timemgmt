#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import subprocess

# WORK_MINUTES = 1
# BREAK_MINUTES = 0

class Tomato:
    def __init__(self):
        self.spend_time = 0
        self.work_minutes = 0
        self.break_minutes = 0

    def start(self, work_minutes, break_minutes):
        try:
            if len(sys.argv) <= 1:
                print(f'🍅 tomato {work_minutes} minutes. Ctrl+C to exit')
                self.tomato(work_minutes, 'It is time to take a break')
                print(f'🛀 break {break_minutes} minutes. Ctrl+C to exit')
                self.tomato(break_minutes, 'It is time to work')

            elif sys.argv[1] == '-t':
                minutes = int(sys.argv[2]) if len(sys.argv) > 2 else work_minutes
                print(f'🍅 tomato {minutes} minutes. Ctrl+C to exit')
                self.tomato(minutes, 'It is time to take a break')

            elif sys.argv[1] == '-b':
                minutes = int(sys.argv[2]) if len(sys.argv) > 2 else break_minutes
                print(f'🛀 break {minutes} minutes. Ctrl+C to exit')
                self.tomato(minutes, 'It is time to work')

            elif sys.argv[1] == '-h':
                help()

            else:
                help()

        except KeyboardInterrupt:
            print('\n👋 goodbye')
            return 's'
        except Exception as ex:
            print(ex)
            exit(1)


    def tomato(self, minutes, notify_msg):
        start_time = time.perf_counter()
        while True:
            diff_seconds = int(round(time.perf_counter() - start_time))
            left_seconds = minutes * 60 - diff_seconds
            if left_seconds <= 0:
                print('')
                break

            countdown = '{}:{} ⏰'.format(int(left_seconds / 60), int(left_seconds % 60))
            duration = min(minutes, 25)
            self.spend_time = diff_seconds
            self.progressbar(diff_seconds, minutes * 60, duration, countdown)
            time.sleep(1)

        self.notify_me(notify_msg)


    def progressbar(self, curr, total, duration=10, extra=''):
        frac = curr / total
        filled = round(frac * duration)
        print(f"\r{'🍅' * filled} {'--' * (duration - filled)} [{frac:.0%}] {extra}", end='')


    def notify_me(self, msg):
        '''
        # macos desktop notification
        terminal-notifier -> https://github.com/julienXX/terminal-notifier#download
        terminal-notifier -message <msg>

        # ubuntu desktop notification
        notify-send

        # voice notification
        say -v <lang> <msg>
        lang options:
        - Daniel:       British English
        - Ting-Ting:    Mandarin
        - Sin-ji:       Cantonese
        '''

        print(msg)
        try:
            if sys.platform == 'darwin':
                # macos desktop notification
                subprocess.run(['terminal-notifier', '-title', '🍅', '-message', msg])
                subprocess.run(['say', '-v', 'Daniel', msg])
            elif sys.platform.startswith('linux'):
                # ubuntu desktop notification
                subprocess.Popen(["notify-send", '🍅', msg])
            else:
                # windows?
                # TODO: windows notification
                pass

        except:
            # skip the notification error
            pass


    def help(self, WORK_MINUTES=25, BREAK_MINUTES=0):
        appname = sys.argv[0]
        appname = appname if appname.endswith('.py') else 'tomato'  # tomato is pypi package
        print('====== 🍅 Tomato Clock =======')
        print(f'{appname}         # start a {WORK_MINUTES} minutes tomato clock + {BREAK_MINUTES} minutes break')
        print(f'{appname} -t      # start a {WORK_MINUTES} minutes tomato clock')
        print(f'{appname} -t <n>  # start a <n> minutes tomato clock')
        print(f'{appname} -b      # take a {BREAK_MINUTES} minutes break')
        print(f'{appname} -b <n>  # take a <n> minutes break')
        print(f'{appname} -h      # help')


tomato = Tomato()

if __name__ == "__main__":
    tomato = Tomato()
    tomato.start()
