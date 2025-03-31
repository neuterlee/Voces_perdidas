import csv
import random
import logging
from openai import OpenAI

# Configuración del cliente de DeepSeek
client = OpenAI(api_key="xxx", base_url="https://api.deepseek.com")  # Reemplaza con tu API key

# Configuración de logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def anonymize_case(case):
    """Send the case description, name, and age to DeepSeek for rewriting."""
    try:
        logging.debug(f"Sending case to DeepSeek: {case}")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Eres un asistente útil que reescribe descripciones de desaparición como historias "
                        "breves pero que transmiten lo que pasó en español. Inspiras un poco de melancolía "
                        "pero no drama. Narras una desaparición."
                    )
                },
             {
                    "role": "user",
                    "content": (
                        f"Por favor, reescribe esta descripción como una historia MUY breve, repito muy breve. "
                        f"No agregues título, menciona la fecha y la hora en tu respuesta. La historia debe narrar "
                        f"la desaparición de {case['nombre_completo']}, quien tenía {case['edad_momento_desaparicion']} "
                        f"años al momento de su desaparición. Remueve cualquier numero de casa, placa de auto o dato "
                        f"sensible que veas. Además, anonimiza los nombres de cualquier otra persona mencionada en la "
                        f"descripción, pero deja intacto el nombre {case['nombre_completo']} y presentalo en Sentencecase. "
                        f"Descripción: {case['descripcion_desaparicion']}."
                    )
                 },
            ]
        )
        rewritten_story = response.choices[0].message.content
        logging.debug(f"Received response from DeepSeek: {rewritten_story}")
        return rewritten_story
    except Exception as e:
        logging.error(f"Error communicating with DeepSeek: {e}")
        return f"Error comunicándose con DeepSeek: {e}"

def process_csv(input_file, output_file, num_cases=5):
    """Process the input CSV, filter cases, anonymize them, and save to a new CSV."""
    try:
        # Leer el archivo CSV
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            cases = []

            # Filtrar casos que cumplen con las condiciones
            for row in reader:
                if (row['condicion_localizacion'].strip().upper() == "NO APLICA" and
                        row['estatus_persona_desaparecida'].strip().upper() == "PERSONA DESAPARECIDA"):
                    cases.append(row)

        logging.info(f"Total cases matching criteria: {len(cases)}")

        # Seleccionar 200 casos aleatorios
        if len(cases) < num_cases:
            logging.warning(f"Only {len(cases)} cases available, selecting all.")
            selected_cases = cases
        else:
            selected_cases = random.sample(cases, num_cases)

        # Procesar cada caso y agregar la columna 'descripcion_anonimizada'
        for case in selected_cases:
            case['descripcion_anonimizada'] = anonymize_case(case)

        # Escribir los casos procesados en un nuevo archivo CSV
        with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = list(selected_cases[0].keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(selected_cases)

        logging.info(f"Archivo procesado y guardado en: {output_file}")
    except Exception as e:
        logging.error(f"Error processing CSV: {e}")

if __name__ == "__main__":
    input_csv = '/home/sotavento/Documents/tejer_red/cache/repd_vp_cedulas_principal.csv'
    output_csv = '/home/sotavento/Documents/tejer_red/cache/processed_cases.csv'
    process_csv(input_csv, output_csv)