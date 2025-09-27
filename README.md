# Cloud-Sheet-Data-Chatbot
A web-based chatbot built with Flask that retrieves user data from a live Google Sheet using the Google Sheets API via Google Cloud. Users can enter their ID, name, or email to instantly view matching information on a simple web  UI
## 📌 Features
- Live data fetching from Google Sheets/Excel.
- Cloud-based, secure and scalable.
- User-friendly chatbot interface.
## 🛠️ Tech Stack
Python • Google Sheets API • Google Drive API • Flask/Streamlit • Pandas • Cloud Hosting (AWS/GCP)
## 🚀 How It Works
User enters a User ID → Bot queries Google Sheets API → Fetches matching data → Sends formatted reply.
## ⚙️ Setup
1. Clone repo & install dependencies (`pip install -r requirements.txt`).
2. Enable Google Sheets & Drive API in Google Cloud Console.
3. Create service account, download JSON, and add to `.gitignore`.
4. Share your Google Sheet with service account email (Viewer access).
5. Run app with `python app.py`.
## ⚠️ Note :
This app uses Google Sheets API for live data fetching. You need to provide your own service-account.json file (not included for security reasons).
## 📬 Contact
GitHub: [nandeesh88](https://github.com/nandeesh88) • LinkedIn: [Kuruba Nandeesh](https://linkedin.com/in/kuruba-nandeesh) • Instagram: [mr__nandu__gowda](https://instagram.com/mr__nandu__gowda)
