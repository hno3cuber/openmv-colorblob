 # By: HNO3   - 周一 9月 26 2022
import sensor, image, time,lcd,math
from pyb import UART
import json
#sensor.reset( freq=36000000,dual_buff=True)
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQVGA)#QVGA(320,240)  QQVGA(160,120)
sensor.set_windowing((80,60))
sensor.skip_frames(time=2000)
#sensor.set_framerate(30)
#sensor.set_framebuffers(sensor.DOUBLE_BUFFER)
lcd.init(type=lcd.LCD_SHIELD,width=132,height=162,refresh=30,triple_buffer=False,bgr=False)
sensor.set_hmirror(0)
sensor.set_vflip(0)
clock = time.clock()


uart = UART(3, 115200)#TX:P4 RX:P5


#THRESHOLD = (255,100)
THRESHOLD = (15,105)#需要的色块的灰度阈值，根据实际情况调节
def zhongxin (ax,bx,ay,by):#使用灰度遍历找色块
    midx = 0
    midy = 0
    num = 0
    angle=0
    #img.draw_rectangle(ax,ay,bx+1-ax,by+1-ay, color = (255, 0, 0))
    for x in range(ax,bx,3):#提高运行速度
        for y in range(ay,by,3):
            if img.get_pixel(x,y) == 255:#黑色的灰度值是255，若该像素点是黑色，则黑色像素点的数量+1
                midx += x
                midy += y
                num += 1
    if num > 5:#5不是固定数字，根据识别区域大小设定
        midx /= num#色块中心的坐标
        midy /= num
    img.draw_cross(int(midx), int(midy), color = (160, 160, 160))
    return midx,midy,num
while(True):
    clock.tick()
    img=sensor.snapshot()
    img.lens_corr(1.1)
    img.binary([THRESHOLD])#将画面二值化，黑色即为所需色块
    #img = sensor.snapshot()
    img.draw_rectangle((25,10,30,20),color=127,thickness=1)#框出想要识别的范围
    l0=zhongxin(25,56,10,31)#对范围内进行灰度检测





