import os #branch 2

def award_experience(db,user,action):
    experience_points = 0
    if action == 'forum_post':
        experience_points+= 3
    elif action == 'forum_like':
        experience_points+= 2
    elif action == 'forum_comment':
        experience_points+= 5
    elif action == 'chatbot_submit':
        experience_points+= 2
    elif action == 'shorts_submit':
        experience_points+= 2
    elif action == 'know_card':
        experience_points+= 3
    elif action == 'set_beginner':
        experience_points+= 60
    elif action == 'set_intermediate':
        experience_points+= 120
    elif action == 'set_advanced':
        experience_points+= 180

    user.experience += experience_points
    db.session.commit()

    from flask import session
    session['exp_awarded'] = f"You have earned {experience_points} experience points!"
    return user
    

