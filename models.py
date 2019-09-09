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




"""
class Data(db.Model):
    # 数据表格
    __tablename__ = 'data'

    # 数据id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 数据所属用户!!!这个不是变量！仅仅是关系，后面可以调用！
    data_user = db.relationship('User', backref='user_data')

    # 该数据用户id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), default=None, nullable=False)

    # 添加时间
    create_time = db.Column(db.DateTime, default=datetime.now)

    #数据年份
    data_year = db.Column(db.Integer,default = None,nullable=True)

    # 数据所属学校
    schoolname = db.Column(db.String(100), nullable=True)

    # 数据省份
    province = db.Column(db.String(100), default=None, nullable=True)

    # 数据城市
    city = db.Column(db.String(100), default=None, nullable=True)

    # 数据地区
    county = db.Column(db.String(100), default=None, nullable=True)

# 信息化基础环境
    informatization_foundation_environment = db.Column(db.Float)

    # 1.信息化数据中心，数据中心的建设和应用 (data center service)
    data_center = db.Column(db.Float,default = None,nullable=True)

    # 网络接入
        # 2.校园网的建设与应用
    campus_network= db.Column(db.Float, default=None, nullable=True)
        # 3.网络学习空间的建设与应用
    campus_learningspace = db.Column(db.Float, default=None, nullable=True)

# 管理应用和服务系统
    management_application_service_system = db.Column(db.Float)

    # 管理应用和服务系统开发与集成
        # 4.系统开发
    system_development = db.Column(db.Float, default=None, nullable=True)
        # 5.应用集成
    applications_services= db.Column(db.Float, default=None, nullable=True)

    # 6.管理业务流程信息化,电子校务平台的建设与应用
    process_informatization= db.Column(db.Float, default=None, nullable=True)

    # 7.管理信息共享水平,相关数字教育资源平台和机制的建设与应用
    information_sharing= db.Column(db.Float, default=None, nullable=True)

    # 8.综合数据处理与管理决策支持水平,教育管理信息化顶层设计和业务管理信息系统的优化
    management_decision= db.Column(db.Float, default=None, nullable=True)

# 信息化保障体系
    information_security_system = db.Column(db.Float)
    # 信息化组织保障
        # 9.信息技术领导机构
    IT_leader = db.Column(db.Float, default=None, nullable=True)
        # 10.信息化管理部门
    IT_administration = db.Column(db.Float, default=None, nullable=True)
        # 11.IT服务外包管理
    IT_service_outsourcing = db.Column(db.Float, default=None, nullable=True)

    # 信息化人员保障
        # 12.IT人员管理
    IT_workers_manage = db.Column(db.Float, default=None, nullable=True)
        # 13.集中式和分布式IT人员
    IT_centralized_distributed = db.Column(db.Float, default=None, nullable=True)

    # 14.信息化资金保障
    IT_money = db.Column(db.Float, default=None, nullable=True)

    # 信息化制度保障
        # 15.中长期信息化战略规划与发展政策
    IT_plan = db.Column(db.Float, default=None, nullable=True)
        # 16.信息化运维服务管理标准
    IT_operations_maintenance = db.Column(db.Float, default=None, nullable=True)
        # 17.制度化的评估机制
    IT_Assessment = db.Column(db.Float, default=None, nullable=True)


# 信息安全
    information_security = db.Column(db.Float)
    # 网络安全
        # 18.完备的网络设备
    network_equipment = db.Column(db.Float, default=None, nullable=True)
        # 19.网络设备检查机制
    equipment_inspection = db.Column(db.Float, default=None, nullable=True)
        # 20.网络安全应急措施
    network_security= db.Column(db.Float, default=None, nullable=True)

    # 信息内容安全
        # 21.信息备份
    information_backup= db.Column(db.Float, default=None, nullable=True)
        # 22.信息内容安全审核机制
    information_content_security= db.Column(db.Float, default=None, nullable=True)
        # 23.信息安全防护能力
    safety_protection= db.Column(db.Float, default=None, nullable=True)

    # 总分
    all_score = db.Column(db.Float)

    __mapper_args__ = {
        "order_by": -create_time
    }
"""