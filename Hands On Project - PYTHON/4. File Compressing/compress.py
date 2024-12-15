import zlib, base64

with open('D:/Htb_dev/Python bootcamp/source_code/Everything-From-Basic-To-Advanced-with-Python/Hands On Project - PYTHON/4. File Compressing/demo.txt', 'r') as my_file:
    data = my_file.read()

data_bytes = bytes(data, 'utf-8')
compress_data = base64.b64encode(zlib.compress(data_bytes, 9))