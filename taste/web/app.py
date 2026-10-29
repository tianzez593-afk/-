from flask import Flask,request
app = Flask(__name__)
@app.route('/')
def home():
    return  """
    <h1>我的第一个网页</h1>
    <form action="/hello">
       <input name="name" placeholder="输入你的名字">
       <button>提交</button>
    </form>
    """
@app.route("/hello")
def hello():
    name=request.args.get("name","陌生人")
    return f"<h1>你好，{name}!</h1>"
if __name__=="__main__":
    app.run(debug=True)
