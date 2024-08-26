from flask import Blueprint, request, redirect, url_for, render_template
from openai import OpenAI
from flask_login import login_required, current_user
from io import BytesIO
import requests
from generate_picture.generate_picture_form import PictureGenerationForm

generate_picture_blueprint = Blueprint('generate_picture', __name__)

@generate_picture_blueprint.route('/generate_picture', methods=['GET', 'POST'])
@login_required
def generate_picture():
    from app import db 
    form = PictureGenerationForm() 

    if form.validate_on_submit(): 
        profile_gender = form.gender_option.data 
        profile_role = form.role_option.data 

        client = OpenAI()
        response = client.images.generate(
            model="dall-e-3",
            prompt=f"Illustrate a young {profile_gender} student {profile_role}",
            quality="standard",
            size="1024x1024",
            n=1,
        )

        image_url = response.data[0].url
        image_response = requests.get(image_url)
        image_data = BytesIO(image_response.content)

        user = current_user
        user.profile_picture = image_data.read()
        db.session.commit()

        return redirect(url_for('profile', username=user.username))

    return render_template('custom_picture_form.html', form=form)