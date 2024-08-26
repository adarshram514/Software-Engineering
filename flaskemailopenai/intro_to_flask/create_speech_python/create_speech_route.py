import os
import openai
from openai import OpenAI
import re #regular expressions module
from markupsafe import escape #protects projects against injection attacks
from intro_to_flask import app
import sys 
sys.dont_write_bytecode = True
from flask import render_template, request, Flask, Blueprint, url_for
from .create_speech_form import Speechme

speech_blueprint = Blueprint('speechme', __name__)

@speech_blueprint.route('/speechme',methods=['GET', 'POST'])
@app.route('/speechme',methods=['GET', 'POST'])
def speechme():
  form = Speechme(request.form)
  
  if request.method == 'POST':
      if form.validate() == False:
        return render_template('create_speech.html', form=form)
      else:
        # The following response code adapted from example on: 
        # https://platform.openai.com/docs/api-reference/images
        client = OpenAI()

        speech_file_name = "createspeech.mp3"
        speech_file_path = os.path.join("intro_to_flask/static/", speech_file_name)

        response = client.audio.speech.create(
          model="tts-1",
          voice="shimmer",
          input=form.prompt.data,
        )

        with open(speech_file_name, 'wb') as audio_file:
           audio_file.write(response.content)
           
        response.stream_to_file(speech_file_path)
        speech_url = url_for('static', filename=speech_file_name)
        return render_template('create_speech.html', speech_me_prompt=form.prompt.data,speech_me_response=speech_url,success=True)
      
  elif request.method == 'GET':
      return render_template('create_speech.html', form=form)