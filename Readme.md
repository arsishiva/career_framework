# Wise Analytics Career Framework

A production-ready Streamlit web application that displays the [Wise Analytics Career Map](https://wise.jobs/analytics-career-map) for goal setting, performance evaluation, and promotion planning.

## Features

- **Career Map Navigation** - Browse all levels (IC1-IC4, AL1-AL3) across multiple dimensions
- **Level Details** - View expectations, responsibilities, skills, and salary bands per level
- **Dimension Explorer** - Explore expectations across Ownership, Problem Solving, Influence, Team Management, and Technical Skills
- **Goal Setting** - Set OKRs aligned to specific responsibilities (planned)
- **Performance Evaluation** - Evaluate impact against level expectations (planned)

## Project Structure

```
career_framework/
├── app/                   # Application source code
│   ├── components/        # Reusable UI components
│   ├── data/              # Career map data structures
│   ├── pages/             # Streamlit multi-page app navigation
│   ├── services/          # Business logic services
│   └── utils/             # Utilities and styling
├── tests/                 # Unit tests
├── .streamlit/            # Streamlit configuration
└── scripts/               # Setup and deployment scripts
```

## Prerequisites

- Python 3.11+
- pip package manager

## Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/career-framework.git
cd career-framework

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run streamlit_app.py
```

## Deployment

### Local Development

```bash
streamlit run streamlit_app.py
```

The app will be available at `http://localhost:8501`.

### Streamlit Cloud

1. Push the code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Link your GitHub repository
4. Set the entry point to `streamlit_app.py`
5. Deploy

### Docker

```bash
docker build -t career-framework .
docker run -p 8501:8501 career-framework
```

## Data Source

Career map expectations are based on the [Wise Analytics Career Map](https://wise.jobs/analytics-career-map).

## License

MIT