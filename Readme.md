# Foreground isolation using Gabor kernels

Texture filtering using gabor filter: Gabor is used for feature extraction mainly texture or in other words repeating patterns in local areas(size of the kernel), it has multiple parameters however theta is an important one as it defines the angular rotation(orientation) of the filter. Since its applied as a 2D convolutional filter, it has an averaging/blurring effect on the image. Output results do indicate a blurring of continuous background ie image area having the same localized repeating patterns. <br>
Since these parameters are tuned for 1280*720 sized images, it may not yield the desired results for other sized images.
<br><br>

code used from: https://cvtuts.wordpress.com/2014/04/27/gabor-filters-a-practical-overview/