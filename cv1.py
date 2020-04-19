import cv2
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


def formatting():
    """读取图片，转换压缩图片"""
    # 读取为灰度图
    scr = finding()
    img = cv2.imread(r'C:\Users\Vin\Pictures\wallpaper\Pokemon\{}'.format(scr), cv2.IMREAD_GRAYSCALE)

    # 转换为2值图
    nothing, img2 = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)

    # 压缩图片（60，60）
    img60 = cv2.resize(img2, (40, 40), interpolation=cv2.INTER_AREA)
    return img60


def outline(img60):
    """勾勒"""
    points = []
    for m in range(40):
        for n in range(39):
            if img60[m, n] == img60[m, n + 1]:
                pass
            else:
                points.append((n, m))
    return points


img_draw = formatting()
points = outline(img_draw)


time.sleep(3)

for (x, y) in points:
    pyautogui.click(x*8 + 900, y*8 + 300)

# print(len(points))