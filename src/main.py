import os
import cv2
import numpy as np
import argparse
import face_detect as fd
import color_match as cm 
import lipcolor

def faceDetect(path, idx, output_dir):
    img = cv2.imread(path)
    #copy the input image for the later crop#
    img_clone = np.copy(img)
    cv2.imwrite("%s/source%d.jpg" % (output_dir, 2*idx), img_clone)
    #save the lip position to pos array#
    pos = np.zeros((3,2), dtype=int)
    result = fd.detect_mouth(img, pos)
    cv2.imwrite("%s/source%d.jpg" % (output_dir, 2*idx+1), result)
    #crop the lip areas#
    source = cv2.imread("%s/source%d.jpg" % (output_dir, 2*idx))
    fd.crop(source,pos)
    # show the result
    #cv2.startWindowThread()
    cv2.imshow('FaceDetect',result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="set configs for lipstick matcher")
    parser.add_argument('input_dir', help="the directory of pictures")
    parser.add_argument('-m', '--mode', default='faceDetect', help="faceDetect or match")
    parser.add_argument('-o', '--output_dir', default="../result", help="the directory of results")
    args = parser.parse_args()

    paths = [os.path.join(args.input_dir, p) for p in os.listdir(args.input_dir)] 
    if args.mode == "faceDetect":
        for idx, path in enumerate(paths):
            faceDetect(path, idx, args.output_dir)
        color_dir = args.output_dir 

    elif args.mode == "match":
        color_dir = args.input_dir

    else:
        print("Error: illegal parameters for [--mode]")
        exit()

    l = []
    count = lipcolor.load_color(color_dir, l)
    meanColor = lipcolor.Mean_color(count, l)
    print("the extracted RGB value of the color is {0}".format(meanColor))
    cm.data_operate(meanColor)
