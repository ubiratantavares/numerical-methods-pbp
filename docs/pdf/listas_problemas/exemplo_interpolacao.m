%   Interpolate a signal by a factor of four.
t = 0:0.001:.029;                       % Time vector
x = sin(2 * pi * 30 * t) + sin( 2 * pi * 60 * t);    % Original Signal
y = interp(x,4);                        % Interpolated Signal
subplot(211);
stem(x);
title('Original Signal');

subplot(212);
stem(y); 

title('Interpolated Signal');