# Fiche de Révision --- Python (Module : Fonctions avancées & Décorateurs)

Cette fiche résume **les notions et outils utilisés dans les exercices
du module** (sauf le dernier exercice).\
Objectif : revoir rapidement les concepts importants.

------------------------------------------------------------------------

# 1. Fonctions de première classe

En Python, les fonctions sont des **objets**.

Cela signifie qu'on peut : - les stocker dans des variables - les passer
en argument - les retourner depuis une fonction

Exemple :

``` python
def greet(name):
    return f"Hello {name}"

f = greet
print(f("Alice"))
```

------------------------------------------------------------------------

# 2. Fonctions d'ordre supérieur (Higher‑Order Functions)

Une **fonction d'ordre supérieur** est une fonction qui :

-   prend une fonction en argument
-   ou retourne une fonction

Exemple :

``` python
def apply(func, value):
    return func(value)
```

------------------------------------------------------------------------

# 3. Fonctions imbriquées (Nested Functions)

Une fonction peut être définie **à l'intérieur d'une autre fonction**.

``` python
def outer():
    def inner():
        print("Hello")
    inner()
```

Cela permet de : - organiser le code - créer des closures

------------------------------------------------------------------------

# 4. Closures

Une **closure** est une fonction interne qui se souvient des variables
de la fonction externe.

Exemple :

``` python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

------------------------------------------------------------------------

# 5. `nonlocal`

Le mot‑clé `nonlocal` permet de modifier une variable définie dans la
fonction externe.

Sans `nonlocal`, Python créerait une nouvelle variable locale.

------------------------------------------------------------------------

# 6. Décorateurs

Un décorateur est une fonction qui :

-   prend une fonction
-   retourne une fonction modifiée

Structure :

``` python
def decorator(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

Utilisation :

``` python
@decorator
def my_function():
    pass
```

Equivalent à :

``` python
my_function = decorator(my_function)
```

------------------------------------------------------------------------

# 7. Décorateurs avec paramètres

Quand un décorateur prend des arguments :

``` python
@power_validator(10)
```

Python transforme cela en :

    cast_spell = power_validator(10)(cast_spell)

Structure :

    decorator_factory(param)
            ↓
         decorator(func)
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

# 8. `functools.wraps`

`wraps` copie les métadonnées de la fonction originale.

Sans `wraps` :

    function.__name__ == "wrapper"

Avec `wraps` :

    function.__name__ == nom_original

Utilisation :

``` python
import functools

@functools.wraps(func)
def wrapper():
    pass
```

------------------------------------------------------------------------

# 9. `*args` et `**kwargs`

Permettent d'accepter **un nombre variable d'arguments**.

### `*args`

Arguments positionnels → tuple

``` python
def f(*args):
    print(args)
```

### `**kwargs`

Arguments nommés → dictionnaire

``` python
def f(**kwargs):
    print(kwargs)
```

------------------------------------------------------------------------

# 10. Paramètres vs Arguments

  Terme       Signification
  ----------- --------------------------------------------
  Paramètre   variable dans la définition de la fonction
  Argument    valeur passée lors de l'appel

Exemple :

``` python
def add(a, b):  # paramètres
    return a + b

add(2, 3)       # arguments
```

------------------------------------------------------------------------

# 11. `@staticmethod`

Une méthode statique :

-   appartient à une classe
-   ne reçoit pas `self`
-   ne dépend pas d'une instance

Exemple :

``` python
class MageGuild:

    @staticmethod
    def validate_name(name):
        return name.isalpha()
```

Appel :

``` python
MageGuild.validate_name("Gandalf")
```

------------------------------------------------------------------------

# 12. `functools.partial`

`partial` permet de créer une fonction avec certains arguments déjà
fixés.

``` python
from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)

double(5)
```

Equivalent :

``` python
def double(x):
    return multiply(2, x)
```

------------------------------------------------------------------------

# 13. `functools.singledispatch`

Permet d'avoir **plusieurs versions d'une fonction selon le type de
l'argument**.

``` python
import functools

@functools.singledispatch
def spell(value):
    return "unknown"
```

Ajouter des types :

``` python
@spell.register(int)
def _(value):
    return "damage spell"
```

``` python
@spell.register(str)
def _(value):
    return "enchantment"
```

------------------------------------------------------------------------

# 14. Type Hinting

Les annotations de type servent à documenter le code.

Exemple :

``` python
from typing import Callable, Any

def decorator(func: Callable) -> Callable:

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)

    return wrapper
```

### Types utiles

  Type               Signification
  ------------------ --------------------------------------
  Callable           fonction
  Any                n'importe quel type
  list\[int\]        liste d'entiers
  dict\[str, int\]   dictionnaire clé string → valeur int

------------------------------------------------------------------------

# 15. Fonctions utilitaires importantes

### `sorted` avec `key`

``` python
sorted(data, key=lambda x: x["power"])
```

### `map`

``` python
map(lambda x: x*2, numbers)
```

### `max` / `min` avec `key`

``` python
max(mages, key=lambda m: m["power"])
```

------------------------------------------------------------------------

# Schéma mental des décorateurs

### Décorateur simple

    decorator(func)
          ↓
       wrapper

### Décorateur avec paramètres

    factory(param)
          ↓
    decorator(func)
          ↓
       wrapper

------------------------------------------------------------------------

# À retenir

-   Les fonctions sont des objets en Python.
-   Les décorateurs modifient une fonction sans changer son code.
-   `*args` et `**kwargs` rendent les décorateurs génériques.
-   `wraps` conserve les métadonnées.
-   `partial` crée des fonctions spécialisées.
-   `singledispatch` choisit une fonction selon le type d'argument.
