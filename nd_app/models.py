from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from datetime import datetime
from nd_app.pwdfunc import PasswordHash

db = SQLAlchemy()

class Customers(db.Model):
	__tablename__ = 'customers'
	customers_id = db.Column(db.Integer, primary_key = True)
	customers_firstname = db.Column(db.String(255))
	customers_lastname = db.Column(db.String(255))
	customers_email_address = db.Column(db.String(255), unique = True)
	customers_telephone = db.Column(db.String(255))
	customers_cellphone = db.Column(db.String(255))
	customers_password = db.Column(db.String(60))
	pass_raw = db.Column(db.String(60))
	customers_username = db.Column(db.String(255))
	customers_profile_image = db.Column(db.Text)
	raw_pass = db.Column(db.String(50))
	referral_code = db.Column(db.String(30))
	referral_expiry = db.Column(db.DateTime)
	stripe_customer_id = db.Column(db.String(254))
	stripe_subscription_id = db.Column(db.String(254))
	facebook_id = db.Column(db.Integer)
	twitter_id = db.Column(db.Integer)
	device_token = db.Column(db.Text)
	cur_badge = db.Column(db.Integer)
	created = db.Column(db.DateTime)
	modified = db.Column(db.DateTime)
	score = db.Column(db.Integer)
	zipcode = db.Column(db.Integer)
	age = db.Column(db.Integer)
	budget = db.Column(db.Float)
	redeems = db.Column(db.Integer)
	no_show = db.Column(db.Integer)
	num_of_rstrnt_ratings = db.Column(db.Integer)

	def __init__(self, customers_firstname, customers_lastname,
				customers_email_address, customers_telephone,
				customers_cellphone,customers_password,
				pass_raw, customers_username,
				customers_profile_image, raw_pass,
				referral_code, stripe_customer_id, stripe_subscription_id,
				facebook_id, twitter_id, device_token, cur_badge,
				created, modified, score, zipcode, age, budget, redeems,
				no_show, num_of_rstrnt_ratings):
		self.customers_firstname = customers_firstname
		self.customers_lastname = customers_lastname
		self.customers_email_address = customers_email_address
		self.customers_telephone = customers_telephone
		self.customers_cellphone = customers_cellphone
		self.pass_raw = pass_raw
		self.customers_username = customers_username
		self.customers_profile_image = customers_profile_image
		self.raw_pass = raw_pass
		self.referral_code = referral_code
		self.stripe_customer_id = stripe_customer_id
		self.stripe_subscription_id = stripe_subscription_id
		self.facebook_id = facebook_id
		self.twitter_id = twitter_id
		self.device_token = device_token
		self.cur_badge = cur_badge
		self.created = datetime.now()
		self.modified = datetime.now()
		self.score = score
		self.zipcode = zipcode
		self.age = age
		self.budget = budget
		self.redeems = redeems
		self.no_show = no_show
		self.num_of_rstrnt_ratings = num_of_rstrnt_ratings

	def set_password(self, pass_raw):
		pwdhash = PasswordHash(10, True);
		self.customers_password = pwdhash.hash_password(pass_raw)

	def check_password(self, pass_raw):
		pwdhash = PasswordHash(10, True);
		return pwdhash.check_password(pass_raw, self.customers_password)

	@property
	def serialize(self):
		"""Return object data in serializeable format"""
		return {
			# 'customers_id': self.customers_id,
                        'customers_firstname' : self.customers_firstname,
			'customers_lastname': self.customers_lastname,
			'score': self.score
		}

class CustomersInfo(db.Model):
	__tablename__ = 'customers_info'
	customers_info_id = db.Column(db.Integer, primary_key = True)
	customers_info_date_of_last_logon = db.Column(db.DateTime)
	customers_info_number_of_logons = db.Column(db.Integer)
	customers_info_date_account_created = db.Column(db.DateTime)
	customers_info_date_account_last_modified = db.Column(db.DateTime)
	global_product_notifications = db.Column(db.Integer)
	password_reset_key = db.Column(db.String)
	password_reset_date = db.Column(db.DateTime)

	def __init__(self, customers_info_id, customers_info_date_of_last_logon, customers_info_number_of_logons,
				customers_info_date_account_created, customers_info_date_account_last_modified):
		self.customers_info_id = customers_info_id
		self.customers_info_date_of_last_logon = customers_info_date_of_last_logon
		self.customers_info_number_of_logons = customers_info_number_of_logons
		self.customers_info_date_account_created = customers_info_date_account_created
		self.customers_info_date_account_last_modified = customers_info_date_account_last_modified

class Restaurants(db.Model):
	__tablename__ = 'restaurants'
	id = db.Column(db.Integer, primary_key = True)
	restaurant_name = db.Column(db.String(254))
	street_address = db.Column(db.String(254))
	area = db.Column(db.String(100))
	city = db.Column(db.String(100))
	state = db.Column(db.String(100))
	zip = db.Column(db.String(100))
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	phone = db.Column(db.String(30))
	cuisine_type = db.Column(db.Text)
	category = db.Column(db.String(30))
	description = db.Column(db.Text)
	nd_rating = db.Column(db.Integer)
	menu_link = db.Column(db.Text)
	locked = db.Column(db.Enum('Y','N'))
	created = db.Column(db.DateTime)
	updated = db.Column(db.DateTime)
	status = db.Column(db.Enum('A','I'))
	is_deleted = db.Column(db.Enum('Y','N'))
	yelp_rating = db.Column(db.Float(3,5))
	yelp_pricerange = db.Column(db.Float(3,5))
	dinerscode_rank = db.Column(db.Float)
	perk = db.Column(db.Text)
	redeem = db.Column(db.Text)
	password = db.Column(db.String(60))
	pwd_reset_key = db.Column(db.String)
	pwd_reset_date = db.Column(db.DateTime)

	def set_password(self, pass_raw):
		pwdhash = PasswordHash(10, True);
		self.password = pwdhash.hash_password(pass_raw)

	def check_password(self, pass_raw):
		pwdhash = PasswordHash(10, True);
		return pwdhash.check_password(pass_raw, self.password)

	@property
	def serialize(self):
		"""Return object data in serializeable format"""
		return {
			'id': self.id,
			'restaurant_name': self.restaurant_name,
			'area': self.area,
			'cuisine_type': self.cuisine_type,
			'perk': self.perk,
			'street_address': self.street_address,
			'category': self.category,
			'menu_link': self.menu_link,
			'redeem': self.redeem,
			'phone': self.phone,
			'latitude': self.latitude,
			'longitude': self.longitude,
			'yelp_rating': float('%0.1f'%self.yelp_rating),
			'yelp_pricerange': float('%0.1f'%self.yelp_pricerange),
			'dinerscode_rank': self.dinerscode_rank
		}

class RstrntGall(db.Model):
	__tablename__ = 'restaurants_gallery'
	id = db.Column(db.Integer, primary_key = True)
	restaurant_id = db.Column(db.Integer)
	uploaded_file = db.Column(db.Text)
	uploaded_type = db.Column(db.Text)
	uploaded_size = db.Column(db.Integer)
	uploaded_width = db.Column(db.Integer)
	uploaded_height = db.Column(db.Integer)
	sort_order = db.Column(db.Integer)

	@property
	def serialize(self):
		"""Return object data in serializeable format"""
		return {
			'uploaded_file': self.uploaded_file
		}

class RstrntCateg(db.Model):
	__tablename__ = 'restaurant_categories'
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100), unique = True)
	description = db.Column(db.Text)
	sort_order = db.Column(db.Integer)
	status = db.Column(db.Enum('A','I'))
	created = db.Column(db.DateTime)
	updated = db.Column(db.DateTime)
	is_deleted = db.Column(db.Enum('Y','N'))

	@property
	def serialize(self):
		"""Return object data in serializeable format"""
		return {
			'title': self.title,
			'description': self.description
		}

class ZipcodeIncome(db.Model):
	__tablename__ = 'zipcode_income'
	id = db.Column(db.Integer, primary_key = True)
	zip_code = db.Column(db.Text)
	median_income = db.Column(db.Text)

class RedeemInfo(db.Model):
	__tablename__ = 'redeem_info'
	id = db.Column(db.Integer, primary_key = True)
	customer_id = db.Column(db.Integer)
	restaurant_id = db.Column(db.Integer)
	datetime = db.Column(db.DateTime)

	def __init__(self, customer_id, restaurant_id, datetime):
		self.customer_id = customer_id
		self.restaurant_id = restaurant_id
		self.datetime = datetime

class RatingInfo(db.Model):
	__tablename__ = 'rating_info'
	id = db.Column(db.Integer, primary_key = True)
	customer_id = db.Column(db.Integer)
	restaurant_id = db.Column(db.Integer)
	arrival = db.Column(db.Float)
	overall = db.Column(db.Float)
	datetime = db.Column(db.DateTime)

	def __init__(self, customer_id, restaurant_id, arrival, overall, datetime):
		self.customer_id = customer_id
		self.restaurant_id = restaurant_id
		self.arrival = arrival
		self.overall = overall
		self.datetime = datetime

class Favorites(db.Model):
	__tablename__ = 'favorites'
	customers_id = db.Column(db.Integer, primary_key = True)
	fav2 = db.Column(db.Integer)
	fav3 = db.Column(db.Integer)
	fav4 = db.Column(db.Integer)
	fav5 = db.Column(db.Integer)
	fav6 = db.Column(db.Integer)
	fav7 = db.Column(db.Integer)
	fav8 = db.Column(db.Integer)
	fav9 = db.Column(db.Integer)
	fav10 = db.Column(db.Integer)
	fav11 = db.Column(db.Integer)
	fav12 = db.Column(db.Integer)
	fav13 = db.Column(db.Integer)
	fav14 = db.Column(db.Integer)
	fav15 = db.Column(db.Integer)
	fav16 = db.Column(db.Integer)
	fav17 = db.Column(db.Integer)
	fav18 = db.Column(db.Integer)
	fav19 = db.Column(db.Integer)

	def __init__(self, customer_id, fav2, fav3, fav4, fav5, fav6, fav7, fav8, fav9 ,fav10 ,fav11, fav12, fav13, fav14, fav15, fav16, fav17, fav18, fav19):
		self.fav2 = fav2
		self.fav3 = fav3
		self.fav4 = fav4
		self.fav5 = fav5
		self.fav6 = fav6
		self.fav7 = fav7
		self.fav8 = fav8
		self.fav9 = fav9
		self.fav10 = fav10
		self.fav11 = fav11
		self.fav12 = fav12
		self.fav13 = fav13
		self.fav14 = fav14
		self.fav15 = fav15
		self.fav16 = fav16
		self.fav17 = fav17
		self.fav18 = fav18
		self.fav19 = fav19

# class SessionRestaurnInfo(db.Model):
# 	__tablename__ = 'session_rest_info'
# 	id = db.Column(db.Integer, primary_key = True)
# 	restaurant_id = db.Column(db.Integer)
# 	restaurant_name = db.Column(db.Float)
# 	area = db.Column(db.String(100))
# 	cuisine = db.Column(db.Text)

# 	def __init__(self, restaurant_id, restaurant_name, area, cuisine):
# 		self.restaurant_id = restaurant_id
# 		self.restaurant_name = restaurant_name
# 		self.area = area
# 		self.cuisine = cuisine
