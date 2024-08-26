import os
import openai
from openai import OpenAI
import re
from markupsafe import escape
from intro_to_flask import app
import sys 
sys.dont_write_bytecode = True
from flask import render_template, request, Flask, Blueprint
from .draw_form import DrawmeForm

draw_blueprint = Blueprint('drawme', __name__)

@draw_blueprint.route('/drawme', methods=['GET', 'POST'])
@app.route('/drawme', methods=['GET', 'POST'])
def drawme():
    form = DrawmeForm(request.form)
    if request.method == 'POST':
        if not form.validate():
            return render_template('drawme.html', form=form)
        else:
            client = OpenAI()
            original_prompt = form.prompt.data
            
            response = client.images.generate(
                model="dall-e-3",
                prompt=original_prompt,
                quality=form.image_quality.data,
                size=form.image_size.data,
                n=1,
            )
            display_image_url = response.data[0].url
            revised_prompt = response.data[0].revised_prompt

            return render_template('drawme.html', form=form, draw_me_prompt=original_prompt, revised_prompt=revised_prompt, draw_me_response=display_image_url, success=True)
    elif request.method == 'GET':
        return render_template('drawme.html', form=form)
