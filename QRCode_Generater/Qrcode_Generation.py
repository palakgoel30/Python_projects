import qrcode


link = input("Enter url link for which you want to create a QRCode")
features = qrcode.QRCode(version=1, box_size=40, border=2)
features.add_data(link)
features.make(fit=True)
generate_image1 = features.make_image(fill_color="red", back_color='white')
generate_image1.save('link.png')

generate_image2 = qrcode.make("sample sample")
generate_image2.save('sample.png')
