from flask import Flask,url_for,redirect,render_template,request
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    '''print(request.args)
    print(request.args['name'])
    print(request.args['marks'])'''
    if request.method=='POST':
        print(request.form)
        name=request.form['name']
        m1=int(request.form['m1'])
        physics=int(request.form['phy'])
        ps=int(request.form['ps'])
        total=m1+physics+ps
        '''if m1>=28 and physics >=28 and ps>=28:
            result='passed'
            if 90<=total<=120:
                grade='c'
            elif 121<=total<=150:
                grade='b'
            else:
                grade='a'
        else:
            result='fail'
            grade='f' '''

        return render_template('result.html',name=name,m1=m1,phy=physics,ps=ps,total=total)
    else:
        return render_template('index.html')
app.run(use_reloader=True,debug=True)