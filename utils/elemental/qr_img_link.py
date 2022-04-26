import qrcode
from PIL import Image


def qr_picture(logo, url, **dat):
    fc = dat.get("upcolor", "black")
    bg = dat.get("bgcolor", "white")
    fa = Image.open(logo)
    face = fa
    #.resize((60,60))
    qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr_big.add_data(url)
    qr_big.make()
    img_qr_big = qr_big.make_image(fill_color=fc, back_color=bg).convert('RGB')
    pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)
    img_qr_big.paste(face, pos)
    return img_qr_big