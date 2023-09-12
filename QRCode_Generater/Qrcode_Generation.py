import qrcode

features = qrcode.QRCode(version=1, box_size=40, border=2)
features.add_data('https://github.com/palakgoel30/Snake_Game')
features.make(fit=True)
generate_image1 = features.make_image(fill_color="red", back_color='white')
generate_image1.save('link.png')

generate_image2 = qrcode.make("sample sample")
generate_image2.save('sample.png')
