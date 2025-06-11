from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the input from the user
    data = request.json  # Expecting JSON input
    input_text = data.get('text', '').replace(" ", "").lower()

    # Define letter values
    letter_values = {
        'a': 1, 'i': 1, 'q': 1, 'y': 1,
        'b': 2, 'j': 2, 'r': 2, 'z': 2,
        'c': 3, 'k': 3, 's': 3,
        'd': 4, 'l': 4, 't': 4,
        'e': 5, 'm': 5, 'u': 5,
        'f': 6, 'n': 6, 'v': 6,
        'g': 7, 'o': 7, 'w': 7,
        'h': 8, 'p': 8, 'x': 8
    }

    # Calculate the total sum of the input letters
    total = sum(letter_values.get(char, 0) for char in input_text)
    return jsonify({'sum': total})

if __name__ == '__main__':
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
