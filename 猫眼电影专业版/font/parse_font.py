from PIL import ImageFont, Image, ImageDraw
import io, ddddocr
from fontTools.ttLib import TTFont


class ParseFont(object):
    def __init__(self):
        self.path = ''
        self.ocr = ddddocr.DdddOcr()

    # 实习僧字体反爬处理
    def parse_font_list(self, txt):
        img_size = 1024
        img = Image.new("1", (img_size, img_size), 255)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.path, int(img_size * 0.7))
        txt = chr(txt)
        x, y = draw.textsize(txt, font=font)
        draw.text(((img_size - x) // 2, (img_size - y) // 2), txt, font=font, fill=0)
        return img

    """识别字体"""

    def font_analysis(self):
        font_old_list = []
        font_new_list = []
        f = TTFont(self.path)
        for i, glyp in f.getBestCmap().items():
            pil = self.parse_font_list(i)
            bytes_to = io.BytesIO()
            pil.save(bytes_to, format="PNG")
            res = self.ocr.classification(bytes_to.getvalue())
            font_old_list.append(i)
            font_new_list.append(res)
        font_list = list(zip(font_old_list[1:], font_new_list[1:]))
        font_data_dict = {}
        for font in font_list:
            hex_data = hex(font[0])
            font_data_dict[hex_data] = font[1]
        # 最终识别的字体
        return font_data_dict


    def parse_font(self, font_list):
        # 处理猫眼电影字体反爬
        charlist = []
        font = ImageFont.truetype(self.path, 40)
        for uchar in font_list:
            uniknow_char = f"\\u{uchar[3:]}".encode().decode("unicode_escape")
            im = Image.new(mode="RGB", size=(42, 40), color="white")
            draw = ImageDraw.Draw(im=im)
            draw.text(xy=(0, 0), text=uniknow_char, fill=0, font=font)
            img_byte = io.BytesIO()
            im.save(img_byte, format="JPEG")
            charlist.append(self.ocr.classification(img_byte.getvalue()))
        # 此处返回识别到的最终字体
        return charlist
