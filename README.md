# ComicCraftAI 🎨📖

## AI Comic Story Creator

ComicCraftAI is a web-based application that uses Artificial Intelligence to create personalized comic stories and illustrations from user-provided prompts.

## 📌 Project Description

ComicCraftAI allows users to enter a story idea along with a main character, setting, tone, and art style. The application uses AI models to generate a panel-by-panel comic story with narration, dialogues, and illustrations.

## ✨ Features

- Generate creative comic stories using AI
- Generate a 5-panel comic storyline
- Create narration and dialogues for each panel
- Generate comic-style illustrations
- Support different story tones
- Support different art styles
- Preview the generated comic
- Export the complete comic as a PDF
- Simple and user-friendly web interface

## 🛠️ Technologies Used

- Python
- FastAPI
- Google Gemini AI
- Stable Diffusion
- Hugging Face Diffusers
- HTML
- CSS
- Jinja2
- Pillow
- FPDF

## 🤖 AI Models

- Gemini Flash – Used for generating the comic outline
- Gemini Pro – Used for detailed story narration and dialogues
- Stable Diffusion – Used for generating comic illustrations

## 📂 Project Structure

```text
ComicCraftAI/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── config.py
│   ├── schemas.py
│   ├── gemini_flash.py
│   ├── gemini_pro.py
│   ├── image_generator.py
│   ├── layout_builder.py
│   └── exporters.py
│
├── templates/
│   ├── index.html
│   ├── comic_preview.html
│   └── export_success.html
│
├── static/
│   ├── panels/
│   └── exports/
│
├── requirements.txt
└── README.md
