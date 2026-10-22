VENV    = venv_mac
PYTHON  = $(VENV)/bin/python
PIP     = $(VENV)/bin/pip
FLASK   = $(VENV)/bin/flask
APP     = cinema

.PHONY: all install run clean help

all: run

install:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) -m flask --debug --app=$(APP) run

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf instance/cinema.db
	rm -rf instance/
	@echo "Limpieza completada."


clean-all: clean
	rm -rf $(VENV)
	@echo "Entorno virtual eliminado. Ejecuta 'make install' para recrearlo."

help:
	@echo ""
	@echo "Comandos disponibles:"
	@echo "  make install    Crea el venv e instala dependencias"
	@echo "  make run        Arranca el servidor Flask (debug)"
	@echo "  make clean      Borra caché Python y base de datos local"
	@echo "  make clean-all  Borra todo lo anterior + el entorno virtual"
	@echo ""
