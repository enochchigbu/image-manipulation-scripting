% Read image, change to 0-255 value, show image

img = imread('cat.png');

img_1d = reshape(img, 1, []);

dlmwrite('input.txt', img_1d, 'delimiter', ' ');

imshow(img);