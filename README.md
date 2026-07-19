# 🧠 AI-Powered MCQ Generator using Google Gemini

Generate high-quality Multiple Choice Questions (MCQs) from **PDF** and **Text** documents using **Google Gemini AI**. The application provides an interactive quiz interface, instant scoring, explanations for each answer, performance analytics, and downloadable PDF results.

---

## 🚀 Live Demo

The application is deployed on Render:

🔗 https://automated-mcq-generator-using-openai-api.onrender.com

---

## 📸 Screenshots

> Add screenshots after deployment.

| Home Page | Generated Quiz | Results Dashboard |
|-----------|----------------|-------------------|
| ![Home](screenshots/home.png) | ![Quiz](screenshots/quiz.png) | ![Results](screenshots/results.png) |

---

# ✨ Features

- 📄 Upload PDF or TXT files
- 🤖 AI-generated MCQs using Google Gemini
- 🎯 Select number of questions
- 📚 Choose subject
- 🎚 Select difficulty level (Easy / Medium / Hard)
- ✅ Interactive quiz interface
- 📊 Automatic score calculation
- 💡 Answer explanations
- 📈 Quiz performance visualization
- 📥 Download quiz results as PDF
- 🎨 Clean Streamlit UI

---

# 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API**
- **PyPDF2**
- **Matplotlib**
- **Pandas**
- **ReportLab**

---

# 📂 Project Structure

```
AI-MCQ-Generator
│
├── src
│   └── mcqgenerator
│       ├── gemini_generator.py
│       ├── pdf_generator.py
│       ├── utils.py
│       ├── logger.py
│       └── MCQGenerator.py
│
├── StreamlitAPP.py
├── requirements.txt
├── README.md
├── Response.json
└── data.txt
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Go to the project folder

```bash
cd YOUR_REPOSITORY
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your API key from:

https://aistudio.google.com/

---

# ▶️ Run the Application

```bash
streamlit run StreamlitAPP.py
```

---

# 📖 How It Works

1. Upload a PDF or TXT document.
2. The application extracts the text.
3. Google Gemini analyzes the content.
4. AI generates multiple-choice questions.
5. Attempt the quiz.
6. Submit your answers.
7. View score and explanations.
8. Download the quiz result as a PDF.

---

# 📊 Current Features

- AI-based MCQ generation
- PDF text extraction
- TXT file support
- Interactive quiz
- Automatic evaluation
- Performance analytics
- PDF result export
- Responsive Streamlit interface

---

# 🔮 Future Improvements

- User authentication
- Question timer
- Question bookmarking
- Multiple AI model support
- Leaderboard
- Dark mode
- CSV export
- Cloud database integration
- Quiz history

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 👨‍💻 Author

**Neeraj Mahajan**

- GitHub: https://github.com/neeraj477
- LinkedIn: https://www.linkedin.com/in/neeraj-mahajan-5254b0258/

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.