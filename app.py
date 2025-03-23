# import os
# from flask import Flask, request, redirect, jsonify, render_template
# from flask_sqlalchemy import SQLAlchemy
# import hashlib

# app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Adarshpal021%40@localhost/url_shortener'
# # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# db = SQLAlchemy(app)

# class URLMapping(db.Model):
#     __tablename__ = 'urls'
#     id = db.Column(db.Integer, primary_key=True)
#     long_url = db.Column(db.String(500), unique=True, nullable=False)
#     short_code = db.Column(db.String(10), unique=True, nullable=False)
#     click_count=db.Column(db.Integer, default=0)

#     def __init__(self, long_url, short_code):
#         self.long_url = long_url
#         self.short_code = short_code
#         self.click_count=0  

# # Create the database tables
# with app.app_context():
#     db.create_all()

# def generate_short_code(long_url):
#     """Generate a short unique code using a hash."""
#     return hashlib.md5(long_url.encode()).hexdigest()[:6]  # First 6 chars

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/shorten', methods=['POST'])
# # def shorten_url():
# #     """Shorten a given long URL."""
# #     data = request.json
# #     long_url = data.get('long_url')

# #     if not long_url:
# #         return jsonify({'error': 'URL is required'}), 400

# #     # Check if URL already exists
# #     existing_entry = URLMapping.query.filter_by(long_url=long_url).first()
# #     if existing_entry:
# #         short_code = existing_entry.short_code
# #     else:
# #         short_code = generate_short_code(long_url)
# #         new_entry = URLMapping(long_url, short_code)
# #         db.session.add(new_entry)
# #         db.session.commit()

# #     return jsonify({'short_url': f"http://localhost:5000/{short_code}"})

# # def shorten_url():
# #     """Shorten a given long URL."""
# #     data=request.json #added
# #     long_url = request.form.get('long_url')  # ✅ Changed from `request.json.get(...)` to `request.form.get(...)`

# #     if not long_url:
# #         return jsonify({'error': 'URL is required'}), 400

# #     # Check if URL already exists
# #     existing_entry = URLMapping.query.filter_by(long_url=long_url).first()
# #     if existing_entry:
# #         short_code = existing_entry.short_code
# #     else:
# #         short_code = generate_short_code(long_url)
# #         new_entry = URLMapping(long_url, short_code)
# #         db.session.add(new_entry)
# #         db.session.commit()

# #     return jsonify({'short_url': f"http://127.0.0.1:5000/{short_code}"})

# # RAILWAY_BASE_URL = "https://url-shortener-production-8cc2.up.railway.app"

# # def shorten_url():
# #     """Shorten a given long URL."""
# #     if request.content_type != 'application/json':
# #         return jsonify({'error': 'Invalid content type. Use application/json'}), 415

# #     try:
# #         data = request.get_json()
# #         print("Received Data:", data)  # ✅ Debugging print statement
# #     except Exception as e:
# #         print("JSON Parsing Error:", str(e))
# #         return jsonify({'error': 'Invalid JSON format'}), 400

# #     if not data or 'long_url' not in data:
# #         return jsonify({'error': 'URL is required'}), 400

# #     long_url = data.get('long_url')
# #     if not long_url.strip():  # Prevent empty URLs
# #         return jsonify({'error': 'URL cannot be empty'}), 400

# #     # Check if URL already exists
# #     existing_entry = URLMapping.query.filter_by(long_url=long_url).first()
# #     if existing_entry:
# #         short_code = existing_entry.short_code
# #     else:
# #         short_code = generate_short_code(long_url)
# #         new_entry = URLMapping(long_url, short_code)
# #         db.session.add(new_entry)
# #         db.session.commit()

# #     return jsonify({'short_url': f"http://127.0.0.1:5000/{short_code}"})
#     # return jsonify({'short_url': f"https://url-shortener-production-8cc2.up.railway.app"{short_code}})
# def shorten_url():
#     """Shorten a given long URL."""
#     if request.content_type != 'application/json':
#         return jsonify({'error': 'Invalid content type. Use application/json'}), 415

#     try:
#         data = request.get_json()
#         print("Received Data:", data)  # ✅ Debugging print statement
#     except Exception as e:
#         print("JSON Parsing Error:", str(e))
#         return jsonify({'error': 'Invalid JSON format'}), 400

#     if not data or 'long_url' not in data:
#         return jsonify({'error': 'URL is required'}), 400

#     long_url = data.get('long_url').strip()
#     if not long_url:
#         return jsonify({'error': 'URL cannot be empty'}), 400

#     # Check if URL already exists
#     existing_entry = URLMapping.query.filter_by(long_url=long_url).first()
#     if existing_entry:
#         short_code = existing_entry.short_code
#     else:
#         short_code = generate_short_code(long_url)
#         new_entry = URLMapping(long_url=long_url, short_code=short_code)
#         db.session.add(new_entry)
#         db.session.commit()

#     return jsonify({'short_url': f"https://url-shortener-production-8cc2.up.railway.app/{short_code}"})

# @app.route('/<short_code>', methods=['GET'])
# def redirect_url(short_code):
#     """Redirect to the original long URL."""
#     mapping = URLMapping.query.filter_by(short_code=short_code).first()
#     if mapping:
#         mapping.click_count+=1
#         db.session.commit()
#         return redirect(mapping.long_url)
#     return jsonify({'error': 'URL not found'}), 404

# @app.route('/stats/<short_code>', methods=['GET'])

# def get_stats(short_code):
#     """Fetch statistics for a short URL."""
#     mapping = URLMapping.query.filter_by(short_code=short_code).first()
#     if mapping:
#         return jsonify({
#             'long_url': mapping.long_url,
#             'short_url': f"http://localhost:5000/{short_code}",
#             'click_count': mapping.click_count  # 🔹 Return the number of times accessed
#         })
#     return jsonify({'error': 'URL not found'}), 404


# if __name__ == '__main__':
#     app.run(debug=True)




import os
from flask import Flask, request, redirect, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import hashlib
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

class URLMapping(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(500), unique=True, nullable=False)
    short_code = db.Column(db.String(6), unique=True, nullable=False)
    click_count = db.Column(db.Integer, default=0)

    def __init__(self, long_url, short_code):
        self.long_url = long_url
        self.short_code = short_code
        self.click_count = 0  

# Create the database tables
with app.app_context():
    db.create_all()

# Base62 Encoding (Shortens URL)
BASE62_ALPHABET = string.ascii_letters + string.digits  # a-zA-Z0-9

def base62_encode(num, length=6):
    """Convert a number into a short Base62 string."""
    if num == 0:
        return BASE62_ALPHABET[0] * length
    encoded = []
    base = len(BASE62_ALPHABET)
    while num:
        encoded.append(BASE62_ALPHABET[num % base])
        num //= base
    return ''.join(encoded[::-1]).rjust(length, BASE62_ALPHABET[0])

def generate_short_code(long_url):
    """Generate a short, unique code using Base62 encoding."""
    hash_value = int(hashlib.md5(long_url.encode()).hexdigest(), 16)
    return base62_encode(hash_value % (62**6), length=6)  # Shorten to 6 chars

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Shorten a given long URL."""
    if request.content_type != 'application/json':
        return jsonify({'error': 'Invalid content type. Use application/json'}), 415

    try:
        data = request.get_json()
    except Exception:
        return jsonify({'error': 'Invalid JSON format'}), 400

    if not data or 'long_url' not in data:
        return jsonify({'error': 'URL is required'}), 400

    long_url = data.get('long_url').strip()
    if not long_url:
        return jsonify({'error': 'URL cannot be empty'}), 400

    # Check if URL already exists
    existing_entry = URLMapping.query.filter_by(long_url=long_url).first()
    if existing_entry:
        short_code = existing_entry.short_code
    else:
        short_code = generate_short_code(long_url)
        new_entry = URLMapping(long_url=long_url, short_code=short_code)
        db.session.add(new_entry)
        db.session.commit()

    return jsonify({'short_url': f"https://url-shortener-production-8cc2.up.railway.app/{short_code}"})

@app.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    """Redirect to the original long URL."""
    mapping = URLMapping.query.filter_by(short_code=short_code).first()
    if mapping:
        mapping.click_count += 1
        db.session.commit()
        return redirect(mapping.long_url)
    return jsonify({'error': 'URL not found'}), 404

@app.route('/stats/<short_code>', methods=['GET'])
def get_stats(short_code):
    """Fetch statistics for a short URL."""
    mapping = URLMapping.query.filter_by(short_code=short_code).first()
    if mapping:
        return jsonify({
            'long_url': mapping.long_url,
            'short_url': f"https://url-shortener-production-8cc2.up.railway.app/{short_code}",
            'click_count': mapping.click_count
        })
    return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
