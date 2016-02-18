from nd_app.models import db, Restaurants
from sqlalchemy.sql import func
from sqlalchemy import or_

def get_maximum_rank(score):
	""" Return the maximum restaurant rank customer can access
	"""
	scores = [0, 300, 450, 600, 750]  # ranges 0-299, 300-449, etc.
	rank = None
	for i in range(len(scores)):
		if score >= scores[i]:
			rank = i + 1

	return rank

def show_restaurants(customer_score, seed_number=1, offset=0, limit=9999999, area=None, rank=None, search_key=None):
	""" Show restaurants randomly by seed_number from offset to offset + limit
	"""
	cuisine_match = {
		'american': ['American','Steak','New American','French-American'],
		'french': ['French','French/Italian','French-American','French| Gluten Free'],
		'italian': ['Italian','French/Italian'],
		'asian': ['Asian','Japanese','Middle Eastern','Chinese','Korean','Indian','Thai'],
	}
	rank_match = {'Platinum': 5, 'Gold': 4, 'Silver': 3, 'Bronze': 2, 'Blue': 1}

	query = Restaurants.query.filter(Restaurants.dinerscode_rank >= 1, Restaurants.dinerscode_rank <= get_maximum_rank(customer_score), Restaurants.is_deleted == 'N')

	if area and area != 'ALL':
		query = query.filter(Restaurants.area == area)
 
	if rank in rank_match:
		query = query.filter(Restaurants.dinerscode_rank == rank_match[rank])

	if search_key:
		search_key = search_key.lower()
		cuisine_lst = cuisine_match[search_key] if search_key in cuisine_match else (search_key,)
		query = query.filter(or_(Restaurants.restaurant_name.ilike('%{}%'.format(search_key)),
		                     		 Restaurants.cuisine_type.in_(cuisine_lst),
		                     		 Restaurants.cuisine_type.ilike('%{}%'.format(search_key))))
		# restaurants = [res for res in restaurants if search_key in res.restaurant_name.lower() or search_key in res.cuisine_type.lower()]

	query = query.order_by(func.rand(seed_number)).offset(offset).limit(limit).all()

	return query

def filter_restaurants(customer_score, seed_number=1, area=None, rank=None, search_key=None):
	""" Show restaurants randomly by seed_number from offset to offset + limit
	"""
	cuisine_match = {
		'american': ['American','Steak','New American','French-American'],
		'french': ['French','French/Italian','French-American','French| Gluten Free'],
		'italian': ['Italian','French/Italian'],
		'asian': ['Asian','Japanese','Middle Eastern','Chinese','Korean','Indian','Thai'],
	}
	rank_match = {'Platinum': 5, 'Gold': 4, 'Silver': 3, 'Bronze': 2, 'Blue': 1}

	query = Restaurants.query.filter(Restaurants.dinerscode_rank >= 1, Restaurants.dinerscode_rank <= get_maximum_rank(customer_score), Restaurants.is_deleted == 'N')

	if area and area != 'ALL':
		query = query.filter(Restaurants.area == area)

	if rank in rank_match:
		query = query.filter(Restaurants.dinerscode_rank == rank_match[rank])

	if search_key:
		search_key = search_key.lower()
		cuisine_lst = cuisine_match[search_key] if search_key in cuisine_match else (search_key,)
		query = query.filter(or_(Restaurants.restaurant_name.ilike('%{}%'.format(search_key)),
		                     		 Restaurants.cuisine_type.in_(cuisine_lst),
		                     		 Restaurants.cuisine_type.ilike('%{}%'.format(search_key))))

	query = query.order_by(func.rand(seed_number))

	return query


def show_p_restaurants(query, offset=0, limit=9999999, area=None, rank=None, search_key=None):
	return query.offset(offset).limit(limit).all()