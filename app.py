from flask import Flask, render_template
import random
import csv
import logging
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure logging to track application behavior and errors
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def load_cases_from_csv(file_path):
    """
    Load disappearance cases from a CSV file.

    :param file_path: Path to the CSV file containing disappearance cases.
    :return: A list of cases (each case is a dictionary).
    """
    logging.debug(f"Loading cases from CSV file: {file_path}")
    cases = []
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            cases = [row for row in reader]
        logging.debug(f"Loaded {len(cases)} cases from the CSV file.")
    except Exception as e:
        logging.error(f"Error loading cases from CSV: {e}")
    return cases


def calculate_days_missing(fecha_desaparicion):
    """
    Calculate how many days have passed since the disappearance date.

    :param fecha_desaparicion: Disappearance date in 'YYYY-MM-DD' format.
    :return: Number of days since the disappearance.
    """
    try:
        fecha_desaparicion_dt = datetime.strptime(fecha_desaparicion, '%Y-%m-%d')
        fecha_actual = datetime.now()
        return (fecha_actual - fecha_desaparicion_dt).days
    except ValueError as e:
        logging.error(f"Error processing disappearance date: {e}")
        return None


@app.route('/')
def home():
    """
    Main route of the application. Displays a random disappearance case.

    - Loads cases from a CSV file.
    - Selects a random case.
    - Calculates the number of days since the disappearance.
    - Passes the anonymized narrative and case details to the HTML template.
    """
    logging.info("Handling request to '/' route.")

    # Load cases from the processed CSV file
    cases = load_cases_from_csv('./data/processed_cases.csv')
    if not cases:
        logging.error("No cases found in the processed CSV file.")
        return "No cases available."

    # Select a random case
    selected_case = random.choice(cases)
    logging.debug(f"Selected case: {selected_case}")

    # Calculate days missing
    selected_case['dias_desaparecido'] = calculate_days_missing(selected_case['fecha_desaparicion'])

    # Pass the anonymized narrative and case details to the template
    narrative = selected_case['descripcion_anonimizada']
    return render_template('index.html', narrative=narrative, case=selected_case)


if __name__ == '__main__':
    """
    Entry point of the application. Starts the Flask development server.
    """
    logging.info("Starting Flask app...")
    app.run(debug=True)