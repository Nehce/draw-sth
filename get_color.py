import colorsys
from PIL import Image
import numpy
import cv2


def get_accent_color(path):
    im = Image.open(path)
    if im.mode != "RGB":
        im = im.convert('RGB')
        im.show()
    delta_h = 0.3
    avg_h = sum(t[0] for t in[colorsys.rgb_to_hsv(*im.getpixel((x, y))) for x in range(im.size[0]) for y in
                              range(im.size[1])])/(im.size[0]*im.size[1])
    beyond = list(filter(lambda x: abs(colorsys.rgb_to_hsv(*x)[0] - avg_h) > delta_h,
                         [im.getpixel((x, y)) for x in range(im.size[0]) for y in range(im.size[1])]))
    if len(beyond):
        r = int(sum(e[0] for e in beyond)/len(beyond))
        g = int(sum(e[1] for e in beyond)/len(beyond))
        b = int(sum(e[2] for e in beyond)/len(beyond))
        for i in range(int(im.size[0]/2)):
            for j in range(int(im.size[1]/10)):
                im.putpixel((i, j), (r, g, b))
        # im.save('res'+path)
        return r, g, b
    return None


scr = r'C:\Users\Vin\Pictures\wallpaper\Pokemon\025Pikachu.png'
result = get_accent_color(scr)
print(result)

r, g, b = result

blank = numpy.zeros((512, 512, 3), numpy.uint8)
blank[:] = [b, g, r]
# im = Image.fromarray(blank)
# im.show()


cv2.imshow('what', blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
