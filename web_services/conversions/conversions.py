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
@app.route("/v1/grams/<float:grams>")
@app.route("/v1/ounces/<float:ounces>")
def convert(miles=None, kilometers=None, grams=None, ounces=None):
    unit = None
    if miles:
        unit = formulas.miles_to_kilometers(miles)
    elif kilometers:
        unit = formulas.kilometers_to_miles(kilometers)
    elif grams:
        unit = formulas.grams_to_ounces(grams)
    elif ounces:
        unit = formulas.ounces_to_grams(ounces)

    return conversion(unit=unit)


@app.errorhandler(500)
def internal_server_error(error):
    return str(json.dumps({"message": Exception})), 500


@app.errorhandler(404)
def not_found_error(error):
    return str(json.dumps({"message": 'Try entering a decimal'})), 404


if __name__ == "__main__":
    app.run(debug=False)

