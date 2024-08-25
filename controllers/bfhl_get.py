from flask import jsonify


def bfhl_get():
    return (jsonify({"operation_code": 1}), 200)
