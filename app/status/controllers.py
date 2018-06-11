from flask import Blueprint


status = Blueprint('status', __name__)


@status.route('/')
def index():
    return "status"
