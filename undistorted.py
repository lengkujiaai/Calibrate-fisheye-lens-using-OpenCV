# You should replace these 3 lines with the output in calibration step
import numpy as np
import cv2
import sys
DIM=(1280, 720)
K=np.array([[-31190.47191209647, -0.0, 667.330647269763], [0.0, -14405.222579044883, 80.68167531658455], [0.0, 0.0, 1.0]])
D=np.array([[152.50098302679038], [-150.36440309694163], [83.13957034501341], [-39.63732437907149]])
def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    #cv2.imshow("undistorted", undistorted_img)
    cv2.imwrite("normal.jpg",undistorted_img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
if __name__ == '__main__':
    for p in sys.argv[1:]:
        undistort(p)
