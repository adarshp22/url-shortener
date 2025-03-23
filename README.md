# URL Shortener API

A simple URL shortening service similar to Bit.ly, built with **Flask** and **PostgreSQL**, and deployed on **Railway**.

##  Features
- **Shorten URLs**: Generate a short URL for a given long URL.
- **Redirect to Original URL**: Short links automatically redirect users.
- **Track Clicks**: Monitor the number of times a short link is accessed.
- **Ensure Uniqueness**: The same long URL always maps to the same short code.
- **Database Integration**: Store mappings between long and short URLs using PostgreSQL.
- **Consistent Short Links**: The same long URL always maps to the same short code.

---

## 📌 API Endpoints

### 1️⃣ Shorten a URL
- **Endpoint**: `POST /shorten`
- **Description**: Converts a long URL into a short URL.
- **Request Body (JSON)**:
  ```json
  {
    "long_url": "https://www.codechef.com/learn"
  }
  ```
- **Response (JSON)**:
  ```json
  {
    "short_url": "https://url-shortener-production-8cc2.up.railway.app/a1a68f"
  }
  ```

### 2️⃣ Redirect to Original URL
- **Endpoint**: `GET /<short_code>`
- **Description**: Redirects users to the original long URL.
- **Example**: Accessing `https://url-shortener-production-8cc2.up.railway.app/a1a68f` redirects to `https://www.codechef.com/learn`.

### 3️⃣ Get Click Statistics
- **Endpoint**: `GET /stats/<short_code>`
- **Description**: Fetch statistics for a short URL.
- **Example Request**:
  ```bash
  GET https://url-shortener-production-8cc2.up.railway.app/stats/a1a68f
  ```
- **Example Response (JSON)**:
  ```json
  {
    "long_url": "https://www.codechef.com/learn",
    "short_url": "https://url-shortener-production-8cc2.up.railway.app/a1a68f",
    "click_count": 5
  }
  ```
### Handling edge cases:

If users forget to add http:// or https://, the system automatically appends https:// to ensure proper redirection.

Updated Code in **app.py**:

long_url = data.get('long_url').strip()

# Ensure the URL starts with http:// or https://
if not long_url.startswith(("http://", "https://")):
    long_url = "https://" + long_url

**Converts google.com → https://google.com** 
**Ensures all links redirect properly**
---

##  How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and define your **PostgreSQL Database URL**:
```
DATABASE_URL=postgresql://username:password@localhost/url_shortener
```

### 5️⃣ Initialize the Database
```python
from app import db
from app import app

with app.app_context():
    db.create_all()
```

### 6️⃣ Run the Server
```bash
flask run  # or python app.py
```

The API should now be running on `http://127.0.0.1:5000/`.

---

## 🛠️ Deployment
###  **Deploying on Railway**
1. Sign up at [Railway](https://railway.app/)
2. Create a new project and connect your GitHub repository.
3. Add an environment variable `DATABASE_URL` pointing to your PostgreSQL instance.
4. Deploy and obtain your production URL.

---

## 📝 Additional Notes
- The same long URL always generates the same short URL.
- The short links are **not actually shorter than Railway’s domain** (consider using a custom domain for truly short URLs).
- Statistics tracking allows you to see how many times a short link has been accessed.

---



---

## 📞 Contact
For any queries, reach out to me at:
- **Email**: adarshp22@iitk.ac.in
- **GitHub**: [github.com/adarshp22](https://github.com/adarshp22)
- **LinkedIn**: [linkedin.com/in/adarsh-pal-816764255](https://www.linkedin.com/in/adarsh-pal-816764255/)

