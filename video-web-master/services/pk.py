import os
from flask import render_template, request, jsonify, session, Blueprint

# 创建一个蓝图对象
pk_blueprint = Blueprint('pk', __name__)

RANKING_FILE = "TxtDB/ranking.txt"  # 排行榜文件
BACKGROUND_IMAGE_URL = "https://img.picui.cn/free/2025/03/15/67d597e3d7dc6.png"  # 背景图的 URL


@pk_blueprint.route("/pk")
def pk():
    """PK 界面"""
    return render_template("pk.html", background_image_url=BACKGROUND_IMAGE_URL)


@pk_blueprint.route("/submit_answer", methods=["POST"])
def submit_answer():
    """处理用户答题"""
    data = request.json
    user_answer = data.get("answer")
    time_spent = data.get("time_spent")

    if user_answer == "还来就菊花":
        score = max(0, 100 - int(time_spent * 2))  # 每 0.5 秒扣 1 分
        username = session.get("user", "匿名用户")  # 记录登录用户或匿名用户
        save_score(username, score)
        return jsonify(success=True, score=score)
    else:
        return jsonify(success=False, message="答案错误")


def save_score(username, score):
    """保存分数"""
    scores = []
    if os.path.exists(RANKING_FILE):
        with open(RANKING_FILE, "r", encoding="utf-8") as f:
            scores = [line.strip().split(",") for line in f if line.strip()]

    scores.append([username, str(score)])
    scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)[:10]  # 取前 10 名

    with open(RANKING_FILE, "w", encoding="utf-8") as f:
        for user, score in scores:
            f.write(f"{user},{score}\n")


@pk_blueprint.route("/get_ranking")
def get_ranking():
    """获取排行榜"""
    if not os.path.exists(RANKING_FILE):
        return jsonify([])
    with open(RANKING_FILE, "r", encoding="utf-8") as f:
        return jsonify([dict(zip(["username", "score"], line.strip().split(","))) for line in f])
