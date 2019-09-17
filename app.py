from flask import Flask,render_template,redirect,url_for,request,session,g,views,flash

import config
from exts import db
from decorators import login_required
from models import User, Questionnaire
from forms import LoginForm, RegisterForm, AddDataForm

"""
这里是智能导学系统的app模块
"""

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/index')
@login_required
def index():
    question = Questionnaire.query.filter_by(user_id=g.user.id).first()
    context = {
        'child' : question
    }
    return render_template('index.html',**context)


#在请求之前进行的检测，修饰函数。用来确定g的数据的
@app.before_request
def before_request():
    if 'user_id' in session:
        user_id = session.get('user_id')
        user = User.query.get(user_id)
        if user:
            g.user = user


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
                if Questionnaire.query.filter_by(user_id=user.id).first():
                    return redirect(url_for('index'))
                return redirect(url_for('question'))
            else:
                #flash('邮箱或密码错误')
                return self.get(message='邮箱或密码错误')
        else:
            message = form.get_error()
            # print(message)
            return self.get(message=message)
# 绑定视图函数
app.add_url_rule('/',view_func=LoginView.as_view('/'))

# 注销视图函数
@app.route('/logout')
@login_required
def logout():
    # session.clear()
    del session['user_id']
    return redirect(url_for('/'))


# 注册用户函数
class AddUserView(views.MethodView):

    def get(self,message=None):
        return render_template('login.html', message=message)

    def post(self):
        form = RegisterForm(request.form)
        email = form.email.data
        username = form.username.data
        password = form.password.data
        schoolname = form.schoolname.data
        grade = form.grade.data
        userage = form.userage .data
        usergender = form.usergender .data
        #print(email)
        #print('数据获取')
        #print(form.validate())
        """
        context = {
            'oldusername': username,
            'email': email,
            'password': password,
            'grade': grade,
            'userage': userage,
            'usergender': usergender,
            'schoolname': schoolname
        }"""
        if form.validate():

            user = User(username=username,
                        parent_id=2,
                        email=email,
                        password=password,
                        role_permission=3,
                        grade=grade,
                        userage=userage,
                        usergender=usergender,
                        schoolname=schoolname)
            if not User.query.filter_by(email=email).first():
                db.session.add(user)
                db.session.commit()
                # print('注册正常')
                # flash('添加用户'+username+'成功')
                # message = '注册成功，请登录'
                return redirect(url_for('/'))
            else:
                flash("该邮箱已被注册！请更换邮箱!")
                message = "该邮箱已被注册！请更换邮箱!"
                return render_template('login.html',message =message)
        else:
            flash(form.get_error())
            message = form.get_error()
            return self.get(message=message)
# 绑定函数
app.add_url_rule('/register',view_func=AddUserView.as_view('register'))


# 添加问卷数据
class AddDataView(views.MethodView):

    def get(self,message=None):
        return render_template('question.html')

    def post(self):
        form = AddDataForm(request.form)
        #print('test')
        SF1 = form.SF1.data
        SF2 = form.SF2.data
        SF3 = form.SF3.data
        SF4 = form.SF4.data
        SF5 = form.SF5.data
        SF6 = form.SF6.data
        SF7 = form.SF7.data
        SF8 = form.SF8.data
        SF9 = form.SF9.data
        SF10 = form.SF10.data
        SF11 = form.SF11.data
        SF12 = form.SF12.data
        SF13 = form.SF13.data
        SF14 = form.SF14.data
        SF15 = form.SF15.data
        SF16 = form.SF16.data
        SF17 = form.SF17.data
        SF18 = form.SF18.data
        SF19 = form.SF19.data
        SF20 = form.SF20.data
        SF21 = form.SF21.data
        SF22 = form.SF22.data
        SF23 = form.SF23.data
        SF24 = form.SF24.data
        SF25 = form.SF25.data

        ST1 = form.ST1.data
        ST2 = form.ST2.data
        ST3 = form.ST3.data
        ST4 = form.ST4.data
        ST5 = form.ST5.data
        ST6 = form.ST6.data
        ST7 = form.ST7.data
        ST8 = form.ST8.data
        ST9 = form.ST9.data
        ST10 = form.ST10.data
        ST11 = form.ST11.data
        ST12 = form.ST12.data
        ST13 = form.ST13.data
        ST14 = form.ST14.data
        ST15 = form.ST15.data
        ST16 = form.ST16.data
        ST17 = form.ST17.data
        ST18 = form.ST18.data
        ST19 = form.ST19.data
        ST20 = form.ST20.data
        ST21 = form.ST21.data
        ST22 = form.ST22.data
        ST23 = form.ST23.data
        ST24 = form.ST24.data
        ST25 = form.ST25.data

        NT1 = form.NT1.data
        NT2 = form.NT2.data
        NT3 = form.NT3.data
        NT4 = form.NT4.data
        NT5 = form.NT5.data
        NT6 = form.NT6.data
        NT7 = form.NT7.data
        NT8 = form.NT8.data
        NT9 = form.NT9.data
        NT10 = form.NT10.data
        NT11 = form.NT11.data
        NT12 = form.NT12.data
        NT13 = form.NT13.data
        NT14 = form.NT14.data
        NT15 = form.NT15.data
        NT16 = form.NT16.data
        NT17 = form.NT17.data
        NT18 = form.NT18.data
        NT19 = form.NT19.data
        NT20 = form.NT20.data
        NT21 = form.NT21.data
        NT22 = form.NT22.data
        NT23 = form.NT23.data
        NT24 = form.NT24.data
        NT25 = form.NT25.data

        NF1 = form.NF1.data
        NF2 = form.NF2.data
        NF3 = form.NF3.data
        NF4 = form.NF4.data
        NF5 = form.NF5.data
        NF6 = form.NF6.data
        NF7 = form.NF7.data
        NF8 = form.NF8.data
        NF9 = form.NF9.data
        NF10 = form.NF10.data
        NF11 = form.NF11.data
        NF12 = form.NF12.data
        NF13 = form.NF13.data
        NF14 = form.NF14.data
        NF15 = form.NF15.data
        NF16 = form.NF16.data
        NF17 = form.NF17.data
        NF18 = form.NF18.data
        NF19 = form.NF19.data
        NF20 = form.NF20.data
        NF21 = form.NF21.data
        NF22 = form.NF22.data
        NF23 = form.NF23.data
        NF24 = form.NF24.data
        NF25 = form.NF25.data

        SF = form.SF.data
        ST = form.ST.data
        NT = form.NT.data
        NF = form.NF.data
        questionnaire = Questionnaire(
            user_id = g.user.id,
            SF1=SF1,
            SF2=SF2,
            SF3=SF3,
            SF4=SF4,
            SF5=SF5,
            SF6=SF6,
            SF7=SF7,
            SF8=SF8,
            SF9=SF9,
            SF10=SF10,
            SF11=SF11,
            SF12=SF12,
            SF13=SF13,
            SF14=SF14,
            SF15=SF15,
            SF16=SF16,
            SF17=SF17,
            SF18=SF18,
            SF19=SF19,
            SF20=SF20,
            SF21=SF21,
            SF22=SF22,
            SF23=SF23,
            SF24=SF24,
            SF25=SF25,
            ST1=ST1,
            ST2=ST2,
            ST3=ST3,
            ST4=ST4,
            ST5=ST5,
            ST6=ST6,
            ST7=ST7,
            ST8=ST8,
            ST9=ST9,
            ST10=ST10,
            ST11=ST11,
            ST12=ST12,
            ST13=ST13,
            ST14=ST14,
            ST15=ST15,
            ST16=ST16,
            ST17=ST17,
            ST18=ST18,
            ST19=ST19,
            ST20=ST20,
            ST21=ST21,
            ST22=ST22,
            ST23=ST23,
            ST24=ST24,
            ST25=ST25,
            NT1=NT1,
            NT2=NT2,
            NT3=NT3,
            NT4=NT4,
            NT5=NT5,
            NT6=NT6,
            NT7=NT7,
            NT8=NT8,
            NT9=NT9,
            NT10=NT10,
            NT11=NT11,
            NT12=NT12,
            NT13=NT13,
            NT14=NT14,
            NT15=NT15,
            NT16=NT16,
            NT17=NT17,
            NT18=NT18,
            NT19=NT19,
            NT20=NT20,
            NT21=NT21,
            NT22=NT22,
            NT23=NT23,
            NT24=NT24,
            NT25=NT25,
            NF1=NF1,
            NF2=NF2,
            NF3=NF3,
            NF4=NF4,
            NF5=NF5,
            NF6=NF6,
            NF7=NF7,
            NF8=NF8,
            NF9=NF9,
            NF10=NF10,
            NF11=NF11,
            NF12=NF12,
            NF13=NF13,
            NF14=NF14,
            NF15=NF15,
            NF16=NF16,
            NF17=NF17,
            NF18=NF18,
            NF19=NF19,
            NF20=NF20,
            NF21=NF21,
            NF22=NF22,
            NF23=NF23,
            NF24=NF24,
            NF25=NF25,
            SF=SF,
            ST=ST,
            NT=NT,
            NF=NF
        )

        db.session.add(questionnaire)
        db.session.commit()

        return redirect(url_for('index'))
# 绑定函数
app.add_url_rule('/question',view_func=AddDataView.as_view('question'))

if __name__ == '__main__':
    app.run()
