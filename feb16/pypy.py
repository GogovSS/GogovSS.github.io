from flask import *
app = Flask(__name__)

try:
    with open ('sys.txt','r')as f:
        i = int(f.read())
except:
    i = 0

@app.route('/')
def start():
    res = ''
    for j in range(i):
        with open ('code' + str(j) + '.txt', 'r') as f:
            ff = f.read()
        res += ff + '<br><br>'
    res = res.replace('\n\n','<br>')
    print(res)
    res = res[:-4]
    return f"<a href = '/code' style = 'font-size: 30px'> Ввести новый код</a> <br> <p style = 'font-size:20px; border: 1px solid black; padding: 10px'> {res} </p> <p>"

@app.route('/code',methods = ['get'])
def code():
    return """<form action = '/code', method = 'post'>
    Введите код: <textarea name = 'nm'>  </textarea>
    <input type = 'submit'>
    </form>"""

@app.route('/code',methods = ['post'])
def check():
    global i
    if request.method == "POST":
        nm = request.form.get('nm')
    with open ('code'+str(i)+'.txt','w') as f:
        f.write(nm)
    i = i+1
    with open ('sys.txt','w')as f:
        f.write(str(i))
    return redirect('/')

app.run()
