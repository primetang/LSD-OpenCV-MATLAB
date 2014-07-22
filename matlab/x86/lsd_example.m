% lsd2_example.m
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
    plot(points(1:2, i), points(3:4, i),'LineWidth', 2, 'Color', [1, 0, 0]);
end
