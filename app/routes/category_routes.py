

from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Category
from app.extensions import db


category_bp = Blueprint('category', __name__)




