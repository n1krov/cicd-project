from validador import validar_texto_saludo

def test_saludo_exacto():
    assert validar_texto_saludo("Hola Mundo") is True

def test_saludo_vacio():
    assert validar_texto_saludo("") is False

def test_saludo_muy_largo():
    assert validar_texto_saludo("a" * 51) is False

def test_saludo_largo_limite():
    assert validar_texto_saludo("a" * 50) is False

def test_saludo_diferente():
    assert validar_texto_saludo("Hola Mundo!") is False
    assert validar_texto_saludo("Hola") is False

def test_entrada_no_string():
    assert validar_texto_saludo(None) is False
    assert validar_texto_saludo(123) is False
