import math
import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import askinteger

from PIL import Image # 필로우 라이브러리 중 Image 객체만 사용

## 함수 선언부
### 공통 함수부 ###
def loadImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    filename = askopenfilename(parent=window,
            filetypes=(("칼라파일", "*.png *.jpg *.bmp *.gif "),("모든 파일", "*.*")))
    # 파일 크기 알아내기
    pillow = Image.open(filename)
    inH = pillow.height #필로우한테 가로 물어보기
    inW = pillow.width #필로우한테 세로 물어보기
    # fSize = os.path.getsize(filename)  # Byte 단위
    # inH = inW = int(math.sqrt(fSize)) #### 중요한 코드!!!!!!
    # 메모리 확보 (영상 크기)
    inImage = [[[0 for _ in range(inW)] for _ in range(inH)] for _ in range(3)] # rgb세종류
    # 파일 --> 메모리 로딩
    pillowRGB = pillow.convert('RGB') #RGB 모델로 변경
    for i in range(inH):
        for k in range(inW):
            r, g, b = pillowRGB.getpixel((k,i))
            inImage[0][i][k] = r
            inImage[1][i][k] = g
            inImage[2][i][k] = b

    colorEqualImage()

def displayImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    if canvas != None :
        canvas.destroy()
    window.geometry(str(outW) + 'x' + str(outH))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outW / 2, outH / 2), image=paper, state='normal')
    # for i in range(outH) :
    #     for k in range(outW) :
    #         r = g = b = outImage[i][k]
    #         paper.put('#%02x%02x%02x' % (r, g, b), (k, i))
    rgbString = "" ##위는 주석처리(속도개선)
    for i in range(outH):
        tmpString =""
        for k in range(outW):
            r = outImage[0][i][k]
            g = outImage[1][i][k]
            b = outImage[2][i][k]
            tmpString += '#%02x%02x%02x ' % (r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)

    canvas.pack()


def saveImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.raw',filetypes=(("RAW파일", "*.raw"),("모든 파일", "*.*")))
    import struct
    for i in range(outH) :
        for k in range(outW) :
            saveFp.write(struct.pack('B', outImage[i][k]))
        saveFp.close()
        messagebox.showinfo('성공', saveFp.name + '으로 저장')

## 영상 처리 함수부 ##
def colorEqualImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3) :
        for i in range(inH) :
            for k in range(inW) :
                outImage[rgb][i][k] = inImage[rgb][i][k]
    ##############################
    displayImage()
def colorGrayImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;  outW = inW;
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for i in range(inH) :
        for k in range(inW) :
            hap = inImage[0][i][k] + inImage[1][i][k] + inImage[2][i][k]
            outImage[0][i][k] = outImage[1][i][k] = outImage[2][i][k] = hap//3
    ##############################
    displayImage()

def colorReverseImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = 255 - inImage[rgb][i][k]
    ##############################
    displayImage()
def colorAddImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    value = askinteger("밝게할 값", "-255부터 255까지 입력", minvalue=-255, maxvalue=255)
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if (inImage[rgb][i][k] + value > 255) :
                    outImage[rgb][i][k] = 255
                elif (inImage[rgb][i][k] + value < 0) :
                    outImage[rgb][i][k] = 0
                else :
                    outImage[rgb][i][k] = inImage[rgb][i][k] + value
    ##############################
    displayImage()

def colorRealGrayImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if (inImage[rgb][i][k] < 127):
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = 255
    ##############################
    displayImage()

def colorMeanGrayImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    hap = 0
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                hap += inImage[rgb][i][k]
        avg = hap / (3 * inH * inW)
    for rgb in range(3):
        for i in range(inH) :
            for k in range(inW) :
                if (inImage[rgb][i][k] < avg):
                    outImage[rgb][i][k] = 255
                else:
                    outImage[rgb][i][k] = 0
    ##############################
    displayImage()

def colorMoveImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    xVal = askinteger("X값","")
    yVal = askinteger("Y값","")

    for rgb in range(3) :
        for i in range(inH) :
            for k in range(inW) :
                if (0 <= i+xVal < outH) and (0 <= k+yVal < outW) :
                    outImage[rgb][i+xVal][k+yVal] = inImage[rgb][i][k] # 범위 넘으면 버리기
    ##############################
    displayImage()

def colorZoomOutImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    scale = askinteger("축소배율","")
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH//scale
    outW = inW//scale
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3) :
        for i in range(inH) :
            for k in range(inW) :
                outImage[rgb][i//scale][k//scale] = inImage[rgb][i][k]
    ##############################
    displayImage()

def colorZoomInImage(): ##그냥(forwarding)하면 빈 곳 많이 생김 -> 홀문제는 backwarding으로 해결 하기
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    scale = askinteger("확대배율", "")
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH * scale
    outW = inW * scale
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3) :
        for i in range(outH):
            for k in range(outW):
                outImage[rgb][i][k] = inImage[rgb//scale][i//scale][k//scale]
    ##############################
    displayImage()

def colorRotateImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    angle = askinteger("각도", "0~360")
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH
    outW = inW
    # 메모리 할당

    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    radian = angle * math.pi / 180.0
    cx = inH // 2
    cy = inW // 2
    for rgb in range(3) :
        for i in range(outH) :
            for k in range(outW) :
                oldI = int(math.cos(radian) * (i-cx) - math.sin(radian)*(k-cy)) + cx
                oldK = int(-math.sin(radian) * (i-cx) - math.cos(radian) * (k-cy)) + cy

                if( 0<= oldI < inH ) and( 0<= oldK < inW ):
                    outImage[rgb][i][k] = inImage[rgb][oldI][oldK]
    ##############################
    displayImage()





## 전역 변수부
window, canvas, paper = None, None, None
filename = ""
inImage, outImage = None, None
inH, inW, outH, outW = 0, 0, 0, 0

## 메인 코드부
window = Tk()
window.geometry('300x300')
window.title('GrayScale Image Processing (Beta 1)')

mainMenu = Menu(window) # 메뉴의 틀
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu) # 상위 메뉴(파일)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=loadImage)
fileMenu.add_command(label='저장', command=saveImage)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exit)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label='영상처리1', menu=image1Menu)
image1Menu.add_command(label='동일영상', command=colorEqualImage)
image1Menu.add_command(label='그레이스케일', command=colorGrayImage)
image1Menu.add_command(label='반전', command=colorReverseImage)
image1Menu.add_command(label='밝게/어둡게', command=colorAddImage)
image1Menu.add_command(label='완전흑백', command=colorRealGrayImage)
image1Menu.add_command(label='흑백(평균)', command=colorMeanGrayImage)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label='기하학 처리', menu=image2Menu)
image2Menu.add_command(label='이동', command=colorMoveImage)
image2Menu.add_command(label='축소', command=colorZoomOutImage)
image2Menu.add_command(label='확대', command=colorZoomInImage)
image2Menu.add_command(label='회전', command=colorRotateImage)








window.mainloop()






