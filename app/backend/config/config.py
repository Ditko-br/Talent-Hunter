import os 

class Config:
    # init database in sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)

    # Mail settings (Flask-Mail)
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", "587"))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "true").lower() == "true"
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL", "false").lower() == "true"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", MAIL_USERNAME or "no-reply@example.com")

    # Scraper defaults
    SCRAPER_USER_AGENT = os.getenv(
        "SCRAPER_USER_AGENT",
        "TalentHunterBot/1.0 (+https://example.com) Python-requests"
    )
    SCRAPER_TIMEOUT = int(os.getenv("SCRAPER_TIMEOUT", "15"))
