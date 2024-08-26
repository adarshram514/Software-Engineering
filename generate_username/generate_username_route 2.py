from flask import Blueprint, jsonify
from openai import OpenAI

generate_username_blueprint = Blueprint('generate_username', __name__)

@generate_username_blueprint.route('/generate_username', methods=['GET', 'POST'])
def generate_username():
    client = OpenAI()
    from app import User
    random_username = None

    while not random_username:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Create a creative username for a student learning about investments. Do not use a word 'investment'"}
            ],
            max_tokens=20
        )
        potential_username = response.choices[0].message.content

        if not User.query.filter_by(username=potential_username).first():
            random_username = potential_username

    return jsonify({'username': random_username})
