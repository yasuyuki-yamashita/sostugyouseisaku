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
    c.execute("insert into task values(null,?)",(task,))
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
    c.execute("SELECT id,task FROM task")
    # 配列に格納
    task_list_py=[]
    # 辞書型に追加
    for row in c.fetchall():
        task_list_py.append({"tpl_id":row[0],"tpl_task":row[1]})
    # DBを閉じる
    c.close()
    # task_list_pyを出力
    print(task_list_py)
    # HTMLに渡す
    return render_template("list.html",tpl_task_list=task_list_py)
    # テスト用記述 breakpoint() そこから先は実行されません
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
    print("ここに表示するよ")
    print(id)
    # DBにテータを追加
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    # 情報が一個の時は、カンマを入れる
    c.execute("insert into answer values(null,?,?)",(answer,item["tpl_id"]))
    # 情報を書き込み
    conn.commit()
    # DBを閉じる
    c.close()
    # ホームページにリダイレクト
    return redirect("/list")

# @app.route("/Q&Alist")
# def QAlist():
#     # DBに接続
#     conn=sqlite3.connect("flask.db")
#     # SQL文を実行
#     c=conn.cursor()
#     c.execute("SELECT id,task FROM answer")
#     c.execute("SELECT id,task FROM task")
#     # 配列に格納
#     task_list_py=[]
#     answer_list_py=[]

    # # 辞書型に追加
    # for row in c.fetchall():
    #     task_list_py.append({"tpl_id":row[0],"tpl_task":row[1]})
    #     answer_list_py.append({"tpl_id":row[0],"tpl_answer":row[1]})
    # # DBを閉じる
    # c.close()
    # # task_list_pyを出力
    # print(task_list_py)
    # print(answer_list_py)
    # # HTMLに渡す
    # return render_template("Q&Alist.html",tpl_task_list=task_list_py,tpl_answer_list=answer_list_py)
    # # テスト用記述 breakpoint() そこから先は実行されません
# ★★★★★★★★★★★★★★★


# ★★★★★編集★★★★★
@app.route("/edit/<int:id>")
# idを受け取り
def edit(id):
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
    item={"tpl_id":id,"tpl_task":task}
    return render_template("edit.html",tpl_task=item)
    # answer.htmlを作成 idとtaskを受け取り、編集できるようにする

@app.route("/edit",methods=["POST"])
def edit_post():
    # htmlから送られてきたidを取得、変数task_idに格納
    item_id=request.form.get("task_id")
    item_id=int(item_id)
    # htmlから送られてきたデータを取得、変数taskに格納
    task=request.form.get("task_input")
    # DBに接続
    conn=sqlite3.connect("flask.db")
    # SQL文を実行
    c=conn.cursor()
    # 受け取った情報をもとにtaskテーブルを書き換えるSQL
    c.execute("UPDATE task SET task=? WHERE id=?",(task,item_id))
    conn.commit()
    c.close
    return redirect("/list")
# ★★★★★★★★★★★★★★★


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
    c.close
    return redirect("/list")
# ★★★★★★★★★★★★★★★


# ★★★★★定型文★★★★★
# エラーハンドラー
@app.errorhandler(404)
def page_not_found(error):
    return 'ないよ！', 404

if __name__=="__main__":
    app.run(debug=True)
# ★★★★★★★★★★★★★★★