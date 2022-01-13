"CONVERT A IMAGE TO PENCIL SKETCH USING PYTHON CODE"



In internet there are lot of colorful pictures. pencil sketch  won't be avilable for all pics.
pencil sketch would be easy for an artists to draw.This code helps to convert image to pencil sketch
In order to obtain a pencil sketch, we will make use of two image blending techniques, known as dodging and burning. 



procedure to achieve a pencil sketch from  image:
1.install opencv

2.Convert the color image to grayscale.

3.Invert the grayscale image to get a negative.

4.Apply a Gaussian blur to the negative from step

5.Blend the grayscale image from step 1 with the blurred negative from step 3 using a color dodge.




Here are samples which got from the code:

INPUT IMAGES

![girl](https://user-images.githubusercontent.com/96882910/149399250-dcd73e51-0e53-4ca5-b358-46b34b8599ec.jpg)
![poter](https://user-images.githubusercontent.com/96882910/149399374-bbaf3ca0-87b7-4079-b357-2ebf00d718ca.jpg)
![cartoon](https://user-images.githubusercontent.com/96882910/149399490-08175b6d-236f-4ae5-adb5-f7d74ce24e70.jpg)

OUTPUT IMAGES


1. <img width="957" alt="girl sketch" src="https://user-images.githubusercontent.com/96882910/149398274-5c182ee4-b64a-4b60-b519-39106199570d.png">
2. <img width="960" alt="cartoon" src="https://user-images.githubusercontent.com/96882910/149398304-49a5eb2b-7fc2-435e-a852-9046bce39a73.png">
3. <img width="960" alt="poter" src="https://user-images.githubusercontent.com/96882910/149398325-7a380bce-fad7-42aa-851b-fc33f0b26e22.png">



