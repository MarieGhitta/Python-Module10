# Fiche de Révision -- Python : Décorateurs et Fonctions Avancées

## 1. Les Décorateurs

### Qu'est-ce qu'un décorateur ?

Un décorateur est une fonction qui :

-   prend une fonction en argument
-   retourne une nouvelle fonction

Structure générale :

``` python
def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper
```

Utilisation :

``` python
@decorator
def ma_fonction():
    pass
```

Python transforme en réalité cela en :

``` python
ma_fonction = decorator(ma_fonction)
```

------------------------------------------------------------------------

## 2. Décorateurs avec paramètres

Exemple :

``` python
@power_validator(10)
def cast_spell(...):
```

Python exécute en réalité :

``` python
cast_spell = power_validator(10)(cast_spell)
```

Structure :

    factory_decorateur(parametre)
            ↓
         decorateur(func)
            ↓
            wrapper

Exemple :

``` python
def power_validator(min_power):

    def decorator(func):

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator
```

------------------------------------------------------------------------

## 3. functools.wraps

`functools.wraps(func)` permet de **copier les métadonnées de la
fonction originale** dans le wrapper.

Sans `wraps` :

    fonction.__name__ = "wrapper"

Avec `wraps` :

    fonction.__name__ = nom_de_la_fonction_originale

Utilisation :

``` python
@functools.wraps(func)
def wrapper(*args, **kwargs):
```

------------------------------------------------------------------------

## 4. \*args et \*\*kwargs

### \*args

`*args` récupère **tous les arguments positionnels** dans un tuple.

Exemple :

``` python
def f(*args):
    print(args)

f(1,2,3)
```

Résultat :

    (1,2,3)

### \*\*kwargs

`**kwargs` récupère **tous les arguments nommés** dans un dictionnaire.

Exemple :

``` python
def f(**kwargs):
    print(kwargs)

f(name="Gandalf", power=100)
```

Résultat :

    {'name': 'Gandalf', 'power': 100}

### Pourquoi tuple et dict ?

  syntaxe      structure
  ------------ --------------
  \*args       tuple
  \*\*kwargs   dictionnaire

------------------------------------------------------------------------

## 5. Paramètre vs Argument

  Terme       Signification
  ----------- -----------------------------------
  Paramètre   variable définie dans la fonction
  Argument    valeur passée lors de l'appel

Exemple :

``` python
def add(a,b):   # paramètres
    return a+b

add(2,3)        # arguments
```

------------------------------------------------------------------------

## 6. @staticmethod

Une `@staticmethod` :

-   appartient à une classe
-   ne reçoit **pas `self`**
-   ne dépend pas d'une instance

Exemple :

``` python
class MageGuild:

    @staticmethod
    def validate_mage_name(name):
        return name.isalpha()
```

Appel :

``` python
MageGuild.validate_mage_name("Gandalf")
```

On peut aussi l'appeler via un objet :

``` python
guild = MageGuild()
guild.validate_mage_name("Gandalf")
```

------------------------------------------------------------------------

## 7. functools.partial

`partial` permet de créer **une nouvelle fonction avec certains
arguments déjà fixés**.

Exemple :

``` python
from functools import partial

def multiply(a,b):
    return a*b

double = partial(multiply,2)

double(5)
```

Equivalent à :

``` python
def double(x):
    return multiply(2,x)
```

------------------------------------------------------------------------

## 8. functools.singledispatch

Permet de définir **plusieurs comportements selon le type de
l'argument**.

Exemple :

``` python
@functools.singledispatch
def spell(value):
    return "unknown"
```

Enregistrement des types :

``` python
@spell.register(int)
def _(value):
    return "damage spell"

@spell.register(str)
def _(value):
    return "enchantment"
```

Exemple :

``` python
spell(10)     -> "damage spell"
spell("wand") -> "enchantment"
```

------------------------------------------------------------------------

## 9. Type Hinting pour les décorateurs

Structure classique :

``` python
from typing import Callable, Any

def decorator(func: Callable) -> Callable:

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)

    return wrapper
```

Pourquoi `Any` ?

Parce qu'un décorateur ne connaît pas la signature exacte de la fonction
décorée.

------------------------------------------------------------------------

# Modèle mental rapide

Décorateur simple :

    decorator(func)
          ↓
       wrapper

Décorateur avec paramètres :

    factory(parametre)
            ↓
         decorator(func)
            ↓
            wrapper

------------------------------------------------------------------------

# Points clés à retenir

-   Les décorateurs permettent de modifier une fonction sans changer son
    code.
-   `functools.wraps` conserve les métadonnées de la fonction.
-   `*args` et `**kwargs` rendent les décorateurs compatibles avec
    toutes les fonctions.
-   `@staticmethod` sert à organiser des fonctions liées à une classe.
-   `partial` permet de créer des fonctions spécialisées.
-   `singledispatch` permet de choisir une implémentation selon le type
    d'un argument.
