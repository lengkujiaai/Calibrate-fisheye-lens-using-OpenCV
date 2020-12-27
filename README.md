# Calibrate-fisheye-lens-using-OpenCV
用opencv矫正鱼眼图片


日期：20201227

注意：python2.7下运行成功，3.5下失败

当你使用鱼眼镜头（大于160度的视野），OpenCV中经典的矫正镜头的方法可能失效。即便你小心的按照OpenCV文档中的步骤执行，你也可能得到没有矫正的图片，如下图：
![image](https://github.com/lengkujiaai/Calibrate-fisheye-lens-using-OpenCV/blob/main/img_readme/1.png)

如果你发现自己是这种情况，请继续阅读

从OpenCV 3.0开始，OpenCV包含了cv2.fisheye包用来处理鱼眼镜头的矫正。然而，如果你不是数学家，这个模块的手册可能很难进行。

这也是写作这篇指导的初衷。即便你没有任何OpenCV的先验知识，你也可以实现矫正图片的目的。

# 矫正图片主要分为两大步：

第一、帮助OpenCV发现镜头的2个内参。OpenCV中称作K和D。你只需要知道K和D是numpy数组，不需要关心他们的真正含义

第二、通过使用K和D矫正图片




第一步：

## 1、下载棋盘图片

在运行程序获取相机参数之前，需要先下载黑白的棋盘图片，打印出来，贴到平整的硬板上，棋盘图片在img_readme文件夹下，具体形状见图片：
![image](https://github.com/lengkujiaai/Calibrate-fisheye-lens-using-OpenCV/blob/main/img_readme/chessboard.png)

你需要确保直线是直的。

## 2、拍照

把棋盘放在相机前面，拍取一些图片。你需要从不同的位置和角度拍照。要点：棋盘要展现处扭曲变形的样子，这样OpenCV才能知道关于镜头的更多信息。

这里有一些例子：

![image]()

## 3、将这些图片以JPG格式保存到一个文件夹中

## 4、运行代码

通过文件calibrate.py和多张黑白棋盘图片（差不多20张）获取相机内参值

需要修改CHECKERBOARD = (5,7)，因为棋盘是6X8，所以改成（5，7）

把calibrate.py和xx.jpg图片文件夹放在一个文件夹下面，输入python calibrate.py后，稍等一分钟即可得到结果，具体见截图：
![image](https://github.com/lengkujiaai/Calibrate-fisheye-lens-using-OpenCV/blob/main/img_readme/get_parameters.png)

如果一切顺利，你可以看到打印：

DIM=(1280, 720)
K=np.array([[-31190.47191209647, -0.0, 667.330647269763], [0.0, -14405.222579044883, 80.68167531658455], [0.0, 0.0, 1.0]])
D=np.array([[152.50098302679038], [-150.36440309694163], [83.13957034501341], [-39.63732437907149]])

DIM是图片长宽的分辨率

# 正常图片

# 2、通过undistorted.py和内参值DIM、K、D将图片矫正
我的结果：很不理想啊，中间部分正常，边上不行

结果看图片：纠正前是0.jpg纠正后的是1.jpg

英文参考连接：https://medium.com/@kennethjiang/calibrate-fisheye-lens-using-opencv-333b05afa0b0
