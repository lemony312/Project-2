from flask_wtf import Form
from wtforms import TextField, SelectField, RadioField, BooleanField, SubmitField, StringField, TextAreaField, PasswordField, validators, ValidationError, IntegerField, FloatField
from wtforms.validators import InputRequired, EqualTo

class EmailForm(Form):
	customers_email_address = TextField('Email', validators=[InputRequired('Please enter your email.'), validators.Email('Please enter a valid email address.')])
	signup_submit = SubmitField('Sign Up')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)


class SigninForm(Form):
	customers_email_address = TextField('Email', validators=[InputRequired('Please enter your email.'), validators.Email('Please enter a valid email address.')])
	pass_raw = PasswordField('Password', validators=[InputRequired('Please enter your password.')])
	signin_submit = SubmitField('Sign In')
	remember_me = BooleanField('Remember Me', default='checked')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class ForgetPwdForm(Form):
	customers_email_address = TextField('Email', validators=[InputRequired('Please enter your email.'), validators.Email('Please enter a valid email address.')])
	submit = SubmitField('Submit')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class ResetPwdForm(Form):
	customers_email_address = TextField('Email', validators=[InputRequired('Please enter your email.'), validators.Email('Please enter a valid email address.')])
	pass_raw = PasswordField('Password', validators=[InputRequired('Please enter your password.')])
	confirm = PasswordField('Repeat Password', validators=[InputRequired('Passwords must match.'), EqualTo('pass_raw', 'Passwords must match.')])
	pin_num = StringField('PIN', validators=[InputRequired('Please enter the PIN number')])
	reset_submit = SubmitField('Reset')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class QuestionForm(Form):
	age = RadioField('Age', choices=[(18,'below 21'), (23,'21 - 25'), (30,'26 - 35'),
									(40,'36 - 45'), (50,'46 - 55'), (60,'56+')], default=18)
	zip_code = IntegerField('Zipcode', validators=[InputRequired('Please answer the question.')])
	cost = FloatField('Cost', validators=[InputRequired('Please answer the question.')])
	submit = SubmitField('Submit')


	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class RegistrationForm(Form):
	name = TextField("Full Name", validators=[InputRequired('Please enter your full name.')])
	age = IntegerField("Your Age (don't worry we won't tell anyone)", validators=[InputRequired('Please enter your age.')])
	zipcode = IntegerField('Zipcode', validators=[InputRequired('Please enter your zipcode.')])
	cost = FloatField('Cost', validators=[InputRequired('Please enter your dining cost.')])
	# email = TextField("Email", validators=[InputRequired('Please enter your email.'),validators.Email('Please enter a valid email address.')])
	# telephone = TextField("Telephone")
	pass_raw = PasswordField("Set Password", validators=[InputRequired('Please enter your password.'), validators.Length(min=5, message='Password must be minimum 5 characters.')])
	confirm = PasswordField("Confirm Password", validators=[InputRequired('Passwords must match.'), EqualTo('pass_raw', 'Passwords must match.')])
	submit = SubmitField("Get Started!")

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class RedeemForm(Form):
	submit = SubmitField('Redeem')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class SearchForm(Form):
	search_key = TextField('Search Restaurant')
	place = SelectField('Neighborhood',
						choices=[('ALL','Area'),
								('CHELSEA','Chelsea'),
								('EAST VILLAGE','East Village'),
								('GREENWICH VILLAGE','Greenwich Village'),
								('LOWER EAST SIDE', 'Lower East Side'),
								('MIDTOWN EAST','Midtown East'),
								('MIDTOWN SOUTH','Midtown South'),
								('MIDTOWN WEST','Midtown West'),
								('SOHO','Soho'),
								('TRIBECA','Tribeca'),
								('UPPER EAST SIDE','Upper East Side'),
								('UPPER WEST SIDE','Upper West Side'),
								('WEST VILLAGE','West Village'),])
	rank = SelectField('Color', choices=[('All','Color'),('Platinum','Platinum'),('Gold','Gold'),('Silver','Silver'),
								('Bronze','Bronze'),('Blue','Blue')])
	submit = SubmitField('Search')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class AccountForm(Form):
	name = TextField('First Name', validators=[InputRequired('Please enter your name.')])
	email = TextField('Email Adress', validators=[InputRequired('Please enter your email.'),validators.Email('Please enter a valid email address.')])
	telephone = TextField('Telephone', validators=[InputRequired('Please enter your phone number.')])
	pass_old = PasswordField('Password', validators=[InputRequired('Please enter your password.')])
	pass_raw = PasswordField('Change Password', validators=[validators.Length(min=5)])
	confirm = PasswordField('Confirm Password', validators=[EqualTo('pass_raw', 'Passwords must match.')])
	update = SubmitField('Update')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class FeedbackForm(Form):
	name = TextField('Name', validators=[InputRequired('Please enter your name.')])
	email = TextField('E-mail', validators=[InputRequired('Please enter your email.'),validators.Email('Please enter a valid email address.')])
	subject = TextField('Subject', validators=[InputRequired('Please enter the subject')])
	feedback = TextAreaField('Message')
	submit = SubmitField('Send')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class RestaurantSigninForm(Form):
	name = TextField('Username', validators=[InputRequired('Please enter your DinersCode Restaurant ID.')])
	pass_raw = PasswordField('Password', validators=[InputRequired('Please enter your password.')])
	signin_submit = SubmitField('Sign In')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class RestaurantForgetPwdForm(Form):
	name = TextField('Username', validators=[InputRequired('Please enter your DinersCode Restaurant ID.')])
	email = TextField('Email', validators=[InputRequired('Please enter your email.'), validators.Email('Please enter a valid email address.')])
	submit = SubmitField('Submit')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class CustomerSearchForm(Form):
	customer_id = IntegerField('Name', validators=[InputRequired('Please enter the customer\'s ID.')])
	submit = SubmitField('Search')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class RestaurantAccountForm(Form):
	pass_old = PasswordField('Password', validators=[InputRequired('Please enter your current password.')])
	pass_raw = PasswordField('Change Password', validators=[validators.Length(min=5), InputRequired('Please enter your new password.')])
	confirm = PasswordField('Confirm Password', validators=[EqualTo('pass_raw', 'Passwords must match.')])
	update = SubmitField('Update')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)




