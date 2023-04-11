import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=15, border=4,)
qr.add_data("https://github.com/junead449?tab=repositories")
qr.make(fit=True)
img=qr.make_image(fill_color="Green", back_color="White")
img.save("Chaudhary_junead_Git.jpg")
