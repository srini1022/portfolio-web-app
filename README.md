# Portfolio Web Application

This is a simple, responsive portfolio web application built as part of the hiring assessment for **Twenty20 Systems**.

The application provides user registration and login functionality and displays a personal portfolio page after successful authentication.

---

## 🚀 Features

- User Registration (Email & Password)
- Secure Login with authentication
- Password hashing using Werkzeug
- Portfolio page with:
  - About section
  - Skills
  - Projects
  - Certificates
  - Contact details
- Resume download option
- Logout functionality
- Responsive design (Desktop & Mobile)

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Tailwind CSS
- **Backend:** Python (Flask)
- **Database:** MySQL
- **Authentication:** Flask Sessions
- **Deployment:** Cloud Hosting (Live Demo)

---

## 📂 Project Structure

portfolio-web-app/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│ ├── login.html
│ ├── register.html
│ └── portfolio.html
├── static/
│ ├── css/
│ ├── js/
│ ├── img/
│ └── resume/
└── .env (ignored)



---

## ⚙️ Local Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/<your-username>/portfolio-web-app.git


2.Create and activate virtual environment

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt


4. Configure environment variables
Create a .env file in the root directory:

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=portfolio_app
SECRET_KEY=your_secret_key


5. Run the application
python app.py

🔐 Authentication Flow

User registers with email and password
Password is securely hashed and stored in the database
User logs in using registered credentials
Successful login redirects to the portfolio page
Logout clears the session and redirects to the landing page

🌐 Live Demo
👉 Live URL: (Will be added after deployment)

👤 Author
Srinidhi M D
📧 Email: srinidhidevraj2267@gmail.com
📞 Phone: +91 9110414399
💻 GitHub: https://github.com/srini1022
🔗 LinkedIn: https://linkedin.com/in/srinidhimd22