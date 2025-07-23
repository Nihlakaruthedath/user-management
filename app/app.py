#app.py is flask App & Routers"



from flask import Flask, jsonify, request
from models import db, User

#creating flask application
app= Flask(__name__)

#Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#bind sqlalchemy to the Flask App #linking database to the app
db.init_app(app)

# adding a simple GET endpoint to fetch all users from the database
@app.route('/users', methods=['GET'])
def get_all_users():
    users= User.query.all()   #fetching all the users from database
    users_list=[]
    for user in users:
        users_list.append({'id':user.id,
                           'name': user.name,
                           'email':user.email})
    return jsonify(users_list), 200


#GET route for single or specific user ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user=User.query.get(user_id)
    if user is None:
        return jsonify({"error":"user not found"}), 404

    return jsonify({"id": user.id, "name": user.name, "email": user.email})




#adding POST API to insert users to database
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email= data.get('email')

    #validation
    if not name or not email:
        return jsonify({"error": "missing name or email"}), 400
    
    #duplication handling
    existing_user=User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"error": "User with this email already exist"}), 409

    new_user=User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "user created succesfully",
                    'id': new_user.id,
                    'name': new_user.name,
                    'email': new_user.email}), 201



# adding PUT API to modify the existing user
@app.route('/users/<int:id>', methods = ['PUT'])
def update_user(id):
    user= User.query.get(id)
    if not user:
        return jsonify({'error':'user not found'}), 404
    
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error":'invalid json format'}), 415
    
    if not isinstance(data, dict):
        return jsonify({"error": "Payload must be a json object"}), 400
    
    name = data.get('name')
    email= data.get('email')


    #basic validation
    if not name or not email:
        return jsonify({"error":'Name and email required'}), 400

    #update user   
    user.name=name
    user.email=email

    # save changes to db
    db.session.commit()

    return jsonify({'id':user.id, 
                    'name': user.name,
                    'email': user.email}), 200

    

#Adding DELETE API for removing existing user
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user=User.query.get(id)
    if not user:
        return jsonify({'error':'user not found'}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"User {id} deleted successfully"}), 200








if __name__=='__main__':
    with app.app_context():   #getting the access to the application context
        db.create_all()
    app.run(debug=True)

