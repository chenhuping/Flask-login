# coding:utf-8


from flask import session, make_response, Flask, request, render_template
from config import AboutConfig
from utils.captcha.captcha import captcha
import redis


app = Flask(__name__)
app.config.from_object(AboutConfig)
app.config.update(
    DEBUG=True,
)


redis_conn = redis.StrictRedis(host='127.0.0.1', port=6379)


@app.route('/imageCode', methods=['POST'])
def get_image_code():
    """
    获取图片验证码
    1.接收请求，获取UUID和上一个uuid
    2.判断数据库保存的uuid是否等于last_uuid等于删除，
    3.生成图片验证码
    4.保存新的uuid，对应的图片文本信息
    :return: josnify 验证码图片
    """
    # 1.接收请求，获取UUID，last_uuid
    data = request.get_json(silent=True)
    if not data:
        return '参数不完整'
    uuid = data.get('uuid')
    last_uuid = data.get('last_uuid')
    if not uuid:
        return '参数不完整'
    # 2.生成图片验证码 名字，文字信息，图片信息
    name, text, image = captcha.generate_captcha()
    # 4.删除上次生成的验证码图片
    try:
        if last_uuid:
            redis_conn.delete('ImageCode:'+last_uuid)
        # 3.保存UUID对应的验证码文字信息,设置时长
        redis_conn.set('ImageCode:' + uuid, text, 600)
    except Exception as e:
        print e
        return '保存图片验证码失败'
    print redis_conn.get('ImageCode:' + uuid)
    response = make_response(image)
    response.headers['Content-Type'] = 'image/jpg'
    return response


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=False)
    if not data:
        return '参数不完整'
    user_name = data.get('user_name')
    password = data.get('password')
    image_code = data.get('image_code').lower()

    uuid = data.get('uuid')
    if not all([user_name, password, image_code, uuid]):
        return '参数不完整'
    # 根据uuir去redis中获取对应的值，看是否与image_code一致
    old_image_code = redis_conn.get('ImageCode:' + uuid)
    if old_image_code:
        old_image_code = old_image_code.lower()
    if old_image_code != image_code:
        return '验证码不正确'
    if user_name == 'chenhuping' and password == '123456':
        redis_conn.delete('ImageCode:' + uuid)
        return '登录成功'
    else:
        return '账户名或密码错误'


if __name__ == '__main__':
    # app.secret_key = 'i-like-python-nmba'
    app.run()
