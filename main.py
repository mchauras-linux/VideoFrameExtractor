import cv2
import sys
import os

def createPath(dirToBeCreated):
    if not os.path.exists(dirToBeCreated):
        print(dirToBeCreated)
        try:
            os.makedirs(dirToBeCreated)
        except OSError as exc: # Guard against race condition
            print("Directory Cannot be created due to error\n" + exc)
            exit()


if len(sys.argv) != 3:
    print("Usage: \n python3 main.py <src_file> <dest_dir>")
    exit()

file_path = sys.argv[1]
dest_dir = sys.argv[2].rstrip('/')
print(dest_dir)
createPath(dest_dir)

# Opens the Video file
cap= cv2.VideoCapture(file_path)
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    dest_file = dest_dir+'/frame'+str(i)+'.jpg'
    
    while True:
        if not os.path.exists(dest_file):
            break
        else:
            i+=1
            dest_file = dest_dir+'/frame'+str(i)+'.jpg'

    cv2.imwrite(dest_dir+'/frame'+str(i)+'.jpg', frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()

