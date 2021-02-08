f= open('fileone.txt', 'w+')
f.write('file one!')

f= open('filetwo.txt', 'w+')
f.write('file two!')

import zipfile
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")