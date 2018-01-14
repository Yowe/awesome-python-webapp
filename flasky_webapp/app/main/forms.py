from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(Form):
    name = StringField('请输入名称：', validators=[DataRequired()])
    submit = StringField('Submit')