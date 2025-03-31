# Voces_perdidas

Aplicación web basada en Flask diseñada para crear conciencia sobre las personas desaparecidas, presentando historias anonimizadas de sus desapariciones. La aplicación procesa datos de un archivo CSV que contiene detalles sobre las personas desaparecidas y utiliza un modelo de IA para generar narrativas basadas en descripciones reales. El objetivo es sensibilizar al público al mostrar estas historias de manera impactante.

## Estructura del Proyecto

El proyecto consta de los siguientes archivos y directorios:

- **templates/index.html**: El documento HTML principal que contiene la estructura de la página web.
- **static/**: Directorio que contiene los recursos estáticos como imágenes, íconos y estilos CSS.
- **app.py**: Archivo principal de Flask que maneja las rutas y la lógica del servidor.
- **process_cases.py**: Script que procesa los datos del archivo CSV con la bse de datos completa y genera narrativas anonimizadas.
- **data/processed_cases.csv**: Archivo CSV que contiene los datos originales de los casos de desapariciones.

## Instrucciones de Configuración

1. **Clonar el Repositorio**: 
   ```bash
   git clone https://github.com/neuterlee/Voces_perdidas.git
   cd Voces_perdidas
   ```

2. **Instalar Dependencias**: 
   Asegúrate de tener Python instalado. Luego ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la Aplicación**: 
   Inicia el servidor Flask ejecutando el archivo `app.py`:
   ```bash
   python app.py
   ```

4. **Acceder a la Aplicación**: 
   Abre tu navegador web y navega a `http://localhost:5000` para ver la aplicación.

## Uso

Al cargar la aplicación, se mostrará una descripción narrativa de un caso de desaparición en el centro de la página. El texto se generará dinámicamente utilizando las descripciones proporcionadas en el archivo `casos.csv`, asegurando que los nombres y ubicaciones sean anonimizados para proteger la privacidad.

## Contribuciones

Las contribuciones para mejorar la aplicación son bienvenidas. Por favor, haz un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.