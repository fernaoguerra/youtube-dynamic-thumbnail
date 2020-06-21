from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import subprocess
from datetime import datetime
import time
from youtube import get_views

def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text) 
    else:
        # split the line by spaces to get words
        words = text.split(' ')  
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''         
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word, 
            # add the line to the lines array
            lines.append(line)    
    return lines
 
def draw_text(dt_string):
    x = 610
    y = 130
    views = get_views()
    #print (views)
    img = Image.open('bg.jpg')
    image_size = img.size
    font = ImageFont.truetype('Roboto-Bold.ttf', size=117)
    text = "HOJE É "+ dt_string +". ESSE VIDEO TEM APROX " +str(views)+ " VIZUALIZAÇÕES. ESSA IMAGEM ALTERA A CADA 5 MINUTOS"
    lines = text_wrap(text, font, image_size[0] - x)
    line_height = font.getsize('hg')[1]
    draw = ImageDraw.Draw(img)

    for line in lines:
        # draw the line on the image 
        draw.text((x, y), line, fill=(255,255,255,128), font=font)
        
        # update the y position so that we can use it for next line
        y = y + line_height
    # save the image
    thumb = str(dt_string)+".png"
    img.save('thumbnails/'+ str(thumb), optimize=True)
    cmd = "python3 thumb.py --video-id Al5W-wZ2FOs --file "+ "thumbnails/"+thumb
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    print (out)

count = 0
while True:
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y")
    draw_text(dt_string)
    count = count + 1
    print (count)
    time.sleep(300)
