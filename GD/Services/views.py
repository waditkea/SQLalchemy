from flask import Blueprint,jsonify,request,abort,render_template,redirect,url_for
from GD.Services.models import Employee,db


mod=Blueprint("xyz",__name__)

@mod.route("/1",methods=["POST"])
def Create_Employee():#creating table ,
    emp=request.get_json()
    eid=emp["Emp_id"]
    name= emp["Name"]
    address = emp["Address"]
    emp_data=Employee(Emp_id=eid,Name=name,Address=address)
    db.session.add(emp_data)
    db.session.commit()
    # return jsonify(emp_data)
    return "user added"

@mod.route("/2",methods=["GET"])
def fetch_all():
    emp_details=Employee.query.all()#select * from Employee
    # print(emp_details)
    # print(type(emp_details),"for check")
    response=[x.__repr__() for x in emp_details]
    # print(type(response),"for repr")
    return (response)
#
# @mod.route("/3/<int:id>",methods=["GET"])
# def fetch_id(id):
#     emp_details=Employee.query.get(id)#select * from Employee
#     response=emp_details.__repr__()#fetching all the data
#     return response
#
# @mod.route("/4",methods=["GET"])
# def fetch_BY_Nameall():
#     user_name=request.args.get("Name")
#     emp_details=Employee.query.filter(Employee.Name==user_name)#select * from Employee
#     response = [x.__repr__() for x in emp_details]#it will list of matched records
#     return response
#
# @mod.route('/5', methods=['GET'])  # Retrieve user based on username
# def fetch_user_by_name_particular():#if args,compulsory use ? to retrieve data
#     name = request.args.get('Name')  # select * from user where username = username
#     Emp = Employee.query.filter(Employee.Name == name).first()#it will dictionary of fist matched items
#     response = Emp.__repr__()
#     return jsonify(response)
#
# @mod.route("/6/<Name>",methods=["GET"])#retriving data by particular name
# def fetch_all_by_name(Name):
#     emp_details=Employee.query.all()#select * from Employee
#     response=[x.__repr__() for x in emp_details]
#     user_detals=[x for x in response if x["Name"]==Name]
#     return (user_detals)
#
# # @mod.route("/7",methods=["GET"])
# # def fetch_all_second_table():
# #     emp_details=Employee1.query.all()#select * from Employee
# #     print(type(emp_details),"for check")
# #     response=[x.__repr__() for x in emp_details]
# #     print(type(response),"for repr")
# #     return (response)
#
# # @mod.route("/8",methods=["POST"])
# # def Create_Employee_post():#creating table ,
# #     emp=request.get_json()
# #     eid=emp["Emp_id1"]
# #     name= emp["Name1"]
# #     address = emp["Address1"]
# #     emp_data=Employee1(Emp_id1=eid,Name1=name,Address1=address)
# #     db.session.add(emp_data)
# #     db.session.commit()
# #     # return jsonify(emp_data)
# #     return "user added"
#
@mod.route("/9",methods=["POST"])
def Create_Employee_by_form():#creating table ,

    eid=request.form.get("Emp_id")
    name=request.form.get("Name")
    address=request.form.get("Address")
    emp_data=Employee(Emp_id=eid,Name=name,Address=address)
    db.session.add(emp_data)
    db.session.commit()
    # return jsonify(emp_data)
    return "user added"
#
# @mod.route("/10",methods=["POST","GET"])
# def Create_Employee_1():#creating table ,
#     if request.method=="POST":
#         emp=request.get_json()
#         eid=emp["Emp_id"]
#         name= emp["Name"]
#         address = emp["Address"]
#         emp_data=Employee(Emp_id=eid,Name=name,Address=address)
#         db.session.add(emp_data)
#         db.session.commit()
#         # return jsonify(emp_data)
#         return "user added"
#     else:
#         z=Employee.query.all()
#         s=[x.__repr__() for x in z]
#         return s
#
#
# @mod.route("/11/<int:id>",methods=["PUT"])
# def Create_Employee_by_form_1(id):#creating table ,
#     # id=request.get_json()
#     user_data=Employee.query.get(id)
#     name=request.json["Name"]
#     address = request.json["Address"]
#     if user_data is None:
#         abort(404)
#     else:
#         user_data.Name=name
#         user_data.Address = address
#         db.session.add(user_data)
#         db.session.commit()
#         return "user updated"
#
# @mod.route("/12/<int:id>",methods=["PUT"])
# def Create_Employee_by_form_12(id):#creating table ,
#     user_data1=request.get_json()
#     user_data=Employee.query.get(id)
#     # print(user_data)#it creats problem to run program
#     print(type(user_data),"for check")
#     name=user_data1["Name"]
#     address = user_data1["Address"]
#     user_data.Name=name
#     user_data.Address = address
#     db.session.add(user_data)
#     db.session.commit()
#     return "user updated"
#
# @mod.route("/13/<int:id>",methods=["DELETE"])
# def Create_Employee_by_form_13(id):#creating table ,
#     user_data=Employee.query.get(id)
#     db.session.delete(user_data)
#     db.session.commit()
#     return "user updated"
#
# # @mod.route("/home1")
# # def index():
# #     return render_template("index.html")
#
# @mod.route("/form_insert",methods=["GET","POST"])#submit button will directly call this method
# def Create_Employee45():#creating table ,
#     # eid=request.form.get["Emp_id"]#given autoincrement
#     if request.method=="GET":
#         return render_template("index.html")
#     if request.method=="POST":
#
#         name= request.form.get("Name")
#         address = request.form.get("Address")
#         # eid=int(eid)
#         emp_data=Employee(Name=name,Address=address)
#         db.session.add(emp_data)
#         db.session.commit()
#         # return jsonify(emp_data)
#         return "user added"
#
@mod.route("/update_form",methods=["GET","POST"])#submit button will directly call this method
def update_data11():#BROWSER side no delete and put, only allowed methods are get, post
    if request.method=="GET":
        return render_template("update.html")
    if request.method=="POST":
        id=request.form.get("id")
        data=Employee.query.get(id)
        name = request.form.get("name")
        address = request.form.get("Address")
        data.Name=name
        data.Address = address
        # db.session.add(data)
        db.session.commit()
        return "user_updated"

@mod.route("/update_form_name",methods=["GET","POST"])#submit button will directly call this method
def update_data111():#BROWSER side no delete and put, only allowed methods are get, post
    if request.method=="GET":
        return render_template("update.html")
    if request.method=="POST":
        name=request.form.get("name")
        address = request.form.get("Address")
        data=Employee.query.filter_by(Name=name).first()
        # name = request.form.get("name")

        # data.Name=name
        data.Address = address
        # db.session.add(data)
        db.session.commit()
        return "updated"

@mod.route("/update_form_name",methods=["GET","POST"])#submit button will directly call this method
def update_data11111():#BROWSER side no delete and put, only allowed methods are get, post
    if request.method=="GET":
        return render_template("update.html")
    if request.method=="POST":
        name=request.form.get("name")
        address = request.form.get("Address")
        data=Employee.query.filter_by(Name=name).update(dict(Address=address))
        # name = request.form.get("name")
        # data.Name=name
        # data.Address = address
        # db.session.add(data)
        db.session.commit()
        return "updated"

@mod.route("/update_form_name_1",methods=["GET","POST"])#submit button will directly call this method
def update_data111133():#BROWSER side no delete and put, only allowed methods are get, post
    if request.method=="GET":
        return render_template("update.html")#no need to write code, mntion end point in html for method to be called


@mod.route("/delete",methods=["GET"])#submit button will directly call this method
def update_data1111122():#BROWSER side no delete and put, only allowed methods are get, post
    if request.method=="GET":
        user_details=Employee.query.all()
        return render_template("views.html",user_details=user_details)#to display on browser



@mod.route("/delete1/<int:id>")
def Create_Employee_by_form_131(id):#creating table ,
    Employee.query.filter_by(Emp_id=id).delete()
    db.session.commit()
    # return redirect("/delete")#option1 for redirecting
    return redirect(url_for("xyz.update_data1111122"))#option2 for redirecting

@mod.route("/delete2/<int:id>")
def Create_Employee_by_form_1312(id):#creating table ,
    user_details=Employee.query.get(id)
    db.session.delete(user_details)
    db.session.commit()
    # return redirect("/delete")#option1 for redirecting
    return redirect(url_for("xyz.update_data1111122"))#option2 for redirecting



