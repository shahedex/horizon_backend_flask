from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

auth_blueprint = Blueprint('auth', __name__)


class TestApi(MethodView):
    """
    This is a test API
    """
    def get(self):
        responseObject = {
            'status': 'success',
            'message': 'This is a successful call'
        }
        return make_response(jsonify(responseObject)), 200


testApi_view = TestApi.as_view('test_api')
auth_blueprint.add_url_rule(
    '/test',
    view_func=testApi_view,
    methods=['GET']
    )