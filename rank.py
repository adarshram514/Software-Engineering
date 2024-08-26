#branch 3 
"""
Update the user's rank based on their experience points.
Retrieve the rank name based on the rank number.

"""
# Defining experience points threshold for each rank
def update_user_rank(db, user):
    rank_thresholds = {
         1: 60,  #Beginner
         2: 120,  #Intermediate 
         3: 180,  #Advanced
         4: 240 #Expert
    }
# Determine the user's rank based on their experience points
    new_rank = user.rank
    print(new_rank)

    for rank, threshold in rank_thresholds.items():
        if user.experience > threshold:
            new_rank = rank + 1
        else:
            break #DON'T DELETE this stops the search after the rank is found

    # Update the user's rank if its changed    
        if new_rank != user.rank:
            user.rank = new_rank
            db.session.commit()

def get_rank_name(rank_number):
    ranks = {
        1: 'Beginner',
        2: 'Intermediate',
        3: 'Advanced',
        4: 'Expert'
    }
    return ranks.get(rank_number, 'Beginner')
