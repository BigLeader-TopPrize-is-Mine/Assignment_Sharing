import math
import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from tkinter import messagebox
from PIL import Image # 필로우 라이브러리 중 Image 객체만 사용

## 함수
###  공통 함수 ###
def loadImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    filename = askopenfilename(parent=window,
            filetypes=(("칼라", "*.png;*.jpg;*.bmp;*.gif;"),("모든 파일", "*.*")))
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
            r, g, b = pillowRGB.getpixel((k, i))
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
    for i in range(outH) :
        tmpString = ""
        for k in range(outW) :
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
    saveFp = asksaveasfile(parent=window, mode='wb',
        defaultextension='*.png',
        filetypes=(("칼라", "*.png;*.jpg;*.bmp;*.gif;"),("모든 파일", "*.*")))
    import struct
    for i in range(outH) :
        for k in range(outW) :
            saveFp.write( struct.pack('B', outImage[i][k]))
    saveFp.close()
    messagebox.showinfo('성공',  saveFp.name + '으로 저장')

### 영상 처리 함수 ###
def equalImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = inImage[rgb][i][k]
    #########################
    displayImage()

def grayImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    hap = 0
    for i in range(inH):
        for k in range(inW):
            hap = inImage[0][i][k] + inImage[1][i][k] + inImage[2][i][k]
            outImage[0][i][k] = outImage[1][i][k] = outImage[2][i][k] = hap//3
    #########################
    displayImage()

def reverseImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = 255 - inImage[rgb][i][k]
    #########################
    displayImage()

def addImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    val = askinteger("밝게할 값", "-255 부터 255까지 입력", minvalue = -255, maxvalue = 255)

    hap = 0
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if inImage[rgb][i][k] + val > 255:
                    outImage[rgb][i][k] = 255
                elif inImage[rgb][i][k] + val < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] += val

    #########################
    displayImage()

def blacknwhiteMImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    hap = 0
    for i in range(inH):
        for k in range(inW):
            hap = inImage[0][i][k] + inImage[1][i][k] + inImage[2][i][k]
            if hap//3 < 127:
                outImage[0][i][k] = outImage[1][i][k] = outImage[2][i][k] = 0
            else:
                outImage[0][i][k] = outImage[1][i][k] = outImage[2][i][k] = 255

    #########################
    displayImage()

def blacknwhiteAImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    hap = 0
    for i in range(inH):
        for k in range(inW):
            hap = inImage[0][i][k] + inImage[1][i][k] + inImage[2][i][k]
            outImage[0][i][k] = outImage[1][i][k] = outImage[2][i][k] = hap//3

    avg = hap / (inH * inW)

    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if inImage[rgb][i][k] < avg:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = 255

    #########################
    displayImage()

def quick_sort(A):
    if len(A) <= 1:
        return A
    p = A[0]
    S, M, L = [], [], []
    for elem in A:
        if elem < p:
            S.append(elem)
        elif elem > p:
            L.append(elem)
        else:
            M.append(elem)

    return quick_sort(S) + M + quick_sort(L)


def blacknwhiteSImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    image_list = [elem for inner_list in inImage for elem in inner_list]
    sorted = quick_sort(image_list)
    m = sorted[len(sorted) // 2]

    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] < m:
                outImage[i][k] = 0
            else:
                outImage[i][k] = 255
    #########################
    displayImage()

def moveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    xval = askinteger("x값", "")
    yval = askinteger("y값", "")

    for i in range(inH):
        for k in range(inW):
            if (0 <= i+xval < outH) and (0 <= k+yval < outW):
                outImage[i+xval][k+yval] = inImage[i][k]
    #########################
    displayImage()

def zoomOutImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    scale = askinteger("축소배율", "")
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH//scale, inW//scale
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    for i in range(inH):
        for k in range(inW):
            outImage[i//scale][k//scale] = inImage[i][k]
    #########################
    displayImage()


def zoomInImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    scale = askinteger("확대배율", "")
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH * scale, inW * scale
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    for i in range(outH):
        for k in range(outW):
            outImage[i][k] = inImage[i//2][k//2] # backwarding
    #########################
    displayImage()


def rotateFImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    angle = askinteger("회전 각도", "0~360")
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    radian = angle * math.pi / 180.0
    cx, cy = inH//2, inW//2

    # for i in range(inH):
    #     for k in range(inW):
    #         newI = int(math.cos(radian)*(i-cx) - math.sin(radian)*(k-cy))+cx
    #         newK = int(math.sin(radian)*(i-cx) + math.cos(radian)*(k-cy))+cy
    #
    #         if (0 <= newI < outH) and (0 <= newK < outW):
    #             outImage[newI][newK] = inImage[i][k]

    for i in range(outH):
        for k in range(outW):
            oldI = int(math.cos(radian)*(i-cx) + math.sin(radian)*(k-cy))+cx
            oldK = int(-math.sin(radian)*(i-cx) + math.cos(radian)*(k-cy))+cy

            if (0 <= oldI < inH) and (0 <= oldK < inW):
                outImage[i][k] = inImage[oldI][oldK]
    #########################
    displayImage()

def gammaImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = 255*(inImage[i][k] / 255)**(1.2)
    #########################
    displayImage()

def parabolaCapImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = 255 - 255*((inImage[i][k]/127)**2)
    #########################
    displayImage()

def parabolaCupImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 -> 알고리즘에 따라
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    ## ** 영상처리 알고리즘 ** ##
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = 255*((inImage[i][k]/127)**2)
    #########################
    displayImage()

## 전역 변수
window, canvas, paper = None, None, None # canvas는 선만 그릴 수 있음, 점을 위해 paper
filename = ''
inImage, outImage = None, None
inH, inW, outH, outW = 0, 0, 0, 0

## 메인
window = Tk()
window.geometry('300x300')
window.title('GrayScale Image Processing (Beta 1)')

mainMenu = Menu(window) # 메뉴의 틀
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu) # 상위 메뉴(파일)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=loadImage)
fileMenu.add_command(label='저장', command= saveImage)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=None)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label='영상처리1', menu=image1Menu)
image1Menu.add_command(label='동일영상', command=equalImage)
image1Menu.add_command(label='그레이스케일', command=grayImage)
image1Menu.add_command(label='반전', command=reverseImage)
image1Menu.add_command(label='밝게/어둡게', command=addImage)
image1Menu.add_command(label='흑백(127)', command=blacknwhiteMImage)
image1Menu.add_command(label='흑백(평균)', command=blacknwhiteAImage)
image1Menu.add_command(label='흑백(중앙값)', command=blacknwhiteSImage)
image1Menu.add_command(label='감마 연산(1.2)', command=gammaImage)
image1Menu.add_command(label='파라볼라 연산(Cap)', command=parabolaCapImage)
image1Menu.add_command(label='파라볼라 연산(Cup)', command=parabolaCupImage)


image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label='기하학 처리', menu=image2Menu)
image2Menu.add_command(label='이동', command=moveImage)
image2Menu.add_command(label='축소', command=zoomOutImage)
image2Menu.add_command(label='확대', command=zoomInImage)
image2Menu.add_command(label='회전', command=rotateFImage)



window.mainloop()