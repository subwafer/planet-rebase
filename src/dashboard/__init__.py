from flask import Blueprint, render_template, request
from ..robot_manager import get_some_robots

dashboard = Blueprint("dashboard", __name__, template_folder="./templates")

@dashboard.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        some_robots = get_some_robots()
        
        return render_template("index.html", some_robots=some_robots)