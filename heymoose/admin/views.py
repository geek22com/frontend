from flask import render_template, g, abort
from heymoose.admin import blueprint as bp
from heymoose.core import actions

from restkit.errors import ResourceError

#TODO: make paging in user interface
@bp.route('/')
#@admin_only
def index():
	#acs = actions.actions.get_actions(0, 100)
	#if acs: g.params['actions'] = acs

	return render_template('admin/index.html', params=g.params)

@bp.route('/orders/')
def orders():
	ods = actions.orders.get_orders(0, 100)
	return render_template('admin/orders.html', orders=ods)

@bp.route('/orders/stats')
def orders_stats():
	return render_template('admin/orders-stats.html')

@bp.route('/orders/<int:id>')
def orders_info(id):
	try:
		order = actions.orders.get_order(id)
	except ResourceError as e:
		abort(e.status_int)
	return render_template('admin/orders-info.html', order=order)

@bp.route('/orders/<int:id>/stats')
def orders_info_stats(id):
	try:
		order = actions.orders.get_order(id)
	except ResourceError as e:
		abort(e.status_int)
	return render_template('admin/orders-info-stats.html', order=order)


@bp.route('/customers/<int:id>')
def customers_info(id):
	customer = actions.users.get_user_by_id(id, True)
	return '{0} ({1})'.format(customer.nickname, customer.email)

