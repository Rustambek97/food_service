from flask import Flask, render_template, request, redirect, session
from database.db import mydb
app = Flask(__name__)

app.secret_key = "123456789"

@app.route('/')
def Home():
    return render_template("home.html")

@app.route('/menulist')
def menulist():
    foodlist = mydb.foodlist()
    # foodprice = []
    # for food in foodlist:
    #     a = mydb.foodprice(food[0])
    #     foodprice.append(a)

    return render_template("menu/menulist.html", foodlist=foodlist)

@app.route("/detail/<id>/<nomi>/")
def menudetail(id, nomi):
    ovqat = mydb.menudetail(id)
    return render_template("menu/menudetail.html", ovqat=ovqat, nomi=nomi)


@app.route("/savatcha/")
def savatcha():
    zakazlar = mydb.savatcha()
    return render_template("zakaz/savatcha.html", zakazlar=zakazlar)

@app.route("/addsavat/<ovqatid>/")
def addsavat(ovqatid):
    pass

@app.route("/user/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("users/login.html", xato=None)
    elif request.method == 'POST':
        log = request.form['login']
        parol = request.form['parol']

        user = mydb.check_user(log, parol)
        if user:
            session['username'] = user[3]
            return redirect("/")
        else:
            return render_template("users/login.html", xato="login yoki parol xato")


@app.route("/user/registration/", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        ism = request.form['ism']
        familiya = request.form['familiya']
        login = request.form['login']
        parol = request.form['parol']

        mydb.adduser(ism, familiya, login, parol)
        return redirect('/')

    elif request.method == 'GET':
        return render_template("users/register.html")

if __name__=="__main__":
    app.run(debug=True)