from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        input_data = request.get_json()
        data = input_data.get('data', [])
        
        # User details
        user_id = "jyothsna_hanumanthu_12012005"  
        email = "hanumanthu.jyothsna2022@vitstudent.ac.in"
        roll_number = "22BDS0065"
        
        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        num_sum = 0
        all_chars = []
        
        for item in data:
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                num_sum += num
            elif item.isalpha():
                alphabets.append(item.upper())
                for c in item:
                    all_chars.append(c)
            else:
                special_characters.append(item)
        
        # Build concat_string
        reverse_chars = all_chars[::-1]
        concat_string = ''
        for i, c in enumerate(reverse_chars):
            if i % 2 == 0:
                concat_string += c.upper()
            else:
                concat_string += c.lower()
        
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(num_sum),
            "concat_string": concat_string
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)