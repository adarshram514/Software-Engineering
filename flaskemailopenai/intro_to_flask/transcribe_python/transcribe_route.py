import os
import openai
import re #regular expressions module
from markupsafe import escape #protects projects against injection attacks
from intro_to_flask import app
import sys 
sys.dont_write_bytecode = True
from flask import render_template, request, Flask, Blueprint
from .transcribe_form import TranscribemeForm
from openai import OpenAI

transcribe_blueprint = Blueprint('transcribeme', __name__)

@app.route('/transcribeme',methods=['GET', 'POST'])
def transcribeme():
  form = TranscribemeForm(request.form)
  
  if request.method == 'POST':
      if form.validate() == False:
        return render_template('transcribeme.html', form=form)
      else:
        # The following response code is an (older) from example on: 
        # https://platform.openai.com/docs/api-reference/audio/createTranscription
        audio_file= open(form.prompt.data, "rb")
        client = OpenAI()
        transcript = client.audio.transcriptions.create(
          model="whisper-1",
          file=audio_file
        )
        return render_template('transcribeme.html', transcribe_me_prompt=form.prompt.data,transcribe_me_response=transcript.text,success=True)
      
  elif request.method == 'GET':
      return render_template('transcribeme.html', form=form)