# SMART PCOD AWARENESS CHATBOT FOR WOMEN’S HEALTH SUPPORT

## Table of Contents
- Overview
- Project Purpose
- Key Features
- Tech Stack
- System Architecture
- Educational Value
- Overall Summary

## Overview
The Smart PCOD Awareness Chatbot is a full-stack educational system developed to support women’s-health awareness, specifically focusing on Polycystic Ovarian Disease (PCOD). PCOD is a common hormonal condition that affects menstrual patterns, skin health, weight, and ovulation, yet many women struggle to find clear, reliable information online. Most available resources are scattered, complex, or filled with myths, making it difficult for users to understand the condition and make informed lifestyle decisions.  
This project was created to address that gap by offering a simple, accessible, and research-supported digital tool that explains PCOD in everyday language. The chatbot functions as a non-clinical educational assistant, helping users learn about symptoms, causes, menstrual changes, diet basics, lifestyle practices, fertility questions, common myths, and indicators for seeking professional care. It does not diagnose or collect personal information, it runs locally, maintains full privacy, and includes a clear disclaimer to ensure responsible use.  
The system is built using a complete end-to-end architecture:  
- A FastAPI backend processes user messages and selects the correct response based on rule-matching logic.  
- A SQLite database stores a curated set of PCOD rules, each written from peer-reviewed research and rewritten into simple, understandable content.  
- A React frontend provides a clean, user-friendly chat interface supporting message formatting, auto-scrolling, timestamps, and smooth interaction.  

The backend uses a lightweight rule-based matching engine that identifies keywords from user input, even when the question is short. This helps support users with limited reading or writing skills and keeps the learning process accessible. On the frontend, each response is displayed instantly, creating a smooth conversational experience.  
This project follows key health-informatics principles such as structured content delivery, user-centered communication, data minimization, and clear educational boundaries. The literature review that guided this work emphasized the need for reliable, simple, and private tools that can help individuals understand PCOD without diagnostic risk.  
Overall, the Smart PCOD Awareness Chatbot demonstrates how digital tools can simplify complex health information and present it responsibly. The system is modular, easy to maintain, and suitable for academic use, public-health education, and foundational chatbot development. It brings together backend logic, database structure, and frontend design into one practical solution supporting women’s-health awareness.

## Project Purpose
The main goal of the chatbot is to improve PCOD awareness by transforming research findings into simple, direct, and relatable responses. It supports individuals who may struggle with reading or typing full sentences by recognizing keywords from short or incomplete input. This makes the system accessible for a wide range of users and encourages open learning without judgment.

## Key Features
•	Simple, research-based PCOD explanations in everyday language  
•	Covers symptoms, causes, menstrual patterns, lifestyle, diet, myths, and fertility  
•	Clear disclaimer to maintain non-clinical boundaries  
•	Privacy-preserving: no data collection, no diagnosis  
•	Lightweight rule-based logic for consistent and transparent results  
•	Works even with short queries  
•	Clean React UI with smooth scrolling and timestamps  
•	Modular structure for easy enhancement

## Tech Stack
- Frontend: React, JavaScript, HTML, CSS  
- Backend: FastAPI (Python)  
- Database: SQLite with SQLAlchemy ORM  
- API Communication: Axios  
- Tools: VS Code, GitHub

## System Architecture
•	User types a question in the React interface  
•	Frontend sends the query to FastAPI  
•	Backend processes input and applies rule-matching logic  
•	System checks keywords in SQLite rule database  
•	Highest-priority matched rule is selected  
•	Response is returned to React and shown instantly  

This architecture clearly separates presentation, backend logic, and data storage, keeping the system organized and easy to maintain.

## Educational Value
The project is designed using important health-informatics principles:  
•	simplified content delivery  
•	privacy and data minimization  
•	user-friendly communication  
•	structured educational boundaries  
•	evidence-supported information  
•	inclusive support for different literacy levels  
The content is shaped by literature review findings that highlight the need for clear, accurate, stigma-free PCOD education.

## Overall Summary
The Smart PCOD Awareness Chatbot brings together all parts of the project, research, technology, and user-centered design into one practical educational tool. It translates complex PCOD information into simple guidance that users can access instantly, privately, and without any technical barriers. The combination of a structured backend, a well-organized rule database, and an intuitive React interface creates a smooth learning experience for anyone seeking clarity about PCOD.  
The system reflects strong public-health informatics principles by emphasizing accuracy, accessibility, and privacy. Its lightweight design makes it easy to maintain and expand, offering a strong foundation for future enhancements or additional women’s-health modules. As a whole, the project shows how a focused digital solution can support awareness, reduce misinformation, and present health education in a format that feels approachable and reliable.

---

