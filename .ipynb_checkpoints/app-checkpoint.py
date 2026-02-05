import os
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DB_PATH = "event.db"
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# إنشاء فولدر للصور لو مش موجود
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# إنشاء قاعدة البيانات إذا مش موجود
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS participants(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date_of_birth DATE NOT NULL,
        gender TEXT NOT NULL,
        package TEXT NOT NULL,
        phone INTEGER NOT NULL,
        national_id TEXT NOT NULL,
        payment_proof TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

# الصفحة الرئيسية - GET للعرض، POST للتسجيل
@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        name = request.form["name"]
        dob = request.form["date_of_birth"]
        gender = request.form["gender"]
        package = request.form["package"]
        phone = request.form["phone"]
        national_id = request.form["national_id"]
        payment_file = request.files.get("payment_proof")

        # التحقق من الرقم القومي
        if len(national_id) != 14 or not national_id.isdigit():
            message = "الرقم القومي يجب أن يكون 14 رقمًا بالظبط."
        elif not phone.isdigit():
            message = "رقم الهاتف يجب أن يحتوي على أرقام فقط."
        elif package not in ["normal","premium","elite","luxury"]:
            message = "الباكدج غير صحيح."
        else:
            # رفع الصورة إذا موجودة
            if payment_file and payment_file.filename != "":
                filename = payment_file.filename
                payment_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                filename = None

            # تسجيل البيانات في قاعدة البيانات
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute("""
                INSERT INTO participants(name,date_of_birth,gender,package,phone,national_id,payment_proof)
                VALUES (?,?,?,?,?,?,?)
            """, (name,dob,gender,package,phone,national_id,filename))
            conn.commit()
            conn.close()

            # الرسالة بعد التسجيل مع الاسم والباكدج جوا أقواس
            message = f"\u202Bشكراً ({name})! تم تسجيلك في باكدج ({package}) بنجاح."

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
