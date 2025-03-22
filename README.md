# URL Shortener

This is a simple URL Shortener built with Flask and PostgreSQL. It allows users to shorten URLs and track usage statistics.

## Features
- Shorten long URLs.
- Redirect users when they visit a short URL.
- Track how many times a short URL has been accessed.

## Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-github-username>/url-shortener.git
cd url-shortener

2️⃣ Install Dependencies
Make sure you have Python and PostgreSQL installed, then run:

bash
Copy
Edit
pip install -r requirements.txt

3️⃣ Configure Database
Open PostgreSQL and create a new database:

sql
Copy
Edit
CREATE DATABASE url_shortener;


Update app.py with your database credentials:

python
Copy
Edit
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@localhost/url_shortener'



4️⃣ Run the Application
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000 in your browser.


API Endpoints
1. Shorten a URL
Request:

bash
Copy
Edit
POST /shorten
Content-Type: application/json

{
  "long_url": "https://www.example.com"
}
Response:

json
Copy
Edit
{
  "short_url": "http://127.0.0.1:5000/abc123"
}
2. Redirect to the Original URL
Request:

bash
Copy
Edit
GET /abc123
Redirects to: https://www.example.com

3. Get URL Statistics
Request:

bash
Copy
Edit
GET /stats/abc123
Response:

json
Copy
Edit
{
  "long_url": "https://www.example.com",
  "short_url": "http://127.0.0.1:5000/abc123",
  "click_count": 5
}
