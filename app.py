import json
import os
from flask import Flask, jsonify, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, RadioField
from wtforms.validators import InputRequired, Length, ValidationError, Email, EqualTo
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from datetime import datetime
from flask_migrate import Migrate
from skillquiz import QuizForm, load_quiz_questions, create_quiz_form, load_easy_quiz_questions, load_medium_quiz_questions, load_hard_quiz_questions
import logging
from short_form_creator import short_form_creator
from dotenv import load_dotenv
from flask import make_response
from flask import flash
# import pyodbc
from experience import award_experience #branch 2
from rank import update_user_rank #branch 3
from rank import get_rank_name  #branch 3
from dotenv import load_dotenv
#import pyodbc
from urllib.parse import quote_plus
from flask_cors import CORS
from itsdangerous import URLSafeTimedSerializer as Serializer # token generator
from flask_mail import Mail, Message
import base64
import random
from flask import current_app

from chatbot.chatbot_route import chatbot_bp
from chatbot.chatbot_form import ChatbotForm

from generate_username.generate_username_route import generate_username_blueprint
from generate_picture.generate_picture_route import generate_picture_blueprint
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from datetime import datetime, timezone

app = Flask(__name__) 

app.secret_key = os.urandom(24)                                                                          
load_dotenv()

# Uncomment for cloud development
server = os.environ.get('SERVER')
database = os.environ.get('DATABASE')
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
driver= os.environ.get('DRIVER')
connection_string = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc:///?odbc_connect={quote_plus(connection_string)}'

# Uncomment for local development
# current_dir = os.path.abspath(os.path.dirname(__file__))                    
# db_file_path = os.path.join(current_dir, 'users.db')                     
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file_path     
# app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)            
migrate = Migrate(app, db)      

login_manager = LoginManager()      
login_manager.init_app(app)         
login_manager.login_view = "login"  

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    __table_args__ = None
    id = db.Column(db.Integer, primary_key=True)             
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)      
    password = db.Column(db.String(120), nullable=False)
    profile_picture = db.Column(db.BLOB) 
    experience = db.Column(db.Integer, default=0)
    rank = db.Column(db.Integer, default=1)
    daily_visited = db.Column(db.Boolean, default=False) #branch2
    profile_picture = db.Column(db.LargeBinary, nullable=True)
    level = db.Column(db.Integer, default=0)
    skill_lvl_set = db.Column(db.Boolean, default=False)
    member_since = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_verified = db.Column(db.Boolean, default=False)
    is_loaded = db.Column(db.Boolean, default=False)
    flashcards = db.relationship('Flashcard', backref='owner', lazy=True)

    def get_reset_token(self): 
        s = Serializer(app.secret_key)
        return s.dumps({'user_id': self.id})
        
    def get_email_token(self):
        s = Serializer(app.secret_key)
        return s.dumps(self.email)
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.secret_key)
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    @staticmethod
    def verify_email_token(token):
        s = Serializer(app.secret_key)
        try:
            email = s.loads(token)
            return email
        except Exception:
            return False
        
class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    front = db.Column(db.String(), nullable=False)
    back = db.Column(db.String(), nullable=False)
    known = db.Column(db.Boolean, default=False)
    difficulty_level = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def import_data(user):

    with open('data/flashcards.json', 'r') as file:
        flashcards_data = json.load(file)

    # Import cards and link them to the specified user by user_id
    for category in ['easy_cards', 'medium_cards', 'hard_cards']:
        difficulty = category.split('_')[0]  # Extract 'easy', 'medium', or 'hard'
        for card in flashcards_data[category]:
            new_card = Flashcard(
                front=card['front'],
                back=card['back'],
                known=bool(int(card['known'])),  # Convert 'known' string to boolean
                difficulty_level=difficulty,
                user_id=user.id  # Associate card with the user
            )
            db.session.add(new_card)
    
    db.session.commit()

#def get_flashcards_for_user(user):
    # Mapping user rank to difficulty levels
    #difficulty_map = {1: 'easy', 2: 'medium', 3: 'hard', 4: 'hard'}
    #user_difficulty = difficulty_map.get(user.rank, 'easy')  # Default to 'easy' if no match

    # Query flashcards based on the mapped difficulty
    #return Flashcard.query.filter_by(difficulty_level=user_difficulty).all()

def get_flashcards_for_user(user):
    # Map user rank to difficulty levels
    difficulty_map = {1: 'easy', 2: 'medium', 3: 'hard', 4: 'hard'}
    
    # Determine the difficulty level based on user rank
    user_difficulty = difficulty_map.get(user.rank, 'easy')
    
    # Fetch flashcards that match the user ID and the difficulty level
    return Flashcard.query.filter_by(user_id=user.id, difficulty_level=user_difficulty).all()

    
class RequestResetForm(FlaskForm):
    email = StringField('Enter your username', validators=[InputRequired(), Email(), Length(max=50)])
    submit = SubmitField("Continue") 

    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email is None:
            raise ValidationError("No account is associated with that email.")

class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[InputRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField('Confirm New Password', validators=[InputRequired(), EqualTo('password', message='New passwords must match.')])
    submit = SubmitField("Reset Password") 

@app.route("/reset_password_request", methods=['GET', 'POST'])
def reset_password_request():
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        token = user.get_reset_token()
        
        confirm_url = url_for('reset_token', token=token, _external=True)
        html = render_template('confirm_password_reset.html', confirm_url=confirm_url)
        subject = 'Hindsight | Verify Your Email Address'

        send_email(user.email, subject, html)
        return redirect(url_for('login'))
    return render_template('reset_password_request.html', title='Reset Password', form=form)


@app.route("/reset_password_request/<token>", methods=['GET', 'POST'])
def reset_token(token):
    user = User.verify_reset_token(token)
    if user is None:
        return redirect(url_for('reset_password_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.password = bcrypt.generate_password_hash(form.password.data)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
    
@app.route("/confirm/<token>", methods=['GET'])
def confirm_email(token):
    email = User.verify_email_token(token)
    if email:
        user = User.query.filter_by(email=email).first()
        if user and not user.is_verified:
            user.is_verified = True
            db.session.commit()
            return redirect(url_for('login')) 
    raise ValidationError("The provided token is invalid or has expired.")

@app.route("/inactive")
def inactive():
    return render_template("inactive.html")

@app.route("/resend", methods=['GET'])
def resend_confirmation():
    username = session.get('resend_username') 
    if username:
        user = User.query.filter_by(username=username).first()
        if user and not user.is_verified:
            token = user.get_email_token()
            confirm_url = url_for('confirm_email', token=token, _external=True)
            html = render_template('confirm_email.html', confirm_url=confirm_url)
            subject = 'Hindsight | Verify Your Email Address'
            send_email(user.email, subject, html)
            return redirect(url_for('inactive'))
    raise ValidationError('Invalid resend request.')

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender='hindsight@demo.com',
    )
    mail.send(msg)

class RegisterForm(FlaskForm):              
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)])    
    email = StringField(validators=[InputRequired(), Email(), Length(max=50)])  
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)])  
    submit = SubmitField("create")
    

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("That username already exists. Please choose a different one.")
        
    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError("This email address is already registered.")
        
class LoginForm(FlaskForm):              
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})      
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})  
    submit = SubmitField("Login")

@app.route('/')
def welcome():
    # render the welcome page
    return render_template('welcome.html')

@app.route('/forum')
def forum():
    # return the forum page
    posts = load_posts()
    return render_template('forum.html', posts=posts['posts'])

'''
@app.route('/daily', methods=['GET', 'POST']) #branch 2
@login_required
def daily():  
    # render the daily page
    return render_template('daily.html')     
'''

from news import NEWS
#seans news route talk to group and determine what we are going to route this too
@app.route('/news', methods=['GET'])
@login_required
def news():
    user = current_user
    news_obj = NEWS()
    #find a way to get the requested news from the user
    news_json = news_obj.get_news("CryptoCurrency")

    return render_template('news.html', news_json=news_json, user_level=user.level, user_xp=user.experience, db=db, user=user)

#route to handle the dynamic retrieval of the news articles from the API
@app.route('/get_news', methods=['GET'])
def get_news():
    category = request.args.get('category')
    news_obj = NEWS()
    news_json = news_obj.get_news(category)
    return news_json


@app.route('/learn', methods=['GET', 'POST'])
@login_required
def learn():
    user = current_user
    if user.skill_lvl_set:
        return render_template('learn.html', user_level = user.level, user_xp = user.experience, db = db, user = current_user)
    else:
        return redirect(url_for('set_skill_level'))
    
@app.route('/flashcard', methods=['GET', 'POST'])
def flashcard():
    user = current_user

    if not user.is_loaded:
        import_data(user)
        user.is_loaded = True
        db.session.commit()
        
    if 'flashcards' not in session or not session['flashcards'] or session.get('user_id') != user.id:
        flashcards = get_flashcards_for_user(user)
        flashcards_info = [{'id': card.id, 'front': card.front, 'back': card.back, 'user_id': user.id} for card in flashcards]
        session['flashcards'] = flashcards_info
        session['card_index'] = 0
        session['user_id'] = user.id

    card = session['flashcards'][session['card_index']]
    print(f"Current card: {card}")  # Confirm the current card details

    return render_template('flashcard.html', card=card, user_level = user.level)
    
@app.route('/next_card', methods=['POST'])
def next_card():
    if 'flashcards' in session and 'card_index' in session:
        session['card_index'] = (session['card_index'] + 1) % len(session['flashcards'])
        card = session['flashcards'][session['card_index']]
        print(f"Current card: {card}")
        return jsonify(card)
    return jsonify({'error': 'No cards loaded'}), 404

@app.route('/update_card_status', methods=['POST'])
@login_required
def update_card_status():

    user = current_user
    # Debug: Print request data
    print("Received JSON:", request.json)  # Check what JSON is received

    card_id = request.json.get('card_id')
    status = request.json.get('status')  # This will be either 'known' or 'not_known'

    print(f"Card ID: {card_id}, Status: {status}")  # Debug output

    card = Flashcard.query.get(card_id)
    if not card:
        print("No card found with ID:", card_id)  # Debug output

    if card and card.user_id == current_user.id:
        if status == 'known':
            card.known = True
            action = "marked as known"
            user = award_experience(db, user, 'know_card')
        elif status == 'not_known':
            card.known = False
            action = "marked as unknown"
        else:
            return jsonify({'error': 'Invalid status value'}), 400
        
        update_user_rank(db, user)
        db.session.commit()
        return jsonify({'success': f'Card status updated successfully, {action}'}), 200
    else:
        # More detailed error messages can help diagnose the issue
        if card:
            error_message = f"Access denied for card {card_id} owned by {card.user_id}, accessed by {current_user.id}"
        else:
            error_message = f"Card {card_id} not found or not accessible by user {current_user.id}"
        
        print(error_message)  # Debug output
        return jsonify({'error': error_message}), 404
    
@app.route('/learn/set_skill_level', methods=['GET', 'POST'])
def set_skill_level():
    return render_template('set_skill_level.html')

@app.route('/handle_skill_buttons', methods=['POST'])
def handle_skill_buttons():

    user = current_user

    action = request.form['action']
    
    if action == "b":
        user = award_experience(db, user, 'set_beginner')
    elif action == "i":
        user = award_experience(db, user, 'set_intermediate')
    elif action == "a":
        user = award_experience(db, user, 'set_advanced')

    user.skill_lvl_set = True
    update_user_rank(db, user)
    db.session.commit()
    
    # Redirect or render a template as needed
    return redirect(url_for('learn'))

@app.route('/learn/set_skill_level/skill_quiz', methods=['GET', 'POST'])
def skill_quiz():

    user = current_user

    questions = load_quiz_questions()
    create_quiz_form(questions)
    form = QuizForm()
    user_lvl = 0

    if form.validate_on_submit():
        correct_count = 0
        for i, question in enumerate(questions, start=1):
            user_answer = request.form.get(f'question_{i}')
            correct_answer = question['answer']
            if user_answer == correct_answer:
                correct_count += 1

        if 0 <= correct_count <= 3:
            user = award_experience(db, user, 'set_beginner')
        elif 4 <= correct_count <= 6:
            user = award_experience(db, user, 'set_intermediate')
            user_lvl = 1
        elif 7 <= correct_count <= 8:
            user = award_experience(db, user, 'set_advanced')
            user_lvl = 2

        user.skill_lvl_set = True
        update_user_rank(db, user)
        db.session.commit()

        #logger.debug(f"Total correct: {correct_count}")
        return redirect(url_for('passed'))
        #return render_template('passed.html', level=user_lvl)
        
    return render_template('skill_quiz.html', form=form)
   
   #questions = load_quiz_questions()
   #return render_template('learn.html', )

@app.route('/learn/skill_quiz/passed')
def passed(): 
    user = current_user
    rank_name = get_rank_name(user.rank) 
    #user_lvl = request.args.get('level', None)
    return render_template('passed.html', user_rank=rank_name)

@app.route('/practice_quiz', methods=['GET', 'POST'])
def practice_quiz():

    user = current_user

    if user.rank == 1:
        questions = load_easy_quiz_questions()
    elif user.rank == 2:
        questions = load_medium_quiz_questions()
    elif user.rank >= 3:
        questions = load_hard_quiz_questions()

    create_quiz_form(questions)
    form = QuizForm()

    if form.validate_on_submit():
        correct_count = 0
        for i, question in enumerate(questions, start=1):
            user_answer = request.form.get(f'question_{i}')
            correct_answer = question['answer']
            if user_answer == correct_answer:
                correct_count += 1

        user.skill_lvl_set = True
        update_user_rank(db, user)
        db.session.commit()

        #logger.debug(f"Total correct: {correct_count}")
        return render_template('practice_quiz_results.html', count=correct_count)
        #return render_template('passed.html', level=user_lvl)
        
    return render_template('skill_quiz.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            if not user.is_verified:
                session['resend_username'] = username 
                return redirect(url_for('inactive'))
            session.clear()
            login_user(user)
            session['user_id'] = user.id
            logging.debug(f"Session data after login: {session.items()}")
            return redirect(url_for('profile', username=username))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register(): 
    # render the sign up page
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        with open('static/default_profile_photo.png', 'rb') as f:
            default_picture_data = f.read()

        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password, profile_picture=default_picture_data)
        db.session.add(new_user)
        db.session.commit()

        token = new_user.get_email_token() 
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('confirm_email.html', confirm_url=confirm_url)
        subject = 'Hindsight | Verify Your Email Address'
        send_email(new_user.email, subject, html)

        session['resend_username'] = form.username.data
        return redirect(url_for('inactive'))
    return render_template('register.html', form=form)

@app.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()
    user_experience = user.experience
    print(user_experience)
    if user:
        if user.profile_picture is not None:
            image_data = user.profile_picture
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            image_data_url = "data:image/png;base64," + image_base64
        else:
            image_base64 = None
        rank_name = get_rank_name(user.rank)     
        update_user_rank(db, user)        
        icons = {
            'Beginner': 'fas fa-coins',
            'Proficient': 'fas fa-wallet',
            'Competent': 'fas fa-money-bill-wave',
            'Expert': 'fas fa-briefcase',
        }
        
        icon_class = icons.get(rank_name, 'fas fa-question')       
        if user.profile_picture is not None:               
            return render_template('profile.html', user=user, rank_name=rank_name, experience=user_experience, image_data_url=image_data_url, icon_class=icon_class)
        else:
            return render_template('profile.html', user=user, rank_name=rank_name, experience=user_experience, icon_class=icon_class)
       #branch 3                                         
    
@app.route('/upload_picture', methods=['POST'])
@login_required
def upload_picture():
    user = current_user
    
    if request.method == 'POST':
        profile_picture = request.files['profile_picture']
        if profile_picture:
            if profile_picture.filename.endswith('.png'):
                image_data = profile_picture.read()
                user.profile_picture = image_data  # Store the decoded data in the new column
                db.session.commit()
            else:
                raise ValidationError('Please upload a PNG image.')
        else:
            raise ValidationError('No file uploaded.')
    return redirect(url_for('profile', username=user.username))


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():

    if 'flashcards' in session:
        del session['flashcards']
    if 'card_index' in session:
        del session['card_index']
    if 'user_id' in session:
        del session['user_id']


    logout_user()
    session.clear() 
    return redirect(url_for('login'))
    
@app.route('/create')           # IMPORTANT for creating tables do not remove!!! 
def create():                   # DON'T USE python3 use flask shell in your terminal. 
    db.create_all()             # Flask shell provides Flask application context you need.
    return 'All tables created'

# @app.route('/delete', methods=['GET', 'POST'])
# def delete_tables():
#     # Drop all tables
#     db.drop_all()
    
#     # Return a message indicating that tables have been deleted
#     return 'All tables deleted'

#route to the short form video editor
@app.route('/shorts', methods=['GET','POST'])
def shorts():
    return render_template('shorts.html')

shorts = short_form_creator()

@app.route('/handle_form', methods=['POST'])
def form_handler():
    if request.form['action'] == 'clear':
        return render_template('shorts.html')
    elif request.form['action'] == 'submit':   
        user_input = request.form['freeform']
        user_input,flagged = shorts.moderation(user_input)
        
        return render_template('shorts_response.html',flagged_var=flagged, video_url=user_input)
    
@app.route('/shorts_response.html', methods=['POST'])
def shorts_response_handler():
    user = current_user
    if request['action'] == "Go Back":
        return render_template('shorts.html', user_level=user.level, user_xp=user.experience, db=db, user=user)
    
class UpdateUsername(FlaskForm):
    current_username = StringField('Current Username', validators=[InputRequired()])
    new_username = StringField('New Username', validators=[InputRequired()])
    confirm_new_username = StringField('Confirm New Username', validators=[InputRequired(), EqualTo('new_username', message='New usernames must match.')])
    submit_username = SubmitField('Confirm Username Change')

class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[InputRequired()])
    new_password = PasswordField('New Password', validators=[InputRequired(), Length(min=4, max=20)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[InputRequired(), EqualTo('new_password', message='New passwords must match.')])
    submit_password = SubmitField('Confirm Password Change')

@app.route('/security', methods=['GET', 'POST'])
@login_required
def security():
    username_form = UpdateUsername()
    password_form = PasswordChangeForm()
    user = current_user
    
    if username_form.validate_on_submit():
        current_username = username_form.current_username.data
        new_username = username_form.new_username.data

        if current_username != new_username:
            user_to_update = User.query.filter_by(username=current_username).first()
            if user_to_update:
                user_to_update.username = new_username
                db.session.commit()
                return redirect(url_for('profile', username=user.username))
            else:
                raise ValidationError('Current username not found!')
        else:
            raise ValidationError('New username must be different from the current one.')

    if password_form.validate_on_submit():
        current_password = password_form.current_password.data
        new_password = password_form.new_password.data

        if bcrypt.check_password_hash(user.password, current_password):
            user.password = bcrypt.generate_password_hash(new_password)
            db.session.commit()
            return redirect(url_for('profile', username=user.username))
        else:
            raise ValidationError('Current password is incorrect.')

    return render_template('security.html', username_form=username_form, password_form=password_form, user=user)

    
app.register_blueprint(generate_username_blueprint) 
app.register_blueprint(generate_picture_blueprint) 

if __name__ == '__main__':
    app.run(debug=True)

def load_posts():
    with open('forum.json', 'r') as f:
        return json.load(f)

def save_posts(posts):
    with open('forum.json', 'w') as f:
        json.dump(posts, f, indent=4)

@app.route('/submit_post', methods=['POST'])
@login_required
def submit_post():
    title = request.form['post-title']
    content = request.form['post-content']

    user = current_user
    
    if user.profile_picture is not None:
        image_data = user.profile_picture
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        image_data_url = "data:image/png;base64," + image_base64
    else:
        image_data_url = None

    username = user.username if user.is_authenticated else "Anonymous"

    # Generates the timestamps for the posts
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    posts = load_posts()
    
    posts['posts'].append({'username': username, 'title': title, 'content': content, 'likes': 0, 'dislikes': 0, 'comments': [], 'timestamp': timestamp, 
                           'profile_photo': image_data_url})
    
    save_posts(posts)

    # Awarding the experience points
    user = current_user 
    user = award_experience(db, user, 'forum_post')  
    update_user_rank(db, user)

    # Set the session message right after awarding experience
    if hasattr(user,'experience_awarded'):  # Make sure this attribute is managed in award_experience
        session['exp_awarded'] = f"You have earned {user.experience_awarded} experience points!"

      # Render the forum template with a response object
    response = make_response(redirect(url_for('forum')))

    # Check if the 'exp_awarded' session key exists
    if 'exp_awarded' in session:
        # Save the message in a variable to pass to the template
        flash_message = session['exp_awarded']
        # Now remove 'exp_awarded' session key to prevent re-displaying the message
        session.pop('exp_awarded')

        # Optionally, you can use Flask's flash system to send one-off messages
        flash(flash_message)

    return response


@app.route('/like_post/<int:post_index>', methods=['POST'])
def like_post(post_index):
    posts = load_posts()
    
    posts['posts'][post_index]['likes'] += 1
    
    save_posts(posts)
    
    return redirect(url_for('forum'))

@app.route('/dislike_post/<int:post_index>', methods=['POST'])
def dislike_post(post_index):
    posts = load_posts()

    posts['posts'][post_index]['dislikes'] += 1

    save_posts(posts)
    
    return redirect(url_for('forum'))

@app.route('/submit_comment/<int:post_index>', methods=['POST'])
@login_required
def submit_comment(post_index):
    comment_text = request.form['comment-text']
    username = current_user.username if current_user.is_authenticated else "Anonymous"
    
    posts = load_posts()

    posts['posts'][post_index]['comments'].append({'username': username, 'text': comment_text})
    
    save_posts(posts)
    
    return redirect(url_for('forum'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(chatbot_bp)
@app.route('/chatbot', methods=['GET', 'POST'])
def home():
    form = ChatbotForm()
    return render_template('index.html', form=form)

#sean summary route
@app.route('/summary', methods=['GET'])
def summary():
    
    return render_template('summary.html')


if __name__ == '__main__':
    app.run(debug=True)