from flask import Blueprint,request
from model import Todo

todo = Blueprint("task",__name__)

@users.route("/", methods=["GET")
def get_form():
    list_users = json.loads(Users.objects.to_json())
    return jsonify({"usuarios":list_users})
