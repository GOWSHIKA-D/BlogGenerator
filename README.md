AI Blog Generator 🤖
Overview

AI Blog Generator is a simple Streamlit web application that generates complete blog articles from a given title using Google's Gemini AI model.

Users can enter a blog topic, click the submit button, and instantly receive an AI-generated blog post with headings and structured content.

Features
Generate blog articles from a title
AI-powered content generation using Gemini 2.5 Flash
Simple and user-friendly interface
Automatic blog structure with headings
Fast content generation
Technologies Used
Python
Streamlit
Google Generative AI (Gemini API)
Installation
1. Clone the Repository
git clone https://github.com/your-username/ai-blog-generator.git
cd ai-blog-generator
2. Install Required Packages
py -m pip install streamlit
py -m pip install google-generativeai
3. Configure API Key

Open the Python file and replace:

genai.configure(api_key="YOUR_API_KEY")

with your Gemini API key:

genai.configure(api_key="YOUR_GEMINI_API_KEY")
Running the Application

Execute the following command:

streamlit run app.py

Replace app.py with your actual Python file name.

Project Structure
AI-Blog-Generator/
│
├── app.py
├── README.md
└── requirements.txt
Code Description
streamlit is used to create the web interface.
google.generativeai is used to interact with the Gemini AI model.
The user enters a blog title.
The application sends the title along with predefined instructions to Gemini.
Gemini generates a complete blog article.
The generated content is displayed on the web page.
Sample Input
Benefits of Artificial Intelligence in Education
Sample Output
Title: Benefits of Artificial Intelligence in Education

Introduction

AI is transforming the education sector by...

Benefits
1. Personalized Learning
2. Automated Grading
3. Intelligent Tutoring Systems

Conclusion

AI continues to reshape modern education...
Future Enhancements
Multiple writing tones (Professional, Casual, Creative)
Blog length selection
Copy-to-clipboard feature
Download blog as PDF
Blog image generation
SEO optimization support
Author

Gowshika D

B.Tech Information Technology
Web Developer | Python Developer | AI Enthusiast

License

This project is open-source and available for educational and learning purposes.
