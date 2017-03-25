from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, HiddenField, validators
from wtforms.validators import DataRequired

search_validator = validators.Regexp('^[a-zA-Z0-9\. ]*$', message="Search contains invalid characters.")

class SearchForm(Form):
    search_terms = StringField("search_terms", validators=[search_validator, validators.Length(max=100, message="Search too long."), DataRequired()])
