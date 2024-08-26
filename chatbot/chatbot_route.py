from flask import Blueprint, jsonify, request
from openai import OpenAI
import os
import load_dotenv
load_dotenv.load_dotenv()

chatbot_bp = Blueprint('chatbot', __name__)

# Set up OpenAI API key
client = OpenAI()

def get_chatbot_response(user_input, user_level, user_xp, db, user):
    if user is not None:
        user.experience += 1
        db.session.commit()
    if user_level == 1 or user_level <= 0 or None:
        prompt = f"{user_input}\n Talk to me like I'm a beginner learning about the stock market and I'm 16 years old."
    elif user_level == 2:
        prompt = f"{user_input}\n Talk to me like I have some basic knowledge about the stock market."
    elif user_level == 3:
        prompt = f"{user_input}\n Talk to me like I have intermediate knowledge about the stock market."
    elif user_level >= 4:
        prompt = f"{user_input}\n Talk to me like I'm an expert in the stock market. I have been trading for a while and I believe to be a know it all."
        
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return response.choices[0].message.content

# Route to handle chatbot responses
@chatbot_bp.route('/chatbot_response', methods=['POST'])
def chatbot_response():
    user_input = request.json.get('user_input')
    user_level = request.json.get('user_level')
    user_xp = request.json.get('user_xp')
    db = request.json.get('db')
    user = request.json.get('user')
    if user_input:
        chatbot_response = get_chatbot_response(user_input, user_level, user_xp, db, user)
        return jsonify({'response': chatbot_response})
    else:
        return jsonify({'error': 'Invalid request'})
