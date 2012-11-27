# -*- coding: utf-8 -*-
from flask import request, abort
from heymoose import app, resource as rc
from heymoose.forms import forms
from heymoose.admin import blueprint as bp
from heymoose.admin.helpers import superadmin_required
from heymoose.views.decorators import template, sorted, paginated


OFFER_STATS_PER_PAGE = app.config.get('OFFER_STATS_PER_PAGE', 20)
AFFILIATE_STATS_PER_PAGE = app.config.get('AFFILIATE_STATS_PER_PAGE', 20)
ADVERTISER_STATS_PER_PAGE = app.config.get('ADVERTISER_STATS_PER_PAGE', 20)
SITE_STATS_PER_PAGE = app.config.get('SITE_STATS_PER_PAGE', 20)
SUBOFFER_STATS_PER_PAGE = app.config.get('SUBOFFER_STATS_PER_PAGE', 20)


@bp.route('/stats/offer')
@template('admin/stats/offer.html')
@superadmin_required()
@sorted('clicks_count', 'desc')
@paginated(OFFER_STATS_PER_PAGE)
def stats_offer(**kwargs):
	form = forms.OfferStatsFilterForm(request.args)
	kwargs.update(form.backend_args())
	stats, count = rc.offer_stats.list_all(**kwargs) if form.validate() else ([], 0)
	return dict(stats=stats, count=count, form=form)

@bp.route('/stats/affiliate')
@template('admin/stats/affiliate.html')
@superadmin_required()
@sorted('clicks_count', 'desc')
@paginated(AFFILIATE_STATS_PER_PAGE)
def stats_affiliate(**kwargs):
	form = forms.DateTimeRangeForm(request.args)
	kwargs.update(form.backend_args())
	stats, count = rc.offer_stats.list_affiliate(**kwargs) if form.validate() else ([], 0)
	return dict(stats=stats, count=count, form=form)

@bp.route('/stats/advertiser')
@template('admin/stats/advertiser.html')
@superadmin_required()
@sorted('clicks_count', 'desc')
@paginated(ADVERTISER_STATS_PER_PAGE)
def stats_advertiser(**kwargs):
	form = forms.DateTimeRangeForm(request.args)
	kwargs.update(form.backend_args())
	stats, count = rc.offer_stats.list_advertiser(**kwargs) if form.validate() else ([], 0)
	return dict(stats=stats, count=count, form=form)

@bp.route('/stats/site/')
@template('admin/stats/site.html')
@superadmin_required()
@sorted('clicks_count', 'desc')
@paginated(SITE_STATS_PER_PAGE)
def stats_site(**kwargs):
	form = forms.DateTimeRangeForm(request.args)
	kwargs.update(form.backend_args())
	stats, count = rc.offer_stats.list_by_site(**kwargs) if form.validate() else ([], 0)
	return dict(stats=stats, count=count, form=form)

@bp.route('/stats/site/periods/')
@template('admin/stats/site-periods.html')
@superadmin_required()
@sorted('second_period_click_count', 'asc')
@paginated(SITE_STATS_PER_PAGE)
def stats_site_periods(**kwargs):
	form = forms.DoubleDateTimeRangeForm(request.args)
	kwargs.update(form.backend_args())
	stats, count = rc.sites.list_stats(**kwargs) if form.validate() else ([], 0)
	return dict(stats=stats, count=count, form=form)

@bp.route('/stats/total')
@template('admin/stats/total.html')
@superadmin_required()
def stats_total():
	form = forms.DateTimeRangeForm(request.args)
	stats = rc.offer_stats.total(**form.backend_args()) if form.validate() else []
	return dict(stats=stats, form=form)

@bp.route('/stats/suboffer')
@template('admin/stats/suboffer.html')
@superadmin_required()
@sorted('leads_count', 'desc')
@paginated(SUBOFFER_STATS_PER_PAGE)
def stats_suboffer(**kwargs):
	offer = rc.offers.get_by_id(request.args.get('offer'))
	form = forms.DateTimeRangeForm(request.args)
	kwargs.update(form.backend_args())
	stats, count = rc.offer_stats.list_suboffer(offer_id=offer.id, **kwargs) if form.validate() else ([], 0)
	return dict(stats=stats, count=count, offer=offer)

@bp.route('/stats/suboffer/affiliate')
@template('admin/stats/suboffer.html')
@superadmin_required()
@sorted('leads_count', 'desc')
@paginated(SUBOFFER_STATS_PER_PAGE)
def stats_suboffer_affiliate(**kwargs):
	affiliate = rc.users.get_by_id(request.args.get('aff_id'))
	form = forms.DateTimeRangeForm(request.args)
	kwargs.update(form.backend_args())
	stats, count = rc.offer_stats.list_suboffer_by_affiliate(aff_id=affiliate.id, **kwargs) if form.validate() else ([], 0)
	return dict(stats=stats, count=count, affiliate=affiliate)

@bp.route('/stats/suboffer/advertiser')
@template('admin/stats/suboffer.html')
@superadmin_required()
@sorted('leads_count', 'desc')
@paginated(SUBOFFER_STATS_PER_PAGE)
def stats_suboffer_advertiser(**kwargs):
	advertiser = rc.users.get_by_id(request.args.get('adv_id'))
	form = forms.DateTimeRangeForm(request.args)
	kwargs.update(form.backend_args())
	stats, count = rc.offer_stats.list_suboffer_by_advertiser(adv_id=advertiser.id, **kwargs) if form.validate() else ([], 0)
	return dict(stats=stats, count=count, advertiser=advertiser)

@bp.route('/stats/suboffer/site')
@template('admin/stats/suboffer.html')
@sorted('leads_count', 'desc')
@paginated(SUBOFFER_STATS_PER_PAGE)
def stats_suboffer_site(**kwargs):
	site = rc.sites.get_by_id(request.args.get('site_id'))
	form = forms.DateTimeRangeForm(request.args)
	kwargs.update(site_id=site.id, **form.backend_args())
	stats, count = rc.offer_stats.list_suboffer_by_site(**kwargs) if form.validate() else ([], 0)
	return dict(stats=stats, count=count, site=site)
