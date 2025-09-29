# Author: Srini Pusuluri
# Date: 9/28/2025
# Description: YouTube Search Bot - A web application to search and display YouTube videos using NiceGUI

import os
from nicegui import ui

# Function to generate YouTube search URL sorted by upload date (recent posts)
def generate_youtube_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://www.youtube.com/results?search_query={query_encoded}&sp=CAMSBAgCEAEA"

# Function to generate Google search URL
def generate_google_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://www.google.com/search?q={query_encoded}"

# Function to generate GitHub search URL
def generate_github_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://github.com/search?q={query_encoded}"

# Function to generate ArXiv search URL
def generate_arxiv_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://arxiv.org/search/?query={query_encoded}&searchtype=all&source=header"

# Function to generate Google PDF search URL
def generate_google_pdf_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://www.google.com/search?q={query_encoded}&filetype:pdf"

# Function to generate Google AI News search URL
def generate_google_ai_news_search_url():
    return "https://www.google.com/search?q=AI+news&gl=us&hl=en&tbm=nws"

# Function to generate LinkedIn Jobs search URL
def generate_linkedin_jobs_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://www.linkedin.com/jobs/search/?keywords={query_encoded}"

# Function to generate Twitter/X search URL
def generate_twitter_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://twitter.com/search?q={query_encoded}"

# Function to generate Reddit search URL
def generate_reddit_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://www.reddit.com/search/?q={query_encoded}"

# Function to generate Stack Overflow search URL
def generate_stackoverflow_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://stackoverflow.com/search?q={query_encoded}"

# Function to generate Hugging Face search URL
def generate_huggingface_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://huggingface.co/search/full-text?q={query_encoded}"

# Function to generate Medium search URL
def generate_medium_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://medium.com/search?q={query_encoded}"

# Function to generate Quora search URL
def generate_quora_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://www.quora.com/search?q={query_encoded}"

# Function to generate Kaggle search URL
def generate_kaggle_search_url(query):
    return f"https://kaggle.com/search?q={query}"

# Function to generate Coursera search URL
def generate_coursera_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://www.coursera.org/search?query={query_encoded}"

# Function to generate Wikipedia search URL
def generate_wikipedia_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://en.wikipedia.org/wiki/Special:Search?search={query_encoded}"

# Function to generate Semantic Scholar search URL
def generate_semanticscholar_search_url(query):
    query_encoded = query.replace(' ', '+')
    return f"https://www.semanticscholar.org/search?q={query_encoded}"

# Function to perform search and display link to YouTube search
def search_youtube(topic):
    url = generate_youtube_search_url(topic)
    ui.notify(f"Searching for {topic} on YouTube...")
    youtube_container.clear()
    with youtube_container:
        ui.label(f"Search for '{topic}' on YouTube:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open YouTube Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Google search
def search_google(topic):
    url = generate_google_search_url(topic)
    ui.notify(f"Searching for {topic} on Google...")
    google_container.clear()
    with google_container:
        ui.label(f"Search for '{topic}' on Google:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open Google Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to GitHub search
def search_github(topic):
    url = generate_github_search_url(topic)
    ui.notify(f"Searching for {topic} on GitHub...")
    github_container.clear()
    with github_container:
        ui.label(f"Search for '{topic}' on GitHub:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open GitHub Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to ArXiv search
def search_arxiv(topic):
    url = generate_arxiv_search_url(topic)
    ui.notify(f"Searching for {topic} on ArXiv...")
    arxiv_container.clear()
    with arxiv_container:
        ui.label(f"Search for '{topic}' on ArXiv:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open ArXiv Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Google PDF search
def search_google_pdfs(topic):
    url = generate_google_pdf_search_url(topic)
    ui.notify(f"Searching for PDF files related to {topic}...")
    google_container.clear()
    with google_container:
        ui.label(f"Search for '{topic}' PDF files on Google:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open Google PDF Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Google AI News
def search_google_ai_news():
    url = generate_google_ai_news_search_url()
    ui.notify("Searching for latest AI news...")
    google_container.clear()
    with google_container:
        ui.label("Latest AI News:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open AI News Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to LinkedIn Jobs search
def search_linkedin_jobs(topic):
    url = generate_linkedin_jobs_url(topic)
    ui.notify(f"Searching for {topic} jobs on LinkedIn...")
    linkedin_container.clear()
    with linkedin_container:
        ui.label(f"Search for '{topic}' jobs on LinkedIn:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open LinkedIn Jobs Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Twitter/X search
def search_twitter(topic):
    url = generate_twitter_search_url(topic)
    ui.notify(f"Searching for {topic} on Twitter/X...")
    twitter_container.clear()
    with twitter_container:
        ui.label(f"Search for '{topic}' on Twitter/X:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open Twitter/X Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Reddit search
def search_reddit(topic):
    url = generate_reddit_search_url(topic)
    ui.notify(f"Searching for {topic} on Reddit...")
    reddit_container.clear()
    with reddit_container:
        ui.label(f"Search for '{topic}' on Reddit:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open Reddit Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Stack Overflow search
def search_stackoverflow(topic):
    url = generate_stackoverflow_search_url(topic)
    ui.notify(f"Searching for {topic} on Stack Overflow...")
    stackoverflow_container.clear()
    with stackoverflow_container:
        ui.label(f"Search for '{topic}' on Stack Overflow:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open Stack Overflow Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Hugging Face search
def search_huggingface(topic):
    url = generate_huggingface_search_url(topic)
    ui.notify(f"Searching for {topic} on Hugging Face...")
    huggingface_container.clear()
    with huggingface_container:
        ui.label(f"Search for '{topic}' on Hugging Face:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open Hugging Face Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Medium search
def search_medium(topic):
    url = generate_medium_search_url(topic)
    ui.notify(f"Searching for {topic} on Medium...")
    medium_container.clear()
    with medium_container:
        ui.label(f"Search for '{topic}' on Medium:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open Medium Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Quora search
def search_quora(topic):
    url = generate_quora_search_url(topic)
    ui.notify(f"Searching for {topic} on Quora...")
    quora_container.clear()
    with quora_container:
        ui.label(f"Search for '{topic}' on Quora:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open Quora Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Kaggle search
def search_kaggle(topic):
    url = generate_kaggle_search_url(topic)
    ui.notify(f"Searching for {topic} on Kaggle...")
    kaggle_container.clear()
    with kaggle_container:
        ui.label(f"Search for '{topic}' on Kaggle:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open Kaggle Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Coursera search
def search_coursera(topic):
    url = generate_coursera_search_url(topic)
    ui.notify(f"Searching for {topic} on Coursera...")
    coursera_container.clear()
    with coursera_container:
        ui.label(f"Search for '{topic}' on Coursera:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open Coursera Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Wikipedia search
def search_wikipedia(topic):
    url = generate_wikipedia_search_url(topic)
    ui.notify(f"Searching for {topic} on Wikipedia...")
    wikipedia_container.clear()
    with wikipedia_container:
        ui.label(f"Search for '{topic}' on Wikipedia:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open Wikipedia Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to perform search and display link to Semantic Scholar search
def search_semanticscholar(topic):
    url = generate_semanticscholar_search_url(topic)
    ui.notify(f"Searching for {topic} on Semantic Scholar...")
    semanticscholar_container.clear()
    with semanticscholar_container:
        ui.label(f"Search for '{topic}' on Semantic Scholar:").classes("text-lg font-bold mb-2")
        ui.link("🔗 Open Semantic Scholar Search", url).props('target="_blank"').classes("text-blue-600 underline text-lg")

# Function to search all platforms
def search_all(topic):
    search_youtube(topic)
    search_google(topic)
    search_github(topic)
    search_arxiv(topic)
    search_linkedin_jobs(topic)
    search_twitter(topic)
    search_reddit(topic)
    search_stackoverflow(topic)
    search_huggingface(topic)
    search_medium(topic)
    search_quora(topic)
    search_kaggle(topic)
    search_coursera(topic)
    search_wikipedia(topic)
    search_semanticscholar(topic)

# Function to search with a predefined topic
def search_topic(topic):
    topic_input.value = topic
    search_all(topic)

# UI Elements
ui.label("🔎 Multi-Platform Search Bot").classes("text-2xl font-bold mb-4")

ui.label("Note: Enter search Term and scroll down for results").classes("text-xl font-bold mb-4")


# Summary
ui.label("""This Multi-Platform Search Bot is a powerful web application designed to streamline your research across multiple platforms.
""").classes("text-sm text-gray-600 mb-4")

ui.label("""
How to Use:

1. Enter a search query or click a quick tag to search across YouTube, Google, GitHub, and ArXiv simultaneously.

2. Choose specific platforms with individual buttons (e.g., Search PDFs or AI News for Google-specific searches).

3. Click the displayed links to open search results in new tabs for comprehensive browsing.

4. Use the Refresh button to clear all results and start over.
""").classes("text-sm text-green-600 mb-4")

ui.label("""


Use quick tags for popular AI topics like Machine Learning, Deep Learning, LLMs, RAG, and more to discover content across all platforms at once.
Whether you're learning about Python libraries, exploring GitHub repos, reading academic papers on ArXiv, or watching tutorials on YouTube, this tool saves time and enhances productivity.""").classes("text-sm text-blue-600 mb-4")


# Input field for topic
topic_input = ui.input(label="Click Tag below or Enter search text - like llm ").props("outlined").classes("w-96 mb-4")

# Quick tags for AI-related topics organized by category
ui.label("Quick Tags: [ select  any tag below]").classes("text-lg font-bold mb-2")
# Define color for each category using Tailwind CSS classes for distinction
color_map = {
    "bg-green-600": ["Python", "Python Libraries", "NLP"],  # Dark green for Python and NLP
    "bg-blue-700": ["Machine Learning", "Deep Learning", "Neural Networks", "Reinforcement Learning"],  # Darker blue for ML/DL
    "bg-purple-600": ["LLM", "LLM Fine Tuning", "PEFT", "RLHP", "Prompt Engineering"],  # Purple for LLM
    "bg-orange-600": ["RAG", "RAG Fine Tuning"],  # Deeper orange for RAG
    "bg-pink-600": ["Computer Vision", "Stable Diffusion", "LORA", "Generative AI", "AI Ethics"]  # Pink for Vision/Diffusion and Generative AI/Ethics
}
tags_list = ["Python", "Python Libraries", "Machine Learning", "Deep Learning", "Neural Networks", "Reinforcement Learning", "NLP", "LLM", "LLM Fine Tuning", "PEFT", "RLHP", "Prompt Engineering", "RAG", "RAG Fine Tuning", "Computer Vision", "Stable Diffusion", "LORA", "Generative AI", "AI Ethics"]
for i in range(0, len(tags_list), 4):
    chunk = tags_list[i:i+4]
    with ui.row().classes("gap-2 mb-2"):
        for tag in chunk:
            # Assign color based on category
            bg_color = "bg-gray-500"  # Default gray
            for color, tags in color_map.items():
                if tag in tags:
                    bg_color = color
                    break
            ui.button(tag, on_click=lambda t=tag: search_topic(t)).classes(f"{bg_color} text-white px-3 py-1 rounded text-sm")
# Search buttons
ui.label("Channel Selection: [ select one or many tages below]").classes("text-lg font-bold mb-2")
search_buttons = [
    {"text": "Search All", "color": "warning", "on_click": lambda: search_all(topic_input.value)},
    {"text": "Search Google", "color": "primary", "on_click": lambda: search_google(topic_input.value)},
    {"text": "Search YouTube", "color": "negative", "on_click": lambda: search_youtube(topic_input.value)},
    {"text": "Search GitHub", "color": "info", "on_click": lambda: search_github(topic_input.value)},
    {"text": "Search ArXiv", "color": "positive", "on_click": lambda: search_arxiv(topic_input.value)},
    {"text": "Search LinkedIn Jobs", "color": "accent", "on_click": lambda: search_linkedin_jobs(topic_input.value)},
    {"text": "Search PDFs", "color": "info", "on_click": lambda: search_google_pdfs(topic_input.value)},
    {"text": "AI News", "color": "info", "on_click": lambda: search_google_ai_news()},
    {"text": "Search Twitter/X", "color": "primary", "on_click": lambda: search_twitter(topic_input.value)},
    {"text": "Search Reddit", "color": "negative", "on_click": lambda: search_reddit(topic_input.value)},
    {"text": "Search Stack Overflow", "color": "info", "on_click": lambda: search_stackoverflow(topic_input.value)},
    {"text": "Search Hugging Face", "color": "positive", "on_click": lambda: search_huggingface(topic_input.value)},
    {"text": "Search Medium", "color": "accent", "on_click": lambda: search_medium(topic_input.value)},
    {"text": "Search Quora", "color": "primary", "on_click": lambda: search_quora(topic_input.value)},
    {"text": "Search Kaggle", "color": "negative", "on_click": lambda: search_kaggle(topic_input.value)},
    {"text": "Search Coursera", "color": "info", "on_click": lambda: search_coursera(topic_input.value)},
    {"text": "Search Wikipedia", "color": "positive", "on_click": lambda: search_wikipedia(topic_input.value)},
    {"text": "Search Semantic Scholar", "color": "accent", "on_click": lambda: search_semanticscholar(topic_input.value)},
]
for i in range(0, len(search_buttons), 2):
    chunk = search_buttons[i:i+2]
    with ui.row().classes("gap-2 mb-2"):
        for btn in chunk:
            ui.button(btn["text"], on_click=btn["on_click"], color=btn["color"]).classes("px-4 py-2 rounded")

# Google Search Section
ui.label("Google Search Results").classes("text-xl font-bold mb-2 text-blue-500")
google_container = ui.column()

# YouTube Search Section
ui.label("YouTube Search Results").classes("text-xl font-bold mb-2 mt-8 text-red-500")
youtube_container = ui.column()

# GitHub Search Section
ui.label("GitHub Search Results").classes("text-xl font-bold mb-2 mt-8 text-cyan-500")
github_container = ui.column()

# ArXiv Search Section
ui.label("ArXiv Search Results").classes("text-xl font-bold mb-2 mt-8 text-green-500")
arxiv_container = ui.column()

# LinkedIn Jobs Search Section
ui.label("LinkedIn Jobs Search Results").classes("text-xl font-bold mb-2 mt-8 text-blue-600")
linkedin_container = ui.column()

# Twitter/X Search Section
ui.label("Twitter/X Search Results").classes("text-xl font-bold mb-2 mt-8 text-gray-600")
twitter_container = ui.column()

# Reddit Search Section
ui.label("Reddit Search Results").classes("text-xl font-bold mb-2 mt-8 text-orange-600")
reddit_container = ui.column()

# Stack Overflow Search Section
ui.label("Stack Overflow Search Results").classes("text-xl font-bold mb-2 mt-8 text-orange-500")
stackoverflow_container = ui.column()

# Hugging Face Search Section
ui.label("Hugging Face Search Results").classes("text-xl font-bold mb-2 mt-8 text-yellow-600")
huggingface_container = ui.column()

# Medium Search Section
ui.label("Medium Search Results").classes("text-xl font-bold mb-2 mt-8 text-black")
medium_container = ui.column()

# Quora Search Section
ui.label("Quora Search Results").classes("text-xl font-bold mb-2 mt-8 text-red-600")
quora_container = ui.column()

# Kaggle Search Section
ui.label("Kaggle Search Results").classes("text-xl font-bold mb-2 mt-8 text-blue-800")
kaggle_container = ui.column()

# Coursera Search Section
ui.label("Coursera Search Results").classes("text-xl font-bold mb-2 mt-8 text-indigo-600")
coursera_container = ui.column()

# Wikipedia Search Section
ui.label("Wikipedia Search Results").classes("text-xl font-bold mb-2 mt-8 text-gray-800")
wikipedia_container = ui.column()

# Semantic Scholar Search Section
ui.label("Semantic Scholar Search Results").classes("text-xl font-bold mb-2 mt-8 text-teal-600")
semanticscholar_container = ui.column()

# Refresh button to clear results
ui.button("Refresh", on_click=lambda: (youtube_container.clear(), google_container.clear(), github_container.clear(), arxiv_container.clear(), linkedin_container.clear(), twitter_container.clear(), reddit_container.clear(), stackoverflow_container.clear(), huggingface_container.clear(), medium_container.clear(), quora_container.clear(), kaggle_container.clear(), coursera_container.clear(), wikipedia_container.clear(), semanticscholar_container.clear()), color="secondary").classes("px-4 py-2 rounded mt-4")

# Start the NiceGUI application on dynamic port if available (e.g., for Render)
port = int(os.environ.get('PORT', 8083))
ui.run(port=port)
