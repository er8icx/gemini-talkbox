from flask import Flask,render_template,request,session
from utils import call_gemini
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=="POST":
        prompt=request.form["user_input"]
        response=call_gemini(prompt)
        return render_template("main.html",user_input=prompt,response=response,loading=False)
    return render_template("main.html",loading=False)

if __name__=="__main__":
    app.run(debug=True)