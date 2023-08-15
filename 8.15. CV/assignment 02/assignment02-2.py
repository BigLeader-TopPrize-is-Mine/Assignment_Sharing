import cv2
import numpy as np
import matplotlib.pyplot as plt

def HPF(src, offset=0.01):
	img = cv2.imread(src)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	height, width = gray.shape
	dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
	dft_shift = np.fft.fftshift(dft)
	row, col = int(height / 2), int(width / 2)

	HPF = np.ones((height, width, 2), np.uint8)
	HPF[int(row - row*offset):int(row+row*offset), int(col - col*offset):int(col + col*offset)] = 0
	HPF_shift = dft_shift * HPF
	HPF_ishift = np.fft.ifftshift(HPF_shift)
	HPF_img = cv2.idft(HPF_ishift)
	HPF_img = cv2.magnitude(HPF_img[:, :, 0], HPF_img[:, :, 1])
	# afterHPF = cv2.cvtColor(HPF_img, cv2.COLOR_GRAY2RGB)

	plt.imshow(HPF_img, cmap='gray')
	plt.show()

def high_pass_filter(src, kernel):
	color_image = cv2.imread(src)
	b, g, r = cv2.split(color_image)

	b_filtered = cv2.filter2D(b, -1, kernel)
	g_filtered = cv2.filter2D(g, -1, kernel)
	r_filtered = cv2.filter2D(r, -1, kernel)

	filtered_image = cv2.merge((b_filtered, g_filtered, r_filtered))

	cv2.imshow('Filtered Color Image', filtered_image)
	cv2.waitKey(0)

	return filtered_image

if __name__ == "__main__":
	# HPF('lenna.png', 0.1)
	# HPF('moon.png', 0.1)
	kernel_zero = np.array([[1,1,1],
	                        [1,1,1],
	                        [1,1,1]])

	kernel_first = np.array([[0, -1, 0],
			                   [-1, 5, -1],
			                   [0, -1, 0]])

	kernel_second = np.array([[1, -2, 1],
			                   [-2, 5, -2],
			                   [1, -2, 1]])

	kernel_third = np.array([[-1, -2, -1],
	                          [-2, 19, -2],
	                          [-1, -2, -1]])

	kernel_5 = np.array([[ 0, 0,-1, 0, 0],
	                     [ 0, 0, 0, 0, 0],
	                     [-1, 0, 5, 0,-1],
	                     [ 0, 0, 0, 0, 0],
	                     [ 0, 0,-1, 0, 0]])

	high_pass_filter('room.jpg', kernel_first)
	high_pass_filter('room.jpg', kernel_second)
	high_pass_filter('room.jpg', kernel_third)
	high_pass_filter('room.jpg', kernel_5)
