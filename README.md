# MerlinQAAutoProject
Automatizacion basica de scenario con Playwright python


Google no es una web adecuada para pruebas automatizadas E2E debido a:

    Mecanismos anti-bot (CAPTCHA)

    Bloqueos por automatización

    Restricciones en sus términos de uso

En un entorno real, esta automatización se reemplazaría por:

    Uso directo de la URL del resultado esperado (Wikipedia)

    Uso de una API de búsqueda

    Uso de un buscador interno controlado por la empresa

“Para garantizar estabilidad, la automatización comienza directamente en Wikipedia, ya que el objetivo real del test es validar la extracción de información y no el buscador de Google.”

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar todas las pruebas
behave

# Ejecutar un feature específico
behave features/petstore_api.feature

# Ejecutar con más verbosidad
behave -v

# Ejecutar y generar reporte Allure (opcional)
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results