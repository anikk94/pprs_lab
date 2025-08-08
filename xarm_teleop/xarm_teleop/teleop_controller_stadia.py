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


import pygame

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

        self.current_direction = {'x': 0, 'y': 0, 'z': 0}
        self.move_step = 2.0

    # not useful, just to try        
    @property
    def x_val(self):
        print("x()")
        return self.x



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
        #while self.running:
        #
        #    1

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
        

        while self.is_alive and self.running:
            ret, pos = self._arm.get_position(is_radian=False)

            if ret == 0:
                current_x, current_y, current_z, roll, pitch, yaw = pos          
                
                target_x = current_x + self.current_direction['x'] * self.move_step
                target_y = current_y + self.current_direction['y'] * self.move_step
                target_z = current_z + self.current_direction['z'] * self.move_step

                self._arm.set_servo_cartesian(
                    [target_x, target_y, target_z, roll, pitch, yaw],
                    speed=20,
                    mvacc=2000,
                )

            time.sleep(0.01)

def on_press(key, injected):
    try:
        print(' alphanumeric key {} pressed; it was {}'.format(
            key.char, 'faked' if injected else 'not faked'))


        if key.char == '0':
            print('mode 0')
            arm.set_mode(0)
        elif key.char == '1':
            print('mode 1')
            arm.motion_enable(True)
            arm.set_mode(1)
            arm.set_state(0)
            time.sleep(0.1)
        elif key.char == '2':
            print('mode 2')
            arm.set_mode(2)
        elif key.char == '3':
            print('mode 3')
            arm.set_mode(3)
        elif key.char == '4':
            print('mode 4')
            arm.set_mode(4)
        elif key.char == '5':
            print('mode 5')
            arm.set_mode(5)
        elif key.char == '6':
            print('mode 6')
            arm.set_mode(6)
        elif key.char == '7':
            print('mode 7')
            arm.set_mode(7)
        elif key.char == '8':
            print('mode 8')
            arm.set_mode(8)
        elif key.char == '9':
            print('mode 9')
            arm.set_mode(9)
        elif key.char == '-':
            print('setting arm state to 0')
            arm.set_state(0)
        elif key.char == 'a' or key.char == "A":
            print('z+')
            robot_main.current_direction['z'] = 1
        elif key.char == 's' or key.char == "S":
            print('z-')
            robot_main.current_direction['z'] = -1

    except AttributeError:
        print(' special key {} pressed'.format(
            key))
        if key == keyboard.Key.esc:
            print("Stopping Program")
            robot_main.running = False
            return False
        #elif key == keyboard.Key.up:
        #    print("up key pressed")
        #    robot_main.x+=5
        #    arm.set_position(robot_main.x,robot_main.y,robot_main.z,177, -19.5,0)
        #elif key == keyboard.Key.down:
        #    print("down key pressed")
        #    robot_main.x-=5
        #    arm.set_position(robot_main.x,robot_main.y,robot_main.z,177, -19.5,0)
        #elif key == keyboard.Key.left:
        #    print("up key pressed")
        #    robot_main.y+=5
        #    arm.set_position(robot_main.x,robot_main.y,robot_main.z,177, -19.5,0)
        #elif key == keyboard.Key.right:
        #    print("down key pressed")
        #    robot_main.y-=5
        #    arm.set_position(robot_main.x,robot_main.y,robot_main.z,177, -19.5,0)
        elif key == keyboard.Key.up:
            robot_main.current_direction['x']=1
        elif key == keyboard.Key.down:
            robot_main.current_direction['x']=-1
        elif key == keyboard.Key.right:
            robot_main.current_direction['y']=-1
        elif key == keyboard.Key.left:
            robot_main.current_direction['y']=1


def on_release(key, injected):
    print('{} released; it was {}'.format(
        key, 'faked' if injected else 'not faked'))
    if key == keyboard.Key.esc:
        # Stop listener
        robot_main.running = False
        return False
    elif key == keyboard.Key.up:
        robot_main.current_direction['x']=0
    elif key == keyboard.Key.down:
        robot_main.current_direction['x']=0
    elif key == keyboard.Key.right:
        robot_main.current_direction['y']=0
    elif key == keyboard.Key.left:
        robot_main.current_direction['y']=0
    elif key.char == 'a' or key.char == "A":
        print("a/A released")
        robot_main.current_direction['z'] = 0
    elif key.char == 's' or key.char == "S":
        print("s/S released")
        robot_main.current_direction['z'] = 0


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



if __name__ == '__main__':

    pygame.init()

    pygame.joystick.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 500

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("joysticks")

    font_size = 30
    font = pygame.font.SysFont("Futura", font_size)

    clock = pygame.time.Clock()
    FPS = 60

    joysticks = []

    x = 350
    y = 200
    player = pygame.Rect(x, y, 100, 100)


    col="royalblue"

    run = True
    while run:
        clock.tick(FPS)

        screen.fill(pygame.Color("midnightblue"))

        player.topleft=(x, y)


        draw_text("controllers: " + str(pygame.joystick.get_count()), font, pygame.Color("azure"), 10, 10)
        for joystick in joysticks:
            draw_text("Battery Level: " +str(joystick.get_power_level()), font, pygame.Color("azure"), 10, 35 )
            draw_text("Controller Type: " +str(joystick.get_name()), font, pygame.Color("azure"), 10, 60) 
            draw_text("Number of Axes: " +str(joystick.get_numaxes()), font, pygame.Color("azure"), 10, 85)

        for joystick in joysticks:
            if joystick.get_button(0):
                    col = "royalblue"
            if joystick.get_button(1):
                    col = "crimson"
            if joystick.get_button(2):
                    col = "fuchsia"
            if joystick.get_button(3):
                    col = "forestgreen"


            # 0  - abxy
            # 1  - abxy
            # 2  - abxy
            # 3  - abxy
            # 4  - L1
            # 5  - R1
            # 6  - ... button
            # 7  - ||| button
            # 8  - STADIA button
            # 9  - L3 button
            # 10 - R3 button
            # 11 - ASSISTANT button
            # 12 - FULLSCREEN button
            # 13 - R2 button
            # 14 - L2 button
            # 15 - NA button
            # 16 - NA button
            # 17 - NA button

            if joystick.get_button(4):
                player.scale_by(1.1)
            if joystick.get_button(14):
                player.scale_by(0.9)
            h_move = joystick.get_axis(0)
            v_move = joystick.get_axis(1)
            if abs(v_move) > 0.05:
                y+= v_move *10
            if abs(h_move) > 0.05:
                x+= h_move *10

            if joystick.get_hat(0)[1]== -1:
                y += 10
            if joystick.get_hat(0)[1]== 1:
                y -= 10
            if joystick.get_hat(0)[0]== 1:
                x += 10
            if joystick.get_hat(0)[0]== -1:
                x -= 10


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("User closed program")
                run = False
            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks.append(joy)
            
        
        pygame.draw.rect(screen, pygame.Color(col), player)

        pygame.display.flip()


    # RobotMain.pprint('xArm-Python-SDK Version:{}'.format(version.__version__))
    # arm = XArmAPI('192.168.1.221', baud_checkset=False)
    # robot_main = RobotMain(arm)

    # robot_main.run()
    # arm.disconnect()
