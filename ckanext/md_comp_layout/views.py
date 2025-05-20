from flask import Blueprint, redirect, url_for, render_template

from ckan.plugins.toolkit import c, render, request
import ckan.lib.helpers as h

md_comp_layout = Blueprint(u'md_comp_layout', __name__)

@md_comp_layout.route(u'/competition')
def competition():
    return render_template('competition.html')
@md_comp_layout.route(u'/imprint_crc')
def imprint_crc():
    return render_template('imprint_crc.html')
@md_comp_layout.route(u'/terms_and_condition')
def terms_and_condition():
    return render_template('terms_and_condition.html')

def get_blueprints():
    return [md_comp_layout]