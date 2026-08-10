from PIL import Image
import cv2 as cv
from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt
def midpoint_finder(vertices):
    
    mid = []

    for n in vertices:
        mid.append((np.sum(n[:,0])/3,np.sum(n[:,1])/3))
    print(f"point 1: {mid[0]}")
    mid = np.array(mid)
    return mid

def edgesfunc():
    plt.figure(figsize=(10,10))
    plt.imshow(img)
    plt.triplot(
        points[:,0],
        points[:,1],
        tri.simplices,
        linewidth=0.4,
        color="white"
    )
    plt.scatter(mid[:,0],mid[:,1],s =1)

    plt.show()

def colourpicker(vertices):
    mid = midpoint_finder(vertices)
    colour = []
    for n in  mid:
        x = int(round(n[0]))
        y = int(round(n[1]))
        r,g,b = img[y,x]
        colour.append((r,g,b))
    return np.array(colour)

img  = Image.open("dog.jpg")
img = np.array(img)
gray_image = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
h, w = gray_image.shape
edges = cv.Canny(gray_image, 50, 100)
print(len(edges[0]))
edge_points = []
edgepoints_first = []
edgepoints_last = []
plt.title('edges Features')

for y, n in enumerate(edges):
    first = True
    for x, i in enumerate(n):
        if i == 255:
            if first:
                edgepoints_first.append((x,y))
                edgepoints_last.append((x,y))
                first = False
            edgepoints_last.pop()
            edgepoints_last.append([x,y])
            edge_points.append([x,y])
edgepoints_last = np.array(edgepoints_last)
edgepoints_first = np.array(edgepoints_first)
edge_points = np.array(edge_points)
points= []
plt.scatter(w-edge_points[:,0],h-edge_points[:,1],s = 2)
plt.show()
plt.scatter(w-edgepoints_last[:,0],h-edgepoints_last[:,1],s = 2)
plt.scatter(w-edgepoints_first[:,0],h-edgepoints_first[:,1],s = 2)
plt.show()
sift = cv.SIFT_create()
for x,n in enumerate(edgepoints_first):
    if np.random.randint(0,100)>20:
        randcoord = np.random.randint(0,n[0])
        points.append([randcoord,n[1]])
for x,n in enumerate(edgepoints_last):
    if np.random.randint(0,100)>20:
        randcoord = np.random.randint(n[0],w)
        points.append([randcoord,n[1]])
keypoints, descriptors = sift.detectAndCompute(gray_image, None)
image_with_sift = cv.drawKeypoints(img, keypoints, None)
#plt.imshow(cv.cvtColor(image_with_sift, cv.COLOR_BGR2RGB))
#plt.title('SIFT Features')
plt.show()

for kp in keypoints:
    x,y = kp.pt
    points.append((int(x),int(y)))

#print(len(points))
#plt.imshow(img)
#for x,y in points:
#    plt.scatter(x,y,s=2,c = "red")
#plt.show()

points.extend([
    (0,0),
    (w-1,0),
    (0,h-1),
    (w-1,h-1)
])

points = np.unique(np.array(points), axis=0)
tri = Delaunay(points)
vertices = points[tri.simplices]
print(vertices.shape)
colour = colourpicker(vertices)
plt.figure(figsize=(10,10))
plt.imshow(img)
for n,rgb in zip(vertices,colour):
    x = n[:,0]
    y = n[:,1]
    rgb =np.array(rgb)
    plt.fill(x, y, color = rgb/255)
plt.show()



