from exts import db
from datetime import datetime
from werkzeug.security import check_password_hash

class CMSPermission(object):
    # 开发者管理员
    DEVELOPER = 1
    # 区域管理员
    TEACHER = 2
    # 学校管理员
    STUDENT = 3

class Role(db.Model):
    # 用户角色表
    __tablename__ = 'role'
    # 角色名称
    name = db.Column(db.String(50), nullable=False)
    # 角色描述
    desc = db.Column(db.String(200),nullable=True)
    # 用户权限（主键）
    permission = db.Column(db.Integer,nullable=False,primary_key=True)

class User(db.Model):
    # 用户信息表
    __tablename__ = 'user'

    # 用户id
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    #  一下是必须填写的信息
    # 用户姓名
    username = db.Column(db.String(50),nullable=False)

    # 用户学校
    schoolname = db.Column(db.String(100), nullable=False)

    # 年龄
    userage = db.Column(db.Integer, nullable=False)

    # 性别 1代表男，2代表女
    usergender = db.Column(db.Integer, nullable=False)

    # 年级，1-12表示K12
    grade = db.Column(db.Integer, nullable=False)

    # 用户密码
    password = db.Column(db.String(100),nullable=False)

    # 用户邮箱
    email = db.Column(db.String(50),nullable=False,unique=True)

    # 这些信息都是自动生成的
    # 添加时间
    join_time = db.Column(db.DateTime,default=datetime.now)

    # 角色权限
    role_permission = db.Column(db.Integer, db.ForeignKey('role.permission'), default=None, nullable=False)

    # 用户角色
    user_role = db.relationship('Role', backref='role_users')

    parent_id = db.Column(db.Integer, default=None, nullable=True)

    # 这些信息可以后续完善，现在只需要简单的一些信息即可
    # 用户省份
    province = db.Column(db.String(100), default=None, nullable=True)

    # 用户城市
    city = db.Column(db.String(100), default=None, nullable=True)

    # 用户地区
    county = db.Column(db.String(100),default=None, nullable=True)

class Questionnaire(db.Model):
    __tablename__ = 'questionnaire'

    # 数据id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 数据所属用户的id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), default=None, nullable=False)

    # 用户角色
    user_data = db.relationship('User', backref='data_users')

    # S-F风格感官 - 感受
    # 个人的
    SF1 = db.Column(db.Integer,default = None,nullable=False)

    # 人
    SF2 = db.Column(db.Integer, default=None, nullable=False)

    # 即兴的
    SF3 = db.Column(db.Integer, default=None, nullable=False)

    # 和谐
    SF4 = db.Column(db.Integer, default=None, nullable=False)

    # 合作
    SF5 = db.Column(db.Integer, default=None, nullable=False)

    # 与个人相关
    SF6 = db.Column(db.Integer, default=None, nullable=False)

    # 讨论
    SF7 = db.Column(db.Integer, default=None, nullable=False)

    # 人际互动
    SF8 = db.Column(db.Integer, default=None, nullable=False)

    # 感受
    SF9 = db.Column(db.Integer, default=None, nullable=False)

    # 温暖
    SF10 = db.Column(db.Integer, default=None, nullable=False)

    # 直觉
    SF11 = db.Column(db.Integer, default=None, nullable=False)

    # 人性的
    SF12 = db.Column(db.Integer, default=None, nullable=False)

    # 融洽
    SF13 = db.Column(db.Integer, default=None, nullable=False)

    # 说服
    SF14 = db.Column(db.Integer, default=None, nullable=False)

    # 建立关系
    SF15 = db.Column(db.Integer, default=None, nullable=False)

    # 社会化
    SF16 = db.Column(db.Integer, default=None, nullable=False)

    # 同情的
    SF17 = db.Column(db.Integer, default=None, nullable=False)

    # 亲密
    SF18 = db.Column(db.Integer,default = None,nullable=False)

    # 忠诚
    SF19 = db.Column(db.Integer, default=None, nullable=False)

    # 经验的
    SF20 = db.Column(db.Integer, default=None, nullable=False)

    # 依恋
    SF21 = db.Column(db.Integer, default=None, nullable=False)

    # 移情
    SF22 = db.Column(db.Integer, default=None, nullable=False)

    # 仿效
    SF23 = db.Column(db.Integer, default=None, nullable=False)

    # 经验
    SF24 = db.Column(db.Integer, default=None, nullable=False)

    # 社交的
    SF25 = db.Column(db.Integer, default=None, nullable=False)

    # S-T风格感官-思考
    # 组织的
    ST1 = db.Column(db.Integer, default=None, nullable=False)

    # 事实
    ST2 = db.Column(db.Integer, default=None, nullable=False)

    # 字面的
    ST3 = db.Column(db.Integer, default=None, nullable=False)

    # 功用
    ST4 = db.Column(db.Integer, default=None, nullable=False)

    # 竞争
    ST5 = db.Column(db.Integer, default=None, nullable=False)

    # 记忆
    ST6 = db.Column(db.Integer, default=None, nullable=False)

    # 指导
    ST7 = db.Column(db.Integer, default=None, nullable=False)

    # 细节
    ST8 = db.Column(db.Integer, default=None, nullable=False)

    # 目标
    ST9 = db.Column(db.Integer, default=None, nullable=False)

    # 行为
    ST10 = db.Column(db.Integer, default=None, nullable=False)

    # 尝试错误
    ST11 = db.Column(db.Integer, default=None, nullable=False)

    # 现实的
    ST12 = db.Column(db.Integer, default=None, nullable=False)

    # 特性
    ST13 = db.Column(db.Integer, default=None, nullable=False)

    # 精确
    ST14 = db.Column(db.Integer, default=None, nullable=False)

    # 知道
    ST15 = db.Column(db.Integer, default=None, nullable=False)

    # 程序化
    ST16 = db.Column(db.Integer, default=None, nullable=False)

    # 实际的
    ST17 = db.Column(db.Integer, default=None, nullable=False)

    # 信息
    ST18 = db.Column(db.Integer, default=None, nullable=False)

    # 规则
    ST19 = db.Column(db.Integer, default=None, nullable=False)

    # 有秩序的
    ST20 = db.Column(db.Integer, default=None, nullable=False)

    # 正确
    ST21 = db.Column(db.Integer, default=None, nullable=False)

    # 明确
    ST22 = db.Column(db.Integer, default=None, nullable=False)

    # 范例
    ST23 = db.Column(db.Integer, default=None, nullable=False)

    # 努力
    ST24 = db.Column(db.Integer, default=None, nullable=False)

    # 循序渐进的
    ST25 = db.Column(db.Integer, default=None, nullable=False)

    # N-T风格直觉-思考
    # 分析的
    NT1 = db.Column(db.Integer, default=None, nullable=False)

    # 公式
    NT2 = db.Column(db.Integer, default=None, nullable=False)

    # 解析的
    NT3 = db.Column(db.Integer, default=None, nullable=False)

    # 问题
    NT4 = db.Column(db.Integer, default=None, nullable=False)

    # 批判
    NT5 = db.Column(db.Integer, default=None, nullable=False)

    # 理由
    NT6 = db.Column(db.Integer, default=None, nullable=False)

    # 辩论
    NT7 = db.Column(db.Integer, default=None, nullable=False)

    # 规律
    NT8 = db.Column(db.Integer, default=None, nullable=False)

    # 想法
    NT9 = db.Column(db.Integer, default=None, nullable=False)

    # 智慧
    NT10 = db.Column(db.Integer, default=None, nullable=False)

    # 策略
    NT11 = db.Column(db.Integer, default=None, nullable=False)

    # 理论的
    NT12 = db.Column(db.Integer, default=None, nullable=False)

    # 概念
    NT13 = db.Column(db.Integer, default=None, nullable=False)

    # 逻辑
    NT14 = db.Column(db.Integer, default=None, nullable=False)

    # 理解
    NT15 = db.Column(db.Integer, default=None, nullable=False)

    # 系统化
    NT16 = db.Column(db.Integer, default=None, nullable=False)

    # 智力的
    NT17 = db.Column(db.Integer, default=None, nullable=False)

    # 询问
    NT18 = db.Column(db.Integer, default=None, nullable=False)

    # 原则
    NT19 = db.Column(db.Integer, default=None, nullable=False)

    # 逻辑的
    NT20 = db.Column(db.Integer, default=None, nullable=False)

    # 论证
    NT21 = db.Column(db.Integer, default=None, nullable=False)

    # 好奇
    NT22 = db.Column(db.Integer, default=None, nullable=False)

    # 解释
    NT23 = db.Column(db.Integer, default=None, nullable=False)

    # 测试
    NT24 = db.Column(db.Integer, default=None, nullable=False)

    # 科学的
    NT25 = db.Column(db.Integer, default=None, nullable=False)

    # N-F风格直觉-感受
    # 创造性的
    NF1 = db.Column(db.Integer, default=None, nullable=False)

    # 热情
    NF2 = db.Column(db.Integer, default=None, nullable=False)

    # 有弹性的
    NF3 = db.Column(db.Integer, default=None, nullable=False)

    # 想象
    NF4 = db.Column(db.Integer, default=None, nullable=False)

    # 创造
    NF5 = db.Column(db.Integer, default=None, nullable=False)

    # 重新组织
    NF6 = db.Column(db.Integer, default=None, nullable=False)

    # 发现
    NF7 = db.Column(db.Integer, default=None, nullable=False)

    # 可能性
    NF8 = db.Column(db.Integer, default=None, nullable=False)

    # 洞察力
    NF9 = db.Column(db.Integer, default=None, nullable=False)

    # 怀疑
    NF10 = db.Column(db.Integer, default=None, nullable=False)

    # 有了！
    NF11 = db.Column(db.Integer, default=None, nullable=False)

    # 唯美的
    NF12 = db.Column(db.Integer, default=None, nullable=False)

    # 价值
    NF13 = db.Column(db.Integer, default=None, nullable=False)

    # 预测
    NF14 = db.Column(db.Integer, default=None, nullable=False)

    # 表达
    NF15 = db.Column(db.Integer, default=None, nullable=False)

    # 理想化
    NF16 = db.Column(db.Integer, default=None, nullable=False)

    # 理想的
    NF17 = db.Column(db.Integer, default=None, nullable=False)

    # 发明
    NF18 = db.Column(db.Integer, default=None, nullable=False)

    # 隐喻
    NF19 = db.Column(db.Integer, default=None, nullable=False)

    # 启示的
    NF20 = db.Column(db.Integer, default=None, nullable=False)

    # 取舍
    NF21 = db.Column(db.Integer, default=None, nullable=False)

    # 独创性
    NF22 = db.Column(db.Integer, default=None, nullable=False)

    # 推断
    NF23 = db.Column(db.Integer, default=None, nullable=False)

    # 热情
    NF24 = db.Column(db.Integer, default=None, nullable=False)

    # 对称的
    NF25 = db.Column(db.Integer, default=None, nullable=False)

    # 感官-感受
    SF =  db.Column(db.Integer, default=None, nullable=False)

    # 感官-思考
    ST =  db.Column(db.Integer, default=None, nullable=False)

    # 直觉-思考
    NT =  db.Column(db.Integer, default=None, nullable=False)

    # 直觉-感受
    NF =  db.Column(db.Integer, default=None, nullable=False)

    # 添加时间
    create_time = db.Column(db.DateTime, default=datetime.now)

    __mapper_args__ = {
        "order_by": -create_time
    }
