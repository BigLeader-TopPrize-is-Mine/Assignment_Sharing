import math
import os

from tkinter import *

## def

def displayImage() : 
    global window, canvas, paper, height, width, file_name
    if canvas != None :
        canvas.destroy()

    canvas = Canvas(window, height = height, width = width)
    paper = PhotoImage(height=height,width=width)
    canvas.create_image((width/2,height/2), image=paper, state='normal')

    for i in range(height):
        for k in range(width):
            r = g = b = image[i][k]
            paper.put("#%02x%02x%02x" %(r,g,b),(k,i))
    
    canvas.pack()

def reverseImage() :
    for i in range(height):
        for k in range(width) :
            image[i][k] = 255 - image[i][k]
    displayImage()

def brightImage() :
    for i in range(height):
        for k in range(width) :
            if (image[i][k]+10) > 255 :
                image[i][k] = 255
            else :
                image[i][k] += 10
    displayImage()

def darkImage() :
    for i in range(height):
        for k in range(width) :
            if (image[i][k]-10) < 0 :
                image[i][k] = 0
            else :
                image[i][k] -= 10
    displayImage()

def greyImageAvg() :
    hap = 0

    for i in range(height) :
        for k in range(width) :
            hap += image[i][k]

    avg = hap//(height*width)

    for i in range(height):
        for k in range(width) :
            if image[i][k] > avg :
                image[i][k] = 255
            else :
                image[i][k] = 0
    displayImage()

#90도 회전
def rotateImage90():
    global image
    result = [[0]*width for i in range(height)]

    for i in range(height) :
        for k in range(width) :
            result[k][height-i-1] = image[i][k]

    image = result

    displayImage()

#좌우반전
def LR(lst) :
    center = len(lst)//2

    for i in range(center) :
        #홀수일때와 짝수일때가 다르다
        #홀수일때는 -i-1 붙히자.
        lst[center+center-i-1],lst[i] = lst[i], lst[center+center-i-1]
    return lst

def lrChange() :
    for i in range(height) :
        image[i] = LR(image[i])

    displayImage()

#상하반전
def udChange() :
    global image, height

    i = 0
    k = height-1

    while (i <= k) :
        image[i],image[k] = image[k],image[i]
        i+=1
        k-=1

    displayImage()

def gammaChange(num,gamma) :
    return int(num**(1/gamma))
    #감마 보정 공식 사용..

def gammaReturn() :
    for i in range(height) :
        for k in range(width) :
            image[i][k] = gammaChange(image[i][k],1.2)
    
    displayImage()

##parabolic(밝은 곳을 입체적으로/ 어두운 곳을 입체적으로, CAP&CUP algorithmn)



def cupCalculus():
    for i in range(height) :
        for k in range(width) :
            result = int(255-(255*((image[i][k]/127)-1)**2))

            if result < 0 : 
                image[i][k] = 0
            else :
                image[i][k] = int(255-(255*((image[i][k]/127)-1)**2))    
    displayImage()

def capCalculus():
    for i in range(height) :
        for k in range(width) :
            result = int(255*(((image[i][k]/127)-1)**2))

            if result > 255 : 
                image[i][k] = 255
            else :
                image[i][k] = int(255*(((image[i][k]/127)-1)**2))
    displayImage()

def zoomIn() :
    global window, canvas, paper, height, width, file_name, image
    result = []
    temp = []

    for i in range(width):
        for k in range(height) :
                temp += [image[i][k]]*2
        
        for i in range(2) :
            result.append(temp)
        temp = []

    #image, height, result, print
    image = result

    height = height*2
    width = width*2
    
    displayImage()

def zoomOut() :
    global window, canvas, paper, height, width, file_name, image

    result = []
    temp = []

    for i in range(0,width,2):
        for k in range(0,height,2) :
            temp.append(image[i][k])
        result.append(temp)
        temp = []

    image = result

    height = height//2
    width = width//2

    displayImage()

## arg
window, canvas, paper = None, None, None
# file_name = "Etc_Raw(squre)/LENA256.RAW"
file_name = "pepe.raw"
fSize = os.path.getsize(file_name)

height = width = int(math.sqrt(fSize))
image = []
image = [[0]*width for i in range(height)]

#파일 --> 메모리로 로딩
rfp = open(file_name,'rb')

for i in range(height) :
    for k in range(width) :
        image[i][k] = ord(rfp.read(1)) # ord : str to byte num

rfp.close()


## main
window = Tk()

label1 = Label(window, width= 50, height = 50)
label1.pack()
label2 = Label(window, width= 50, height = 50)
label2.pack()

window.title("alpha")
window.geometry('750x750')

#buttons
btnReverse = Button(label1, text="반전",command=reverseImage)
btnReverse.pack(side="left")

btnBright = Button(label1, text="밝게", command=brightImage)
btnBright.pack(side="left")

btnDark = Button(label1, text="어둡게", command=darkImage)
btnDark.pack(side="left")

btntoGrey = Button(label1, text="흑백반전(avg)", command = greyImageAvg)
btntoGrey.pack(side="left")

btn90rotate = Button(label1, text="90도 회전", command = rotateImage90)
btn90rotate.pack(side="left")

btnLRchange = Button(label1, text="좌우반전", command = lrChange)
btnLRchange.pack(side="left")

btnUpDwnChange = Button(label1, text="상하반전", command= udChange)
btnUpDwnChange.pack(side="left")

btnGammaChange = Button(label2, text="감마공식적용", command= gammaReturn)
btnGammaChange.pack(side="left")

btnCupCalculus = Button(label2, text="CUP Algo", command=capCalculus)
btnCupCalculus.pack(side="left")

btnCapCalculus = Button(label2, text="CAP Algo", command=capCalculus)
btnCapCalculus.pack(side="left")

btnZoomIn = Button(label2, text="Zoom", command=zoomIn)
btnZoomIn.pack(side="left")

btnZoomOut = Button(label2, text="ZoomOut", command=zoomOut)
btnZoomOut.pack(side="left")

# display, mainloop
displayImage()
window.mainloop()


############### 영상 처리의 기본

#퀴즈 : 밝게, 어둡게, 흑백(127), 흑백(평균)

#과제 : 자기 사진 쓰기
# 512x512 이미지 처리하기
# return input 해보기

# [1,2][3,4] -> 