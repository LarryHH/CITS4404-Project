import cv2
import os

image_folder = '/Users/yeah/Documents/UNI/Postgrad/CITS4404 - AI & AA/ProjExt'
video_name = 'video.avi'

fps = 30

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort()
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, fps, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))
    print(image)

cv2.destroyAllWindows()
video.release()
