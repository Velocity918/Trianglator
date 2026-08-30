
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

The lower threshold removes edges weaker than the specified value, while the higher threshold ensures that edges above it are retained. Edges that fall between the two thresholds are classified based on whether they are connected to a strong edge.

It also allows you to play around with Images.
<table>
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/Velocity918/Trianglator/5c763bc1f57605fb147274c9e249ca8c84bf0333/README_files/Canny.png" alt="Image with only Background Points" width="400">
      <br>
      <em>Image with only Background Points</em>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/Velocity918/Trianglator/e4c1be10841213f9c470b7d786cb971f56129f6a/README_files/SIFT.png?raw=true" alt="Image with only SIFT points" width="400">
      <br>
      <em>Image with only SIFT points</em>
    </td>
  </tr>
</table>

The Combination of the two is what triangulator uses


![Canny+SIFT](https://github.com/Velocity918/Trianglator/blob/main/README_files/Canny+Sift.png?raw=true "Combining the two images outputs")


Check out the [Gallery](https://trianglator-kohl.vercel.app/gallery)


Processing can take 10+ seconds depending on the image and settings.
