import cv2
import numpy as np
from matplotlib import pyplot as plt


def plot_cdf(image):
	pixel_values = image.flatten()
	hist, bins = np.histogram(pixel_values, bins=256, range=(0, 256), density=True)

	cdf = hist.cumsum()

	fig, ax1 = plt.subplots()

	ax1.hist(pixel_values, bins=256, range=(0, 256), color='b', alpha=0.7)
	ax1.set_title('Histogram of Image')
	ax1.set_xlabel('Pixel Value')
	ax1.set_ylabel('Frequency')

	ax2 = ax1.twinx()
	ax2.plot(bins[:-1], cdf, color='r')

	plt.tight_layout()
	plt.show()


if __name__ == "__main__":
	img = cv2.imread("./lenna.png", cv2.IMREAD_COLOR)
	img = cv2.resize(img, (900, 600), interpolation=cv2.INTER_LINEAR)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


	h, s, v = cv2.split(hsv)

	# equalizing
	equalizedH = cv2.equalizeHist(h)
	equalizedV = cv2.equalizeHist(v)
	equalizedS = cv2.equalizeHist(s)

	metric = np.vectorize(lambda x: x * 0.95 if x > 127 else x * 1.2)

	on_v = cv2.merge([h, s, equalizedV])
	on_s_v = cv2.merge([h, equalizedS, equalizedV])

	hsv2 = cv2.merge([equalizedH, equalizedS, equalizedV])
	plot_cdf(img)
	plot_cdf(hsv2)