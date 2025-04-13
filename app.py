from flask import Flask, render_template, request
import random
import os
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# Path to your local cat memes
MEME_FOLDER = 'static/memes'

# Load available meme filenames
cat_memes = os.listdir(MEME_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    meme_path = None
    if request.method == 'POST':
        prompt = request.form['prompt']

        # Pick random meme
        selected_meme = random.choice(cat_memes)

        # Create meme with the prompt text
        meme_path = create_meme(selected_meme, prompt)

    return render_template('index.html', meme_path=meme_path)

def create_meme(meme_filename, text):
    meme_full_path = os.path.join(MEME_FOLDER, meme_filename)
    img = Image.open(meme_full_path)

    draw = ImageDraw.Draw(img)

    # Set font (make sure you have this .ttf file or adjust path)
    font_path = "arial.ttf"   # Or provide full path to font
    font = ImageFont.truetype(font_path, size=30)

    # Draw the user's prompt on the image
    draw.text((10, 10), text, font=font, fill="black")

    # Save the new meme
    new_filename = f"static/generated/{random.randint(0, 100000)}.png"
    os.makedirs(os.path.dirname(new_filename), exist_ok=True)
    img.save(new_filename)

    return new_filename

if __name__ == '__main__':
    app.run(debug=True)
