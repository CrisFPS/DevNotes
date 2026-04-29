from backend.app.services.extension_classifier import classify


def test_python_classification():
    result = classify(".py")
    assert result["language"] == "Python"
    assert result["object_type"] == "Python"


def test_sql_classification():
    result = classify(".sql")
    assert result["language"] == "SQL"


def test_powerbuilder_window():
    result = classify(".srw")
    assert result["language"] == "PowerBuilder"
    assert result["object_type"] == "PowerBuilder Window"


def test_powerbuilder_datawindow():
    result = classify(".srd")
    assert result["language"] == "PowerBuilder"
    assert result["object_type"] == "PowerBuilder DataWindow"


def test_powerbuilder_menu():
    result = classify(".srm")
    assert result["object_type"] == "PowerBuilder Menu"


def test_powerbuilder_function():
    result = classify(".srf")
    assert result["object_type"] == "PowerBuilder Function"


def test_unknown_extension():
    result = classify(".xyz")
    assert result["language"] == "Outro"
    assert result["object_type"] == ""


def test_markdown():
    result = classify(".md")
    assert result["language"] == "Markdown"


def test_java():
    result = classify(".java")
    assert result["language"] == "Java"
