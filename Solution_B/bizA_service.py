#查詢業務 A 的個性化資料
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/user-profile/<user_id>', methods=['GET'])
def get_biz_user_profile(user_id):
    # 模擬從業務 A 專屬資料庫查個性化欄位
    # 例如：大頭貼、積分、偏好設定等
    return jsonify({
        "profile_pic": f"https://cdn.bizA.com/avatar/{user_id}.png",
        "vip_level": "Gold",
        "preferences": ["dark_mode", "email_notification"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
