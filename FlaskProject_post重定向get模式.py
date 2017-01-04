#coding=utf-8
from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='nibuzhidao'

class NameForm(Form):
    name = StringField(u'你的名字?',validators=[DataRequired()])
    submit = SubmitField(u'提交')


@app.route('/',methods=['POST','GET'] )
def index():
    name=''
    string = u'的页面'
    form=NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        # print session['name']
        return redirect(url_for('index'))
        # form.name.data = ''

    return render_template('index.html', string=string,form=form,name=session.get('name'))

@app.route('/add',methods=['POST',])
def add():
    pass


if __name__ == '__main__':
    app.run()
