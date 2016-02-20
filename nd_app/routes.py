from nd_app import app
from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify
from datetime import datetime, timedelta
from flask.ext.mail import Message, Mail
from nd_app.models import db, Customers, CustomersInfo, Restaurants, RstrntGall, RstrntCateg, ZipcodeIncome, RedeemInfo, RatingInfo
from nd_app.forms import SigninForm, ForgetPwdForm, ResetPwdForm, QuestionForm, RedeemForm, SearchForm, EmailForm, AccountForm, FeedbackForm, RegistrationForm, CustomerSearchForm, RestaurantAccountForm, RestaurantSigninForm, RestaurantForgetPwdForm
from nd_app.searchfunc import show_restaurants, filter_restaurants ,show_p_restaurants
from operator import attrgetter
import string
import random
import time
import pytz

try:
    import urllib3.contrib.pyopenssl
    urllib3.contrib.pyopenssl.inject_into_urllib3()
except ImportError:
    pass

mail = Mail()

DATA_MAX = 12

YELP_MAX = 5
AGE_FACTOR = 4
USA_MEDIAN_INCOME = 53046
INCOME_FACTOR = 0.0022222222
BUDGET_FACTOR = 5
RESTAURANT_DEFAULT_PASSWORD = 'restaurant'
HIGHEST_SCORE = 750
HIGHER_SCORE = 600
MIDDLE_SCORE = 450
LOWER_SCORE = 300

#error message
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found."

@app.route('/contact', methods=['GET'])
def contact():
	return render_template('contact.html')

@app.route('/faq', methods=['GET'])
def faq():
	return render_template('faq.html')

@app.route('/confirmation', methods=['GET'])
def confirmation():

	if 'visitor_email_address' not in session:
		return redirect(url_for('index'))

	return render_template('confirmation.html')

@app.route('/privacypolicy', methods=['GET'])
def privacypolicy():
	return render_template('privacypolicy.html')

@app.route('/terms', methods=['GET'])
def terms():
	return render_template('terms.html')

@app.route("/", methods=['GET','POST'])
def index():

	# if 'pass' in session:
	# 	return return_for_ios('redirect_to_home', is_ios)

	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = EmailForm()

 	is_ios = True if request.args.get('ios', None) else False  # for ios app

	if request.method == 'POST':
		customer = Customers.query.filter_by(customers_email_address = form.customers_email_address.data).first()
		if customer is None:
			#add new email into database
			newcustomer = Customers('', '', form.customers_email_address.data,
									'', '', '','',
									'', '', '', '', '', '', 0, 0, '', 0, present,present,0,0,0,0,0,0,0)

			db.session.add(newcustomer)
			db.session.commit()
			newcustomerinfo = CustomersInfo(newcustomer.customers_id, present, 1, present, present)
			db.session.add(newcustomerinfo)
			db.session.commit()

			session['visitor_email_address'] = form.customers_email_address.data

			return return_for_ios("register.html", is_ios)
		elif not customer.zipcode:
			# user haven't filled out question form
			session['visitor_email_address'] = form.customers_email_address.data
			return return_for_ios("register.html", is_ios)
		else:
			return return_for_ios("register_error_1", is_ios) #That email is already taken.
	elif request.method == 'GET':
		return render_template('index.html', form=form)

@app.route("/fb1", methods=['GET','POST'])
def fb1():
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = EmailForm()

	if request.method == 'POST':
		customer = Customers.query.filter_by(customers_email_address = form.customers_email_address.data).first()
		if customer is None:
			#add new email into database
			newcustomer = Customers('', '', form.customers_email_address.data,
									'', '', '','',
									'', '', '', '', '', '', 0, 0, '', 0, present,present,0,0,0,0,0,0,0)

			db.session.add(newcustomer)
			db.session.commit()
			newcustomerinfo = CustomersInfo(newcustomer.customers_id, present, 1, present, present)
			db.session.add(newcustomerinfo)
			db.session.commit()

			session['visitor_email_address'] = form.customers_email_address.data

			return "questions.html"

		else:
			return "register_error_1" #That email is already taken.
	elif request.method == 'GET':
		return render_template('fb1.html', form=form)

@app.route("/fb2", methods=['GET','POST'])
def fb2():
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = EmailForm()

	if request.method == 'POST':
		customer = Customers.query.filter_by(customers_email_address = form.customers_email_address.data).first()
		if customer is None:
			#add new email into database
			newcustomer = Customers('', '', form.customers_email_address.data,
									'', '', '','',
									'', '', '', '', '', '', 0, 0, '', 0, present,present,0,0,0,0,0,0,0)

			db.session.add(newcustomer)
			db.session.commit()
			newcustomerinfo = CustomersInfo(newcustomer.customers_id, present, 1, present, present)
			db.session.add(newcustomerinfo)
			db.session.commit()

			session['visitor_email_address'] = form.customers_email_address.data

			return "questions.html"

		else:
			return "register_error_1" #That email is already taken.
	elif request.method == 'GET':
		return render_template('fb2.html', form=form)

@app.route("/fb3", methods=['GET','POST'])
def fb3():
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = EmailForm()

	if request.method == 'POST':
		customer = Customers.query.filter_by(customers_email_address = form.customers_email_address.data).first()
		if customer is None:
			#add new email into database
			newcustomer = Customers('', '', form.customers_email_address.data,
									'', '', '','',
									'', '', '', '', '', '', 0, 0, '', 0, present,present,0,0,0,0,0,0,0)

			db.session.add(newcustomer)
			db.session.commit()
			newcustomerinfo = CustomersInfo(newcustomer.customers_id, present, 1, present, present)
			db.session.add(newcustomerinfo)
			db.session.commit()

			session['visitor_email_address'] = form.customers_email_address.data

			return "questions.html"

		else:
			return "register_error_1" #That email is already taken.
	elif request.method == 'GET':
		return render_template('fb3.html', form=form)

def return_for_ios(data, is_ios):

	if not is_ios:
		web_map = {'redirect_to_home': redirect(url_for('home')),
							 'redirect_to_index': redirect(url_for('index')),
							 'rstpwd_success': "<div align='center'><p>Your password has been reset.<br>Please <a href='/login'>click</a> here to login.</p></div>",
							 'feedback_success': "<p>Thank you for reaching out to us. We'll get back to you shortly.</p><br><br><br><br><br><br><br><br><br><br><br><br>"
							 }
		return web_map[data] if data in web_map else data

	""" Choose what to return based on is_ios.
	If is_ios is True, return the corresponding results to client
	"""
	ios_map = {'home.html': jsonify({'data': 'success'}),
				 'register.html': jsonify({'data': 'success'}),
				 'rstpwd.html': jsonify({'data': 'success'}),
				 'rstpwd_success': jsonify({'data': 'success'}),
				 'feedback_success': jsonify({'data': 'success'}),
				 'redeem': jsonify({'data': 'success'}),
				 'redirect_to_home': jsonify({'data': 'logged_in'}),
				 'redirect_to_index': jsonify({'data': 'not_logged_in'}),
				 'login_error_2': (jsonify({'data': 'invalid_pwd'}), 401),
				 'login_error_1': (jsonify({'data': 'invalid_email'}), 401),
				 'rstpwd_error_1': (jsonify({'data': 'invalid'}), 401),
				 'rstpwd_error_2': (jsonify({'data': 'invalid'}), 401),
				 'fgpwd_error_1': (jsonify({'data': 'invalid'}), 400),
				 'register_error_1': (jsonify({'data': 'invalid'}), 400),
			   	 'account_updated': (jsonify({'data': 'update'}))
				 }

	if is_ios and data in ios_map:
		return ios_map[data]

@app.route('/login', methods=['GET', 'POST'])
def login():
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = SigninForm()

	is_ios = True if request.args.get('ios', None) else False  # for ios app

	# if 'pass' in session:
	# 	return return_for_ios('redirect_to_home', is_ios)

	if request.method == 'POST':
		customer = Customers.query.filter_by(customers_email_address = form.customers_email_address.data).first()
		if customer:
			if not customer.score or not customer.customers_password:
				session['visitor_email_address'] = form.customers_email_address.data
				return "register.html"
			if customer.check_password(form.pass_raw.data):
				session['customers_email_address'] = form.customers_email_address.data
				customer = Customers.query.filter_by(customers_email_address = form.customers_email_address.data).first()
				customerinfo = CustomersInfo.query.filter_by(customers_info_id = customer.customers_id).first()
				session['pass'] = True

				customerinfo.customers_info_date_of_last_logon = present
				customerinfo.customers_info_number_of_logons = customerinfo.customers_info_number_of_logons + 1
				customerinfo = db.session.merge(customerinfo)
				db.session.commit()

				if form.remember_me.data:
					session.permanent = True
				else:
					session.permanent = False

				return return_for_ios('home.html', is_ios)
			return return_for_ios("login_error_2", is_ios) #Invalid password.

		return return_for_ios("login_error_1", is_ios) #Invalid email.
	elif request.method == 'GET':
		return render_template('login.html', form=form), is_ios

@app.route('/fgpwd', methods=['GET', 'POST'])
def fgpwd():
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = ForgetPwdForm()
	is_ios = True if request.args.get('ios', None) else False  # for ios app

	if request.method == 'POST':
		customer = Customers.query.filter_by(customers_email_address = form.customers_email_address.data).first()
		if customer:
			if not customer.score:
				session['visitor_email_address'] = form.customers_email_address.data
				return "register.html"
            #generate PIN
			pin = ''.join(random.choice(string.digits) for _ in range(6))
            #send change password email
			msg = Message("DinersCode - New Password", sender=('DinersCode \xF0\x9F\x8D\xB7','contact@dinerscode.com'), recipients=[form.customers_email_address.data])
			msg.html = """
			<p style="font-family: Georgia, Times, 'Times New Roman', serif; color: #404040"><br>
			A new password has been requested for your account at DinersCode.<br>
			<br>
			Please use the below Pin to securely change your password:</b>.<br>
			<br>
			%s<br>
			<br>
			This Pin will be automatically discarded after 24 hours or after your password has been changed.<br>
			<br>
			For help with any of our online services, please email the Administrator : contact@dinerscode.com.<br>
			<br>
			--<br><br>
			Sincerely,<br><br>
			DinersCode<br><br>
			<br>
			</p>
			<a href="http://www.dinerscode.com" target="_blank" ><img src="http://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-link-48.png" height="24" width="24" style="PADDING-RIGHT:10px;PADDING-LEFT:10px"></a>
			<a href="http://www.facebook.com/dinerscode" target="_blank" ><img src="http://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-facebook-48.png" height="24" width="24" style="PADDING-RIGHT:10px;PADDING-LEFT:10px"></a>
			<a href="mailto:contact@dinerscode.com" target="_blank" ><img src="http://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-forwardtofriend-48.png" height="24" width="24" style="PADDING-RIGHT:10px;PADDING-LEFT:10px"></a>
			"""  % (pin)
			mail.send(msg)
			#add new PIN to database
			session['email'] = form.customers_email_address.data
			customer = Customers.query.filter_by(customers_email_address = form.customers_email_address.data).first()
			customerinfo = CustomersInfo.query.filter_by(customers_info_id = customer.customers_id).first()
			customerinfo.password_reset_key = pin
			customerinfo.password_reset_date = present
			customerinfo = db.session.merge(customerinfo)
			db.session.commit()
			return return_for_ios("rstpwd.html", is_ios)
		else:
			return return_for_ios("fgpwd_error_1", is_ios) #Email not found in database.
	elif request.method == 'GET':
		return render_template('fgpwd.html', form=form)

@app.route('/rstpwd', methods=['GET', 'POST'])
def rstpwd():
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = ResetPwdForm()
	is_ios = True if request.args.get('ios', None) else False  # for ios app

	# if 'email' not in session:
	# 	return redirect(url_for('fgpwd'))

	if request.method == 'POST':
		customer = Customers.query.filter_by(customers_email_address = form.customers_email_address.data).first()
		customerinfo = CustomersInfo.query.filter_by(customers_info_id = customer.customers_id).first()
		if (customerinfo.password_reset_key == form.pin_num.data):
			if (present - customerinfo.password_reset_date < timedelta(days=1)):
				customer.pass_raw = form.pass_raw.data
				customer.set_password(form.pass_raw.data)
				customer = db.session.merge(customer)
				customerinfo.password_reset_key = None
				customerinfo.customers_info_date_account_last_modified = present
				customerinfo = db.session.merge(customerinfo)
				db.session.commit()
				session.pop('email', None)
				return return_for_ios('rstpwd_success', is_ios)
			else:
				return return_for_ios("rstpwd_error_1", is_ios) #The PIN number has expired.
		else:
			return return_for_ios("rstpwd_error_2", is_ios) #The PIN number doesn't match.
	elif request.method == 'GET':
		return render_template('rstpwd.html', form=form)

@app.route('/questions', methods=['GET', 'POST'])
def questions():
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = QuestionForm()

	if 'visitor_email_address' not in session:
		return redirect(url_for('index'))

	if request.method == 'POST':
		customer = Customers.query.filter_by(customers_email_address = session['visitor_email_address']).first()

		#add new info to database
		customer.zipcode = form.zip_code.data
		customer.age = form.age.data
		customer.budget = form.cost.data

		age_score = float(form.age.data) * AGE_FACTOR
		zipcode_income = ZipcodeIncome.query.filter_by(zip_code = str(form.zip_code.data)).first()
		if zipcode_income is None:
			zipcode_score = USA_MEDIAN_INCOME * INCOME_FACTOR
		else:
			zipcode_score = float(zipcode_income.median_income) * INCOME_FACTOR
		budget_score = float(form.cost.data) * BUDGET_FACTOR
		customer.score = age_score + zipcode_score + budget_score

		customer.modified = present
		customer = db.session.merge(customer)
		db.session.commit()

		#send greeting email
		msg = Message("Welcome to DinersCode", sender=('DinersCode \xF0\x9F\x8D\xB7','contact@dinerscode.com'), recipients=[customer.customers_email_address])
		msg.html = """
		<p style="font-family: Georgia, Times, 'Times New Roman', serif; color: #404040">
		Welcome to <b>DinersCode</b>.<br>
		<br>
		Your new DinersCode account log-in email is: %s<br>
		<br>
		Please click the link below and set the password for your account.
		<br>
		http://www.dinerscode.com/register<br>
		<br>
		The more you dine, the more perks you get! The perks we offer are privileges for diners who are bona-fide participants of our diners' community. You will be able to see more perks in the future by avoiding no-shows and being a great customer at the eateries.<br>
		<br>
		--<br><br>
		Sincerely,<br><br>
		DinersCode<br><br>
		<br>
		</p>
		<a href="http://www.dinerscode.com" target="_blank" ><img src="http://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-link-48.png" height="24" width="24" style="PADDING-RIGHT:10px;PADDING-LEFT:10px"></a>
		<a href="http://www.facebook.com/dinerscode" target="_blank" ><img src="http://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-facebook-48.png" height="24" width="24" style="PADDING-RIGHT:10px;PADDING-LEFT:10px"></a>
		<a href="mailto:contact@dinerscode.com" target="_blank" ><img src="http://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-forwardtofriend-48.png" height="24" width="24" style="PADDING-RIGHT:10px;PADDING-LEFT:10px"></a>
		"""  % (customer.customers_email_address)
		mail.send(msg)

		return "confirmation.html"

	elif request.method == 'GET':
		return render_template('questions.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = RegistrationForm()

	if request.method == 'POST':
		is_ios = True if request.args.get('ios', None) else False
		customer = Customers.query.filter_by(customers_email_address = session['visitor_email_address']).first()
		if customer:
			fullname = form.name.data.strip().split(' ')
			customer.customers_firstname = fullname[0]
			if len(form.name.data) > 1:
				customer.customers_lastname = fullname[-1]
			customer.age = form.age.data
			customer.zipcode = form.zipcode.data
			customer.budget = form.cost.data

			# calculate score
			age_score = float(form.age.data) * AGE_FACTOR
			zipcode_income = ZipcodeIncome.query.filter_by(zip_code = str(form.zipcode.data)).first()
			if zipcode_income is None:
				zipcode_score = USA_MEDIAN_INCOME * INCOME_FACTOR
			else:
				zipcode_score = float(zipcode_income.median_income) * INCOME_FACTOR
			budget_score = float(form.cost.data) * BUDGET_FACTOR
			customer.score = age_score + zipcode_score + budget_score

			new_pwd = form.pass_raw.data
			customer.set_password(new_pwd)

			customer.modified = present
			customer = db.session.merge(customer)
			db.session.commit()

			session['customers_email_address'] = session['visitor_email_address']
			session['pass'] = True

			return return_for_ios("home.html", is_ios)

		else:
			return return_for_ios("login_error_1", is_ios) #Invalid email.

	elif request.method == 'GET':
		customer = None
		customer_found = False
		if 'visitor_email_address' in session:
			customer = Customers.query.filter_by(customers_email_address = session['visitor_email_address']).first()
			if customer:
				customer_found = True
		else:
			return redirect(url_for('index'))

		return render_template('register.html', form=form, user=customer, customer_found=customer_found)


@app.route("/favorites", methods=['GET', 'POST'])
def favorites():
	return home()

def generateList(customer_score):
	seed_number = random.randrange(100)
	session['rest_seed_number'] = seed_number
	print seed_number, "first time"
	if 'area' not in session:
		restaurants = filter_restaurants(customer_score, seed_number)
		#restaurants = show_restaurants(customer.score, seed_number, limit=DATA_MAX)
		session['prev_area'] = 'ALL'
		session['prev_rank'] = 'All'

	else:
		area = session['area']
		rank = session['rank']

		restaurants = filter_restaurants(customer.score, seed_number, area=area, rank=rank, search_key=search_key)
		#restaurants = show_restaurants(customer.score, seed_number, limit=DATA_MAX, area=area, rank=rank, search_key=search_key)
		session['prev_area'] = area
		session['prev_rank'] = rank

	session['restaurants'] = []
	for restaurant in restaurants:
		rstrnt = []

		rstrntgall = RstrntGall.query.filter_by(restaurant_id = restaurant.id).first()
		if rstrntgall is None:
			rstrntgall = [RstrntGall.query.filter_by(id = 1).first()]
			rstrntgall[0].uploaded_file = "default.jpg"

		rstrnt.append(restaurant)
		rstrnt.append(rstrntgall)
		session['restaurants'].append(rstrnt)	

###### Diner Account Page ######
@app.route("/home", methods=['GET', 'POST'])
def home():
	form = SearchForm()
	is_ios = True if request.args.get('ios', None) else False  # for ios app

	# if 'customers_email_address' not in session or 'pass' not in session:
	# 	return return_for_ios('redirect_to_index', is_ios)
	#if 'offset' not in session:
	#	session['offset'] = 0

	#print "Everytime we render", session['offset']

		
	customer = Customers.query.filter_by(customers_email_address = session['customers_email_address']).first()
	customer_id = "%05d" % (customer.customers_id)
	need_seemore_tab = True

	if request.method == 'POST':
		if request.args.get('search', None):
			session['area'] = form.place.data
			session['rank'] = form.rank.data
			session['search_key'] = form.search_key.data
		if request.args.get('see_more', None):
			session['offset'] = session['offset'] + DATA_MAX
			print "Everytime we hit see_more", session['offset']
			session['see_more'] = True
	else: 
		session['offset'] = 0
		session['see_more'] = False
		print "when we restart this page", session['offset']

	search_key = session['search_key'] if 'search_key' in session else ''

	if 'see_more' in session and session['see_more']:
		seed_number = session['rest_seed_number'] if 'rest_seed_number' in session else 1
		print "second time and number of offset", session['offset']
		if 'area' not in session:
			#restaurant = show_p_restaurants(session['restaurants'],offset = session['offset'], limit = session['offset']+DATA_MAX)
			restaurants = show_restaurants(customer.score, seed_number,offset = session['offset'], limit = session['offset']+DATA_MAX)
			session['prev_area'] = 'ALL'
			session['prev_rank'] = 'All'

		else:
			area = session['area']
			rank = session['rank']
			#restaurants = show_p_restaurants(session['restaurants'], offset = session['offset'], limit = session['offset']+DATA_MAX, area=area, rank=rank, search_key=search_key)
			restaurants = show_restaurants(customer.score, seed_number, offset = session['offset'], limit = session['offset']+DATA_MAX, area=area, rank=rank, search_key=search_key)

		
		if len (restaurants)<DATA_MAX:
			need_seemore_tab = False
			session['see_more'] = False
		print len(restaurants)
	else: #traverse list first time
	 	seed_number = random.randrange(100)
	 	session['rest_seed_number'] = seed_number
	 	print seed_number, "first time"
	 	if 'area' not in session:
	 		#restaurants = show_p_restaurants(customer.score, seed_number, limit=DATA_MAX)
	 		restaurants = show_restaurants(customer.score, seed_number, limit=DATA_MAX)
	 		session['prev_area'] = 'ALL'
	 		session['prev_rank'] = 'All'

	 	else:
			area = session['area']
	 		rank = session['rank']

	 		#restaurants = show_p_restaurants(customer.score, seed_number, limit=DATA_MAX, area=area, rank=rank, search_key=search_key)
			restaurants = show_restaurants(customer.score, seed_number, limit=DATA_MAX, area=area, rank=rank, search_key=search_key)
			session['prev_area'] = area
	 		session['prev_rank'] = rank

	rstrnts = []
	for restaurant in restaurants:
		rstrnt = []

		rstrntgall = RstrntGall.query.filter_by(restaurant_id = restaurant.id).first()
		if rstrntgall is None:
			rstrntgall = [RstrntGall.query.filter_by(id = 1).first()]
			rstrntgall[0].uploaded_file = "default.jpg"

		rstrnt.append(restaurant)
		rstrnt.append(rstrntgall)
		rstrnts.append(rstrnt)


	form.search_key.data = search_key  # prevent search field from being cleared

	session.pop('area', None)
	session.pop('rank', None)
	session.pop('search_key', None)

	form.place.choices = [('ALL','All Areas'),
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
							('WEST VILLAGE','West Village'),
							('Harlem', 'Harlem'),
							('Brooklyn', 'Brooklyn')]

	if customer.score > HIGHEST_SCORE:
		form.rank.choices = [('All','All Colors'),('Platinum','Platinum'),('Gold','Gold'),('Silver','Silver'),('Bronze','Bronze'),('Blue','Blue')]
	elif customer.score > HIGHER_SCORE:
		form.rank.choices = [('All','All Colors'),('Gold','Gold'),('Silver','Silver'),('Bronze','Bronze'),('Blue','Blue')]
	elif customer.score > MIDDLE_SCORE:
		form.rank.choices = [('All','All Colors'),('Silver','Silver'),('Bronze','Bronze'),('Blue','Blue')]
	elif customer.score > LOWER_SCORE:
		form.rank.choices = [('All','All Colors'),('Bronze','Bronze'),('Blue','Blue')]
	else:
		form.rank.choices = [('All','All Colors'),('Blue','Blue')]

	if (session['prev_area'], session['prev_area'].title()) in form.place.choices:
		form.place.choices.remove((session['prev_area'], session['prev_area'].title()))
		form.place.choices.insert(0, (session['prev_area'], session['prev_area'].title()))
	if (session['prev_rank'], session['prev_rank'].title()) in form.rank.choices:
		form.rank.choices.remove((session['prev_rank'], session['prev_rank'].title()))
		form.rank.choices.insert(0, (session['prev_rank'], session['prev_rank'].title()))

	if is_ios:
		rstrnts = [dict(r.serialize, **r.gallery.serialize) for r in restaurants]
		customer = customer.serialize
		if len(rstrnts) == 0:
			return jsonify(form=form.data, rstrnts=rstrnts, show="show_popup", success=False, user=customer, many_restaurants=need_seemore_tab)
		else:
			return jsonify(form=form.data, rstrnts=rstrnts, success=True, user=customer, many_restaurants=need_seemore_tab)

	if len(rstrnts) == 0:
		return render_template("home.html", form=form, rstrnts=rstrnts, show="show_popup", success=False, user=customer, customer_id=customer_id, many_restaurants=need_seemore_tab)
	else:
		return render_template("home.html", form=form, rstrnts=rstrnts, success=True, user=customer, customer_id=customer_id, many_restaurants=need_seemore_tab)


@app.route('/description/<rstrnt_id>', methods=['GET', 'POST'])
@app.route('/description', defaults={'rstrnt_id':None}, methods=['GET', 'POST'])
def description(rstrnt_id=None):
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = RedeemForm()

	is_ios = True if request.args.get('ios', None) else False  # for ios app

	if 'customers_email_address' not in session or 'pass' not in session:
		return return_for_ios('redirect_to_index', is_ios)

	customer = Customers.query.filter_by(customers_email_address = session['customers_email_address']).first()
	customer_id = "%05d" % (customer.customers_id)

	if request.method == 'POST':

		midnight = present.replace(hour=0,minute=0,second=0,microsecond=0)
		redeems_today = []
		redeems_today = RedeemInfo.query.filter(RedeemInfo.customer_id == customer.customers_id, RedeemInfo.datetime > midnight).all()

		if len(redeems_today) <= 1:
			points = 5
			customer.score = customer.score + points
			customer.redeems = customer.redeems + 1
			customer = db.session.merge(customer)
			db.session.commit()
		else:
			customer.redeems = customer.redeems + 1
			customer = db.session.merge(customer)
			db.session.commit()

		newredeem = RedeemInfo(customer.customers_id, session['restaurant_id'], present)

		db.session.add(newredeem)
		db.session.commit()

		return return_for_ios("redeem", is_ios)

	elif request.method == 'GET':
		restaurant = Restaurants.query.filter(Restaurants.id == rstrnt_id).first()
		session['restaurant_id'] = restaurant.id

		if (restaurant.menu_link == ''):
			menu_exist = False
		else:
			menu_exist = True

		no_phone = 'Text our concierge'
		text_concierge = False
		if restaurant.redeem.find(no_phone) >= 0:
			text_concierge = True

		rstrnt = []

		desctmp = restaurant.description
		descstrs = []
		pos_start = 0
		while True:
			pos_end = string.find(desctmp, "\r\n")
			if (pos_end == -1):
				descstrs.append(desctmp[pos_start:])
			else:
				descstrs.append(desctmp[pos_start:pos_end])
			pos_start = pos_end + 2
			desctmp = desctmp[pos_start:]
			pos_start = 0
			if (pos_end == -1):
				break

		rstrntgall = RstrntGall.query.filter_by(restaurant_id = restaurant.id).all()
		if rstrntgall is None:
			rstrntgall = [RstrntGall.query.filter_by(id = 1).first()]
			rstrntgall[0].uploaded_file = "default.jpg"

		rstcategs = RstrntCateg.query.filter_by(is_deleted = 'N').all()
		rating = restaurant.yelp_rating / YELP_MAX * 100
		price = restaurant.yelp_pricerange

		valid_date = dt + timedelta(days=30)
		valid_date = valid_date.strftime('%m/%d/%Y')

		if is_ios:
			restaurant = restaurant.serialize
			rstrntgall = [r.serialize for r in rstrntgall]
			rstcategs = [r.serialize for r in rstcategs]
			customer = customer.serialize
			return jsonify(form=form.data, rstrnt=restaurant, text_concierge=text_concierge,
			               descstrs=descstrs, menu_exist=menu_exist, galls=rstrntgall,
			               rstcategs=rstcategs, user=customer,
			               customer_id=customer_id, valid_date=valid_date)

		return render_template('description.html', form=form, rstrnt=restaurant, text_concierge=text_concierge,
								descstrs=descstrs, menu_exist=menu_exist, galls=rstrntgall,
								rstcategs=rstcategs, rating=rating, price=price, user=customer, customer_id=customer_id,
								valid_date=valid_date)


@app.route('/account', methods=['GET', 'POST'])
def account():
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form_update = AccountForm()

	is_ios = True if request.args.get('ios', None) else False  # for ios app

	if 'customers_email_address' not in session:
		return return_for_ios('index', is_ios)
	if 'pass' not in session:
		return return_for_ios('index', is_ios)

	customer = Customers.query.filter_by(customers_email_address = session['customers_email_address']).first()
	customer_id = "%05d" % (customer.customers_id)

	if request.method == 'POST':
		if form_update.update:
			if customer.check_password(form_update.pass_old.data):
				new_name = form_update.name.data
				new_email = form_update.email.data
				new_telephone = form_update.telephone.data
				new_pwd = form_update.pass_raw.data

				if new_name != customer.customers_firstname:
					customer.customers_firstname = new_name

				if new_email != customer.customers_email_address:
					same_email = Customers.query.filter_by(customers_email_address = new_email).first()
					if same_email is None:
						customer.customers_email_address = new_email
					else:
						return return_for_ios('register_error_1', is_ios) #That email is already taken.

				if new_telephone != customer.customers_telephone and new_telephone != '':
					customer.customers_telephone = new_telephone

				if new_pwd != '':
					customer.set_password(new_pwd)

				customer.modified = present
				customer = db.session.merge(customer)
				db.session.commit()

				return return_for_ios('account_updated', is_ios)
			else:
				return return_for_ios('login_error_2', is_ios) #Invalid password.

	elif request.method == 'GET':
		return render_template('account.html', form=form_update, user=customer, customer_id=customer_id)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
	form = FeedbackForm()
	is_ios = True if request.args.get('ios', None) else False  # for ios app

	if 'customers_email_address' not in session:
		return return_for_ios('redirect_to_index', is_ios)
	if 'pass' not in session:
		return return_for_ios('redirect_to_index', is_ios)

	customer = Customers.query.filter_by(customers_email_address = session['customers_email_address']).first()
	customer_id = "%05d" % (customer.customers_id)

	if request.method == 'POST':
		msg = Message(form.subject.data, sender=('DinersCode \xF0\x9F\x8D\xB7','contact@dinerscode.com'), recipients=['contact@dinerscode.com'])
		msg.html = """
		From: %s <br>
		<br>
		Email: %s <br>
		<br>
		Message: %s
		""" % (form.name.data, form.email.data, form.feedback.data)
		mail.send(msg)
		msg = Message("Thank you for your email! Re: Give Feedback", sender=('DinersCode \xF0\x9F\x8D\xB7','contact@dinerscode.com'), recipients=[form.email.data])
		msg.html = """
		<p style="font-family: Georgia, Times, 'Times New Roman', serif; color: #404040"><br>
		Your unique tastes deserve unique experiences.<br><br>
		Thanks for your feedback! We will get back to you shortly.<br><br>
		<br><br>
		--<br><br>
		Sincerely,<br><br>
		DinersCode<br><br>
		<br>
		</p>
		<a href="http://www.dinerscode.com" target="_blank" ><img src="http://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-link-48.png" height="24" width="24" style="PADDING-RIGHT:10px;PADDING-LEFT:10px"></a>
		<a href="http://www.facebook.com/dinerscode" target="_blank" ><img src="http://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-facebook-48.png" height="24" width="24" style="PADDING-RIGHT:10px;PADDING-LEFT:10px"></a>
		<a href="mailto:contact@dinerscode.com" target="_blank" ><img src="http://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-forwardtofriend-48.png" height="24" width="24" style="PADDING-RIGHT:10px;PADDING-LEFT:10px"></a>
		"""
		mail.send(msg)
		return return_for_ios('feedback_success', is_ios)
	elif request.method == 'GET':
		return render_template('feedback.html', form=form, user=customer, customer_id=customer_id)


@app.route('/faq_app')
def faq_app():
	if 'customers_email_address' not in session:
		return redirect(url_for('index'))
	if 'pass' not in session:
		return redirect(url_for('index'))

	customer = Customers.query.filter_by(customers_email_address = session['customers_email_address']).first()
	customer_id = "%05d" % (customer.customers_id)

	return render_template('faq_app.html', user=customer, customer_id=customer_id)


@app.route('/logout')
def logout():
	is_ios = True if request.args.get('ios', None) else False  # for ios app

	if 'customers_email_address' in session and 'pass' in session:
		session.pop('customers_email_address', None)
		session.pop('pass', None)

	return return_for_ios('redirect_to_index', is_ios)


###### End of Diner Account Page ######


###### Restaurant Account Page ######

@app.route('/rating_login', methods=['GET', 'POST'])
def rating_login():
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = RestaurantSigninForm()

	if 'restaurant_pass' in session:
		return redirect(url_for('rating'))

	if request.method == 'POST':
		restaurant = Restaurants.query.filter_by(restaurant_name = form.name.data).first()

		if restaurant:
			if form.pass_raw.data == RESTAURANT_DEFAULT_PASSWORD and restaurant.password == '':
				restaurant.set_password(RESTAURANT_DEFAULT_PASSWORD)
				restaurant = db.session.merge(restaurant)
				db.session.commit()
				session['username'] = form.name.data
				session['restaurant_id'] = restaurant.id
				session['restaurant_pass'] = True

				return "rating.html"

			elif restaurant.check_password(form.pass_raw.data):
				session['username'] = form.name.data
				session['restaurant_id'] = restaurant.id
				session['restaurant_pass'] = True

				return "rating.html"

			else:
				return "ratinglogin_error_2" #Invalid password

		else:
			return "ratinglogin_error_1" #Invalid username

	elif request.method == 'GET':
		return render_template('rating_login.html', form=form)

@app.route('/restaurant_fgpwd', methods=['GET', 'POST'])
def restaurant_fgpwd():
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = RestaurantForgetPwdForm()

	if request.method == 'POST':
		restaurant = Restaurants.query.filter_by(restaurant_name = form.name.data).first()
		if restaurant:
            #generate PIN
			pin = ''.join(random.choice(string.digits) for _ in range(6))

            #send change password email
			msg = Message("DinersCode - New Password", sender=('DinersCode \xF0\x9F\x8D\xB7','contact@dinerscode.com'), recipients=[form.email.data])
			msg.html = """
			<p style="font-family: Georgia, Times, 'Times New Roman', serif; color: #404040"><br>
			A new password has been requested for your account at DinersCode.<br>
			<br>
			Please use the below Pin to securely change your password:</b>.<br>
			<br>
			%s<br>
			<br>
			This Pin will be automatically discarded after 24 hours or after your password has been changed.<br>
			<br>
			For help with any of our online services, please email the Administrator : contact@dinerscode.com.<br>
			<br>
			--<br><br>
			Sincerely,<br><br>
			DinersCode<br><br>
			<br>
			</p>
			<a href="http://www.dinerscode.com" target="_blank" ><img src="http://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-link-48.png" height="24" width="24" style="PADDING-RIGHT:10px;PADDING-LEFT:10px"></a>
			<a href="http://www.facebook.com/dinerscode" target="_blank" ><img src="http://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-facebook-48.png" height="24" width="24" style="PADDING-RIGHT:10px;PADDING-LEFT:10px"></a>
			<a href="mailto:contact@dinerscode.com" target="_blank" ><img src="http://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-forwardtofriend-48.png" height="24" width="24" style="PADDING-RIGHT:10px;PADDING-LEFT:10px"></a>
			"""  % (pin)
			mail.send(msg)

			#add new PIN to database
			session['username'] = form.name.data
			restaurant.pwd_reset_key = pin
			restaurant.pwd_reset_date = present
			restaurant = db.session.merge(restaurant)
			db.session.commit()

			return "restaurant_rstpwd.html"

		else:
			return "ratinglogin_error_1" #Invalid username

	elif request.method == 'GET':
		return render_template('restaurant_fgpwd.html', form=form)

@app.route('/restaurant_rstpwd', methods=['GET', 'POST'])
def restaurant_rstpwd():
	dt = datetime.now(pytz.timezone('US/Eastern'))
	present = dt.replace(tzinfo=None)
	form = ResetPwdForm()

	# if 'username' not in session:
	# 	return redirect(url_for('restaurant_fgpwd'))

	if request.method == 'POST':
		restaurant = Restaurants.query.filter_by(restaurant_name = session['username']).first()
		if (restaurant.pwd_reset_key == form.pin_num.data):
			if (present - restaurant.pwd_reset_date < timedelta(days=1)):
				restaurant.pass_raw = form.pass_raw.data
				restaurant.set_password(form.pass_raw.data)
				restaurant = db.session.merge(restaurant)
				db.session.commit()

				restaurant.pwd_reset_key = None
				restaurant = db.session.merge(restaurant)
				db.session.commit()

				session.pop('restaurant_id', None)

				return "<div align='center'><p>Your password has been reset.<br>Please <a href='/rating_login'>click</a> here to login.</p></div>"
			else:
				return "rstpwd_error_1" #The PIN number has expired.
		else:
			return "rstpwd_error_2" #The PIN number doesn't match.

	elif request.method == 'GET':
		return render_template('restaurant_rstpwd.html', form=form)


@app.route('/rating/<customer_id>', methods=['GET','POST'])
@app.route('/rating', defaults={'customer_id':None}, methods=['GET','POST'])
def rating(customer_id=None):
	form = CustomerSearchForm()

	if 'username' not in session:
		return redirect(url_for('rating_login'))

	if request.method == 'POST':
		dt = datetime.now(pytz.timezone('US/Eastern'))
		present = dt.replace(tzinfo=None)

		customer_id = int(customer_id)
		rate_arrival = int(request.form['arrival'])
		rate_overall = int(request.form['overall'])

		customer = Customers.query.filter_by(customers_id = customer_id).first()
		customer.score = customer.score + rate_arrival + rate_overall
		customer.num_of_rstrnt_ratings = customer.num_of_rstrnt_ratings + 1
		if rate_arrival == -25:
			customer.no_show = customer.no_show + 1

		customer.modified = present
		customer = db.session.merge(customer)
		db.session.commit()

		newrating = RatingInfo(customer.customers_id, session['restaurant_id'], request.form['arrival'], request.form['overall'], present)

		db.session.add(newrating)
		db.session.commit()

		return render_template("rating.html", form=form, show2="show_popup", found_customer=False, restaurant_id=session['username'])

	elif request.method == 'GET':
		if 'customer_id' not in session:
			return render_template('rating.html', form=form, found_customer=False, restaurant_id=session['username'])

		else:
			customer = Customers.query.filter_by(customers_id = session['customer_id']).first()

			if customer is None:
				return render_template("rating.html", form=form, show1="show_popup", found_customer=False, restaurant_id=session['username'])
			else:
				customer_id = "%05d" % (customer.customers_id)

				return render_template("rating.html", form=form, customer_found=True,
										customer=customer, customer_id=customer_id, restaurant_id=session['username'])

@app.route('/rating_search', methods=['GET','POST'])
def rating_search():
	form = CustomerSearchForm()

	if 'username' not in session:
		return redirect(url_for('rating_login'))

	session['customer_id'] = int(form.customer_id.data)

	return "rating.html"

@app.route('/restaurant_account', methods=['GET','POST'])
def restaurant_account():
	form = RestaurantAccountForm()

	if 'username' not in session:
		return redirect(url_for('rating_login'))

	restaurant = Restaurants.query.filter_by(id = session['username']).first()

	if request.method == 'POST':
		if restaurant.check_password(form.pass_old.data):
			if form.pass_raw.data != '':
				restaurant.set_password(form.pass_raw.data)

			restaurant = db.session.merge(restaurant)
			db.session.commit()

			return "account_updated"

		else:
			return "login_error_2" #Invalid password.

	elif request.method == 'GET':
		return render_template("restaurant_account.html", form=form, restaurant=restaurant, restaurant_id=session['username'])

@app.route('/restaurant_feedback', methods=['GET', 'POST'])
def restaurant_feedback():
	form = FeedbackForm()

	if 'username' not in session:
		return redirect(url_for('rating_login'))

	if request.method == 'POST':
		msg = Message(form.subject.data, sender=('DinersCode \xF0\x9F\x8D\xB7','contact@dinerscode.com'), recipients=['contact@dinerscode.com'])
		msg.html = """
		From: %s <br>
		<br>
		Email: %s <br>
		<br>
		Message: %s
		""" % (form.name.data, form.email.data, form.feedback.data)
		mail.send(msg)

		return "<p>Thank you for reaching out to us. We'll get back to you shortly.</p><br><br><br><br><br><br><br><br><br><br><br><br>"

	elif request.method == 'GET':
		return render_template('restaurant_feedback.html', form=form, restaurant_id=session['username'])

@app.route('/rating_logout')
def rating_logout():
	if 'username' not in session:
		return redirect(url_for('rating_login'))

	session.pop('customer_id', None)
	session.pop('username', None)
	session.pop('restaurant_pass', None)

	return redirect(url_for('rating_login'))

# @app.after_request
# def after_request(response):
# 	"""
# 	Add headers to both force latest IE rendering engine or Chrome Frame,
# 	and also to cache the rendered page for 10 minutes.
# 	"""
# 	response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
# 	response.headers['Cache-Control'] = 'public, max-age=3600'
# 	return response


###### End of Restaurant Account Page ######

if __name__ == '__main__':
	app.run(debug=True)