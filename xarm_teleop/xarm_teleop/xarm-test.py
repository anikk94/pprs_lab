import sys
import math
import time
import queue
import datetime
import random
import traceback
import threading
from xarm import version
from xarm.wrapper import XArmAPI

from pynput import keyboard

class RobotMain(object):
    def __init__(self, robot, **kwargs):
        self.alive = True
        self._arm = robot
        self._ignore_exit_state = False
        self.s = 0.1
        self._tcp_speed = 100*self.s
        self._tcp_acc = 2000*self.s
        self._angle_speed = 20
        self._angle_acc = 500
        self._vars = {}
        self._funcs = {}
        self._robot_init()


        self.running = True
        self.x=195
        self.y=-18.5
        self.z=553.5
        
        
    def _robot_init(self):
        self._arm.clean_warn()
        self._arm.clean_error()
        self._arm.motion_enable(True)
        self._arm.set_mode(0)
        self._arm.set_state(0)
        time.sleep(1)
        self._arm.register_error_warn_changed_callback(self._error_warn_changed_callback)
        self._arm.register_state_changed_callback(self._state_changed_callback)

    def _error_warn_changed_callback(self, data):
        if data and data['error_code'] != 0:
            self.alive = False
            self.pprint('err={}, quit'.format(data['error_code']))
            self._arm.release_error_warn_changed_callback(self._error_warn_changed_callback)

    def _state_changed_callback(self, data):
        if not self._ignore_exit_state and data and data['state'] == 4:
            self.alive = False
            self.pprint('state=4, quit')
            self._arm.release_state_changed_callback(self._state_changed_callback)

    def _check_code(self, code, label):
        if not self.is_alive or code != 0:
            self.alive = False
            ret1 = self._arm.get_state()
            ret2 = self._arm.get_err_warn_code()
            self.pprint('{}, code={}, connected={}, state={}, error={}, ret1={}, ret2={}'.format(
                label, code, self._arm.connected, self_arm.state, self._arm.error_code, ret1, ret2)
            )
        return self.is_alive
            
    @staticmethod
    def pprint(*args, **kwargs):
        try:
            stack_tuple = traceback.extract_stack(limit=2)[0]
            print('[{}][{}] {}'.format(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), stack_tuple[1], ' '.join(map(str, args))
            ))
        except:
            print(*args, **kwargs)
    
    @property
    def arm(self):
        return self._arm

    @property
    def VARS(self):
        return self._vars
    
    @property
    def FUNCS(self):
        return self._funcs

    @property
    def is_alive(self):
        if self.alive and self._arm.connected and self._arm.error_code == 0:
            if self._ignore_exit_state:
                return True
            if self._arm.state == 5:
                cnt = 0
                while self._arm.state == 5 and cnt < 5:
                    cnt += 1
                    time.sleep(0.1)
            return self._arm.state < 4
        else:
            return False

    def run(self):
        print("RobotMain::run()")
        while self.running:
            1
        #try:
        #    # Draw Circle
        #    self._tcp_acc = 2000*self.s
        #    self._tcp_speed = 200*self.s
        #    for i in range(int(10)):
        #        if not self.is_alive:
        #            break
        #        t1 = time.monotonic()
        #        code = self._arm.set_servo_angle(angle=[0.0, -45.0, 0.0, 0.0, -45.0, 0.0], speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=0.0)
        #        if not self._check_code(code, 'set_servo_angle'):
        #            return
        #        code = self._arm.set_position(*[300.0, 0.0, 400.0, 0.0, -90.0, 180.0], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=-1.0, wait=True)
        #        if not self._check_code(code, 'set_position'):
        #            return
        #        code = self._arm.move_circle([350.0, 50.0, 400.0, 180.0, -90.0, 0.0], [350.0, -50.0, 400.0, 180.0, -90.0, 0.0], float(1800) / 360 * 100, speed=self._tcp_speed, mvacc=self._tcp_acc, wait=True)
        #        if not self._check_code(code, 'move_circle'):
        #            return
        #        interval = time.monotonic() - t1
        #        if interval < 0.01:
        #            time.sleep(0.01 - interval)
        #except Exception as e:
        #    self.pprint('MainException: {}'.format(e))
        #finally:
        #    self.alive = False
        #    self._arm.release_error_warn_changed_callback(self._error_warn_changed_callback)
        #    self._arm.release_state_changed_callback(self._state_changed_callback)
        
def on_press(key, injected):
    try:
        print(' alphanumeric key {} pressed; it was {}'.format(
            key.char, 'faked' if injected else 'not faked'))


        if key.char == '0':
            print('mode 0')
            arm.set_mode(0)
        elif key.char == '1':
            print('mode 1')
            arm.set_mode(1)
        elif key.char == '2':
            print('mode 2')
            arm.set_mode(2)
            arm.set_state(0)

    except AttributeError:
        print(' special key {} pressed'.format(
            key))
        if key == keyboard.Key.esc:
            print("Stopping Program")
            robot_main.running = False
            return False
        elif key == keyboard.Key.up:
            print("up key pressed")
            robot_main.x+=5
            arm.set_position(robot_main.x,robot_main.y,robot_main.z,177, -19.5,0)
        elif key == keyboard.Key.down:
            print("down key pressed")
            robot_main.x-=5
            arm.set_position(robot_main.x,robot_main.y,robot_main.z,177, -19.5,0)
        elif key == keyboard.Key.left:
            print("up key pressed")
            robot_main.y+=5
            arm.set_position(robot_main.x,robot_main.y,robot_main.z,177, -19.5,0)
        elif key == keyboard.Key.right:
            print("down key pressed")
            robot_main.y-=5
            arm.set_position(robot_main.x,robot_main.y,robot_main.z,177, -19.5,0)


def on_release(key, injected):
    print('{} released; it was {}'.format(
        key, 'faked' if injected else 'not faked'))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

        
if __name__ == '__main__':


    RobotMain.pprint('xArm-Python-SDK Version:{}'.format(version.__version__))
    arm = XArmAPI('192.168.1.221', baud_checkset=False)
    robot_main = RobotMain(arm)
    
    ## BLOCKING
    #with keyboard.Listener(on_press=on_press, on_release = on_release) as listener:
    #    listener.join()
    #with keyboard.Listener(on_press=on_press) as listener:
    #    listener.join()
    ## NON-BLOCKING
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    robot_main.run()
