from flask import Flask
from services.services import service_blueprint  # 导入服务首页
from services.user import user_blueprint  # 导入用户相关
from services.chat import chat_blueprint  # 导入聊天相关
from services.pk import pk_blueprint  # 导入pk相关
from services.comment import comment_blueprint  # 导入评论相关
from services.digitalman import digitalman_blueprint  # 导入数字人相关
from services.ar import ar_blueprint  # 导入ar相关

app = Flask(__name__)
app.secret_key = "super_secret_key"

# 注册蓝图
app.register_blueprint(service_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(pk_blueprint)
app.register_blueprint(comment_blueprint)
app.register_blueprint(digitalman_blueprint)
app.register_blueprint(ar_blueprint)
app.register_blueprint(chat_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082, debug=True)
