# chatbot.py
# chatbot.py
import pandas as pd

class Chatbot:
    def __init__(self, disease, symptoms=None, context=None):
        self.disease = disease
        self.symptoms = symptoms or []
        self.context = context or {}
        self.questions = self.load_questions_from_csv()
        self.current_question_index = 0

    def load_questions_from_csv(self):
        # Load the CSV file
        csv_file_path = r'C:\Users\user\Desktop\DjangoML_DiseasePrediction-master\health_app\disease_followup_question.csv'  # Update with your actual file path
        df = pd.read_csv(csv_file_path)

        # Filter the rows based on the current disease
        disease_questions = df[df['Disease'] == self.disease]

        # Get the list of questions for the current disease
        questions = disease_questions['Question'].tolist()

        return questions

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return "No more questions. Please consult a healthcare professional."

    def process_input(self, user_input):
        # Store the user's response
        self.context[f"question_{self.current_question_index}"] = user_input
        return self.get_next_question()

    def get_initial_context(self):
        return {
            'disease': self.disease,
            'initial_symptoms': self.symptoms,
            'confirmed_symptoms': []
        }

    def get_updated_context(self):
        return self.context
