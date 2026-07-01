<<<<<<< HEAD
from flask import Flask, render_template, redirect, url_for

# 初始化Flask应用
app = Flask(__name__)
app.config['SECRET_KEY'] = 'flower_delivery_key_2026'

# 首页：默认跳转到身份选择页
@app.route('/')
def index():
    return redirect(url_for('mock_page', filename='identity_select.html'))# 测试页路由：验证环境
@app.route('/test')
def test_page():
    return render_template('test.html', title="鲜花配送系统-环境测试页")

# 通用原型路由：一键访问所有墨刀HTML页面
@app.route('/')
def index():
    return redirect(url_for('mock_page', filename='identity_select.html'))# 本地启动入口
if __name__ == '__main__':
    # 本地开发开启debug=True；上线部署改为False
=======
from flask import Flask, render_template, redirect, url_for

# 初始化Flask应用
app = Flask(__name__)
app.config['SECRET_KEY'] = 'flower_delivery_key_2026'

# 首页：默认跳转到测试页，后续可改为业务首页
@app.route('/')
def index():
    return redirect(url_for('test_page'))

# 测试页路由：验证环境
@app.route('/test')
def test_page():
    return render_template('test.html', title="鲜花配送系统-环境测试页")

# 通用原型路由：一键访问所有墨刀HTML页面
@app.route('/page/<filename>')
def mock_page(filename):
    return render_template(filename)

# 本地启动入口
if __name__ == '__main__':
    # 本地开发开启debug=True；上线部署改为False
>>>>>>> 20dc931aa27b512bcbc59fb592419db57e8f68bb
    app.run(host='0.0.0.0', port=5000, debug=True)