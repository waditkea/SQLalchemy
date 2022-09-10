#to define database

class Config(object):
    SECRET_KEY="key for application"#can be anyname
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@localhost/Employee_Details"#username,password,host,database
    SQLALCHEMY_TRACK_MODIFICATIONS=False#if true will return in console

class Development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True#i need some changes in python code an save it.then it automatically detect changes where happen and reloading server ..i dont need to restart my server
    SQLALCHEMY_ECHO=True#i need to display the queries executed to generate a page alongside the time each query took for.the we should go for True#it displays raw queries on console
    DEBUG=True
app_config={"development":Development}
