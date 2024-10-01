<div align="center">
<img src="https://avatars.githubusercontent.com/ml/17635?s=140&v=" width="100" alt="Arcane Engine Logo">
</div>

<p align="center">
  <a href="https://github.com/apps/arcane-engine/installations/new"><b>Installer</b></a> |
  <a href="https://docs.arcane.engineer">Documentation</a> |
  <a href="https://arcane.engineer/">Site Web</a>
</p>

# Arcane Kit

Bienvenue dans le kit de développement pour **[Arcane Engine](https://arcane.engineer/engine)**, une plateforme qui permet aux développeurs de créer facilement des workflows d'agents.

Ce projet contient le SDK Python officiel.

## Utilisation

Installez le SDK Python avec pip :

```bash
pip install arcane-engine
```

Utilisez la classe `ArcaneEngine` pour créer des tâches et interagir avec le moteur. Voici un exemple de création d'une tâche et d'attente du résultat :

```python
from arcane.engine import ArcaneEngine
from arcane.util import wait_for_result

engine = ArcaneEngine()
task = engine.create_task("arc-eng/kit", "Résumez le fichier README et créez un problème Github avec le résultat.")
result = wait_for_result(task)
print(f"Tâche terminée. Résultat :\n\n{task.result}")
```
