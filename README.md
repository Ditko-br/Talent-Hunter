# Talent Hunter - Job Automation Platform

A comprehensive job automation platform that helps users receive personalized job notifications based on their specific preferences. The platform scrapes job listings from multiple sources including LinkedIn, Gupy, company talent centers, and other job boards.

## Features

### 🎯 Smart Job Matching
- **Area Selection**: Choose from various professional areas (Technology, Design, Communication, Marketing, Sales, etc.)
- **Specialized Subtypes**: Detailed categorization within each area
  - Technology: Data Science, Software Engineering, IT Management, Technical Support, etc.
  - Design: UI/UX, Graphic Design, Product Design, etc.
  - Marketing: Digital Marketing, Content Marketing, Growth Marketing, etc.
- **Seniority Levels**: Junior, Mid-level, Senior, Lead, Management positions
- **Geographic Preferences**: Brazil, USA, EU, Remote positions

### 📧 Automated Notifications
- Email notifications for matching job opportunities
- Customizable notification frequency
- Detailed job information including company, location, and requirements

### 🔍 Multi-Source Job Scraping
- **LinkedIn**: Professional network job listings
- **Gupy**: Brazilian recruitment platform
- **Company Career Pages**: Direct corporate talent centers
- **Extensible Architecture**: Easy to add new job sources

### 👤 User Management
- Secure user authentication and registration
- Personalized dashboard with job preferences
- Profile management and notification settings

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLAlchemy ORM
- **Web Scraping**: BeautifulSoup, Selenium, Requests
- **Email Service**: SMTP integration
- **Frontend**: HTML5, CSS3, JavaScript
- **Task Scheduling**: APScheduler for automated job scraping
- **Authentication**: Flask-Login

## Project Structure

```
talent-hunter/
├── app.py                  # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── app/
│   ├── backend/
│   │   ├── config/
│   │   │   └── config.py           # Application configuration
│   │   ├── routes/
│   │   │   ├── auth.py             # Authentication routes
│   │   │   ├── companies.py        # Company management
│   │   │   ├── keywords.py         # Keyword management
│   │   │   ├── search.py           # Job search functionality
│   │   │   └── users.py            # User management
│   │   ├── schemas/
│   │   │   └── schemas.py          # Data validation schemas
│   │   ├── services/
│   │   │   ├── email.py            # Email notification service
│   │   │   ├── job_scraper.py      # Main scraping orchestrator
│   │   │   ├── notification.py     # Notification management
│   │   │   └── scheduler.py        # Task scheduling
│   │   └── models/
│   │       ├── job.py              # Job data models
│   │       ├── models.py           # Core data models
│   │       ├── notification.py     # Notification models
│   │       └── user.py             # User models
│   └── frontend/
│       ├── js/                     # JavaScript files
│       ├── styles/                 # CSS stylesheets
│       └── templates/              # HTML templates
└── tests/                          # Test suites
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/talent-hunter.git
   cd talent-hunter
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize the database**
   ```bash
   python app.py db init
   python app.py db migrate
   python app.py db upgrade
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Database
DATABASE_URL=sqlite:///talent_hunter.db

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Application Settings
SECRET_KEY=your-secret-key-here
FLASK_ENV=development

# Scraping Configuration
SCRAPING_INTERVAL=3600  # seconds
MAX_CONCURRENT_SCRAPERS=5

# External APIs (if needed)
LINKEDIN_API_KEY=your-linkedin-api-key
GUPY_API_KEY=your-gupy-api-key
```

## Usage

### For Users

1. **Register an Account**: Create a new account with email verification
2. **Set Preferences**: Configure your job search criteria:
   - Select professional areas of interest
   - Choose specific subtypes within those areas
   - Set preferred seniority levels
   - Define geographic preferences
3. **Receive Notifications**: Get email alerts when matching jobs are found
4. **Manage Settings**: Update preferences and notification frequency

### For Developers

1. **Adding New Job Sources**: Implement new scrapers in `app/backend/services/`
2. **Custom Filters**: Extend the filtering logic in the services layer
3. **UI Enhancements**: Modify templates and styles in the frontend directory

## API Endpoints

- `POST /auth/register` - User registration
- `POST /auth/login` - User authentication
- `GET /users/profile` - Get user profile
- `PUT /users/preferences` - Update job preferences
- `GET /jobs/search` - Search job listings
- `GET /notifications` - Get user notifications

## Scraping Strategy

The platform implements a respectful scraping approach:

- **Rate Limiting**: Controlled request frequency to avoid overwhelming servers
- **User-Agent Rotation**: Mimics real browser behavior
- **Proxy Support**: Optional proxy rotation for large-scale scraping
- **Error Handling**: Robust error recovery and logging
- **Data Validation**: Ensures scraped data quality and consistency

## Job Categories

### Technology
- Data Science & Analytics
- Software Engineering
- DevOps & Infrastructure
- Cybersecurity
- IT Management
- Technical Support
- Quality Assurance
- Mobile Development
- Web Development
- AI/Machine Learning

### Design
- UI/UX Design
- Graphic Design
- Product Design
- Brand Design
- Motion Graphics
- Web Design

### Marketing
- Digital Marketing
- Content Marketing
- Growth Marketing
- SEO/SEM
- Social Media Marketing
- Email Marketing
- Product Marketing

### Sales
- Inside Sales
- Outside Sales
- Sales Development
- Account Management
- Business Development
- Sales Operations

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Testing

Run the test suite:

```bash
python -m pytest tests/
```

Run with coverage:

```bash
python -m pytest tests/ --cov=app
```

## Roadmap

- [ ] **Mobile App**: React Native mobile application
- [ ] **Advanced Analytics**: Job market insights and trends
- [ ] **Company Profiles**: Detailed company information and reviews
- [ ] **Salary Insights**: Compensation data and trends
- [ ] **AI Recommendations**: Machine learning-powered job matching
- [ ] **Video Interviews**: Integrated video interview platform
- [ ] **Skills Assessment**: Technical and soft skills evaluation
- [ ] **Career Guidance**: Personalized career development paths

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support and questions:
- Email: contatoditko@gmail.com
- Create an issue on GitHub
- Check the [Wiki](https://github.com/Ditko-br/Talent-Hunter/docs/wiki.md) for documentation

## Acknowledgments

- Thanks to all job board platforms for providing public job listings
- Open source libraries that make this project possible
- Community contributors and testers

---

**Talent Hunter** - Finding the right opportunities, automatically. 