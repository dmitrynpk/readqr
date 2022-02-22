import cv2
from glob import glob
from pylibdmtx import pylibdmtx

if __name__ == "__main__":

    image_files = glob("*.png")
    for image_file in image_files:
        print(image_file)
        img = cv2.imread(image_file)
        datas = pylibdmtx.decode(img)
		
        for data in datas:
            print(data.data)
