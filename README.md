
A Python-based image-to-low-poly converter that uses SIFT, Canny edge detection, and Delaunay triangulation to turn images into low-poly artwork.

Features:
SIFT feature detection
Canny edge detection
Adjustable background point density
Adjustable SIFT feature limit
Web interface using Flask

Usage:
Upload an image.
Adjust the parameters if needed.
Click Process.
Get your low-poly image.

SIFT:
Scale-Invariant Feature Transform (SIFT) is a computer vision algorithm for detecting and describing distinctive image features
Triangulator uses SIFT to find the most important features in the Image, SIFT has a strong bias for choosing points in the foreground and with a lot of texture.
The parameter that control SIFT allows the user to change the number of SIFT points.
Suppose the User has chosen 1000, SIFT will choose the 1000 most important points in the image.

Canny edge detection:
Canny Edge Detection is a Computer Vision algorithm for identifying edges in images.
Triangulator uses this to seperate the Image
![Background Point Only](README_files\Canny.png)


Processing can take 10+ seconds depending on the image and settings.