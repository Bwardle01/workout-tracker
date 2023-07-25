import sys
from flask import Blueprint, request, jsonify, session
from app.models import User, Exercise, Workout, ExerciseStats
from app.db import get_db
# from app.utils.auth import login_required this is a util

bp = Blueprint('api', __name__, url_prefix='/api')


# signup
@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  db = get_db()

  try:
    # attempt creating a new user
    newUser = User(
      username = data['username'],
      email = data['email'],
      password = data['password']
    )

    db.add(newUser)
    db.commit()
  except:
    print(sys.exc_info()[0])

    # insert failed, so rollback and send error to front end
    db.rollback()
    return jsonify(message = 'Signup failed'), 500

  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True

  return jsonify(id = newUser.id)

# logout
@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204

# login
@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()

  try:
    user = db.query(User).filter(User.email == data['email']).one()
  except:
    print(sys.exc_info()[0])

    return jsonify(message = 'Incorrect credentials'),400

  if user.verify_password(data['password']) == False:
    return jsonify(message = 'Incorrect credentials'),400

  session.clear()
  session['user_id'] = user.id
  session['loggedIn'] = True

  return jsonify(id = user.id)

# save data route
@bp.route('/save', methods=['POST'])
def save_workout_data():
    data = request.get_json()
    print('Received data:', data)
    db = get_db()

    try:
        inner_data = data.get('data', None)  # Get the inner data dictionary
        if not inner_data:
            return jsonify(message='Invalid data format'), 400

        # Check for missing keys and provide default values if necessary
        workout_name = inner_data.get('workoutName', None)
        date = inner_data.get('date', None)
        exercise_name = inner_data.get('exerciseName', None)
        weight = inner_data.get('weight', None)
        reps = inner_data.get('reps', None)

        # if any field is not filled in.
        if workout_name is None or date is None or exercise_name is None or weight is None or reps is None:
            return jsonify(message='Missing required data'), 400
        # if a user is logged in.
        user_id = session.get('user_id')
        if not user_id:
            return jsonify(message='User not logged in'), 401

        exercise = Exercise(exerciseName=exercise_name)
        exercise_stats = ExerciseStats(weight=weight, reps=reps)

        new_workout = Workout(
            workoutName=workout_name,
            date=date,
            user_id=user_id  # Use the user_id from the session
        )

        exercise.stats.append(exercise_stats)
        new_workout.exercises.append(exercise)

        db.add(new_workout)
        db.commit()

    except Exception as e:
        print('Error:', e)  # Print the exact exception message
        db.rollback()
        return jsonify(message='Failed to save data'), 500

    return jsonify(id=new_workout.id)
