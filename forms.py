from wtforms import Form,StringField,IntegerField,ValidationError,FloatField
from wtforms.validators import Email,InputRequired,Length,EqualTo
# 用来邮箱验证的
import cache
from models import User
from flask import g

class BaseForms(Form):
    def get_error(self):
        message = self.errors.popitem()[1][0]
        return message


# 登录界面的form表单检测
class LoginForm(BaseForms):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'),InputRequired(message='请输入邮箱！')])
    password = StringField(validators=[Length(6,20,message='请输入正确格式的密码')])

# 注册用户的表单检测
class RegisterForm(BaseForms):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'), InputRequired(message='请输入邮箱！')])
    username = StringField(validators=[InputRequired(message='请输入用户名')])
    password = StringField(validators=[Length(6, 20, message='请输入正确格式的密码')])
    repassword = StringField(validators=[EqualTo("password", message='密码必须保持一致')])
    schoolname = StringField(validators=[InputRequired(message='请输入学校姓名')])
    grade = IntegerField(validators=[InputRequired(message='请选择用户年级')])
    userage = IntegerField(validators=[InputRequired(message='请选择用户年龄')])
    usergender = IntegerField(validators=[InputRequired(message='请选择用户性别')])

    def validate_email(self, field):
        if User.query.filter(User.email == field.data).first():
            raise ValidationError('该邮箱已被注册请另外选择邮箱！')

class AddDataForm(BaseForms):
    SF1 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF2 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF3 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF4 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF5 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF6 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF7 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF8 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF9 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF10 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF11 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF12 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF13 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF14 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF15 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF16 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF17 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF18 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF19 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF20 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF21 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF22 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF23 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF24 = IntegerField(validators=[InputRequired(message='请输入数据')])
    SF25 = IntegerField(validators=[InputRequired(message='请输入数据')])

    ST1 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST2 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST3 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST4 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST5 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST6 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST7 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST8 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST9 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST10 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST11 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST12 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST13 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST14 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST15 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST16 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST17 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST18 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST19 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST20 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST21 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST22 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST23 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST24 = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST25 = IntegerField(validators=[InputRequired(message='请输入数据')])

    NT1 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT2 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT3 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT4 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT5 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT6 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT7 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT8 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT9 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT10 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT11 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT12 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT13 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT14 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT15 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT16 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT17 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT18 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT19 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT20 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT21 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT22 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT23 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT24 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT25 = IntegerField(validators=[InputRequired(message='请输入数据')])

    NF1 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF2 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF3 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF4 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF5 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF6 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF7 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF8 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF9 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF10 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF11 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF12 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF13 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF14 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF15 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF16 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF17 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF18 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF19 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF20 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF21 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF22 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF23 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF24 = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF25 = IntegerField(validators=[InputRequired(message='请输入数据')])

    SF = IntegerField(validators=[InputRequired(message='请输入数据')])
    ST = IntegerField(validators=[InputRequired(message='请输入数据')])
    NT = IntegerField(validators=[InputRequired(message='请输入数据')])
    NF = IntegerField(validators=[InputRequired(message='请输入数据')])


"""
# 重置密码的表单检测
class ResetpwdForm(BaseForms):
    oldpwd = StringField(validators=[Length(6,20,message='请输入正确格式的旧密码')])
    newpwd = StringField(validators=[Length(6,20,message='请输入正确格式的新密码')])
    newpwd2 = StringField(validators=[EqualTo("newpwd",message='确认密码必须和新密码保持一致')])

# 重置邮箱的表单检测
class ResetEmailForm(BaseForms):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱！')])
    captcha = StringField(validators=[Length(min=6,max=6,message='请输入正常长度的验证码！')])

    def validate_captcha(self,field):
        #表单提交的验证码
        captcha = field.data
        # 表单提交的email
        email = self.email.data
        # 缓存email
        
        captcha_cache = cache.get(email)
        print(captcha)
        print(captcha_cache)
        if not captcha_cache and captcha.lower() != captcha_cache.lower():
            raise ValidationError('邮箱验证码错误！')


    def validate_email(self,field):
        email = field.data
        user = g.user
        if user.email == email:
            raise ValidationError('不能修改为相同的邮箱！')

"""