from flask import jsonify
from GD import db

class Employee(db.Model):#calling model method from class SQLAlchemy(),table name shoulf be same as class nae
    __tablename__="Employee"
    Emp_id=db.Column(db.Integer,primary_key=True)
    Name= db.Column(db.String(45),nullable=False,unique=True)
    Address= db.Column(db.String(100),nullable=False)

    def __repr__(self):#converts object into string format
        return {"Emp_id":self.Emp_id,"Name":self.Name,"Address":self.Address}

# class Employee1(db.Model):#calling model method from class SQLAlchemy(),table name shoulf be same as class nae
#     __tablename__ = "Employee_lmn"
#     Emp_id1=db.Column(db.Integer,primary_key=True)
#     Name1= db.Column(db.String(45),nullable=False,unique=True)
#     Address1= db.Column(db.String(100),nullable=False)

    # def __repr__(self):#converts object into string format
    #     return {"Emp_id":self.Emp_id1,"Name":self.Name1,"Address":self.Address1}