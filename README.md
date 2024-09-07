Python Group Project Fall 2022 
Project Description: 
Object and feature detection is one of the key issues in computer vision (CV) and has wide applications. 
For example, self-driving automobiles need traffic sign detection for scene understanding, better cruise 
control, and route design. Materials engineers use CV feature detection methods to perform phase 
recognition and identify grain boundaries to study the performance of different metal alloys. Those 
methods can also be used for Magnetic Resonance Imaging (MRI) images to find specific features which 
are hard to detect by eye. In recent years, with the development of the neural network, the efficiency 
and accuracy of object detection have been significantly improved and have surpassed human vision 
when doing certain tasks like classification of numbers. 
In this project, you will implement a classic object detection method called template matching. You will 
need to program three types of template matching methods based on different metrics, namely the sum 
of squared differences (SSD) method, the correlation coefficient method, and the normalized crosscorrelation method. You will first use these to find the location of Waldo with templates given to you. 
Then you will find/create your own template and implement those methods for a real-life application of 
your choice. 

Requirements: 
1. You will be only allowed to use numpy, time, and matplotlib, and the Python standard 
library. 
2. You are NOT allowed to use OpenCV, scipy, or any other advanced libraries. 
3. Utilize function(s) in this project to allow for modularity and reusability.

Part 1: Image importation 
In the first part of this project, you will develop a Python program to import the image and the template. 
You can find ways to import images using matplotlib in the resources provided and in previous 
Python homework assignments. 

Part 2: Finding Waldo 
Template matching is a commonly used computer vision technique that identifies the object in an image 
that matches a predefined template. Template matching is flexible and relatively straightforward to use, 
which makes it one of the most popular methods of object detection. 

During the matching process, your code will move the template, one pixel at a time, to all possible 
positions in the large source image and compute a numerical value for each location which indicates how 
well the template matches the image in that location. After the calculation, an output map can be 
generated, and the location of the object (e.g. Waldo) can be determined from that map. In this part of 
the project, you will work with grayscale images for template matching. 

Sum of Squared Differences (SSD) 
The Sum of Squared Differences (SSD) directly compares the pixel values of the template and the original 
image and calculates the difference where R is the output map matrix. 
The values in R represent how similar the template is to the source image at each location. For this 
algorithm, the smaller the value in R is the more similar the template is to the source image at that 
location.

Correlation Coefficient 
The correlation coefficient measures the degree to which the pixel values of two images are associated. For this algorithm, the larger the value in R is the more similar the template is to the source image at 
that location. 

Normalized Cross-Correlation 
Cross-correlation is a measure of the similarity of two series as a function of the displacement of one 
relative to the other. In CV, this concept was applied to template matching. To minimize the effect of 
illumination discrepancy (e.g. intensity change due to different exposure time), the pixel value range of 
the template and the source image will be normalized.

For this algorithm, the larger the value in R is the more similar the template is to the source image at 
that location. There are source images and templates of Waldo on Brightspace. You will implement these algorithms 
to find Waldo, and your algorithms should work for any of the image-template pairs. You will need to 
show the output map, the source image with a bounding box that highlights Waldo, and a cropped 
image showing the details, as shown in Figure 3. You will also need to print out the pixel indices of 
Waldo's location.

Your program should: 
- Prompt the user for the type of template matching method.
- Show and output the output map, the original image with a bounding box highlighting the 
template, and a cropped image of Waldo with a bounding box highlighting the template.
- Print out the location of Waldo in the source image. 

Part 3: Real-life application 
In this part of the project, you will pick your own template and image. You will apply the template 
matching for a real-life scenario. It can either be traffic sign detection, street number identification, 
human detection, or any other area where template matching can be used. Be creative! You will need to 
compare the performance of the three methods.

Your program should: 
- Prompt the user for the type of template matching method.
- Show and output the output map, the original image with a bounding box highlighting the 
template, and a cropped image with a bounding box highlighting the template. 




















