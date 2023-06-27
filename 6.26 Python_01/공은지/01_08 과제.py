import math
import os
from tkinter import *
from tkinter import messagebox
# 함수
def displayImage() :
    global window, canvas, paper, height, width, filename
    if canvas != None:
        canvas.destroy()
    canvas = Canvas(window, height=512, width=512)
    paper = PhotoImage(height=512, width=512)
    canvas.create_image((512 / 2, 512 / 2), image=paper, state='normal')

    for i in range(height) :
        for k in range(width) :
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' %(r,g,b), (k,i))

    canvas.pack()

def reverseImage() :
    for i in range(height):
        for k in range(width):
            image[i][k] = 255 - image[i][k]
    displayImage()

def brightImage() :
    for i in range(height):
        for k in range(width):
            if (image[i][k]+50 > 255) :
                image[i][k] = 255
            else :
                image[i][k] += 50
    displayImage()

def darkImage() :
    for i in range(height):
        for k  in range(width):
            if (image[i][k]-100 < 0):
                image[i][k] = 0
            else :
                image[i][k] -= 100
    displayImage()

def grayImage() :
    for i in range(height):
        for k  in range(width):
            if (image[i][k] < 127):
                image[i][k] = 0
            else :
                image[i][k] = 255
    displayImage()

def meanGrayImage() :
    hap = 0
    for i in range(height):
        for k in range(width):
            hap += image[i][k]
    avg = hap / (height * width)

    for i in range(height):
        for k in range(width):
            if (image[i][k] < avg):
                image[i][k] = 255
            else:
                image[i][k] = 0
    displayImage()

def medianCal(A):
    n = len(A)
    for i in range(n):
        # 가장 작은 데이터의 인덱스
        min_idx = i
        for j in range(i + 1, n):
            # 최솟값 찾기
            if (A[min_idx] > A[j]):
                min_idx = j
        # 데이터 간의 자리 변경
        A[i], A[min_idx] = A[min_idx], A[i]
        return A

def medianGrayImage():
    image_list = [elem for inner_list in image for elem in inner_list]
    sorted = medianCal(image_list)
    m = sorted[len(sorted)//2]

    for i in range(height):
        for k in range(width):
            if (image[i][k] < m):
                image[i][k] = 255
            else:
                image[i][k] = 0
    displayImage()

def rotate(arr):
  n = len(arr)
  m = len(arr[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = arr[i][j]
  return result

def rotate90Image():
    rotated = rotate(image)

    for i in range(height):
        for k in range(width):
            image[i][k] = rotated[i][k]

    displayImage()

def rotate180Image():
    rotated = rotate(image)
    rotated180 = rotate(rotated)
    for i in range(height):
        for k in range(width):
            image[i][k] = rotated180[i][k]

    displayImage()

def rotate270Image():
    rotated = rotate(image)
    rotated180 = rotate(rotated)
    rotated270 = rotate(rotated180)
    for i in range(height):
        for k in range(width):
            image[i][k] = rotated270[i][k]

    displayImage()

def parabolaImage():
    for i in range(height):
        for k in range(width):
            image[i][k] = int(255*(image[i][k]/128-1)**2)
    displayImage()

def reverselr(arr):
  n = len(arr)
  m = len(arr[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      rev = m - j - 1
      result[i][j] = arr[i][rev]
  return result

def RevlrImage():
    revlr = reverselr(image)
    for i in range(height):
        for k in range(width):
            image[i][k] = revlr[i][k]

    displayImage()

def reverseud(arr):
  n = len(arr)
  m = len(arr[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      rev = n - i - 1
      result[i][j] = arr[rev][j]
  return result

def RevudImage():
    revud = reverseud(image)
    for i in range(height):
        for k in range(width):
            image[i][k] = revud[i][k]

    displayImage()





# 변수
window, canvas, paper = None, None, None
filename = ""
height, width = 0,0
image = []

# 메인
window = Tk()
window.geometry('500x800') # 창크기
window.title('영상처리 Alpha')

btnReverse = Button(window, text = '반전', command=reverseImage)
btnReverse.pack()
btnBright = Button(window, text = '밝게', command=brightImage)
btnBright.pack()
btnDark = Button(window, text = '어둡게', command=darkImage)
btnDark.pack()
btnGray = Button(window, text = '완전흑백', command=grayImage)
btnGray.pack()
btnMeanGray = Button(window, text = '흑백(평균)', command=meanGrayImage)
btnMeanGray.pack()
btnMedianGray = Button(window, text = '흑백(중앙값)', command=medianGrayImage)
btnMedianGray.pack()
btnRotate90 = Button(window, text = '90도회전', command=rotate90Image)
btnRotate90.pack()
btnRotate180 = Button(window, text = '180도회전', command=rotate180Image)
btnRotate180.pack()
btnRotate270 = Button(window, text = '270도회전', command=rotate270Image)
btnRotate270.pack()
btnParabolaImage = Button(window, text = '파라볼라', command=parabolaImage)
btnParabolaImage.pack()
btnRevlrImage = Button(window, text = '좌우반전', command=RevlrImage)
btnRevlrImage.pack()
btnRevudImage = Button(window, text = '상하반전', command=RevudImage)
btnRevudImage.pack()

filename = 'Etc_Raw(squre)/me.raw'

# 파일 크기 알아내기
fSize = os.path.getsize(filename) # Byte 단위
height = width = int(math.sqrt(fSize))

# 메모리 확보 (영상 크기)
image = [ [0 for _ in range(width)] for _ in range(height)]
# image = [[0*256]*256]


# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height) :
    for k in range(width) :
        image[i][k] = ord(rfp.read(1))

rfp.close()

displayImage()

window.mainloop()


