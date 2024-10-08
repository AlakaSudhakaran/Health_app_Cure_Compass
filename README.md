# Health Prediction App

## Overview
This Django-based web application predicts diseases based on user-input symptoms. It features an interactive bot that asks follow-up questions based on the predicted disease and suggests nearby clinics.

## Features
- Disease prediction based on symptoms
- Interactive chatbot for follow-up questions
- Nearby clinic recommendations
- User-friendly web interface

## Technologies Used
- Python
- Django
-sqlite
## Installation

1. Clone the repository:
   ```
   git clone https://github.com/AlakaSudhakaran/health-prediction-app.git
   cd health-prediction-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

## Usage

1. Start the development server:
   ```
   python manage.py runserver
   ```

2. Open a web browser and navigate to `http://localhost:8000`

3. Enter your symptoms in the provided form

4. View the predicted disease and interact with the chatbot for follow-up questions

5. Receive suggestions for nearby clinics based on your location

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.



## Contact
Alaka Sudhakaran - alaka.sudhakaran.p@gmail.com

Project Link: https://github.com/[your-username]/health-prediction-app
