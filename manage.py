from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import app
from exts import db
from models import User,Role,CMSPermission

    #初始化需要执行的数据库相关的终端代码
    # D:\RuanKeTi
    # `python manage.py db init`：初始化一个迁移脚本的环境，只需要执行一次。
    # `python manage.py db migrate`：将模型生成迁移文件，只要模型更改了，就需要执行一遍这个命令。
    # `python manage.py db upgrade`：将迁移文件真正的映射到数据库中。每次运行了`migrate`命令后，就记得要运行这个命令。
    #python manage.py create_role 创建初始的用户角色
    #python manage.py create_user -u developer -p 123456 -e 123@qq.com -r 1 创建初始化开发者用户
'''
本地测试运行
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py create_role
python manage.py create_user -u 徐浩鑫 -p 123456 -e 123@qq.com -r 1 -s 华东师范大学 -a 23 -g 1 -d 18
python manage.py create_user -u 徐浩鑫 -p 123456 -e 1234@qq.com -r 2 -s 华东师范大学 -a 23 -g 1 -d 18
python manage.py create_user -u 曾志通 -p 123456 -e 12345@qq.com -r 3 -s 复兴中学 -a 14 -g 1 -d 8
'''

'''
服务器部署运行
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
python3 manage.py create_role
'''

manager = Manager(app)

# 使用migrate绑定app和db
migrate = Migrate(app=app,db=db)

manager.add_command('db',MigrateCommand)

@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-e','--email',dest='email')
@manager.option('-r','--role_permission',dest='role_permission')
@manager.option('-s','--schoolname',dest='schoolname')
@manager.option('-a','--userage',dest='userage')
@manager.option('-g','--usergender',dest='usergender')
@manager.option('-d','--grade',dest='grade')
def create_user(username,password,email,role_permission,schoolname,userage,usergender,grade):
    user = User(username=username,password=password,email=email,
                role_permission=role_permission,schoolname=schoolname,userage=userage,usergender=usergender,grade=grade)
    db.session.add(user)
    db.session.commit()
    print('用户添加成功！')

@manager.command
def create_role():
    # 1.开发者
    developer = Role(name='开发者管理员',desc='开发人员，拥有最高权限')
    developer.permission = CMSPermission.DEVELOPER
    # 2.教师
    teacher = Role(name='教师',desc='查看学生数据，添加问题')
    teacher.permission = CMSPermission.TEACHER
    # 3.学生
    student = Role(name='学生',desc='学习技能，使用CSits')
    student.permission = CMSPermission.STUDENT

    db.session.add_all([developer,teacher,student])
    db.session.commit()
    print('角色注册成功！')

if __name__ == '__main__':
    manager.run()