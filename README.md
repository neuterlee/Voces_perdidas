<<<<<<< HEAD
# Voces_perdidas
Aplicación web basada en Flask diseñada para crear conciencia sobre las personas desaparecidas, presentando historias anonimizadas de sus desapariciones. La aplicación procesa datos de un archivo CSV que contiene detalles sobre las personas que no encontramos aun.
=======
# Aplicación Web de Desapariciones

Este proyecto es una aplicación web diseñada para mostrar narrativas de casos de desapariciones. Las narrativas se generan utilizando un modelo de IA basado en descripciones reales proporcionadas en un archivo de texto. La aplicación tiene como objetivo crear conciencia sobre las personas desaparecidas al presentar sus historias de manera impactante.

## Estructura del Proyecto

El proyecto consta de los siguientes archivos y directorios:

- **public/index.html**: El documento HTML principal que contiene la estructura de la página web.
- **src/app.js**: El archivo JavaScript que maneja la lógica para leer el archivo de texto, generar narrativas utilizando DeepAI y actualizar dinámicamente el contenido de la página web.
- **src/styles.css**: El archivo CSS que estiliza la página web, estableciendo un fondo negro, texto blanco y centrando el contenido.
- **data/cedulassampledes.txt**: Un archivo de texto que contiene descripciones originales de casos de desapariciones utilizadas como referencia para generar narrativas.
- **package.json**: El archivo de configuración para npm, que lista las dependencias necesarias para el proyecto.

## Instrucciones de Configuración

1. **Clonar el Repositorio**: 
   ```bash
   git clone <repository-url>
   cd desapariciones-web
   ```

2. **Instalar Dependencias**: 
   Asegúrate de tener Node.js instalado. Luego ejecuta:
   ```bash
   npm install
   ```

3. **Ejecutar la Aplicación**: 
   Inicia un servidor local para servir la aplicación. Puedes usar un paquete como `http-server` u otro servidor de tu elección:
   ```bash
   npx http-server public
   ```

4. **Acceder a la Aplicación**: 
   Abre tu navegador web y navega a `http://localhost:8080` (o el puerto especificado por tu servidor) para ver la aplicación.

## Uso

Al cargar la aplicación, se mostrará una descripción narrativa de un caso de desaparición en el centro de la página. El texto se generará dinámicamente utilizando las descripciones proporcionadas en el archivo `cedulassampledes.txt`, asegurando que los nombres y ubicaciones sean anonimizados para proteger la privacidad.

## Contribuciones

Las contribuciones para mejorar la aplicación son bienvenidas. Por favor, haz un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
>>>>>>> 46c2acb (Initial commit: Add navigation and touch controls for mobile compatibility)
