
from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Step 1: Connect to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service-account.json", scope)
client = gspread.authorize(creds)

# Step 2: Open the correct sheet using the spreadsheet key
sheet = client.open_by_key("1qAbGLzTWa9Vo8f-5a5yjLs8HK3B5KtHrxLCeE6Moqzs").sheet1

# Step 3: Route to handle both GET and POST requests
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_id = request.form.get("user_id")  # Get user input from the form
        data = sheet.get_all_records()         # Fetch all rows as dictionaries
        for row in data:
            if str(row.get("USER_ID")) == user_id:
                result = row
                break
        if not result:
            result = f"No data found for User ID: {user_id}"
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
