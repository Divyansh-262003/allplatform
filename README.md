# AllPlatform - Social Media Management Platform

A unified platform for managing and publishing content across multiple social media platforms simultaneously.

## Features

- **Cross-Platform Posting**: Write once, publish everywhere (Twitter, LinkedIn, Instagram)
- **Smart Content Validation**: Real-time validation for platform-specific requirements
- **Scheduled Publishing**: Plan and schedule your posts for optimal timing
- **Secure Authentication**: Safe and secure OAuth integration with social platforms
- **API Rate Limit Management**: Smart handling of API restrictions
- **Post Analytics**: Track your post performance across platforms

## Tech Stack

- **Frontend**: React.js with Tailwind CSS
- **Backend**: Flask (Python)
- **Authentication**: OAuth 2.0
- **Database**: [Your database choice]

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- Python (v3.8 or higher)
- npm or yarn

### Installation

1. Clone the repository:

```bash
git clone [your-repo-url]
cd allplatform
```

2. Frontend setup:

```bash
cd frontend
npm install
npm start
```

3. Backend setup:

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Environment Variables

Create `.env` files in both frontend and backend directories:

```env
# Frontend
REACT_APP_API_URL=http://localhost:5000

# Backend
TWITTER_API_KEY=your_key
LINKEDIN_API_KEY=your_key
INSTAGRAM_API_KEY=your_key
```

## API Documentation

[Add your API documentation here]

## Contributing

[Add contribution guidelines]

## License

[Add your license]
