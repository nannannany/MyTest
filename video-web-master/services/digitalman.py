from flask import render_template, Blueprint

# 创建一个蓝图对象
digitalman_blueprint = Blueprint('digitalman', __name__)


@digitalman_blueprint.route("/digitalman")
def digitalman():
    # 数字人
    return render_template("digitalman.html")
