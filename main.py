import cv2
import PIL
from PIL import Image

# Video upload
video = cv2.VideoCapture("video path")

images = []

# Beginning and ending frames of the video
start_frame = 1
end_frame = 40
for i in range(start_frame, end_frame):

    ret, frame = video.read()


    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


    image = Image.fromarray(frame)
    images.append(image)

images[0].save("video.gif", save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
