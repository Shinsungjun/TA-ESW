from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb

from Character import Character
from Joystick import Joystick

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
    joystick.disp.image(my_image)
    # 잔상이 남지 않는 코드
    my_circle = Character(joystick.width, joystick.height)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
    while True:
        command = None
        if not joystick.button_U.value:  # up pressed
            command = 'up_pressed'

        elif not joystick.button_D.value:  # down pressed
            command = 'down_pressed'

        elif not joystick.button_L.value:  # left pressed
            command = 'left_pressed'

        elif not joystick.button_R.value:  # right pressed
            command = 'right_pressed'
            
        else:
            command = None

        my_circle.move(command)

        #그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
        my_draw.ellipse(tuple(my_circle.position), outline = my_circle.outline, fill = (0, 0, 0))
    #좌표는 동그라미의 왼쪽 위, 오른쪽 아래 점 (x1, y1, x2, y2)
        joystick.disp.image(my_image)


if __name__ == '__main__':
    main()