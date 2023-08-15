import cv2
import numpy as np
import streamlit as st

# def v_equalized(image, v_val):
# 	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 	array = np.full(hsv.shape, (0, 0, v_val), dtype=np.uint8)
# 	after_v = cv2.add(hsv, array)
#
# 	after_v = cv2.cvtColor(after_v, cv2.COLOR_HSV2BGR)
# 	return after_v
#
# def s_equalized(image, s_scale):
# 	# saturationScale = 0.8
# 	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 	h,s,v = cv2.split(hsv)
# 	cvt_s = np.vectorize(lambda x: x*(1-s_scale) if x>127 else x*(s_scale))
# 	s = cvt_s(s).astype(np.uint8)
# 	print(s)
#
# 	output_img = cv2.merge([h,s,v])
# 	after_s = cv2.cvtColor(output_img, cv2.COLOR_HSV2BGR)
# 	return after_s
#
# def h_equalized(image, h_val):
# 	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 	array = np.full(hsv.shape, (h_val, 0, 0), dtype=np.uint8)
# 	after_v = cv2.add(hsv, array)
#
# 	after_v = cv2.cvtColor(after_v, cv2.COLOR_HSV2BGR)
# 	return after_v

def set_h(origin_h, h_val):
	return (origin_h+h_val)%180

def set_v(origin_v, v_val):
	return np.clip(origin_v*v_val, 0, 255).astype(np.uint8)

def set_s(origin_s, s_val):
	return np.clip(origin_s*s_val, 0, 255).astype(np.uint8)

if __name__ == "__main__":

	st.title("CV Day01 Assignment")
	uploaded_file = st.file_uploader("이미지를 업로드하세요.", type=['jpeg', 'jpg', 'png'])

	if uploaded_file is not None:
		file_byte = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
		uploadImg = cv2.imdecode(file_byte, 1)

		values_h = st.slider('Select a range of h values', 0, 180)
		values_s = st.slider('Select a range of s values', 0.0, 2.0, 1.0, step=0.01)
		values_v = st.slider('Select a range of v values', 0.0, 2.0, 1.0, step=0.01)

		hsv = cv2.cvtColor(uploadImg, cv2.COLOR_BGR2HSV)
		h, s, v = cv2.split(hsv)

		after_hsvImg = cv2.merge([set_h(h, values_h), set_s(s, values_s), set_v(v, values_v)])
		after_Img = cv2.cvtColor(after_hsvImg, cv2.COLOR_HSV2BGR)
		after_Img = cv2.resize(after_Img, dsize=(900, 600), interpolation=cv2.INTER_LINEAR)

		st.image(after_Img, channels="BGR", caption="HSV 조정된 이미지")