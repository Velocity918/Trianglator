
A Python-based image-to-low-poly converter that uses SIFT, Canny edge detection, and Delaunay triangulation to turn images into low-poly artwork.

## Features:
* SIFT feature detection
* Canny edge detection
* Adjustable background point density
* Adjustable SIFT feature limit
* Web interface using Flask

## Usage:
Upload an image.
Adjust the parameters if needed.
Click Process.
Get your low-poly image.
# How the Program Works
## SIFT:
Scale-Invariant Feature Transform (SIFT) is a computer vision algorithm for detecting and describing distinctive image features

Triangulator uses SIFT to find the most important features in the Image, SIFT has a strong bias for choosing points in the foreground and with a lot of texture.

The parameter that control SIFT allows the user to change the number of SIFT points.
Suppose the User has chosen 1000, SIFT will choose the 1000 most important points in the image.

## Canny edge detection:
Canny Edge Detection is a Computer Vision algorithm for identifying edges in images.

Triangulator uses this to seperate the Image's foreground and background.
This allows the program to generate background points by generating points randomly outside the edges.

It also allows you to play around with Images.
<p align="center">
  <img src="https://raw.githubusercontent.com/Velocity918/Trianglator/5c763bc1f57605fb147274c9e249ca8c84bf0333/README_files/Canny.png" alt="only Background Points" width="400">
  <img src="https://github.com/Velocity918/Trianglator/blob/e4c1be10841213f9c470b7d786cb971f56129f6a/README_files/SIFT.png?raw=true" alt="Image with only SIFT points" width="400">
</p>

<p align="center">
  <em>Image with only Background Points</em>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <em>Image with only SIFT points</em>
</p>


Processing can take 10+ seconds depending on the image and settings.
