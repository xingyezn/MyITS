from flask import Flask,render_template,redirect,url_for,request,session,g,views,flash

import config
from exts import db
from models import User,Role,CMSPermission
from forms import LoginForm,RegisterForm
"""
这里是智能导学系统的app模块
"""

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/index')
def index():
    return render_template('index.html')

# 登录视图函数
class LoginView(views.MethodView):

    def get(self,message=None):
        return render_template('login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if user and user.password == password:
                session['user_id'] = user.id
                #if remember:
                    # 如果设置sesion.premanent = True
                    # 过期时间为30天
                    #session.permanent = True
                return redirect(url_for('index'))
            else:
                return self.get(message='邮箱或密码错误')
        else:
            message = form.get_error()
            return self.get(message=message)
# 绑定视图函数
app.add_url_rule('/',view_func=LoginView.as_view('/'))

# 添加用户函数
class AddUserView(views.MethodView):

    def get(self,message=None):
        return render_template('login.html', message=message)

    def post(self):
        form = RegisterForm(request.form)
        # print(request.form)
        # print(form.validate())
        username = form.newusername.data
        parent_id = form.parent_id.data
        email = form.email.data
        password = form.password.data
        password2 = form.password2.data
        permission = form.permission.data
        province = form.province.data
        city = form.city.data
        county = form.county.data
        schoolname = form.school.data
        context = {
            'oldusername': username,
            'email': email,
            'password': password,
            'permission': permission,
            'password2': password2,
            'province': province,
            'city': city,
            'county': county,
            'schoolname': schoolname
        }
        if form.validate():
            user = User(username=username,
                        parent_id=parent_id,
                        email=email,
                        password=password,
                        role_permission=permission,
                        province=province,
                        city=city,
                        county=county,
                        schoolname=schoolname)
            if not User.query.filter_by(email=email).first():
                db.session.add(user)
                db.session.commit()
                flash('添加用户'+username+'成功')
                return redirect(url_for('index'))
            else:
                flash("该邮箱已被注册！请更换邮箱!")
                return render_template('login.html',**context)
        else:
            flash(form.get_error())
            return render_template('login.html',**context)
# 绑定函数
app.add_url_rule('/register',view_func=AddUserView.as_view('register'))


if __name__ == '__main__':
    app.run()
