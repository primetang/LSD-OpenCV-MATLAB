function lsd_mat = lsd2(name)
pos = lsd_image(name);
im = imread(name);
lsd_mat = zeros(size(im, 2), size(im, 1));
lsd_mat(pos) = 255;
lsd_mat = lsd_mat';
end

