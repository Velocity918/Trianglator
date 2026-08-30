import matplotlib
from PIL import Image,ImageOps
matplotlib.use("Agg")
import cv2 as cv
from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
def midpoint_finder(vertices):
    
    mid = []
    mid = np.mean(vertices,axis=1)
    #for n in vertices:
        #mid.append((np.sum(n[:,0])/3,np.sum(n[:,1])/3))
    #print(f"point 1: {mid[0]}")
    #mid = np.array(mid)
    return mid

def colourpicker(vertices,img):
    mid = midpoint_finder(vertices)
    colour = []
    for n in  mid:
        x = int(round(n[0]))
        y = int(round(n[1]))
        r,g,b = img[y,x]
        colour.append((r,g,b))
    return np.array(colour)

def bg_point_adder(edges,points,w,randomizer):

    edgepoints_first = []
    edgepoints_last = []
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
    edgepoints_last = np.array(edgepoints_last)
    edgepoints_first = np.array(edgepoints_first)
    """"
    plt.scatter(w-edge_points[:,0],h-edge_points[:,1],s = 2)
    plt.show()
    plt.scatter(w-edgepoints_last[:,0],h-edgepoints_last[:,1],s = 2)
    plt.scatter(w-edgepoints_first[:,0],h-edgepoints_first[:,1],s = 2)
    plt.show()
    """
    for x,n in enumerate(edgepoints_first):
        if np.random.randint(0,100)>randomizer:
            if n[0]>0:
                randcoord = np.random.randint(0,n[0])
                points.append([randcoord,n[1]])
    for x,n in enumerate(edgepoints_last):
        if np.random.randint(0,100)>randomizer:
            if n[0]<w:
                randcoord = np.random.randint(n[0],w)
                points.append([randcoord,n[1]])
def triangulator(img_string,bg_density = 50,lower_canny = 50,upper_canny=100,sift_points = 0):
    img = Image.open(img_string)

    if img.mode in ("RGBA", "LA") or "transparency" in img.info:
        img = img.convert("RGBA")
        alpha = img.getchannel("A")

        background = Image.new("RGB", img.size, "white")
        background.paste(img, mask=alpha)
        img = background
    else:
        img = img.convert("RGB")
        

    if max(img.size) > 1500:
        img.thumbnail((1500, 1500))
    img = ImageOps.exif_transpose(img)
    img = np.array(img)
    gray_image = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    h, w = gray_image.shape
    edges = cv.Canny(gray_image, lower_canny, upper_canny)

    points= []
    bg_point_adder(edges,points,w,randomizer=(100-bg_density))
    sift = cv.SIFT_create(nfeatures = sift_points)
    keypoints, descriptors = sift.detectAndCompute(gray_image, None)
    image_with_sift = cv.drawKeypoints(img, keypoints, None)
    #plt.imshow(cv.cvtColor(image_with_sift, cv.COLOR_BGR2RGB))
    #plt.title('SIFT Features')
    #plt.show()

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
    colour = colourpicker(vertices,img)
    plt.figure(figsize=(10,10))
    plt.imshow(img)
    for n,rgb in zip(vertices,colour):
        x = n[:,0]
        y = n[:,1]
        rgb =np.array(rgb)
        plt.fill(x, y, color = rgb/255)
    plt.axis("off")
    buffer = BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)

    plt.close()

    return buffer
