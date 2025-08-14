import json
import requests
from flask import Blueprint, render_template, request, Response, jsonify

chat_blueprint = Blueprint("chat", __name__, template_folder=".")

# AI 配置（建议通过环境变量加载敏感信息）
TOKEN = "Bearer pat_wm0n410u3ch6Jnz6idgqqNqZ78gn60X4IzN70pP1122GX8WBH35WEuVOSUVBjdNu"
BOT_ID = "7480570833715642419"
URL = "https://api.coze.cn/v3/chat"

HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Connection": "keep-alive",
}


def stream_ai_response(user_message):
    """调用远程 AI 接口，并按行流式返回处理后的内容"""
    payload = {
        "bot_id": BOT_ID,
        "user_id": "123",  # 根据需要替换为动态用户标识
        "stream": True,
        "auto_save_history": True,
        "additional_messages": [
            {
                "role": "user",
                "content": user_message,
                "content_type": "text"
            }
        ]
    }
    try:
        ai_response = requests.post(URL, headers=HEADERS, json=payload, stream=True)
    except requests.exceptions.RequestException as e:
        return Response(json.dumps({"content": f"网络错误：{str(e)}"}) + "\n",
                        mimetype="application/json")

    def generate():
        # 逐行读取远程返回的流式数据
        for line in ai_response.iter_lines():
            if line:
                try:
                    # 将每行解码为字符串
                    line_str = line.decode("utf-8")
                    # 这里参考你提供的代码逻辑，查找包含 "content" 的行
                    if "content" in line_str:
                        # 注意：这里假设远程返回的格式为类似 "xxx:{...}"
                        # 我们取冒号后面的部分，并解析成 JSON 对象
                        json_str = line_str.split(":", 1)[1]
                        js_data = json.loads(json_str)
                        # 如果类型为 answer，则输出 content 内容
                        if js_data.get("type") == "answer":
                            # 输出处理后的内容，并附加换行符
                            yield json.dumps({"content": js_data.get("content", "")}) + "\n"
                except Exception as e:
                    # 遇到解析错误时输出错误信息
                    yield json.dumps({"content": f"解析错误：{str(e)}"}) + "\n"

    return Response(generate(), mimetype="application/json")


@chat_blueprint.route("/chat")
def chat_page():
    """渲染聊天页面"""
    return render_template("chat.html")


@chat_blueprint.route("/api", methods=["POST"])
def chat_api():
    """接收用户输入，并调用 AI 接口返回流式数据"""
    data = request.json
    user_input = data.get("message", "")
    if not user_input.strip():
        return jsonify({"response": "请输入内容。"})
    return stream_ai_response(user_input)
