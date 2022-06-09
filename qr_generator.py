# qr code generation script
# takes a xlsx file and generate qr code for each row
import qrcode
import pandas as pd


# replace this by the actual excel path
read_file = pd.read_excel ("C:/Users/haokun/OneDrive - UW/Desktop/qr generation/aircraftnum.xlsx")

# change row name accordingly or add additonal col like aircraft serial number
for row in read_file['aircraft number']:
    print(row)
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )

    labeldata = row

    qr.add_data(labeldata)
    qr.make(fit=True)

    img = qr.make_image()
    img.save("{}.jpg".format(labeldata))

print("QR code creation done")
