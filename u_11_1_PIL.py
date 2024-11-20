from PIL import Image, ImageFilter
from pprint import  pprint

#  функция для линейного склеивания изображений, взято с https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
def merge(im1: Image.Image, im2: Image.Image) -> Image.Image:
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGB", (w, h))
    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))
    return im

orig = Image.open('im_orange.jpg')  #  Позволяет работать с картинками - синтаксис как в работе с файлами
pprint(dir(orig))
# с помощью различных атрибутов можно узнать некоторые сведения о файле
print(orig.__doc__, orig.format, orig.size, orig.mode, orig.filename, orig.fp, orig.__module__, orig.info, sep='\n')

img2 = orig.crop((10,10,300,300))

orig.thumbnail((100, 100))  # можно изменять размеры исходного изображения
orig.filter(ImageFilter.BLUR).show()  # можно применять различные фильтры, пример - размытие

img = orig.filter(ImageFilter.EMBOSS)  # если применение фильтра не сохранить, то исходное изображение не изменяется
img.save('im_orange_1.png')
img.show()  # посмотреть результат/картинку, используется средство просмотра изображений по умолчанию

img2.save('im_orange_2.png')
img2.show()

img3 = merge(img, img2)
img3.show()
img3.save('im_orange_3.jpg')

r, g, b = img3.split()
img4 = Image.merge("RGB", (g, b, r))
img4 = img4.resize((500, 500))  # можно менять размеры с изменением отношения сторон
img4.show()
img4.save('im_orange_4.jpg')

img3.close()  # если файлы не закрывать, то они копятся в памяти, у меня после 45 шт. новые картинки не открывались
img.close()
orig.close()
img2.close()


