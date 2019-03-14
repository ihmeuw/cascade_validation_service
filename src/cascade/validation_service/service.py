from cascade.input_data.configuration.form import Configuration

from flask import Blueprint, abort, jsonify, request

bp = Blueprint("service", __name__)

@bp.route("/", methods=("POST",))
def validate():
    if not request.is_json:
        abort(406)
    raw_settings = request.get_json()
    settings = Configuration(raw_settings)
    errors = settings.validate_and_normalize()

    # strip display names
    errors = [[key, error] for key, _, error in errors]

    return jsonify(errors)
