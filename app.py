from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

# ホームページ
@app.route('/')
def home():
    return render_template('home.html')

# 登録ページ
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        employee_name = request.form['employee_name']
        
        # 従業員IDがユニークかどうかをチェックする
        if Employee.query.filter_by(id=employee_id).first():
            return "社員IDはすでに存在します。別のIDを選択してください。"

        new_employee = Employee(id=employee_id, name=employee_name)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('employee_list'))
    
    return render_template('register.html')


# 掲載ページ
@app.route('/list')
def employee_list():
    employees = Employee.query.all() # 登録されている全従業員を取得する
    return render_template('list.html', employees=employees)

# 編集ページ
@app.route('/edit/<string:employee_id>', methods=['GET', 'POST']) # url から id を渡す
def edit_employee(employee_id):
    employee = Employee.query.get(employee_id)
    print(">>>>>>>>>", employee) # 従業員がいればチェックする
    if not employee:
        return "従業員が見つかりません", 404

    if request.method == 'POST':
        employee.name = request.form['employee_name']
        db.session.commit()
        return redirect(url_for('employee_list'))

    return render_template('edit.html', employee=employee)

# 削除ページ
@app.route('/delete/<string:employee_id>')
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id) # url から id で従業員を取得
    if not employee:
        return "<h1> 従業員が見つかりません </h1>", 404

    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('employee_list'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
