# RetailShield AI Backend

A comprehensive Flask-based backend for smart threat detection in retail platforms. This system monitors login attempts, detects various security threats, and provides automated blocking and alerting capabilities.

## Features

### 🔐 Authentication & Monitoring
- User login API with comprehensive logging
- IP address and geolocation tracking
- Login attempt history with timestamps

### 🛡️ Threat Detection
- **Brute Force Detection**: Identifies multiple failed login attempts from the same IP
- **Off-Hours Login Detection**: Flags logins during suspicious hours (12 AM - 6 AM)
- **Unusual Location Detection**: Alerts when users log in from new countries

### 🚫 Blocking System
- Temporary IP and user blocking (15 minutes default)
- Automatic blocking based on threat detection
- Manual unblocking via admin APIs

### 📧 Alert System
- Email notifications to administrators
- Optional SMS alerts via Twilio
- Detailed threat information in alerts

### 👨‍💼 Admin Dashboard APIs
- View all login logs with filtering options
- Monitor currently blocked IPs and users
- Security statistics and analytics
- Manual unblocking capabilities

## Quick Start

### 1. Installation

\`\`\`bash
# Clone the repository
git clone <repository-url>
cd retailshield-ai-backend

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
\`\`\`

### 2. Configuration

Edit the `.env` file with your settings:

\`\`\`env
# Email Configuration (required for alerts)
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
ADMIN_EMAIL=admin@yourcompany.com

# Admin token for API access
ADMIN_TOKEN=your-secure-admin-token

# Optional: Twilio for SMS alerts
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token
TWILIO_PHONE_NUMBER=+1234567890
ADMIN_PHONE=+1987654321
\`\`\`

### 3. Run the Application

\`\`\`bash
python app.py
\`\`\`

The server will start on `http://localhost:5000`

## API Endpoints

### Authentication

#### POST `/api/login`
Login endpoint with threat detection.

**Request:**
\`\`\`json
{
  "username": "admin",
  "password": "admin123"
}
\`\`\`

**Response (Success):**
\`\`\`json
{
  "message": "Login successful",
  "username": "admin",
  "location": {
    "country": "United States",
    "city": "New York"
  },
  "timestamp": "2024-01-15T10:30:00"
}
\`\`\`

#### GET `/api/status`
Get current security status.

### Admin APIs

All admin APIs require the `Authorization` header with your admin token:
\`\`\`
Authorization: Bearer your-admin-token
\`\`\`

#### GET `/api/admin/logs`
Get login logs with optional filtering.

**Query Parameters:**
- `limit`: Number of recent logs to return
- `username`: Filter by specific username
- `success`: Filter by success status (true/false)

#### GET `/api/admin/blocks`
Get currently blocked IPs and users.

#### POST `/api/admin/unblock`
Unblock an IP or user.

**Request:**
\`\`\`json
{
  "type": "ip",
  "value": "192.168.1.100"
}
\`\`\`

#### GET `/api/admin/stats`
Get security statistics and analytics.

## Demo Users

The system includes hardcoded demo users:

- `admin` / `admin123`
- `john_doe` / `password123`
- `jane_smith` / `secure456`
- `test_user` / `test123`

## Testing with Postman

1. Import the `postman_examples.json` file into Postman
2. Update the admin token in the Authorization headers
3. Test various scenarios:
   - Successful logins
   - Failed login attempts (to trigger brute force detection)
   - Off-hours testing (modify system time or off-hours settings)
   - Admin API calls

## Security Features

### Threat Detection Rules

1. **Brute Force**: 5 failed attempts from same IP within 10 minutes
2. **Off Hours**: Logins between 12 AM - 6 AM UTC
3. **Unusual Location**: Login from a country not in user's history

### Blocking Rules

- IPs are blocked after brute force detection
- Users can be blocked for suspicious activity
- Default block duration: 15 minutes
- Blocks automatically expire

### Alert Triggers

Alerts are sent when any threat is detected:
- Email alerts (always sent if configured)
- SMS alerts (if Twilio is configured)
- Detailed threat information included

## File Structure

\`\`\`
retailshield-ai-backend/
├── app.py                 # Main Flask application
├── config/
│   ├── __init__.py
│   └── config.py         # Configuration settings
├── models/
│   ├── __init__.py
│   └── user.py           # User model with demo data
├── routes/
│   ├── __init__.py
│   ├── auth_routes.py    # Authentication endpoints
│   └── admin_routes.py   # Admin dashboard endpoints
├── utils/
│   ├── __init__.py
│   ├── logger.py         # Login logging system
│   ├── geo_location.py   # IP geolocation service
│   ├── threat_detector.py # Threat detection logic
│   ├── blocking_system.py # IP/User blocking system
│   └── alert_system.py   # Email/SMS alerting
├── data/                 # Runtime data storage
├── logs/                 # Application logs
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # This file
\`\`\`

## Production Considerations

1. **Database**: Replace JSON file storage with a proper database (PostgreSQL, MySQL)
2. **Authentication**: Implement proper user authentication with hashed passwords
3. **Rate Limiting**: Add rate limiting middleware
4. **HTTPS**: Use HTTPS in production
5. **Monitoring**: Add application monitoring and logging
6. **Scaling**: Consider Redis for session storage and blocking data

## Troubleshooting

### Email Alerts Not Working
- Verify SMTP settings in `.env`
- For Gmail, use App Passwords instead of regular password
- Check firewall settings for SMTP ports

### Geolocation Not Working
- The system uses ipapi.co which has rate limits
- Local IPs (127.0.0.1, 192.168.x.x) return "Local" as location
- Check internet connectivity

### Admin APIs Returning 401
- Verify the `Authorization` header format: `Bearer your-token`
- Check that `ADMIN_TOKEN` in `.env` matches the token in requests

## License

This project is for demonstration purposes. Please ensure compliance with your organization's security policies before using in production.
