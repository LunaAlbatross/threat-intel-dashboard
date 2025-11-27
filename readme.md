🚨 Threat Intelligence Dashboard

A real-time Threat Intelligence & Firewall Control Dashboard built using Flask, MariaDB, and UFW.
It automatically fetches malicious URLs from Abuse.ch (URLhaus), blocks their IPs at the OS firewall level, and provides a web-based interface to monitor and unblock threats interactively.

✨ Key Features

✅ Real-time malicious URL ingestion from Abuse.ch URLhaus

✅ Automatic outbound IP blocking using UFW

✅ Persistent storage using MariaDB/MySQL

✅ Live Flask-based web dashboard

✅ Auto-refreshing table (every 30 seconds)

✅ One-click Unblock from the dashboard

✅ Status display: Active / Neutralized

✅ Secure database access with a dedicated DB user

🛠 Tech Stack

Backend: Python, Flask

Database: MariaDB / MySQL

Firewall: UFW (Linux)

Frontend: HTML, CSS, JavaScript

Threat Feed: Abuse.ch URLhaus

Scheduler: Custom Python background task

📁 Project Structure

threat-intel-dashboard/
│
├── app.py # Flask web server & API routes
├── scheduler.py # Periodic fetch scheduler
├── unblock_urls.py # Firewall unblock logic
├── requirements.txt # Python dependencies
│
├── db/
│ └── init_db.sql # Database initialization script
│
├── fetcher/
│ ├── init.py
│ └── abusech.py # Abuse.ch fetch + block logic
│
└── templates/
└── index.html # Dashboard UI

⚙️ Setup Instructions
1️⃣ Clone the Repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git


cd threat-intel-dashboard

2️⃣ Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3️⃣ Start MariaDB / MySQL

sudo systemctl start mysql
or
sudo systemctl start mariadb

4️⃣ Initialize the Database

mysql -u root -p < db/init_db.sql

5️⃣ Create a Dedicated Database User (Recommended)

Login to MariaDB:

sudo mysql

CREATE USER 'threat_user'@'localhost' IDENTIFIED BY 'StrongPass123';
GRANT ALL PRIVILEGES ON threat_dashboard.* TO 'threat_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

Update DB credentials in:

app.py

fetcher/abusech.py

unblock_urls.py

🔐 Firewall Permission Setup (IMPORTANT)

To allow the dashboard to unblock URLs without running Flask as root, configure sudo:

Step 1: Find UFW path

which ufw

Example output:
/usr/sbin/ufw

Step 2: Edit sudoers file

sudo visudo

Add this at the bottom (replace path if needed):

albatross ALL=(ALL) NOPASSWD: /usr/sbin/ufw

✅ Prevents password prompts
✅ Prevents backend hanging
✅ Enables instant unblock from the dashboard

▶️ Running the Application
Start the Threat Fetcher & Auto Blocker

source venv/bin/activate
python scheduler.py

Start the Flask Dashboard

In a new terminal:

source venv/bin/activate
python app.py

Open in your browser:

http://127.0.0.1:5000/

🔁 System Workflow
🔹 Threat Fetching & Auto-Blocking

Scheduler calls fetch_abusech_data()

Latest malicious URLs are downloaded from Abuse.ch

Data is parsed and inserted into MariaDB

Each domain is resolved to an IP

IP is blocked using:

ufw deny out to <IP>

🔹 Dashboard Unblock Operation

User clicks Unblock in the UI

JavaScript sends a POST request to /unblock

Flask calls unblock_url(url)

Firewall rule is removed using:

ufw delete deny out to <IP>

UI updates instantly

🔐 Security Considerations

Uses a non-root database user

Uses OS-level firewall (UFW) instead of application-level blocking

Supports secure permission handling via sudoers

Can be extended with authentication for production use

📊 Future Enhancements

📈 Threat analytics & visual charts

👤 Authentication & role-based access

📋 Unblock audit logging

📤 CSV/PDF report export

🌐 Multi-feed threat intelligence (PhishTank, VirusTotal, etc.)

👤 Author

Kowshik Thiruppathi
Cybersecurity & Threat Intelligence Enthusiast
GitHub: Add your GitHub profile link here

If you want, I can also generate:

A short ATS-friendly README

A resume project description

Or an architecture diagram next.