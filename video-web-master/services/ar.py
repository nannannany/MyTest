from flask import render_template, Blueprint

# 创建一个蓝图对象
ar_blueprint = Blueprint('ar', __name__)


@ar_blueprint.route("/ar")
def ar():
    # 数字人
    return render_template("ar.html")
