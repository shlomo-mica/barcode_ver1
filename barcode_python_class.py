import barcode
from barcode.writer import ImageWriter
import IPython
from IPython.display import Image, display
from PIL import Image
#FROM NUMBER TO BARCODE PICTURE
#user_data = input("Enter the data to encode in the barcode:")
user_data_2 = '345678123097'
code2 = barcode.get_barcode_class('upc')
# code = barcode.get('code128', user_data, writer=ImageWriter())
my_barcode = code2(user_data_2, writer=ImageWriter())

my_barcode.save("clcoding_barcode")
pic1 = Image.open(r'../../AppData/Roaming/JetBrains/PyCharmCE2022.2/scratches/clcoding_barcode.png')
# display(Image(filename=filename))
pic1.show()
