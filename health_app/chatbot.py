import os
import pandas as pd
import math

class Chatbot:
    def __init__(self, disease, context=None):
        self.disease = disease
        self.context = context if context else {}
        self.questions_df = self.load_questions()
        self.responses = self.context.get('responses', [])
        self.current_question_index = self.context.get('current_question_index', 0)
        self.base_probability = 0.5  # Starting probability

    def load_questions(self):
        csv_file_path = os.path.join(os.path.dirname(__file__), 'disease_followup_question.csv')
        try:
            df = pd.read_csv(csv_file_path)
            required_columns = ['Disease', 'Questions?', 'Yes_Probability', 'No_Probability']
            if not all(col in df.columns for col in required_columns):
                print(f"Error: Required columns {required_columns} missing from CSV")
                return pd.DataFrame()

            questions_df = df[df['Disease'] == self.disease].reset_index(drop=True)
            if questions_df.empty:
                print(f"No questions found for disease: {self.disease}")
                return pd.DataFrame()

            return questions_df

        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
            return pd.DataFrame()

    def get_next_question(self):
        if self.current_question_index < len(self.questions_df):
            question = self.questions_df.iloc[self.current_question_index]['Questions?']
            return question
        else:
            return self.finalize_disease()

    def process_input(self, user_input):
        self.responses.append(1 if user_input.lower() == 'yes' else 0)
        self.current_question_index += 1
        return self.get_next_question()

    def calculate_probability(self):
        log_odds = math.log(self.base_probability / (1 - self.base_probability))
        
        for i, response in enumerate(self.responses):
            yes_prob = self.questions_df.iloc[i]['Yes_Probability']
            no_prob = self.questions_df.iloc[i]['No_Probability']
            
            if response == 1:  # User answered "yes"
                log_odds += math.log(yes_prob / (1 - yes_prob))
            else:  # User answered "no"
                log_odds += math.log(no_prob / (1 - no_prob))

        probability = 1 / (1 + math.exp(-log_odds))
        return probability

    def finalize_disease(self):
        if not self.responses:
            return "Insufficient responses to validate the disease."

        try:
            probability = self.calculate_probability()
            
            if probability > 0.8:
                return f"Based on your responses, the predicted disease '{self.disease}' is likely confirmed with a probability of {probability:.2f}."
            elif probability > 0.5:
                return f"The predicted disease '{self.disease}' is possible, but not certain, with a probability of {probability:.2f}. Consider consulting a healthcare professional for a definitive diagnosis."
            else:
                return f"The predicted disease '{self.disease}' is less likely based on your responses, with a probability of {probability:.2f}. Please consult a healthcare professional for accurate diagnosis."

        except Exception as e:
            print(f"Error finalizing disease prediction: {e}")
            return "Error in disease prediction."

    def get_initial_context(self):
        return {'responses': self.responses, 'current_question_index': self.current_question_index}

    def get_updated_context(self):
        return {'responses': self.responses, 'current_question_index': self.current_question_index}