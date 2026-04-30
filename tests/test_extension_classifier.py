from backend.app.services.extension_classifier import classify


def test_python_classification():
    """TC-CLS-01 | Unitário | Classificar .py como Python."""
    result = classify(".py")
    assert result["language"] == "Python"
    assert result["object_type"] == "Python"


def test_sql_classification():
    """TC-CLS-02 | Unitário | Classificar .sql como SQL."""
    result = classify(".sql")
    assert result["language"] == "SQL"


def test_powerbuilder_window():
    """TC-CLS-03 | Unitário | Classificar .srw como PowerBuilder Window."""
    result = classify(".srw")
    assert result["language"] == "PowerBuilder"
    assert result["object_type"] == "PowerBuilder Window"


def test_powerbuilder_datawindow():
    """TC-CLS-04 | Unitário | Classificar .srd como PowerBuilder DataWindow."""
    result = classify(".srd")
    assert result["language"] == "PowerBuilder"
    assert result["object_type"] == "PowerBuilder DataWindow"


def test_powerbuilder_menu():
    """TC-CLS-05 | Unitário | Classificar .srm como PowerBuilder Menu."""
    result = classify(".srm")
    assert result["object_type"] == "PowerBuilder Menu"


def test_powerbuilder_function():
    """TC-CLS-06 | Unitário | Classificar .srf como PowerBuilder Function."""
    result = classify(".srf")
    assert result["object_type"] == "PowerBuilder Function"


def test_unknown_extension():
    """TC-CLS-07 | Unitário | Retornar Outro para extensão desconhecida."""
    result = classify(".xyz")
    assert result["language"] == "Outro"
    assert result["object_type"] == ""


def test_markdown():
    """TC-CLS-08 | Unitário | Classificar .md como Markdown."""
    result = classify(".md")
    assert result["language"] == "Markdown"


def test_java():
    """TC-CLS-09 | Unitário | Classificar .java como Java."""
    result = classify(".java")
    assert result["language"] == "Java"


def test_powerbuilder_user_object():
    """TC-CLS-10 | Unitário | .sru deve classificar como PowerBuilder User Object."""
    result = classify(".sru")
    assert result["language"] == "PowerBuilder"
    assert result["object_type"] == "PowerBuilder User Object"


def test_powerbuilder_application():
    """TC-CLS-11 | Unitário | .sra deve classificar como PowerBuilder Application."""
    result = classify(".sra")
    assert result["object_type"] == "PowerBuilder Application"


def test_powerbuilder_structure():
    """TC-CLS-12 | Unitário | .srs deve classificar como PowerBuilder Structure."""
    result = classify(".srs")
    assert result["object_type"] == "PowerBuilder Structure"
