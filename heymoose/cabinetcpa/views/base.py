# -*- coding: utf-8 -*-
from flask import g, request, abort
from heymoose import resource as rc
from heymoose.cabinetcpa import blueprint as bp
from heymoose.forms import forms
from heymoose.views.decorators import template
from heymoose.data.mongo.models import Notification, NewsItem


@template('cabinetcpa/index-affiliate.html')
def index_affiliate():
	form = forms.DateTimeRangeForm()
	args = dict(offset=0, limit=5, ordering='NOT_CONFIRMED_REVENUE', direction='DESC', **form.backend_args())
	offer_stats, _ = rc.offer_stats.list_user(g.user, **args)
	site_stats, _ = rc.offer_stats.list_by_site(aff_id=g.user.id, **args)
	user_notifications_query = Notification.query.filter(Notification.user_id == g.user.id)
	notifications = user_notifications_query.descending(Notification.date).limit(5).all()
	news = NewsItem.query.filter(NewsItem.active == True).descending(NewsItem.date).limit(3).all()
	has_sites, _ = rc.sites.list(aff_id=g.user.id, offset=0, limit=1)
	has_placements, _ = rc.placements.list(aff_id=g.user.id, offset=0, limit=1)
	referral_offer = rc.offers.get_referral_offer() if request.args.get('registered') == g.user.referral_code else None
	return dict(offer_stats=offer_stats, site_stats=site_stats, notifications=notifications, news=news,
		referral_offer=referral_offer, has_sites=has_sites, has_placements=has_placements)

@template('cabinetcpa/index-advertiser.html')
def index_advertiser():
	form = forms.DateTimeRangeForm()
	args = dict(offset=0, limit=999999, ordering='NOT_CONFIRMED_REVENUE', direction='DESC', **form.backend_args())
	stats, _ = rc.offer_stats.list_user(g.user, **args)
	offers, _ = rc.offers.list(advertiser_id=g.user.id, limit=5)
	user_notifications_query = Notification.query.filter(Notification.user_id == g.user.id)
	notifications = user_notifications_query.descending(Notification.date).limit(5).all()
	return dict(stats=stats, offers=offers, notifications=notifications)

@bp.route('/')
def index():
	if g.user.is_advertiser:
		return index_advertiser()
	elif g.user.is_affiliate:
		return index_affiliate()
	else:
		abort(403)
	
	



