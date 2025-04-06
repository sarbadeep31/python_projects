from qrcode import make

if __name__ == '__main__':
    
    link = input("Enter the URL of which you want to create the qr code : ")

    qr_code = make(link)

    title_input = input("Enter the title of the image of qr code along with the extension (.jpg/.png/etc): ")

    qr_code.save(title_input)


