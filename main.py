from PIL import Image
import cv2 as cv
from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt
img  = Image.open("dog.jpg")
print(img)
img = np.array(img)
#Image.fromarray(img).show()
gray_image = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
edges = cv.Canny(gray_image, 50, 200)
#plt.imshow(edges, cmap='gray')
#plt.title('Edge Image')
#plt.show()
Image.fromarray(gray_image).show()
sift = cv.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(gray_image, None)
image_with_sift = cv.drawKeypoints(img, keypoints, None)
plt.imshow(cv.cvtColor(image_with_sift, cv.COLOR_BGR2RGB))
plt.title('SIFT Features')
plt.show()
points= []
for kp in keypoints:
    x,y = kp.pt
    points.append((int(x),int(y)))
print(len(points))
plt.imshow(img)
for x,y in points:
    plt.scatter(x,y,s=2,c = "red")
plt.show()
h, w = gray_image.shape

points.extend([
    (0,0),
    (w-1,0),
    (0,h-1),
    (w-1,h-1)
])
points = np.unique(np.array(points), axis=0)
tri = Delaunay(points)

plt.figure(figsize=(10,10))
plt.imshow(img)

plt.triplot(
    points[:,0],
    points[:,1],
    tri.simplices,
    linewidth=0.4,
    color="white"
)

plt.show()


