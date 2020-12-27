# Calibrate-fisheye-lens-using-OpenCV
用opencv矫正鱼眼图片


日期：20200530
注意：python2.7下运行成功，3.5下失败

当你使用鱼眼镜头（大于160度的视野），OpenCV中经典的矫正镜头的方法可能失效。即便你小心的按照OpenCV文档中的步骤执行，你也可能得到没有矫正的图片，如下图：
![image](https://github.com/lengkujiaai/Calibrate-fisheye-lens-using-OpenCV/blob/main/img_readme/1.png)

将鱼眼图片改成正常看到的图片分两步：

在运行程序获取相机参数之前，需要先下载黑白的棋盘图片，打印出来，贴到平整的硬板上，拍一些照片用来获取相机参数，棋盘图片在img_readme文件夹下，具体形状见图片：
![image](https://github.com/lengkujiaai/Calibrate-fisheye-lens-using-OpenCV/blob/main/img_readme/chessboard.png)

# 1、通过文件calibrate.py（需要修改CHECKERBOARD = (5,7)，因为是6X8，所以改成（5，7））和多张黑白棋盘图片（20张也差不多）获取相机内参值
使用方法：把calibrate.py和xx.jpg图片放在一个文件夹下面，输入python calibrate.py后稍等一分钟即可得到结果，具体见截图：
![image](https://github.com/lengkujiaai/Calibrate-fisheye-lens-using-OpenCV/blob/main/img_readme/get_parameters.png)

DIM是图片长宽的分辨率

DIM=(1280, 720)
K=np.array([[-31190.47191209647, -0.0, 667.330647269763], [0.0, -14405.222579044883, 80.68167531658455], [0.0, 0.0, 1.0]])
D=np.array([[152.50098302679038], [-150.36440309694163], [83.13957034501341], [-39.63732437907149]])

# 2、通过undistorted.py和内参值DIM、K、D将图片矫正
我的结果：很不理想啊，中间部分正常，边上不行

结果看图片：纠正前是0.jpg纠正后的是1.jpg

英文参考连接：https://medium.com/@kennethjiang/calibrate-fisheye-lens-using-opencv-333b05afa0b0
