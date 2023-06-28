from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *
import math
import sys
import struct
sys.setrecursionlimit(10**6)
import os
from PIL import Image # pillow 라이브러ㅣ 중 Image 객체만 사용

# ======================================================================================================
## Function
# ======================================================================================================
##### 공통 함수 #####
def loadImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # https://stackoverflow.com/questions/44403566/add-multiple-extensions-in-one-filetypes-mac-tkinter-filedialog-askopenfilenam
    filename = askopenfilename(parent=window,
                               filetypes=(("칼라", "*.png *.jpg *.bmp *.gif"), ("모든 파일", "*.*")))
    # 파일 크기 알아내기
    pillow = Image.open(filename)
    inH = pillow.height
    inW = pillow.width
    # 메모리 확보 (영상 크기)
    inImage = [[[0 for _ in range(inW)] for _ in range(inH)] for _ in range(3)]

    # 파일 --> 메모리 로딩
    pillowRGB = pillow.convert('RGB') # RGB 모델로 변경
    for i in range(inH):
        for k in range(inW):
            r, g, b = pillowRGB.getpixel((k, i)) # <- pillow 내부에서 경험적인 것.
            inImage[0][i][k] = r
            inImage[1][i][k] = g
            inImage[2][i][k] = b

    equalImage()

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

    rgbString = ""
    for i in range(outH):
        tmpString = ""
        for k in range(outW):
            r = outImage[0][i][k]
            g = outImage[1][i][k]
            b = outImage[2][i][k]
            tmpString += '#%02x%02x%02x ' % (r, g, b)
        rgbString += '{'+tmpString+'} '
    paper.put(rgbString)

    canvas.pack()

def saveImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    saveFp = asksaveasfile(parent=window, mode='wb',
        defaultextension='*.raw',
        filetypes=(("RAW파일", "*.raw"),("모든 파일", "*.*")))

    for i in range(outH) :
        for k in range(outW) :
            saveFp.write( struct.pack('B', outImage[i][k]))
    saveFp.close()
    messagebox.showinfo('성공',  saveFp.name + '으로 저장')

## 영상 처리 함수부 ##
def equalImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;  outW = inW;
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(inH) :
            for k in range(inW) :
                outImage[rgb][i][k] = inImage[rgb][i][k]
    ##############################
    displayImage()

def reverseImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;  outW = inW;
    # 메모리 할당
    inImage = outImage
    # outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(inH) :
            for k in range(inW) :
                outImage[rgb][i][k] = 255- inImage[rgb][i][k]
    ##############################
    displayImage()

def addImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;  outW = inW;
    # 메모리 할당
    inImage = outImage
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    value = askinteger("밝게할 값", "-255 부터 255까지 입력", minvalue=-255, maxvalue=255)
    for rgb in range(3):
        for i in range(inH) :
            for k in range(inW) :
                if (inImage[rgb][i][k] + value > 255) :
                    outImage[rgb][i][k] = 255
                elif (inImage[rgb][i][k] + value < 0) :
                    outImage[rgb][i][k] = 0
                else :
                    outImage[rgb][i][k] = inImage[rgb][i][k] + value
    ##############################
    displayImage()

def moveImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    inImage = outImage
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;  outW = inW;
    # 메모리 할당
    inImage = outImage
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    xVal = askinteger("X값", "")
    yVal = askinteger("Y값", "")

    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(inH) :
            for k in range(inW) :
                if 0 <= i+xVal < outH and 0 <= k+yVal < outW:
                    outImage[rgb][i+xVal][k+yVal] = inImage[rgb][i][k]
    ##############################
    displayImage()

def zoomOutImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    scale = askinteger("축소 배율", "")
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH//scale;  outW = inW//scale;
    # 메모리 할당
    inImage = outImage
    # outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(inH) :
            for k in range(inW) :
                outImage[rgb][i//scale][k//scale] = inImage[rgb][i][k]
    # 프로그램 효율화를 고려한다면 포워딩 방식의 경우 값을 덮어쓰기 때문에 상대적으로 비효율적이다!
    # 즉, 백워딩 방식이 훨씬 효율적이다. 메모리 및 CPU Resource 관리 때문!
    ##############################
    displayImage()

def zoomInImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    scale = askinteger("확대 배율", "")
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH*scale;  outW = inW*scale;
    # 메모리 할당
    inImage = outImage
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    # for i in range(inH) :
    #     for k in range(inW) :
    #         outImage[i*scale][k*scale] = inImage[i][k]
    for rgb in range(3):
        for i in range(outH) :
            for k in range(outW) :
                outImage[rgb][i][k] = inImage[rgb][i//scale][k//scale]
    ##############################
    displayImage()

def rotateImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    angle = askinteger("각도", "0~360")
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;
    outW = inW;
    # 메모리 할당
    inImage = outImage
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    radian = angle * math.pi /180.0
    cx = inH//2
    cy = inW//2

    ## ** 찐 영상처리 알고리즘 ** ##
    # Forwarding
    # for i in range(inH):
    #     for k in range(inW):
    #         newI = int(math.cos(radian)*(i-cx) - math.sin(radian)*(k-cy))+cx
    #         newK = int(math.sin(radian)*(i-cx) + math.cos(radian)*(k-cy))+cy
    #
    #         if 0<newI<outH and 0<newK<outW:
    #             outImage[newI][newK] = inImage[i][k]

    # Backwarding
    for i in range(outH):
        for k in range(outW):
            oldI = int(math.cos(radian)*(i-cx) - math.sin(radian)*(k-cy))+cx
            oldK = int(math.sin(radian)*(i-cx) + math.cos(radian)*(k-cy))+cy

            if 0<oldI<inH and 0<oldK<inW:
                outImage[0][i][k] = inImage[0][oldI][oldK]
                outImage[1][i][k] = inImage[1][oldI][oldK]
                outImage[2][i][k] = inImage[2][oldI][oldK]
    ##############################
    displayImage()

def grayImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;
    outW = inW;
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for i in range(inH):
        for k in range(inW):
            hap = inImage[0][i][k] + inImage[1][i][k] + inImage[2][i][k]
            outImage[0][i][k] = outImage[1][i][k] = outImage[2][i][k] = hap // 3
    ##############################
    displayImage()

def gammaImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;  outW = inW;
    # 메모리 할당
    inImage = outImage
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    value = askfloat("감마 값", "0.1부터 2.5까지 입력", minvalue=0.1, maxvalue=2.5)
    for rgb in range(3):
        for i in range(inH) :
            for k in range(inW) :
                outImage[rgb][i][k] = int(inImage[rgb][i][k]**(1/value))
    ##############################
    displayImage()

def parabollaImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;
    outW = inW;
    # 메모리 할당
    inImage = outImage
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 찐 영상처리 알고리즘 ** ##
    value = askinteger("CAP와 CUP중 선택하세요", "1은 CAP, 2는 CUP", minvalue=1, maxvalue=2)
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if value == 1:
                    outImage[rgb][i][k] = 255-int(255*(inImage[rgb][i][k]/128.0-1.0)**2) # CAP (밝은 곳 입체형)
                elif value ==2:
                    outImage[rgb][i][k] = int(255 * (inImage[rgb][i][k] / 128.0 - 1.0) ** 2)  # CUP (어두운 곳 입체형)
    ##############################
    displayImage()

# ======================================================================================================
## Global Variables
# ======================================================================================================
inImage, outImage = None, None
inH, inW, outH, outW = 0, 0, 0, 0

window, canvas, paper = None, None, None
filename = ""

# ======================================================================================================
## Main Scope
# ======================================================================================================
window = Tk()
window.geometry('1300x1300')
window.title('GrayScale Image Processing (Beta 1)')

mainMenu = Menu(window) # 메뉴의 틀
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu) # 최상위 메뉴 (파일)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=loadImage)
fileMenu.add_command(label='저장', command=saveImage)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exit)

image1Menu = Menu(mainMenu) # 최상위 메뉴 (영상처리)
mainMenu.add_cascade(label='화소점 처리', menu=image1Menu)
image1Menu.add_command(label='동일영상', command=equalImage)
image1Menu.add_command(label='그레이스케일', command=grayImage)
image1Menu.add_command(label='반전', command=reverseImage)
image1Menu.add_command(label='밝게/어둡게', command=addImage)
image1Menu.add_command(label='감마보정', command=gammaImage)
image1Menu.add_command(label='파라볼라보정', command=parabollaImage)

image2Menu = Menu(mainMenu) # 최상위 메뉴 (기하학처리)
mainMenu.add_cascade(label='기하학 처리', menu=image2Menu)
image2Menu.add_command(label='이동', command=moveImage)
image2Menu.add_command(label='축소', command=zoomOutImage)
image2Menu.add_command(label='확대', command=zoomInImage)
image2Menu.add_command(label='회전', command=rotateImage)

window.mainloop()
# ======================================================================================================