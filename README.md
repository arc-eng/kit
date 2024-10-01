<div align="center">
<img src="https://avatars.githubusercontent.com/ml/17635?s=140&v=" width="100" alt="Arcane Engine Logo">
</div>

<p align="center">
  <a href="https://github.com/apps/arcane-engine/installations/new"><b>Installieren</b></a> |
  <a href="https://docs.arcane.engineer">Dokumentation</a> |
  <a href="https://arcane.engineer/">Webseite</a>
</p>

# Arcane Kit

Willkommen zum Entwicklungskit für **[Arcane Engine](https://arcane.engineer/engine)**, eine Plattform, die es Entwicklern ermöglicht, agentische Workflows einfach zu erstellen.

Dieses Projekt enthält das offizielle Python SDK.

## Verwendung

Installieren Sie das Python SDK mit pip:

```bash
pip install arcane-engine
```

Verwenden Sie die `ArcaneEngine`-Klasse, um Aufgaben zu erstellen und mit der Engine zu interagieren. Hier ist ein Beispiel, wie man eine Aufgabe erstellt und auf das Ergebnis wartet:

```python
from arcane.engine import ArcaneEngine
from arcane.util import wait_for_result

engine = ArcaneEngine()
task = engine.create_task("arc-eng/kit", "Fasse die README-Datei zusammen und erstelle ein Github-Issue mit dem Ergebnis.")
result = wait_for_result(task)
print(f"Aufgabe abgeschlossen. Ergebnis:\n\n{task.result}")
```
