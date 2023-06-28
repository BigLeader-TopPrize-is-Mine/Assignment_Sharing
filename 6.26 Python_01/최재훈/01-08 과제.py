from tkinter import *
import math
import sys
sys.setrecursionlimit(10**6)
import os

# ======================================================================================================
## Function
def displayImage(image):
    global window, canvas, paper, height, width, filename
    if canvas != None:
        canvas.destroy()
    height = width = len(image)
    canvas = Canvas(window, height=height, width=width)
    paper = PhotoImage(height=height, width=width)
    canvas.create_image((height / 2, width / 2), image=paper, state='normal')

    origin = []
    origin = image

    for i in range(height):
        for k in range(width):
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r,g,b), (k,i)) # 16진수 2자리로 표현하겠다!
    print(f"displayImg : {height, width}")
    canvas.pack()

def reverseImage():
    for i in range(height):
        for k in range(width):
            origin[i][k] = 255 - origin[i][k]

    displayImage(origin)

def lightenImage():
    for i in range(height):
        for k in range(width):
            if origin[i][k]+50 >=255:
                origin[i][k] = 255
            else:
                origin[i][k] += 50

    displayImage(origin)

def darkenImage():
    for i in range(height):
        for k in range(width):
            if origin[i][k]-100 <=0:
                origin[i][k] = 0
            else:
                origin[i][k] -= 100

    displayImage(origin)

def darkenImage_127():
    for i in range(height):
        for k in range(width):
            if origin[i][k] >= 127:
                origin[i][k] = 255
            else:
                origin[i][k] = 0

    displayImage(origin)

def darkenImage_avg():
    hap = 0
    for i in range(height):
        for k in range(width):
            hap += origin[i][k]
    avg = hap / (height*width)

    for i in range(height):
        for k in range(width):
            if origin[i][k] >= avg:
                origin[i][k] = 255
            else:
                origin[i][k] = 0

    displayImage(origin)

def darkenImage_mid():
    def flatten(data):
        output = []
        for item in data:
            if type(item) == list:
                output.extend(flatten(item))
            else:
                output.append(item)
        return output

    def qsort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        remain = arr[1:]

        left_side = [x for x in remain if x <= pivot]
        right_side = [x for x in remain if x > pivot]

        return qsort(left_side) + [pivot] + qsort(right_side)

    tmp = qsort(flatten(origin))
    mid = tmp[len(tmp)//2]

    for i in range(height):
        for k in range(width):
            if origin[i][k] >= mid:
                origin[i][k] = 255
            else:
                origin[i][k] = 0

    displayImage(origin)

def rotate_90():
    after_rotate = [[0] * width for _ in range(height)]
    for _ in range(90 // 90):
        for i in range(height):
            for k in range(width):
                after_rotate[k][512 - i - 1] = origin[i][k]

    for i in range(height):
        for k in range(width):
            origin[i][k] = after_rotate[i][k]

    displayImage(origin)

def rotate_180():
    after_rotate = [[0] * width for _ in range(height)]
    for _ in range(180 // 90):
        for i in range(height):
            for k in range(width):
                after_rotate[k][512 - i - 1] = origin[i][k]

        for i in range(height):
            for k in range(width):
                origin[i][k] = after_rotate[i][k]

    displayImage(origin)

def rotate_270():
    after_rotate = [[0] * width for _ in range(height)]
    for _ in range(270 // 90):
        for i in range(height):
            for k in range(width):
                after_rotate[k][512 - i - 1] = origin[i][k]

        for i in range(height):
            for k in range(width):
                origin[i][k] = after_rotate[i][k]

    displayImage(origin)

def sideMirroring():
    rem = [[0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            rem[i][height-j-1] = origin[i][j]

    for i in range(height):
        for k in range(width):
            origin[i][k] = rem[i][k]

    displayImage(origin)

def updowMirroring():
    rem = [[0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            rem[height - i - 1][j] = origin[i][j]

    for i in range(height):
        for k in range(width):
            origin[i][k] = rem[i][k]

    displayImage(origin)

def gamma():
    g = 1.2
    for i in range(height):
        for k in range(width):
            origin[i][k] = int(origin[i][k]**(1/g))
    displayImage(origin)

def parabolla():
    for i in range(height):
        for k in range(width):
            # origin[i][k] = 255-int(255*(origin[i][k]/128.0-1.0)**2) # CAP (밝은 곳 입체형)
            origin[i][k] = int(255 * (origin[i][k] / 128.0 - 1.0) ** 2)  # CUP (어두운 곳 입체형)
    displayImage(origin)

def twice_upscale():
    global origin, height, width
    after_upscale = [[0] * int(width*2) for _ in range(int(height*2))]
    for i in range(height):
        for k in range(width):
            after_upscale[int(i*2)][int(k*2)] = origin[i][k]

    displayImage(after_upscale)

def twice_downscale():
    global origin
    after_downscale = [[0] * int(width / 2) for _ in range(int(height / 2))]
    for i in range(height):
        for k in range(width):
            after_downscale[int(i / 2)][int(k/2)] = origin[i][k]
    displayImage(after_downscale)

def rotate_45():
    global origin
    val, pivot = 1/math.sqrt(2), int(width/2*math.sqrt(2)//2)
    after_rotate = [[0] * int(width*math.sqrt(2)) for _ in range(int(height*math.sqrt(2)))]
    print(width, height, val, pivot)
    print(len(after_rotate))
    for i in range(height):
        for k in range(width):
            if i>pivot and k>pivot:
                after_rotate[int(i * val + k * val)-pivot][int(k * val - i * val)-pivot] = origin[i][k]
            elif i>pivot and k<=pivot:
                after_rotate[int(i * val + k * val)-pivot][int(k * val - i * val)-pivot] = origin[i][k]
            elif i<=pivot and k>pivot:
                after_rotate[int(i*val+k*val)+pivot][int(k*val-i*val)+pivot] = origin[i][k]
            elif i<=pivot and k<=pivot:
                after_rotate[int(i * val + k * val) + pivot][int(k * val - i * val) + pivot] = origin[i][k]
    origin = after_rotate
    displayImage(origin)

def reborn():
    global rawForm
    displayImage(rawForm)

# ======================================================================================================
## Variables
window, canvas, paper = None, None, None
filename = ""
origin = []
height = 0
width = 0

# ======================================================================================================
## Main Area
window = Tk()
window.geometry('1300x1300')
window.title('영상처리 Alpha')

# ======================================================================================================
label = Label(window)
label.pack(fill='both')

btnReverse = Button(label,text='반전',command=reverseImage)
btnLighten = Button(label,text='밝게',command=lightenImage)
btnDarken = Button(label,text='어둡게',command=darkenImage)
btnDarken127 = Button(label,text='흑백(127)',command=darkenImage_127)
btnDarkenAvg = Button(label,text='흑백(평균)',command=darkenImage_avg)
btnDarkenMid = Button(label,text='흑백(중앙)',command=darkenImage_mid)
btnSideMirror = Button(label,text='미러링(좌우)',command=sideMirroring)
btnUpDownMirror = Button(label,text='미러링(상하)',command=updowMirroring)
btnGamma = Button(label,text='감마 연산',command=gamma)
btnParabolla = Button(label,text='파라볼라 연산',command=parabolla)
btnTwiceUpscale = Button(label,text='2배 확대',command=twice_upscale)
btnTwiceDownscale = Button(label,text='2배 축소',command=twice_downscale)
btnRotate90 = Button(label,text='90도 회전',command=rotate_90)
btnRotate180 = Button(label,text='180도 회전',command=rotate_180)
btnRotate270 = Button(label,text='270도 회전',command=rotate_270)
btnRotate45 = Button(label,text='45도 회전',command=rotate_45)
btnReborn = Button(label,text='원본',command=reborn)
btnReverse.pack(side='left')
btnLighten.pack(side='left')
btnDarken.pack(side='left')
btnDarken127.pack(side='left')
btnDarkenAvg.pack(side='left')
btnDarkenMid.pack(side='left')
btnSideMirror.pack(side='left')
btnUpDownMirror.pack(side='left')
btnGamma.pack(side='left')
btnParabolla.pack(side='left')
btnTwiceUpscale.pack(side='left')
btnTwiceDownscale.pack(side='left')
btnRotate90.pack(side='bottom')
btnRotate180.pack(side='bottom')
btnRotate270.pack(side='bottom')
btnRotate45.pack(side='bottom')
btnReborn.pack(side='bottom')

# ======================================================================================================
filename = '/Users/choejaehun/Desktop/빅리더/Pet_RAW(squre)/Pet_RAW(512x512)/dog12_512.raw'
# 파일 크기 알아내기
fsize = os.path.getsize(filename)
height = width = int(math.sqrt(fsize))

# 메모리 확보 (영상 크기)
origin = [[0 for _ in range(width)] for _ in range(height)]
rawForm = [[0 for _ in range(width)] for _ in range(height)]

# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height):
    for k in range(width):
        rawForm[i][k] = origin[i][k] = ord(rfp.read(1))

rfp.close()

displayImage(origin)

window.mainloop()
# ======================================================================================================