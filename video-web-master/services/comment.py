import os
import time
from flask import  request, jsonify, session, Blueprint

# 创建一个蓝图对象
comment_blueprint = Blueprint('comment', __name__)

COMMENT_FILE = "TxtDB/comments.txt"  # 评论文件


@comment_blueprint.route("/comment", methods=["POST"])
def comment():
    """提交评论"""
    if "user" not in session:
        return jsonify(success=False, message="请先登录")

    text = request.json["comment"]
    with open(COMMENT_FILE, "a", encoding="utf-8") as f:
        f.write(f"{session['user']}|{text}|{time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    return jsonify(success=True)


@comment_blueprint.route("/comments")
def get_comments():
    """获取所有评论"""
    if not os.path.exists(COMMENT_FILE):
        return jsonify([])
    with open(COMMENT_FILE, "r", encoding="utf-8") as f:
        return jsonify([dict(zip(["username", "text", "time"], line.strip().split("|"))) for line in f])