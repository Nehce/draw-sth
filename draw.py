import cv2
import numpy as np
import pyautogui
import time


def finding():
    name = input()
    dict_pokemon = {
        '妙蛙种子': '001Bulbasaur.png',
        '妙蛙草': '002Ivysaur.png',
        '妙蛙花': '003Venusaur.png',
        '小火龙': '004Charmander.png',
        '火恐龙': '005Charmeleon.png',
        '杰尼龟': '007Squirtle.png',
        '卡咪龟': '008Wartortle.png',
        '水箭龟': '009Blastoise.png',
        '绿毛虫': '010Caterpie.png',
        '铁甲蛹': '011Metapod.png',
        '巴大蝶': '012Butterfree.png',
        '波波': '016Pidgey.png',
        '烈雀': '021Spearow.png',
        '阿柏蛇': '023Ekans.png',
        '皮卡丘': '025Pikachu.png',
        '雷丘': '026Raichu.png',
        '胖丁': '039Jigglypuff.png',
        '超音蝠': '041Zubat.png',
        '走路草': '043Oddish.png',
        '臭臭花': '044Gloom.png',
        '三地鼠': '051Dugtrio.png',
        '喵喵': '052Meowth.png',
        '猫老大': '053Persian.png',
        '可达鸭': '054Psyduck.png',
        '火暴猴': '057Primeape.png',
        '蚊香蝌蚪': '060Poliwag.png',
        '蚊香君': '061Poliwhirl.png',
        '玛瑙水母': '072Tentacool.png',
        '毒刺水母': '073Tentacruel.png',
        '小拳石': '074Geodude.png',
        '烈焰马': '078Rapidash.png',
        '小火马': '077Ponyta.png',
        '呆呆兽': '079Slowpoke.png',
        '大葱鸭': "083Farfetch'd.png",
        '臭臭泥': '089Muk.png',
        '大舌贝': '090Shellder.png',
        '鬼斯通': '093Haunter.png',
        '耿鬼': '094Gengar.png',
        '大岩蛇': '095Onix.png',
        '双弹瓦斯': '110Weezing.png',
        '瓦斯弹': '109Koffing.png',
        '墨海马': '116Horsea.png',
        '宝石海星': '121Starmie.png',
        '迷唇姐': '124Jynx.png',
        '鲤鱼王': '129Magikarp.png',
        '暴鲤龙': '130Gyarados.png',
        '伊布': '133Eevee.png',
        '卡比兽': '143Snorlax.png',
        '火烈鸟': '146Moltres.png',
        '闪电鸟': '145Zapdos.png',
        '急冻鸟': '144Articuno.png',
        '超梦': '150Mewtwo.png',
        '快龙': '149Dragonite.png'
    }
    return dict_pokemon[name]


def formatting(*scr):
    # 读取为灰度图
    if not scr:
        scr = finding()
        img = cv2.imread(r'C:\Users\Vin\Pictures\wallpaper\Pokemon\{}'.format(scr), cv2.IMREAD_GRAYSCALE)
    else:
        img = cv2.imread(r'C:\Users\Vin\Pictures\wallpaper\Pokemon\{}'.format(scr[0]), cv2.IMREAD_GRAYSCALE)

    # cv2.imshow('gray', img)

    # 转换为2值图
    ret, img2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

    # cv2.imshow('binary', img2)

    # 比较相邻点，边缘识别
    edge = np.zeros([img2.shape[0], img2.shape[1]])

    for m in range(img2.shape[0]):
        for n in range(img2.shape[1] - 1):
            if img2[m, n] == img2[m, n + 1]:
                pass
            else:
                edge[m, n] = 255  # 将检测出的边缘点添加到edge图中

    # cv2.imshow('edge', edge)

    return edge


def compress(edge, a, b):
    # 压缩图片（60，60）
    edge2 = cv2.resize(edge, (a, b), interpolation=cv2.INTER_AREA)

    # cv2.imshow('edge2', edge2)

    points = []
    for m in range(a):
        for n in range(b):
            if edge2[m, n]:
                points.append((n, m))
    return points


def check_points(edge, threshold=900, a=100, b=100):
    points = compress(edge, a, b)
    while len(points) > threshold:
        a -= 10
        b -= 10
        points = compress(edge, a, b)
    return points


def draw(points, mode=0):
    a = 800
    b = 240
    time.sleep(3)
    if not mode:
        zero = pyautogui.locateOnScreen('zero.png')
        center = pyautogui.center(zero)
        a = center[0] - 250
        b = center[1] - 200

    for (x, y) in points:
        pyautogui.click(x * 5 + a, y * 5 + b)


if __name__ == "__main__":
    edge1 = formatting()
    points1 = check_points(edge1, 900)

    draw(points1, 1)

    # img = cv2.imread(r'C:\Users\Vin\Pictures\wallpaper\Pokemon\149Dragonite.png', cv2.IMREAD_GRAYSCALE)
    # _, img2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
    #
    # kern = np.ones((1, 2), np.uint8)
    #
    # mg = cv2.morphologyEx(img2, cv2.MORPH_GRADIENT, kern, iterations=1)
    #
    # cv2.imshow('1', mg)
    #
    # points = [(j, i) for i in range(600) for j in range(600) if mg[i, j]]

    # time.sleep(3)
    #
    # for (x, y) in points:
    #     pyautogui.click(x + 300, y + 200)


    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

