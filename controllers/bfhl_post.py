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
                "user_id": "bhuvnesh_bagri_20052003",
                "email": "bhuvneshbagri6@gmail.com",
                "roll_number": "21BCE2629",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": highest_lowercase_alphabet,
            }
        )

    else:
        return "No Input JSON detected", 400
