from flask import Blueprint, request, render_template, jsonify
from http import HTTPStatus
from controller.auth_controller import register_user, authenticate_user
from controller.chat_controller import ChatController
from flask_jwt_extended import jwt_required


app = Blueprint('app', __name__, url_prefix='/api', template_folder='templates')
chat_controller = ChatController()

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html', title="Register")

    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return {"error": "O email e a senha são obrigatórios!"}, HTTPStatus.BAD_REQUEST
    
    try:
        user = register_user(email, password)
    except:
        return {"error": "Erro ao registrar usuário!"}, HTTPStatus.INTERNAL_SERVER_ERROR
    
    return {"message": f"Usuário {user.email} registrado com sucesso!"}, HTTPStatus.CREATED

@app.route("/login", methods=['POST',])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    try:
        user = authenticate_user(email, password)
        return {"access_token": user}, HTTPStatus.OK
    except ValueError as ve:
        print(ve)
        return {"error": str(ve)}, HTTPStatus.UNAUTHORIZED
    except Exception as e:
        print(e)
        return {"error": "Erro ao autenticar usuário."}, HTTPStatus.INTERNAL_SERVER_ERROR


@app.route("/chat", methods=["GET", "POST"])
@jwt_required()
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    response = chat_controller.generate_response(user_message)
    return jsonify({"response": response})
    
    