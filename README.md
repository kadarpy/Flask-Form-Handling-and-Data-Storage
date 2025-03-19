# Flask Form Handling and Data Storage

## 📌 Project Overview
This project is a simple **Flask-based web application** that allows users to submit a form with details such as Name, Email, Phone, Age, Gender, and Address. The submitted data is stored in an **SQLite/MySQL database** and displayed on a separate page in a structured table.

## 🚀 Features
- 📝 **User Form** with validation for required fields and proper formatting.
- 🗄 **Database Storage** using Flask-SQLAlchemy (SQLite/MySQL).
- 📊 **User Data Display** in a table format.
- 🎨 **Modern UI Styling** with Bootstrap and custom CSS.
- 📂 **Organized Project Structure** with templates and static files.

---

## 🛠 Tech Stack
| Component  | Technology |
|------------|------------|
| **Backend** | Flask, Flask-SQLAlchemy |
| **Frontend** | HTML, CSS, JavaScript (Bootstrap) |
| **Database** | SQLite/MySQL |

---

## 📂 Project Structure
```
my_flask_app/
├── app.py  # Main Flask application
├── templates/
│   ├── index.html  # Form page
│   ├── users.html  # Data display page
├── static/
│   ├── styles.css  # Custom styling
├── users.db  # SQLite database file (if using SQLite)
├── README.md  # Project documentation
```

---

## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask Application
```bash
python app.py
```

🚀 The app will run on **http://127.0.0.1:5000/**

---

## 🖥 Usage
- Open **http://127.0.0.1:5000/** in your browser.
- Fill out the form and submit it.
- View submitted data on the **Users Page** (`/users`).

---

## 🔧 Troubleshooting
- If you get a **database error**, try deleting `users.db` and running the app again.
- Ensure Flask and dependencies are installed using `pip install -r requirements.txt`.

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

## 🌟 Contributing
Feel free to contribute by opening issues or submitting pull requests. Happy coding! 🚀

