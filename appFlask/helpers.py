import secrets
import os 
from PIL import Image
from flask import current_app

## to save random name for pic
def save_picture(form_picture,path,output_size = None):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename) ##we want to take the extention , so we ignored the name and we took only the ext
    picture_name = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, path, picture_name)
    i = Image.open(form_picture)
    if output_size :
        i.thumbnail(output_size)
    i.save(picture_path)
    return picture_name
