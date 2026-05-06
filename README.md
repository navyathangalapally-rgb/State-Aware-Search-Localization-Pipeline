## Interactive Documentation System
A custom automation and search interface for localized technical manuals.

## Project Overview
This project solves the challenge of managing and navigating large-scale technical documentation across multiple languages. I built a pipeline that automates the localization of HTML manuals and a lightweight, zero-dependency search engine to make the content instantly accessible within a Microsoft WebView2 environment.

## What I Built
### 1. The Automation Script (localize.py)
The Problem: Manuals were originally in English with complex, broken image paths.

The Solution: I wrote a Python script using BeautifulSoup4 to:

Auto-Extract Text: Scans the HTML structure to extract content from paragraphs, tables, and headers for translation (German/Polish).

Fix Assets: Automatically repairs image links and flattens directory paths so the documentation works perfectly in a local, offline environment.

2. The Search Engine (search.js)
The Problem: Standard browser search is often clunky for embedded documentation.

The Solution: A "Vanilla JS" search engine that requires no external libraries:

State Protection: It saves the original page state before searching, allowing the user to clear highlights without refreshing the page.

Smart Navigation: Uses Regular Expressions to find keywords and automatically scrolls the window to the first match found.

3. The Interface (abi.css)
The Goal: A clean, "sticky" UI that feels like a professional desktop application.

## Key Features:

Responsive Design: Ensures that large technical screenshots scale down for smaller screens without horizontal scrolling.

Sticky Header: Keeps the search bar visible at all times, even when scrolling through long documents.

## Key Technologies
Languages: Python, JavaScript, CSS3, HTML5

Libraries: BeautifulSoup4 (Python)

Environment: Microsoft WebView2
