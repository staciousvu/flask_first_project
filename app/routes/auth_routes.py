

from flask import Blueprint, render_template, request, redirect, url_for
from app.models import User
from app.extensions import db


auth_bp = Blueprint('auth', __name__)


