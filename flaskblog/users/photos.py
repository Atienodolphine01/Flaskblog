import os
import secrets
from PIL import Image
import random
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail
from config import Config
from flaskblog import profile_images

destination = Config.UPLOADED_PROFILEIMAGES_DEST

def save_picture(form_picture):
    # f_ext = os.path.splitext(form_picture.filename)
    # picture_fn = random.randint(2,4564234242342)+'{f_ext}'
    # picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    filename = profile_images.save(form_picture)
    output_size = (125, 125)
    picture_path = os.path.join(destination,filename)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return filename
    