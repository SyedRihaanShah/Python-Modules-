import qrcode 

url = input('Enter URL: ').strip() # here strip removes all the unecessary tabs and spaces
file_path = "qr_code.png"#you can even add a file path of your choice here

img = qrcode.make(str(url))#generates a qr code. by taking a url arguement
img.save(file_path)#saves the qr code image by taking the file path as a argument

print("QR code was generated")