from flask import render_template, Blueprint

# 创建一个蓝图对象
service_blueprint = Blueprint('service', __name__)


@service_blueprint.route("/")
def index():
    """首页"""
    return render_template("index.html")
