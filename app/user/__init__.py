from flask import Blueprint,render_template,request,redirect

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login')
# as customer or as admin
def login():
    # 获取用户输入的用户名
    username = request.args.get('username', None)
    password = request.args.get('password', None)
    # 逻辑处理， 用来判断用户和密码是否正确;
    if username == 'root' and password == 'redhat':
        # 重定向到指定路由；
        return redirect('/')
        # return "登录成功"
    else:
        return "登录失败"
    return render_template('login.html')


@bp.route('/register')
# name, email-id, password, contact number, and address
#   as customer or as admin
def register():
   return render_template('user/register.html')


@bp.route('/logout')
def logout():
    return render_template('user/login.html')
