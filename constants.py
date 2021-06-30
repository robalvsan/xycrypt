import pathlib

CURRENT_WORKING_DIRECTORY = pathlib.Path(__file__).parent.resolve()

DEFAULT_FILEPATH = "datos"
DEFAULT_FILE_EXAMPLE = "file_example_XLSX_5000.xlsx"

FILENAME_PROMPT_EXPLANATION = f"""
A continuación deberá introducir el nombre del fichero de datos que desea proteger.
- Dicho fichero debe estar obligatoriamente ubicado dentro de una carpeta llamada '{DEFAULT_FILEPATH}'.
- Dicha carpeta deberá estar ubicada en el mismo directorio desde donde se ejecute este script.
- El nombre del fichero debe incluir también la extensión (este script únicamente soporta la extensión .xlsx)
- En caso de que el nombre del fichero tenga espacios en blanco, deberá introducirse entre comillas simples".
- Debe introducirse únicamente el nombre del fichero con extensión.
Ejemplos correctos:
> mi_dataset.xlsx
> 'mi dataset.xlsx'
Ejemplos incorrectos:
> mi_dataset
> mi dataset.xlsx
"""

FILENAME_PROMPT = "Nombre del fichero de datos"

FILENAME_PROMPT_ERROR = """
No ha sido posible procesar correctamente el nombre del fichero. Por favor, inténtelo de nuevo.
"""

PWD_PROMPT_EXPLANATION = """
Crea tu clave de encriptación para proteger las columnas sensibles. Esta clave no se guardará, así que debes
custiodarla en un gestor externo de contraseñas seguro sin hacer ningún tipo de anotación que pueda inducir a su
vinculación con este set de datos. Si pierdes esta clave, no podrás desencriptar los datos!
"""

PWD_PROMPT = "Clave de encriptación"

PWD_PROMPT_ERROR = """
No ha sido posible realizar la creación de la clave. Por favor, inténtelo de nuevo.
"""

SENSITIVE_COLUMNS_PROMPT_EXPLANATION = """
Inserte, separados por comas, los nombres de las variables sensibles. Dicho nombres de variables deben
coincidir exactamente con los nombres de variables que figuren en la primera fila del dataset. Al introducir los
nombres, no deje espacios entre las comas. Si alguno de los nombre de variables presentes en el dataset contiene una
coma como parte de su nombre, corríjalo en el dataset original antes de ejecutar este script.
"""

SENSITIVE_COLUMNS_PROMPT = "Variables sensibles"

SENSITIVE_COLUMNS_PROMPT_ERROR = """
No ha sido posible establecer los nombre de variables sensibles. Por favor, inténtelo de nuevo.
"""

ACTION_PROMPT = "Introduce 'E' para encriptar o 'D' para desencriptar."

SALT_PROMPT_EXPLANATION = """
Toma nota de la siguiente clave auxiliar, será necesaria para desencriptar el mensaje. Esta clave auxiliar no se
guardará, así que debes custiodarla en un gestor externo de contraseñas seguro sin hacer ningún tipo de anotación que
pueda inducir a su vinculación con este set de datos.
Si pierdes esta clave auxiliar, no podrás desencriptar los datos!"""

SALT_PROMPT = "Introduce la clave auxiliar que se te proporcionó durante el proceso de encriptación"
