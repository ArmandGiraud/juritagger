#Usage

## simple usage
```python
from juritagger import JuriMatcher

opts = {"dico_files":
        ["./dicos/merged.txt", "./dicos/cluster_merged_classif.json"],
        "spacy_model" : "fr_core_news_md"
        
        }
jm = JuriMatcher(**opts)

text = """L'indemnisation du salarié dépend du nombre de jours de fermeture
de l'entreprise et du nombre de jours de congés JUR acquis par le salarié."""

matches, doc = jm.tag_doc(fiche_text, mode = "flat")
matches

[OUT]
>>> [('JUR', 1, 2),
>>> ('JUR', 3, 4),
>>> ('JUR', 19, 22),
>>> ('JUR', 21, 22),
>>> ('JUR', 26, 27)]
```
![](./images/flat.png)

## classified terms

```python
from juritagger import JuriMatcher

opts = {"dico_files":
        ["./dicos/merged.txt", "./dicos/cluster_merged_classif.json"],
        "spacy_model" : "fr_core_news_md"
        
        }
jm = JuriMatcher(**opts)

text = """L'indemnisation du salarié dépend du nombre de jours de fermeture
de l'entreprise et du nombre de jours de congés JUR acquis par le salarié."""

matches, doc = jm.tag_doc(fiche_text, mode = "class")
matches

>>>[('CHOMAGE', 1, 2),
>>> ('PERS', 3, 4),
>>> ('PERS', 3, 4),
>>> ('CONGE', 19, 22),
>>> ('CONGE', 21, 22),
>>> ('PERS', 26, 27),
>>> ('PERS', 26, 27)]
```
![](./images/class.png)