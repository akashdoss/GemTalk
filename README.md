# GemTalk 💎

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.0%2B-black?style=for-the-badge&logo=flask" alt="Flask Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</div>

### - Your friendly Chatbot with a temporary brain 🤣 -

GemTalk is a sleek, simple, and privacy-focused web application that serves as a user-friendly interface for Google's Gemini models. It's a single-page application built with Flask and vanilla JavaScript, ensuring a lightweight and responsive user experience.

<p align="center">
  <strong>Live Demo</strong>: <a href="https://gemtalk-theta.vercel.app/">https://gemtalk-theta.vercel.app/</a>
</p>

***

#Features ✨

* **Direct Gemini API Integration**: Chat directly with Google's powerful `gemini-1.5-flash` model.
* **Privacy First**: Your Gemini API key is handled exclusively on the client-side and is **never stored** on any server, ensuring your conversations remain private.
* **Sleek User Interface**: A modern, multi-step interface that guides the user from a welcome screen to the chat.
* **Light & Dark Mode**: A beautiful theme toggle that respects your viewing preference and saves it in your browser for the next visit.
* **No Database Needed**: The application is completely stateless, making it incredibly easy to run and deploy.
* **Responsive Design**: A clean layout that works well on both desktop and mobile browsers.

***

#Tech Stack 🛠️

* **Backend**: Python, Flask
* **Frontend**: HTML5, CSS3 (with variables for theming), Vanilla JavaScript
* **API**: Google Generative AI (Gemini)

***

# Getting Started

Follow these instructions to get a local copy up and running.

#Prerequisites

Make sure you have the following installed on your system:
* Python 3.9 or higher
* pip (Python package installer)

# Installation & Setup

1.  **Clone the Repository**
    ```sh
    git clone [https://github.com/your-username/gemtalk.git](https://github.com/your-username/gemtalk.git)
    cd gemtalk
    ```
    2.  **Create a `requirements.txt` file**
    Create a new file named `requirements.txt` in the root of your project and add the following lines to it:
    ```
    Flask
    google-generativeai
    ```

3.  **Install Dependencies**
    Open your terminal in the project directory and run:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Get Your Gemini API Key**
    * Go to the [Google AI Studio](https://aistudio.google.com/app/apikey).
    * Click on "**Create API key in new project**".
    * Copy the generated API key.

5.  **Run the Application**
    ```sh
    python app.py
    ```

6.  **Access GemTalk**
    Open your favorite web browser and navigate to:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

***

# How to Use 🚀

1.  Upon launching the app, you'll see a welcome screen. Click **Get Started**.
2.  Paste your Gemini API Key into the input field and click **Continue**.
3.  You'll be taken to the chat screen. Start your conversation with GemTalk!
4.  Use the 🌙 / ☀️ icon in the top-right corner to toggle between light and dark modes.

***

#Author ✍️

**Akash Doss**

* **LinkedIn**: [Akash Doss](https://www.linkedin.com/in/akash-selvadoss-n-542765252/)
* **GitHub**: [Akash Doss](https://github.com/akashdoss)
    ***

#License 📜

This project is licensed under the MIT License. See the `LICENSE` file for more details.
