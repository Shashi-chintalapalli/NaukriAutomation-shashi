# NaukriAutomation

This project automates updating your **Naukri.com profile headline** using Selenium.  
It logs in with your credentials, navigates to your profile, edits the resume headline, and saves the update.  
This helps in keeping your profile active and visible to recruiters.

---

## 🚀 Features
- Automates login to [Naukri.com](https://www.naukri.com/)
- Updates resume headline automatically
- Uses **Selenium** with Chrome WebDriver
- Can be scheduled to run daily/weekly

---

## ⚙️ Setup Instructions

### 1. Clone this repository


### Install dependencies
pip install -r requirements.txt



🕒 Scheduling the Script
### On macOS/Linux (using cron)

----> Open crontab:

----> crontab -e


Add a line to run daily at 10 AM:

----> 0 10 * * * /usr/bin/python3 /Users/<your-username>/NaukriAutomation/NaukriAutomation.py


Save and exit.
To check scheduled jobs:

crontab -l


### On Windows (Task Scheduler)

 ---->Open Task Scheduler → Create Basic Task.

----> Set the trigger (e.g., daily at 10 AM).

----> In Action, select Start a Program and point to:

python

with Arguments:

----> C:\path\to\NaukriAutomation\NaukriAutomation.py









