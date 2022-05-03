# ★★★★★定型文★★★★★
import sqlite3
from flask import Flask, render_template,request,redirect, session
import flask
# Flaskのインポート

app = Flask(__name__)
# アンダーバー2つ

# sessionを使うには、secret_keyが必要
app.secret_key="sunabaco"
# ★★★★★★★★★★★★★★★


# ★★★★★質問追加★★★★★
@app.route("/add")
def add_get():
    return render_template("add.html")

@app.route("/add",methods=["POST"])
def add_post():
    # HTMLから送られてきたデータを取得、変数flaskに格納
    task=request.form.get("tpl_task")
    # DBにテータを追加
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    # 情報が一個の時は、カンマを入れる
    c.execute("insert into task values(null,?,?)",(task,0))
    # 情報を書き込み
    conn.commit()
    # DBを閉じる
    c.close()
    # ホームページにリダイレクト
    return redirect("/list")

@app.route("/list")
def list():
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    c.execute("SELECT * FROM task WHERE flag=0")
    # 配列に格納
    task_list_py=[]
    # 辞書型に追加
    for row in c.fetchall():
        task_list_py.append({"tpl_id":row[0],"tpl_task":row[1],"tpl_flag":row[2]})
    # DBを閉じる
    c.close()
    # task_list_pyを出力
    print("ここからテストプリントです")
    print(task_list_py)
    # HTMLに渡す
    return render_template("list.html",tpl_task_list=task_list_py)
    # テスト用記述 breakpoint() そこから先は実行されません
# ★★★★★★★★★★★★★★★


# ★★★★★Q&Aリスト★★★★★
@app.route("/QAlist")
def QAlist():
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    c.execute("SELECT * FROM task WHERE NOT flag=0")
    # 配列に格納
    task_list_py=[]
    # 辞書型に追加
    for row in c.fetchall():
        task_list_py.append({"tpl_id":row[0],"tpl_task":row[1],"tpl_flag":row[2]})
    # DBを閉じる
    c.close()
    # HTMLに渡す
    return render_template("Q&Alist.html",tpl_task_list=task_list_py)
# ★★★★★★★★★★★★★★★


# ★★★★★Aリスト★★★★★
@app.route("/alist/<int:id>")
def alist(id):
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    c.execute("SELECT * FROM answer WHERE question_id=?",(id,))
    # 配列に格納
    task_list_py=[]
    # 辞書型に追加
    for row in c.fetchall():
        task_list_py.append({"tpl_id":row[0],"tpl_answer":row[1],"tpl_question_id":row[2]})
    # DBを閉じる
    c.close()
    # HTMLに渡す
    return render_template("Alist.html",tpl_task_list=task_list_py)
# ★★★★★★★★★★★★★★★


# ★★★★★回答★★★★★
@app.route("/answer/<int:id>")
# idを受け取り
def answer_get(id):
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    c.execute("SELECT task FROM task WHERE id=?",(id,))
    # DBからデータを取得
    task=c.fetchone()
    task=task[0]
    # DBを閉じる
    c.close()
    # 配列に格納
    global item
    item={"tpl_id":id,"tpl_task":task}
    return render_template("answer.html",tpl_task=item)

@app.route("/answer",methods=["POST"])
def answer_post():
    # HTMLから送られてきたデータを取得、変数flaskに格納
    answer=request.form.get("tpl_answer")
    # DBにテータを追加
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    c.execute("insert into answer values(null,?,?)",(answer,item["tpl_id"]))
    c.execute("UPDATE task SET flag = flag + 1 WHERE id=?",(item["tpl_id"],))
    # 情報を書き込み
    conn.commit()
    # DBを閉じる
    c.close()
    # ホームページにリダイレクト
    return redirect("/list")

@app.route("/aanswer/<int:id>")
# idを受け取り
def aanswer_get(id):
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    c.execute("SELECT task FROM task WHERE id=?",(id,))
    # DBからデータを取得
    task=c.fetchone()
    task=task[0]
    # DBを閉じる
    c.close()
    # 配列に格納
    global aitem
    aitem={"tpl_id":id,"tpl_task":task}
    return render_template("aanswer.html",tpl_task=aitem)

@app.route("/aanswer",methods=["POST"])
def aanswer_post():
    # HTMLから送られてきたデータを取得、変数flaskに格納
    answer=request.form.get("tpl_answer")
    # DBにテータを追加
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    c.execute("insert into answer values(null,?,?)",(answer,aitem["tpl_id"]))
    c.execute("UPDATE task SET flag = flag + 1 WHERE id=?",(aitem["tpl_id"],))
    # 情報を書き込み
    conn.commit()
    # DBを閉じる
    c.close()
    # ホームページにリダイレクト
    return redirect("/QAlist")
# ★★★★★★★★★★★★★★★


# # ★★★★★編集★★★★★
# @app.route("/edit/<int:id>")
# # idを受け取り
# def edit(id):
#     # DBに接続
#     conn=sqlite3.connect("flask.db")
#     # SQL文を実行
#     c=conn.cursor()
#     c.execute("SELECT task FROM task WHERE id=?",(id,))
#     # DBからデータを取得
#     task=c.fetchone()
#     task=task[0]
#     # DBを閉じる
#     c.close()
#     # 配列に格納
#     item={"tpl_id":id,"tpl_task":task}
#     return render_template("edit.html",tpl_task=item)
#     # answer.htmlを作成 idとtaskを受け取り、編集できるようにする

# @app.route("/edit",methods=["POST"])
# def edit_post():
#     # htmlから送られてきたidを取得、変数task_idに格納
#     item_id=request.form.get("task_id")
#     item_id=int(item_id)
#     # htmlから送られてきたデータを取得、変数taskに格納
#     task=request.form.get("task_input")
#     # DBに接続
#     conn=sqlite3.connect("flask.db")
#     # SQL文を実行
#     c=conn.cursor()
#     # 受け取った情報をもとにtaskテーブルを書き換えるSQL
#     c.execute("UPDATE task SET task=? WHERE id=?",(task,item_id))
#     conn.commit()
#     c.close()
#     return redirect("/list")
# # ★★★★★★★★★★★★★★★


# ★★★★★削除★★★★★
@app.route("/delete/<int:id>",methods=["POST"])
def delete_post(id):
    print(id)
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    # 指定したidのtask削除
    c.execute("DELETE FROM task WHERE id=?",(id,))
    conn.commit()
    c.close()
    return redirect("/list")
# ★★★★★★★★★★★★★★★

# ★★★★★QA削除★★★★★
@app.route("/QAdelete/<int:id>",methods=["POST"])
def QAdelete_post(id):
    print(id)
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    # 指定したidのtask削除
    c.execute("DELETE FROM task WHERE id=?",(id,))
    conn.commit()
    c.close()
    return redirect("/QAlist")
# ★★★★★★★★★★★★★★★

# ★★★★★A削除★★★★★
@app.route("/adelete/<int:id>",methods=["POST"])
def adelete_post(id):
    print(id)
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    # 指定したidのtask削除
    c.execute("SELECT question_id FROM answer WHERE id=?",(id,))
    # DBからデータを取得
    task=c.fetchone()
    task=task[0]
    print("タスクテストプリント")
    print(task)
    c.execute("DELETE FROM answer WHERE id=?",(id,))
    c.execute("UPDATE task SET flag = flag - 1 WHERE id=?",(task,))
    conn.commit()
    c.close()
    return redirect("/alist/"+str(task))
# ★★★★★★★★★★★★★★★


# ★★★★★定型文★★★★★
# エラーハンドラー
@app.errorhandler(404)
def page_not_found(error):
    return 'ないよ！', 404

if __name__=="__main__":
    app.run(debug=True)
# ★★★★★★★★★★★★★★★