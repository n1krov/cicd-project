import os
from behave import given, when, then
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = False
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag

    def handle_endtag(self, tag):
        self.current_tag = None

    def handle_data(self, data):
        if data.strip() == "Hola Mundo" and self.current_tag is not None:
            self.found = True

@given('que el runner de pruebas tiene acceso al archivo de fuentes')
def step_impl(context):
    assert os.path.exists("src"), "La carpeta 'src' no existe"

@when('se examina el contenido del archivo "{filepath}"')
def step_impl(context, filepath):
    assert os.path.exists(filepath), f"El archivo {filepath} no existe"
    with open(filepath, "r", encoding="utf-8") as f:
        context.html_content = f.read()

@then('el documento debe contener una etiqueta estructurada con el texto exacto "Hola Mundo"')
def step_impl(context):
    parser = MyHTMLParser()
    parser.feed(context.html_content)
    assert parser.found, "No se encontró una etiqueta estructurada con el texto exacto 'Hola Mundo'"
