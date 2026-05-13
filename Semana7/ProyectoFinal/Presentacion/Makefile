# Makefile para compilar presentación Beamer

# Variables
MAIN = presentacion
TEX = $(MAIN).tex
PDF = $(MAIN).pdf
LATEX = pdflatex
VIEWER = open  # En macOS. Usa 'xdg-open' en Linux, 'start' en Windows

# Archivos temporales a limpiar
TEMP_FILES = *.aux *.log *.nav *.out *.snm *.toc *.vrb *.bbl *.blg

# Regla por defecto
all: $(PDF)

# Compilar PDF
$(PDF): $(TEX)
	@echo "Compilando presentación..."
	$(LATEX) $(TEX)
	$(LATEX) $(TEX)  # Segunda pasada para referencias
	@echo "✅ Compilación completada: $(PDF)"

# Limpiar archivos temporales
clean:
	@echo "Limpiando archivos temporales..."
	rm -f $(TEMP_FILES)
	@echo "✅ Limpieza completada"

# Limpiar todo (incluyendo PDF)
cleanall: clean
	rm -f $(PDF)
	@echo "✅ Eliminado $(PDF)"

# Compilar y abrir PDF
view: $(PDF)
	$(VIEWER) $(PDF)

# Recompilar desde cero
rebuild: cleanall all

# Ayuda
help:
	@echo "Makefile para presentación Beamer"
	@echo ""
	@echo "Comandos disponibles:"
	@echo "  make          - Compilar presentación"
	@echo "  make clean    - Limpiar archivos temporales"
	@echo "  make cleanall - Limpiar todo (incluyendo PDF)"
	@echo "  make view     - Compilar y abrir PDF"
	@echo "  make rebuild  - Recompilar desde cero"
	@echo "  make help     - Mostrar esta ayuda"

.PHONY: all clean cleanall view rebuild help
