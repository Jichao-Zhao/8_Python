# 数字人体挑战赛
# coding = utf-8

import kfbReader
import cv2 as cv
import numpy as np
import json
import os


'''
# 函数名称：Init()
# 函数功能：初始化函数
# 传入参数：scale：读取倍率
# 传出参数：filenamelist：返回一个包含文件和文件夹名字的列表
'''
def Init():
	# 设置文件路径
	global filepath
	filepath = "E:\\2_Competitions\\2_14_数字人体\\3_技术资料\\0_Data\\pos_0\\"
	# 设置读取倍率
	global scale
	scale =  20


'''
# 函数名称：ReadReturnFileNames()
# 函数功能：读取指定文件夹内，所有的文件名字，
# 		   如果是文件会读取整个文件名，包括后缀名，
# 		   如果是文件夹，也会读取文件夹的名字
# 传入参数：filename：传入要读取的文件夹路径，字符类型
# 传出参数：filenamelist：返回一个包含文件和文件夹名字的列表
'''
def ReadReturnFileNames(filepath):
	# filepath = filepath
	filenamelist = []															# 新建一个空的列表，用来存储读取到的文件名字
	for files in os.listdir(filepath):  										# 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
			filenamelist.append(files)
	return filenamelist


Init()																			# 执行初始化函数

filepath = "E:\\2_Competitions\\2_14_数字人体\\3_技术资料\\0_Data\\pos_0\\"
filenamelist = ReadReturnFileNames(filepath)									# 输入路径，返回文件名列表

for filename in filenamelist:
	filename = filename[:-4]													# 消除文件名字的后缀 .kfb
	file1 = "E:\\2_Competitions\\2_14_数字人体\\3_技术资料\\0_Data\\pos_0\\"+filename+".kfb"
	label1 = "E:\\2_Competitions\\2_14_数字人体\\3_技术资料\\0_Data\\labels\\"+filename+".json"
	
	# 实例化 reader 类，读取提供的图像
	read = kfbReader.reader()
	read.ReadInfo(file1, scale, True)
		
	# 定义存储数据的空列表
	roi_x = []																	# 用来存储 roi 数据
	roi_y = []
	roi_w = []
	roi_h = []
	pos_x = []							# 用来存储 pos 数据
	pos_y = []
	pos_w = []
	pos_h = []
	roi   = []							# 用来存储绘制的 roi 图形

	# 打开 label 文件
	with  open(label1,"r") as f:
		labelContent = json.load(f)		# 获取 label1 标签内容

	# 遍历 label 文件中的标记框的参数
	for dic in labelContent:
		# 如果属于 roi 类，则存储到 roi 开头的列表
		if dic["class"] ==  "roi":
			roi_x.append(dic['x'])
			roi_y.append(dic['y'])
			roi_w.append(dic['w'])
			roi_h.append(dic['h'])
		# 如果属于 pos 类，则存储到 pos 开头的列表
		if dic["class"] ==  "pos":
			pos_x.append(dic['x'])
			pos_y.append(dic['y'])
			pos_w.append(dic['w'])
			pos_h.append(dic['h'])
	# 打印提取到的 roi 和 pos 数据
	# print(roi_x,'roi_x',roi_y,'roi_y',roi_w,'roi_w',roi_h,'roi_h')
	# print(pos_x,'pos_x',pos_y,'pos_y',pos_w,'pos_w',pos_h,'pos_h')

	# 利用数据画出 roi 图和 pos 标记图
	for i in range(len(roi_x)):
		# 利用官方 sdk 读取 kfb 图片，存储到 roi 数组中
		roi.append( read.ReadRoi(roi_x[i], roi_y[i], roi_w[i], roi_h[i], scale) )
		for j in range(len(pos_x)):
			# 循环读取 pos 数据， 绘制矩形框标记在 roi 区域
			x = pos_x[j] - roi_x[i]
			y = pos_y[j] - roi_y[i]
			w = pos_w[j] + x
			h = pos_h[j] + y
			if x>0 and x<10000 :
				# 打印绘制矩形框的数据
				# print(x,y,w,h,'rectangle')
				#cv.rectangle(roi[i], (x,y), (w,h), (0,255,0), 2)
		# 显示已经标记绿色矩形框的图
		# cv.imshow('roi'+str(i), roi[i])
		# 保存处理过的图像
				cv.imwrite(str(filename)+'_'+str(i)+'.jpg', roi[i])
				# 写入文件后再次打开，并保存标记区域
				img = cv.imread(str(filename)+'_'+str(i)+'.jpg')
				imgsave = img[y:h,x:w]
				cv.imwrite(str(filename)+'_roi'+str(i)+'_pos'+str(j)+'.jpg',imgsave)
	# 将列表清空，方便再次存储新的图像数据
	roi_x = []							# 用来存储新的 roi 数据
	roi_y = []
	roi_w = []
	roi_h = []
	pos_x = []							# 用来存储新的 pos 数据
	pos_y = []
	pos_w = []
	pos_h = []
	roi   = []							# 用来存储新的绘制的 roi 图形







