.PHONY: install run test format clean help

install:
	python -m pip install -r requirements.txt

run:
	python -m uvicorn backend.app.main:app --reload --port 8000

test:
	python -m pytest -v

format:
	python -m black backend tests

clean:
	python -c "import pathlib, shutil; [shutil.rmtree(p, ignore_errors=True) for p in ['.pytest_cache', '.tmp_pytest']]; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').glob('.pytest_tmp*')]; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').glob('pytest-cache-files-*')]; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').rglob('__pycache__')]"

help:
	@echo Comandos disponiveis:
	@echo   make install  - Instala as dependencias
	@echo   make run      - Inicia o servidor em localhost:8000
	@echo   make test     - Executa os testes
	@echo   make format   - Formata o codigo Python com Black
	@echo   make clean    - Remove caches e arquivos temporarios
