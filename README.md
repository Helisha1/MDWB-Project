# Local binary patterns and Histogram of Gradients implementation using python3
The program is coded using Windows 10 (64 bit) operating system with Python version 3.5.2.

## Local Binary Pattern
* Local Binary Pattern (LBP) is a feature descriptor used in texture analysis LBP  labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.
* For given image divide the image into n*n window (e.g. n = 8)
* For each pixel in a cell, compare the pixel to each of its 8 neighbors (on its left-top, left-middle, left-bottom, right-top, etc.). Follow the pixels along a circle, i.e. clockwise or counter-clockwise.
* Where the center pixel's value is greater than the neighbor's value, write "0". Otherwise, write "1". This gives an 8-digit binary number (which is usually converted to decimal for convenience).
* Compute the histogram, over the cell, of the frequency of each "number" occurring (i.e., each combination of which pixels are smaller and which are greater than the center). This histogram can be seen as a 256-dimensional feature vector.
Optionally normalize the histogram.
* Concatenate (normalized) histograms of all cells. This gives a feature vector for the entire window.
## Histogram of Gradients
* The histogram of oriented gradients (HOG) is a feature descriptor used in computer vision and image processing for the purpose of object detection.
* In HOG detects Object in the image by the distribution of intensity gradients
* Steps for calculating the HOG:
  * Computation of gradient value. This can be done by applying 1-D centered, point discrete derivative mask in one or both of the horizontal and vertical directions. 
  * Filtering mask
  * [-1 , 0 , 1]  and  transpose of [ -1 , 0 , 1]
* Second step includes the creation of cell histograms  as per the given number of bins.




## Code

### feature_descriptor.py
Generate Descriptors based on Model HOG and LBP
#### generate_HOG_descriptor

    Generate Histogram of gradients of given image
    :param image: Input image of Hand (1200 * 1600)
    :return: feature_descriptor(9576), HOG_image(120*160)
    
#### generate_LBP_descriptor

    Split the given image into 100x100 windows, compute Local Binary Pattern features for each window, and concatenate these to obtain a unified feature descriptor
    :param image: Input image of Hand (1200 * 1600)
    :return: feature_descriptor(49152(12*16*256)), LBP_image(1200*1

### similarity.py
Similarity functions for finding similarity between two descriptors

#### distance_of_LBP

    Return euclidean distance
    :param LBP1: LBP of first image
    :param LBP2: LBP of second image
    :return: distance value
    
#### find_k_similar_LBP

    Find k similar images of given image.
    Retrieve all LBP_image_descriptors from database and compare this LBP descriptors with given image_HOG_descriptor using euclidean distance and find k similar images
    :param image: Input image of Hand (1200 * 1600)
    :param k: number of similar image you want to find
    :return: List of ksimilarimages (imagename, distance_major(euclidian_distance))
    
#### cos_sim

    Function for finding cosine-similarity
    :param a: list1
    :param b: list2
    :return: similarity value [0:1]
    
#### euclidian_distance

    Function for finding euclidean distance
    :param a: list1
    :param b: list2
    :return: distance
    


## Package Version Installation 
The following packages are necessary to run the program:

##### Scikit-image 0.15.0	
    pip install scikit-image
##### Pymongo  3.8.0 
    pip install pymongo
##### Numpy	1.16.4	
    pip install numpy
##### Matplotlib	3.1.1	
    pip install matplotlib
##### Tkinter
    pip install tkinter
##### Glob
    pip install glob

