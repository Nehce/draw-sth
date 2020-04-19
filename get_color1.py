import cv2
import numpy

img = cv2.imread(r'C:\Users\Vin\Pictures\wallpaper\Pokemon\025Pikachu.png', 1)

points = [img[m, n] for m in range(600) for n in range(600) if numpy.any(img[m, n, :] != 0)]

avr = numpy.mean(points, axis=0)
print(avr)

color = numpy.zeros((500, 500, 3), numpy.uint8)
color[:, :, 0] = avr[0]
color[:, :, 1] = avr[1]
color[:, :, 2] = avr[2]
cv2.imshow('out', color)

cv2.waitKey(0)
cv2.destroyAllWindows()
