import math
import os

import PIL
from PIL import Image

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *

### def

#### 영상 처리 함수부 ####
def reverseImage() :
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inY, outH, outW

    outH = inH; outW = inW
    outImage = [[[0]*outW for i in range(outH)] for _ in range(3)]

    for rgb in range(3) :
        for i in range(outH):
            for k in range(outW) :
                outImage[rgb][i][k] = 255 - inImage[rgb][i][k]

    displayImage()
    inImage = outImage

def addImage() :
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inY, outH, outW

    outH = inH; outW = inW
    outImage = [[0]*outW for i in range(outH)]

    value = askinteger("밝게할 값", "-255부터 255까지 입력", minvalue=-255, maxvalue=255)
    
    # ** 진짜 영상처리 알고리즘 구현 **
    for i in range(inH) :
        for k in range (inW) :
            if (inImage[i][k] + value > 255 ) :
                outImage[i][k] = 255
            elif (inImage[i][k] + value < 0) :
                outImage[i][k] = 0
            else :
                outImage[i] [k] = inImage[i][k] + value
    # 출력 호출        
    displayImage()

def grey127Image() :
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inY, outH, outW

    outH = inH; outW = inW

    for i in range(inH) :
        for k in range (inW) :
            if inImage[i][k] > inW//2 :
                outImage[i][k] = 255
            else :
                outImage[i][k] = 0
    displayImage()

#### 공통 함수부 ####
def loadImage() :
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inW, outH, outW

    file_name = askopenfilename(parent=window, filetypes=(("color file", "*.png;*.jpg;*.bmp;*.gif;*.jpeg"),("모든 파일", "*.*")))

    pillow = PIL.Image.open(file_name)
    inH = pillow.height
    inW = pillow.width

    inImage = [[[0]*inW for i in range(inH)] for _ in range(3)]

    #파일 --> 메모리로 로딩
    
    pillowRGB = pillow.convert("RGB") #RGB 모델로 변경.
    for i in range(inH) :
        for k in range(inW) :
            r,g,b = pillowRGB.getpixel((k,i))
            inImage[0][i][k] = r
            inImage[1][i][k] = g
            inImage[2][i][k] = b

    #마지막 동일함수로 만들기~
    equalImage()

##동일 이미지 생성
def equalImage() :
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inY, outH, outW

    #중요! 출력 이미지의 크기를 결정 (알고리즘에 따라서).
    outH = inH; outW = inW
    #메모리 할당
    outImage = [[[0]*outW for i in range(outH)] for _ in range(3)]
    
    # ** 동일영상처리 알고리즘 구현 **
    for rgb in range(3) :
        for i in range(inH) :
            for k in range (inW) :
                outImage[rgb][i][k] = inImage[rgb][i][k]

    # 출력 호출        
    displayImage()

##display
def displayImage() : 
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inY, outH, outW

    if canvas != None :
        canvas.destroy()

    window.geometry(str(outW) + 'x' + str(outH))
    canvas = Canvas(window, height = outH, width = outW)
    paper = PhotoImage(height = outH, width = outW)
    canvas.create_image((outW/2,outH/2), image=paper, state='normal') ##중앙점 찾기.

    #해당 코드 성능 Issue로 improve
    # for i in range(outH):
    #     for k in range(outW):
    #         r = g = b = outImage[i][k]
    #         paper.put("#%02x%02x%02x" %(r,g,b),(k,i))
    
    #개선한 algo
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
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inY, outH, outW

    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.raw', filetypes=((".raw", "*.raw"),("모든 파일", "*.*")))
    
    import struct

    for i in range(outH) :
        for k in range (outW):
            saveFp.write(struct.pack("B",outImage[i][k]))
    saveFp.close()
    messagebox.showinfo("성공, ", saveFp.name + '으로 저장.')

def moveImage() :
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inY, outH, outW

    outH = inH; outW = inW
    outImage = [[[0]*outW for i in range(outH)] for _ in range(3)]

    xVal = askinteger("X값", "")
    yVal = askinteger("Y값", "")

    for rgb in range(3) :
        for i in range(inH) :
            for k in range (inW) :
                if (0<i+yVal<outH-1) and (0<=k+xVal<outW):
                    outImage[rgb][i+yVal][k+xVal] = inImage[rgb][i][k]
    # 출력 호출        
    displayImage()

def zoomOutImage() :
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inY, outH, outW

    #먼저 몇 배를 축소할지 알아야 가능하다.
    scale = askinteger("축소배율","")

    #중요! 출력 이미지의 크기를 결정 (알고리즘에 따라서).
    outH = inH//scale; outW = inW//scale
    #메모리 할당
    outImage = [[[0]*outW for i in range(outH)] for _ in range(3) ]
    
    for rgb in range(3) :
        for i in range(inH) :
            for k in range (inW) :
                outImage[rgb][i//scale][k//scale] = inImage[rgb][i][k]
    # 출력 호출        
    displayImage()

    inImage = outImage

def zoomInImage() :
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inY, outH, outW

    scale = askinteger("확대배율","")

    ## 포워딩 기법은 문제 발생할 수 있다.
    outH = inH*scale; outW = inW*scale
    outImage = [[[0]*outW for i in range(outH)] for _ in range(3)]

    # for i in range(inH) :
    #     for k in range (inW) :
    #         outImage[i*scale][k*scale] = inImage[i][k]

    ## 백워딩으로 outImage[i][k]
    for rgb in range(3) :
        for i in range(outH) :
            for k in range(outW) :
                outImage[rgb][i][k] = inImage[rgb][i//scale][k//scale]
    
    displayImage()

    inImage = outImage

def rotateImage() :
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inY, outH, outW

    outH = inH; outW = inW

    #컴퓨터에서 각도 출력하려면 radian 값으로 바꿔야한다.
    angle = askinteger("각도","0~360")
    radian =  (angle*math.pi)/180.0 #sin, cos값 넣기 위해서 연산

    cX = inH//2
    cY = inW//2

    #메모리 할당
    outImage = [[[0]*outW for i in range(outH)] for _ in range(3)]

    
    
    # 백워딩으로 처리해줘야 HOLE 문제 생기지 않음 + 기준값이 (0,0)이 아닌 중앙에서 처리해야 함.
    # for i in range(inH) :
    #     for k in range(inW) :
    #         newI = int(math.cos(radian)*(i-cX) - math.sin(radian)*(k-cY))+cX
    #         newK = int(math.sin(radian)*(i-cX) + math.cos(radian)*(k-cY))+cY

    #         if (0<=newI<outH) and (0<=newK<outW) :
    #             outImage[newI][newK] = inImage[i][k]


    # 백워딩 처리 결과
    for rgb in range(3) :
        for i in range(inH) :
            for k in range(inW) :
                oldI = int(math.cos(radian)*(i-cX) + math.sin(radian)*(k-cY))+cX
                oldK = int(-math.sin(radian)*(i-cX) + math.cos(radian)*(k-cY))+cY

                if (0<=oldI<inH) and (0<=oldK<inW) :
                    outImage[rgb][i][k] = inImage[rgb][oldI][oldK]

    # 출력 호출        
    displayImage()
    inImage = outImage

def greyImage() :
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inY, outH, outW, greyCounter

    #중요! 출력 이미지의 크기를 결정 (알고리즘에 따라서).
    outH = inH; outW = inW
    #메모리 할당
    outImage = [[[0]*outW for i in range(outH)] for _ in range(3)]
    
    # ** 동일영상처리 알고리즘 구현 **
    for i in range(inH) :
        for k in range (inW) :
            hap = inImage[0][i][k] + inImage[1][i][k] + inImage[2][i][k]
            outImage[0][i][k] = outImage[1][i][k] = outImage[2][i][k] = hap//3

    if greyCounter%2 == 0 :
        displayImage()
    else :
        equalImage()
    greyCounter +=1
    # 출력 호출        

def gammaChange(num,gamma) :
    return int(num**(1/gamma))
    #감마 보정 공식 사용..

def gammaReturn() :
    global window, canvas, paper
    global file_name, inImage, outImage, inH, inY, outH, outW

    gammaNum = askfloat("Gamma Value","")

    outImage = [[[0]*outW for i in range(outH)] for _ in range(3) ]

    for rgb in range(3) :
        for i in range(inH) :
            for k in range(inW) :
                outImage[rgb][i][k] = gammaChange(inImage[rgb][i][k],gammaNum)
    
    displayImage()



### arg
window, canvas, paper = None, None, None
file_name = ""

inImage, outImage = None, None
inH, inY, outH, outW = 0, 0, 0, 0

greyCounter = 0 




### main
window = Tk()
window.title("GreyScale Image Processing (Beta)")
window.geometry(str(outW) + 'x' + str(outH))

mainMenu = Menu(window) #메뉴의 틀
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu) #상위 메뉴(파일)
mainMenu.add_cascade(label="파일", menu=fileMenu)

fileMenu.add_command(label="열기", command=loadImage)  #하위 메뉴 추가
fileMenu.add_command(label="저장", command=saveImage)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=None)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label="영상처리 1", menu=image1Menu)

image1Menu.add_command(label="동일 영상 가져오기", command=None)
image1Menu.add_command(label="그레이 스케일", command=greyImage)
image1Menu.add_command(label="밝기 조정(input)", command=None)
image1Menu.add_command(label="감마 조정", command=gammaReturn)
image1Menu.add_command(label="반전",command=reverseImage)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="기하학 처리", menu=image2Menu)

image2Menu.add_command(label="이동", command=moveImage)
image2Menu.add_command(label="축소", command=zoomOutImage)
image2Menu.add_command(label="확대",command=zoomInImage)
image2Menu.add_command(label="회전",command=rotateImage)

greyMenu = Menu(mainMenu)
mainMenu.add_cascade(label="흑백 3종", menu=greyMenu)

greyMenu.add_command(label="흑백(127)", command=grey127Image)
greyMenu.add_command(label="흑백(avg)", command=None)
greyMenu.add_command(label="흑백(median)", command=None)

window.mainloop()
