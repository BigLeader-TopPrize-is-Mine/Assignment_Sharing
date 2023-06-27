import math
import os
from tkinter import *
from tkinter import messagebox

## 함수
def displayImage(image): # RGB가 다 같은 값이면 grey scale
    global window, canvas, paper, height, width, fileaname
    if canvas != None:
        canvas.destroy()

    n = len(image)

    canvas = Canvas(window, height=n, width=n)
    paper = PhotoImage(height=n, width=n)
    canvas.create_image((n / 2, n / 2), image=paper, state='normal')

    for i in range(n):
        for k in range(n):
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k, i)) # (i, k) 위치에 (r, g, b)를 16진수로 찍음

    canvas.pack()

def reverseImage():
    for i in range(height):
        for k in range(width):
            image[i][k] = 255 - image[i][k]

    displayImage(image)


def brightImage():
    for i in range(height):
        for k in range(width):
            if image[i][k] + 50 > 255:
                image[i][k] = 255
            else:
                image[i][k] += 50

    displayImage(image)


def darkImage():
    for i in range(height):
        for k in range(width):
            if image[i][k] - 100 < 0:
                image[i][k] = 0
            else:
                image[i][k] -= 100

    displayImage(image)

def blacknwhiteMImage():
    for i in range(height):
        for k in range(width):
            if image[i][k] < 127:
                image[i][k] = 0
            else:
                image[i][k] = 255
    displayImage(image)

def blacknwhiteAImage():
    hap = 0
    for i in range(height):
        for k in range(width):
            hap += image[i][k]

    avg = hap / (height * width)

    for i in range(height):
        for k in range(width):
            if image[i][k] < avg:
                image[i][k] = 0
            else:
                image[i][k] = 255

    displayImage(image)

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
    image_list = [elem for inner_list in image for elem in inner_list]
    sorted = quick_sort(image_list)
    m = sorted[len(sorted) // 2]

    for i in range(height):
        for k in range(width):
            if image[i][k] < m:
                image[i][k] = 0
            else:
                image[i][k] = 255

    displayImage(image)

def rotate(A, n):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            temp[i][k] = A[n-1-k][i]
    return temp

def rotate1Image():
    rotated = rotate(image, height)
    for i in range(height):
        for k in range(width):
            image[i][k] = rotated[i][k]

    displayImage(image)

def rotate2Image():
    rotated1 = rotate(image, height)
    rotated2 = rotate(rotated1, height)
    for i in range(height):
        for k in range(width):
            image[i][k] = rotated2[i][k]

    displayImage(image)

def rotate3Image():
    rotated1 = rotate(image, height)
    rotated2 = rotate(rotated1, height)
    rotated3 = rotate(rotated2, height)
    for i in range(height):
        for k in range(width):
            image[i][k] = rotated3[i][k]

    displayImage(image)

def rotate4Image():
    pass

def leftrightImage():
    n = height
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(height):
        for k in range(width):
            temp[i][k] = image[i][n-1-k]

    for i in range(height):
        for k in range(width):
            image[i][k] = temp[i][k]

    displayImage(image)


def updownImage():
    n = height
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(height):
        for k in range(width):
            temp[i][k] = image[n-1-i][k]

    for i in range(height):
        for k in range(width):
            image[i][k] = temp[i][k]

    displayImage(image)

# def gammaImage():
#     for i in range(height):
#         for k in range(width):
#             image[i][k] **= (1.0/1.2)

def gammaImage():
    for i in range(height):
        for k in range(width):
            image[i][k] = 255*(image[i][k] / 255)**(1.2)

    displayImage(image)

def parabolaCapImage():
    for i in range(height):
        for k in range(width):
            image[i][k] = 255 - 255*((image[i][k]/127)**2)

    displayImage(image)

def parabolaCupImage():
    for i in range(height):
        for k in range(width):
            image[i][k] = 255*((image[i][k]/127)**2)

    displayImage(image)

def minimizeImage():
    height_n = height // 2
    width_n = width // 2

    # 축소된 이미지 초기화
    minImage = [[0 for _ in range(height_n)] for _ in range(width_n)]

    # 이미지 축소
    for i in range(height_n):
        for k in range(width_n):
            # 영역의 평균값
            avg_val = (image[2 * i][2 * k] + image[2 * i][2 * k + 1] + image[2 * i + 1][2 * k] + image[2 * i + 1][2 * k + 1]) // 4
            # 축소된 이미지 할당
            minImage[i][k] = avg_val

    for i in range(height_n):
        for k in range(width_n):
            image[i][k] = minImage[i][k]
            image[i][k+width_n] = minImage[i][k]
            image[i+height_n][k] = minImage[i][k]
            image[i+height_n][k+width_n] = minImage[i][k]

    displayImage(image)

def maximizeImage():
    height_n = height * 2
    width_n = width * 2

    # 확대 이미지 초기화
    maxImage = [[0 for _ in range(height_n)] for _ in range(width_n)]

    # 이미지 확대
    for i in range(height):
        for k in range(width):
            maxImage[2*i][2*k] = image[i][k]
            maxImage[2*i][2*k+1] = image[i][k]
            maxImage[2*i+1][2*k] = image[i][k]
            maxImage[2*i+1][2*k+1] = image[i][k]

    displayImage(maxImage)


## 변수
window, canvas, paper = None, None, None # canvas는 선만 그릴 수 있음, 점을 위해 paper
filename = ''
height, width = 0, 0
image = []

## 메인
window = Tk()
window.geometry('1300x1300')
window.title('영상처리 Alpha')

label1 = Label(window, width=50, height=50)
label1.pack(fill="both")

btnReverse = Button(label1, text='반전', command=reverseImage)
btnReverse.pack(side='left')

btnBright = Button(label1, text='밝게', command=brightImage)
btnBright.pack(side='left')

btnDark = Button(label1, text='어둡게', command=darkImage)
btnDark.pack(side='left')

btnBlackWhiteM = Button(label1, text='흑백(127)', command=blacknwhiteMImage)
btnBlackWhiteM.pack(side='left')

btnBlackWhiteA = Button(label1, text='흑백(평균)', command=blacknwhiteAImage)
btnBlackWhiteA.pack(side='left')

btnBlackWhiteS = Button(label1, text='흑백(중앙값)', command=blacknwhiteSImage)
btnBlackWhiteS.pack(side='left')

btnrotate1 = Button(label1, text='회전(90도)', command=rotate1Image)
btnrotate1.pack(side='left')

btnrotate2 = Button(label1, text='회전(180도)', command=rotate2Image)
btnrotate2.pack(side='left')

btnrotate3 = Button(label1, text='회전(270도)', command=rotate3Image)
btnrotate3.pack(side='left')

btnrotate4 = Button(label1, text='회전(45도)', command=rotate4Image)
btnrotate4.pack(side='left')

label2 = Label(window)
label2.pack(fill="both")

btnleftright = Button(label2, text='좌우 미러링', command=leftrightImage)
btnleftright.pack(side='left')

btnupdown = Button(label2, text='상하 미러링', command=updownImage)
btnupdown.pack(side='left')

btngamma = Button(label2, text='감마 연산(1.2)', command=gammaImage)
btngamma.pack(side='left')

btnparabolaCap = Button(label2, text='파라볼라 연산(Cap)', command=parabolaCapImage)
btnparabolaCap.pack(side='left')

btnparabolaCup = Button(label2, text='파라볼라 연산(Cup)', command=parabolaCupImage)
btnparabolaCup.pack(side='left')

btnminimize = Button(label2, text='축소(1/2배)', command=minimizeImage)
btnminimize.pack(side='left')

btnmaximize = Button(label2, text='확대(2배)', command=maximizeImage)
btnmaximize.pack(side='left')

filename = 'Etc_Raw(squre)\LENNA512.raw'

# 파일 크기 알아내기
fSize = os.path.getsize(filename) #Byte 단위
height = width = int(math.sqrt(fSize))


# 메모리 확보 (영상 크기)
image = [[0 for _ in range(width)] for _ in range(height)]

# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height):
    for k in range(width):
        image[i][k] = ord(rfp.read(1)) # 1 byte 문자를 0~256 숫자로 변환

rfp.close()

displayImage(image)

window.mainloop()