
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import io
import piexif
import time
import os
import re

global img1, x1, y1
img1=Image.open('copyright.png')
x1, y1=img1.size
#pic=Image.open('water.png')
#width,height=pic.size #364 51
#print(width,height)
#C:\Users\RichelieuGVG\Desktop\test
 

def change_path(path):
    path1=path[::-1]
    try:
        os.mkdir(path[:len(path)-(path1.index('\\'))]+'copy_image\\')
    except:
        pass
    #ded=len(path)-(path1.index('\\'))
    out=path[:len(path)-(path1.index('\\'))]+'copy_image\\'+path[len(path)-(path1.index('\\')):]
    print("\nAdded new path to image(s)")
    return out


def watermark_text(input_image_path,height, text, pos):
    try:
        photo = Image.open(input_image_path)
 
    # make the image editable
        drawing = ImageDraw.Draw(photo)
 
        color = (152, 152, 152)
        font = ImageFnt.truetype("arial.ttf", 72)#height//48
        drawing.text(pos, text, fill=color, font=font)
        photo.save(input_image_path)

        return 'Counted sucessfully'
    except:
        pass
def one_photo(path):
    print('\nCounting ',path)
    try:
        pic=Image.open(path)
        width,height=pic.size
        pic.paste(img1, (width-x1,height-y1), img1)
        pic.save(change_path(path))

        print('Copyright printed')
    except Exception as e:
        print(e)
        pass

def copy(main_path):
    try:
        
        fname=main_path
        img = Image.open(fname)
        print("Image prepared")
        exif_dict = piexif.load(img.info['exif'])
        
        exif_dict["0th"][315] = b"RichelieuGVG"
        exif_dict["0th"][33432] = b"RichelieuGVG"
        print("Exif data writen")
        exif_bytes = piexif.dump(exif_dict)
        #img.save('_%s' % fname, "jpeg", exif=exif_bytes)
        
        img.save(fname, exif=exif_bytes)
        print("Image saved")
        
    except Exception as e:
        print(e, 2)
        pass
        
try:
    print('Program for printing copyrights on images started.')
    main_path=str(input('Enter path to dir with photos>>'))
    start=time.time()
    lists=[]
    
    if '.' in main_path:
        one_photo(main_path)
        copy(main_path)
        
    else:
        print("Work with directory started")
        os.chdir(main_path)
        for root, dirs, files in os.walk(".", topdown = False):
            for name in files:
                if '.jpg' or '.png' in os.path.join(root, name):
                    lists.append(main_path+os.path.join(root, name)[1:])
                else:
                    continue
        for path in lists:
            one_photo(path)
            copy(path)
                
    print('\nThe program worked normally')
    print('Counted in:', time.time()-start, 'sec.\n')
except Exception as e:
    print(e,1)
finally:
    os.system('pause')



