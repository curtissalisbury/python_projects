# Metric to English Unit Converter
# A Webservice to convert English to Metric and Metric to English

from flask import Flask, json
import web_services.conversions.formulas as formulas

app = Flask(__name__)


def conversion(unit: None):
    ret_unit = {"unit": unit}
    return json.dumps(ret_unit)


@app.route("/v1/miles/<float:miles>")
@app.route("/v1/kilometers/<float:kilometers>")
def convert(miles=None, kilometers=None):
    unit = None
    if miles:
        unit = formulas.miles_to_kilometers(miles)
    elif kilometers:
        unit = formulas.kilometers_to_miles(kilometers)

    return conversion(unit=unit)


@app.errorhandler(500)
def internal_server_error(error):
    return str(json.dumps({"message": Exception})), 500


if __name__ == "__main__":
    app.run(debug=False)

# TODO - Add error handling that is displayed to the user
