LSD-OpenCV-MATLAB
=================
###*Line Segment Detector for OpenCV and MATLAB*
------------------------------------------------

###1. Introduction
LSD-OpenCV-MATLAB is toolbox of Line Segment Detector(LSD) for OpenCV and MATLAB, as part of the GSoC 2013 program. The original code and paper, developed by Rafael Grompone von Gioi, can be found at http://www.ipol.im/pub/art/2012/gjmr-lsd/.

#####Please feel free to contact me [tanggefu@gmail.com] if you have any questions.

###2. Compilation

LSD is written by C++. And it also can be easily used in many contexts through the MATLAB bindings provided with this toolbox.

If you want to test or contribute, [CMAKE](http://www.cmake.org), a cross-platform, open-source build system, is usded to build some tools for the purpose. CMake can be downloaded from [CMake' website](http://www.cmake.org/cmake/resources/software.html).

The compilation rely on [OpenCV](http://opencv.org) - A cross-platform open source computer vision library.

During compilation, create a new directory named `build` in the main directory, then choose a appropriate compiler and switch to the `build` directory, finally, execute the following command according to your machine:

* Windows

```cpp
cmake -DCMAKE_BUILD_TYPE=Release .. -G"NMake Makefiles"
nmake
```

* Linux

```cpp
cmake ..
make
```

If successful, this should create two files named lsd.xxx and lsd_image.xxx in `./build/matlab/`, where xxx is a suffix that depends on what machine you are on.

###3. Usage

* C++/OpenCV

To test LSD algorithm with OpenCV, run `./build/lsd_opencv_example.exe` after compilation.

```cpp
/**
 * @file lsd_opencv_example.cpp
 *
 * Test the LSD algorithm with OpenCV
 */
#include <highgui.h>
#include <cv.h>
#include <lsd.h>

int main(int argc, char **argv)
{
    cv::Mat src = cv::imread("./../../images/test.jpg", CV_LOAD_IMAGE_COLOR);
    cv::Mat tmp, src_gray;
    cv::cvtColor(src, tmp, CV_RGB2GRAY);
    tmp.convertTo(src_gray, CV_64FC1);

    int cols  = src_gray.cols;
    int rows = src_gray.rows;

    image_double image = new_image_double(cols, rows);
    image->data = src_gray.ptr<double>(0);
    ntuple_list ntl = lsd(image);

    cv::Mat lsd = cv::Mat::zeros(rows, cols, CV_8UC1);
    cv::Point pt1, pt2;
    for (int j = 0; j != ntl->size ; ++j)
    {
        pt1.x = ntl->values[0 + j * ntl->dim];
        pt1.y = ntl->values[1 + j * ntl->dim];
        pt2.x = ntl->values[2 + j * ntl->dim];
        pt2.y = ntl->values[3 + j * ntl->dim];
        double width = ntl->values[4 + j * ntl->dim];
        cv::line(lsd, pt1, pt2, cv::Scalar(255), width, CV_AA);
    }
    free_ntuple_list(ntl);

    cv::namedWindow("src", CV_WINDOW_AUTOSIZE);
    cv::imshow("src", src);
    cv::namedWindow("lsd", CV_WINDOW_AUTOSIZE);
    cv::imshow("lsd", lsd);
    cv::waitKey(0);
    cv::destroyAllWindows();
}
```

* MATLAB

To test LSD algorithm with MATLAB, run `./matlab/x64(x86)/lsd_example.m` and `./matlab/x64(x86)/lsd2_example.m`, if your platform is x86, you should compile the corresponding `xxx.mexw32` files by Cmake.


```matlab
% lsd_example.m
% Test LSD algorithm with MATLAB
%% show the image.
im = imread('./images/test.jpg');
imshow(im);
%% get the start_points and end_points of each straight line use LSD.
% note: input parameter is the path of image, use '/' as file separator.
points = lsd('./images/test.jpg');
%% plot the lines.
hold on;
for i = 1:size(points, 2)
    plot(points(1:2, i), points(3:4, i), 'LineWidth', points(5, i) / 2, 'Color', [1, 0, 0]);
end
```

```matlab
% lsd2_example.m
% Test LSD algorithm with MATLAB
%% show the image.
im = imread('./images/test.jpg');
imshow(im);
%% show the binary image after the process of LSD.
% note: input parameter is the path of image, use '/' as file separator.
figure;
imshow(lsd2('./images/test.jpg'));
```

####This is an example:

source
![](https://github.com/primetang/LSD-OpenCV-MATLAB/blob/master/images/test.jpg "source")

result
![](https://github.com/primetang/LSD-OpenCV-MATLAB/blob/master/images/result.jpg "result")
