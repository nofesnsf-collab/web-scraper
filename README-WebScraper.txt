# Web Scraper - Price Monitoring Tool

Automated web scraping tool for extracting product data from e-commerce websites with price monitoring, email alerts, and data export capabilities.

## 🎯 Features

✅ Automated Web Scraping from Multiple Sites
✅ Product Data Extraction (Name, Price, URL)
✅ Price Change Detection & Alerts
✅ Email Notifications for Price Drops
✅ CSV/Excel Export
✅ Historical Data Tracking
✅ Scheduled Execution (Hourly/Daily)
✅ Error Handling & Logging
✅ Duplicate Detection

## 🛠 Technologies

- **Language:** Python 3.8+
- **Web Scraping:** BeautifulSoup4, Requests
- **Data Processing:** Pandas
- **Scheduling:** Schedule, APScheduler
- **Data Storage:** CSV Files
- **Email Notifications:** SMTP (Gmail)
- **Logging:** Python logging module

## 📋 Requirements

- Python 3.8+
- pip
- Internet connection
- Gmail account (for email alerts)

## 🚀 Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/nofesnsf-collab/web-scraper.git
cd web-scraper
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env File
Create a file named `.env` in the root directory:
```
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
TARGET_EMAIL=recipient@gmail.com
```

**Note:** For Gmail, use an [App Password](https://myaccount.google.com/apppasswords), not your regular password.

### 5. Configure Target URL
Edit `main.py` and set your target website:
```python
TARGET_URL = "https://example-ecommerce.com/products"
```

### 6. Run Scraper
```bash
python main.py
```

## 📊 Output Example

CSV file (`output/data.csv`) with columns:
- Product Name
- Price
- URL
- Last Updated
- Availability

## 🔍 Use Cases

- Monitor competitor prices
- Track product availability
- Collect market data for analysis
- Price comparison and alerts
- Automated data collection

## 📈 Features Detail

### Price Monitoring
- Tracks price changes in real-time
- Calculates price differences
- Records historical data

### Scheduled Execution
- Run every hour
- Daily at specific time
- Custom intervals

### Email Alerts
- Automatic email on price drop
- Summary reports
- Custom alert thresholds

## 📧 Contact

Email: nofesnsf@gmail.com
GitHub: github.com/nofesnsf-collab

## 📝 License

MIT License - feel free to use and modify
