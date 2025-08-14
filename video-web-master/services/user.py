from flask import render_template, request, jsonify, session, Blueprint
import os

# 创建一个蓝图对象
user_blueprint = Blueprint('user', __name__)

USER_FILE = "TxtDB/users.txt"  # 用户账号密码


def load_users():
    """加载用户信息"""
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r", encoding="utf-8") as f:
        return dict(line.strip().split(",") for line in f if line.strip())


def save_user(username, password):
    """保存用户信息"""
    with open(USER_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username},{password}\n")


@user_blueprint.route("/login", methods=["POST"])
def login():
    """用户登录"""
    users = load_users()
    data = request.json
    if users.get(data["username"]) == data["password"]:
        session["user"] = data["username"]
        return jsonify(success=True, username=data["username"])
    return jsonify(success=False, message="账号或密码错误")


@user_blueprint.route("/register", methods=["POST"])
def register():
    """用户注册"""
    users = load_users()
    data = request.json
    if data["username"] in users:
        return jsonify(success=False, message="用户名已存在")
    save_user(data["username"], data["password"])
    session["user"] = data["username"]
    return jsonify(success=True, username=data["username"])


@user_blueprint.route("/logout", methods=["POST"])
def logout():
    """用户登出"""
    session.pop("user", None)
    return jsonify({"success": True})