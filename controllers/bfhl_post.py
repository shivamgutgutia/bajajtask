from flask import request, jsonify


def bfhl_post():
    if request.is_json:
        data = request.get_json()
        req = data["data"]
        numbers = []
        alphabets = []
        highest_lowercase_alphabet = []
        for i in req[::-1]:
            if i.isdigit():
                numbers.append(i)
            elif i.isalpha():
                alphabets.append(i)
                if i.islower():
                    if not highest_lowercase_alphabet:
                        highest_lowercase_alphabet.append(i)
        numbers.reverse()
        alphabets.reverse()
        return jsonify(
            {
                "is_success": "true",
                "user_id": "john_doe_17091999",
                "email": "john@xyz.com",
                "roll_number": "ABCD123",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": highest_lowercase_alphabet,
            }
        )

    else:
        return "No Input JSON detected", 400
