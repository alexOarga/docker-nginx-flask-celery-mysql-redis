from flask import Blueprint, request

from src.app.tasks.tasks import example_task

example_bp = Blueprint('example_bp', __name__,
                     template_folder='templates',
                     static_folder='static',
                     static_url_path='assets')

@example_bp.route('/example/', methods=['POST'])
def example_delay_task():

    request_data = request.form

    task = example_task.delay()

    return "celery task initiated!"

