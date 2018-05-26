import numpy as np
import cv2
import platform

system = platform.system()

print "Python version:",platform.python_version()   # 2.7.13
print "OpenCV version:",cv2.__version__             # 2.4.9.1
print "OS running:",system                          # Linux
print "\n\n"

#video codec initialization
if system=="Linux":
    fourcc = cv2.cv.FOURCC(*'MJPG')
elif system=="Windows":
    fourcc = cv2.cv.FOURCC(*'XVID')

n = 10                                                 # number of smaller clips
videoindex = 0                                         # index of current video
index      = 0

videos=[[],[],[],[],[],[],[],[],[],[]]                 

path = "input/video.mp4"
cap = cv2.VideoCapture(path)                           # deschidem filmuletul video.mp4 din folderul input

frames_num = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)   # frame number 
fps        = cap.get(cv2.cv.CV_CAP_PROP_FPS)           # frames per second
width      = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)   # width of frame
height     = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)  # height of frame

width = int(width)                                     # convertim la int pt a avea nr intreg
height = int(height)

totalseconds = frames_num/fps            # duration of video clip, in seconds

frames_every_video = int(frames_num)/n   # duration of smaller clips
print "----Original video----"
print "Video path:",path
print "Duration(seconds):",totalseconds
print "Frames per second:",fps
print "Total frame number:",frames_num
print "Resolution:%sx%s"%(width,height)

print "\n"

print "----Output videos----"
print "Number of videos:",n
print "Duration(sedonds):",totalseconds/n
print "Frames per second:",fps
print "Total frame number:",frames_every_video
print "Resolution:%sx%s"%(width/2,height/2)


while(cap.isOpened()):
     ret, frame = cap.read()                # read frames one-by-one
     index += 1;
     if frames_every_video-index>0:
         small = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # resize the actual frame to a smaller resolution (1:2 ratio)
         videos[videoindex].append(small)                   # append the smaller frame in our list

     elif frames_every_video-index == 0:
         vid = cv2.VideoWriter("output/video%s.avi"%str(videoindex+1),fourcc,25,frameSize=(width/2,height/2)) 
         for i in range(0,len(videos[videoindex])):
             vid.write(videos[videoindex][i])           # write frames in video object
             videos[videoindex][i]=0                    # replace the frames from the list with 0's

         print "[+] Video %s completed!"%str(int(videoindex)+1)

         index = 0;
         videoindex += 1
         if videoindex == n:
             break

cap.release()
cv2.destroyAllWindows()
