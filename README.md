# Multi-Platform AI Search Bot

A web application built with NiceGUI to search across multiple platforms including YouTube, Google, GitHub, ArXiv, LinkedIn, Twitter/X, Reddit, Stack Overflow, Hugging Face, Medium, Quora, Kaggle, Coursera, Wikipedia, and Semantic Scholar.

## Features

- Generate search URLs for various platforms instantly
- Support for AI-related quick tags (e.g., LLM, RAG, Machine Learning)
- Search all platforms at once or individually
- Clean, responsive UI with organized sections for each platform
- Real-time notifications and link opening in new tabs
- No API keys required - uses URL generation for search queries

## Requirements

- Python 3.7+
- nicegui

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai_search
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python ai_search.py
```

Open your browser and navigate to `http://localhost:8083` (or the port specified in the script, default 8083).

Enter a search query or click quick tags to initiate searches. Links will appear below for each platform, opening in new tabs.

## Deployment

The app can be deployed to platforms like Render.com:

1. Push code to GitHub.
2. Connect repository to Render.
3. Create Web Service with Python environment, Build Command: `pip install -r requirements.txt`, Start Command: `python ai_search.py`.
4. The app uses the PORT environment variable for dynamic port assignment.

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).
