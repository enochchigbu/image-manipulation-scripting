% C Image
c_variable = fileread('c_output.txt');
c_array = uint8(str2num(c_variable));
c_matrix = reshape(c_array, 256, 256);

% Haskell Image
hs_variable = fileread('haskell_output.txt');
hs_array = uint8(str2num(hs_variable));
hs_matrix = reshape(hs_array, 256, 256);

% Prolog Image
plg_variable = fileread('prolog_output.txt');
plg_array = uint8(str2num(plg_variable));
plg_matrix = reshape(plg_array, 256, 256);

figure;

% Plot all images

subplot(2, 2, 1); 
imshow(imread('mickey.png'));
title('Original Image');

subplot(2, 2, 2);
imshow(c_matrix);
title('Black and White Image From C');

subplot(2, 2, 3);
imshow(hs_matrix);
title('Color Flipped Image From Haskell');

subplot(2, 2, 4); 
imshow(plg_matrix);
title('Reversed Image From Prolog');

% Pause and Exit
pause(10);
exit;