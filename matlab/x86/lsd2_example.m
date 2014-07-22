% lsd2_example.m
% Test LSD algorithm with MATLAB
%% show the image.
im = imread('./images/test.jpg');
imshow(im);
%% show the binary image after the process of LSD.
% note: input parameter is the path of image, use '/' as file separator.
figure;
imshow(lsd2('./images/test.jpg'));
