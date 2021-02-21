import cv2
import sys
import os

def drawProgressBar(percent, barLen = 20):
    # percent float from 0 to 1.
    sys.stdout.write("\r")
    sys.stdout.write("[{:<{}}] {:.0f}%".format("=" * int(barLen * percent), barLen, percent * 100))
    sys.stdout.flush()

def createPath(dirToBeCreated):
    if not os.path.exists(dirToBeCreated):
        try:
            os.makedirs(dirToBeCreated)
        except OSError as exc: # Guard against race condition
            print("Directory Cannot be created due to error\n" + exc)
            exit()

def generate_frames(file_path, dest_dir):
    createPath(dest_dir)
    print("\nProcessing File: " + file_path)
    # Opens the Video file
    cap= cv2.VideoCapture(file_path)
    number_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    i=0
    cur_frame = 1
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
        drawProgressBar((cur_frame/number_of_frames))
        cur_frame+=1
        cv2.imwrite(dest_dir+'/frame'+str(i)+'.jpg', frame)
        i+=1
    print("\nFinished")

    cap.release()
    cv2.destroyAllWindows()

def main():
    if len(sys.argv) != 3:
        print("Usage: \n python3 main.py <src_file> <dest_dir>")
        exit()

    file_path = sys.argv[1]
    dest_dir = sys.argv[2].rstrip('/')
    if os.path.isdir(file_path):
        #Iterating Recursively through the source path
        for root, dirs, files in os.walk(file_path):
            for file in files:
                #generate Source File Path from root
                sourceFilePath = os.path.abspath(os.path.join(root, file))
                generate_frames(sourceFilePath, dest_dir + "/" + os.path.splitext(file)[0])
    else:
        generate_frames(file_path, dest_dir)

if __name__ == "__main__":
    main()



