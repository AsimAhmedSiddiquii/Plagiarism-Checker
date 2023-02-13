from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PlagForm(FlaskForm):
  checkText = TextAreaField('Copy and paste your text in the box below, then click on the "Check Plagiarism" button.',validators=[DataRequired()])
  submit = SubmitField('🔍 Check Plagiarism')
