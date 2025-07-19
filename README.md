# 🌾 AGROMIND - AI-Powered Agricultural Assistant

AGROMIND is a smart, AI-based agricultural assistant built to empower farmers and agricultural planners with intelligent recommendations. It integrates crop recommendation, yield prediction, weather information, voice interaction, and chatbot support into a single platform.

---

## 🚀 Features

- 🌱 **Crop Recommendation** – Suggests the most suitable crop based on soil, temperature, humidity, and location data.
- 📈 **Yield Prediction** – Uses machine learning to predict the yield of crops using historical and environmental data.
- 🌦️ **Weather Integration** – Fetches real-time weather updates to support decision-making.
- 🧠 **Chatbot & Voice Assistant** – Provides an interactive way for users to ask queries and receive guidance.
- 🔐 **User Authentication** – Secure login and session management using a lightweight SQLite database.

---

## 🗂️ Project Structure

```bash
AGROMIND/
│
├── app.py                   # Main app controller (Flask/Django/Tkinter)
├── auth.py                  # Handles user authentication logic
├── crop_recommender.py      # ML model for crop recommendations
├── Crop_recommendation.csv  # Dataset used for recommendation
├── yield_predictor.py       # Predicts crop yield based on input
├── train_model.py           # Model training script
├── agromind_chatbot.py      # Text-based chatbot
├── voice_bot.py             # Voice assistant interface
├── weather.py               # Weather information fetcher
├── india_locations.py       # Location helper module (states/districts)
├── tk.py                    # Tkinter-based GUI application
├── test.py                  # Unit test for model
├── test_functions.py        # Additional test functions
├── users.db                 # SQLite database for authentication
├── models/                  # Trained ML models (.pkl files)
├── images/                  # Static images
└── README.md                # Project documentation
````

---

## 📦 Installation & Setup

### 🔧 Prerequisites

* Python 3.8+
* pip (Python package installer)

### 📥 Clone the Repository

```bash
git clone https://github.com/sanchitc05/AGROMIND.git
cd AGROMIND
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the Application

#### If using Flask (app.py):

```bash
python app.py
```

#### If using Tkinter GUI:

```bash
python tk.py
```

---

## 🧠 How It Works

### 🟢 Crop Recommendation

Based on user input (N, P, K, temperature, humidity, pH, rainfall), the model predicts the best crop to grow using a classification ML model.

### 🟢 Yield Prediction

The model uses regression techniques to estimate expected yield, which helps in planning and resource management.

### 🟢 Weather Info

Integrates with weather APIs to show current climate conditions for better recommendations.

### 🟢 Voice Assistant

Voice-based input/output support using `speech_recognition` and `pyttsx3` for hands-free interaction.

---

## 🧪 Testing

Run the test scripts:

```bash
python test.py
python test_functions.py
```

---

## 🔐 Security Notes

* Credentials and API keys should be stored securely using environment variables.
* Passwords are hashed before storing in the database.

---

## 📊 Dataset

* **Crop Recommendation**: `Crop_recommendation.csv` – contains labeled data for supervised learning.
* **Weather & Location**: Uses internal static data and external APIs.

---

## 🙌 Contributors

* [Sanchit Chauhan](https://github.com/sanchitc05)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Support

If you like this project, please ⭐ star the repository and share it with others!

```