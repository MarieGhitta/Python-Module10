# Python Module -- Decorators & Advanced Functions (Revision Sheet)

## 1. Decorators

### What is a decorator?

A decorator is a function that: - takes a function as argument - returns
a new function

Pattern:

``` python
def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper
```

Usage:

``` python
@decorator
def my_function():
    pass
```

Equivalent to:

``` python
my_function = decorator(my_function)
```

------------------------------------------------------------------------

## 2. Decorators with Parameters

Example:

``` python
@power_validator(10)
def cast_spell(...):
```

Python actually executes:

``` python
cast_spell = power_validator(10)(cast_spell)
```

Structure:

    decorator_factory(param)
            ↓
         decorator(func)
            ↓
            wrapper

Example structure:

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

`functools.wraps(func)` copies metadata from the original function to
the wrapper.

Without it:

    function.__name__ = "wrapper"

With it:

    function.__name__ = original_function_name

Usage:

``` python
@functools.wraps(func)
def wrapper(*args, **kwargs):
```

------------------------------------------------------------------------

## 4. \*args and \*\*kwargs

### \*args

Collects positional arguments into a tuple.

Example:

``` python
def f(*args):
    print(args)
```

Call:

``` python
f(1,2,3)
```

Result:

    (1,2,3)

### \*\*kwargs

Collects named arguments into a dictionary.

Example:

``` python
def f(**kwargs):
    print(kwargs)
```

Call:

``` python
f(name="Gandalf", power=100)
```

Result:

    {'name': 'Gandalf', 'power': 100}

### Why tuple and dict?

  syntax       structure
  ------------ ----------------------------
  \*args       tuple (ordered arguments)
  \*\*kwargs   dict (key-value arguments)

------------------------------------------------------------------------

## 5. Parameter vs Argument

  term        meaning
  ----------- ----------------------------------------
  Parameter   variable in function definition
  Argument    value passed when calling the function

Example:

``` python
def add(a,b):   # parameters
    return a+b

add(2,3)        # arguments
```

------------------------------------------------------------------------

## 6. Static Methods

A `@staticmethod`: - belongs to a class - does NOT receive `self` - does
NOT need an instance

Example:

``` python
class MageGuild:

    @staticmethod
    def validate_mage_name(name):
        return name.isalpha()
```

Call:

``` python
MageGuild.validate_mage_name("Gandalf")
```

It can also be called through an instance:

``` python
guild = MageGuild()
guild.validate_mage_name("Gandalf")
```

But this is not necessary.

------------------------------------------------------------------------

## 7. functools.partial

`partial` creates a new function with some arguments already fixed.

Example:

``` python
from functools import partial

def multiply(a,b):
    return a*b

double = partial(multiply,2)

double(5)  # 10
```

Equivalent to:

``` python
def double(x):
    return multiply(2,x)
```

------------------------------------------------------------------------

## 8. functools.singledispatch

Allows function overloading based on argument type.

Example:

``` python
@functools.singledispatch
def spell(value):
    return "unknown"
```

Register implementations:

``` python
@spell.register(int)
def _(value):
    return "damage spell"

@spell.register(str)
def _(value):
    return "enchantment"
```

Call:

``` python
spell(10)     -> damage spell
spell("wand") -> enchantment
```

------------------------------------------------------------------------

## 9. Type Hinting for Decorators

Common pattern:

``` python
from typing import Callable, Any

def decorator(func: Callable) -> Callable:

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)

    return wrapper
```

Why `Any`? Because the decorator does not know the exact signature of
the function it wraps.

------------------------------------------------------------------------

# Quick Mental Model for Decorators

Simple decorator:

    decorator(func)
          ↓
       wrapper

Decorator with parameters:

    decorator_factory(param)
            ↓
         decorator(func)
            ↓
            wrapper

------------------------------------------------------------------------

# Key Takeaways

-   Decorators modify functions without changing their code.
-   `wraps` preserves metadata.
-   `*args` and `**kwargs` allow decorators to work with any function.
-   `staticmethod` organizes utility functions inside classes.
-   `partial` pre-fills function arguments.
-   `singledispatch` enables type-based function behavior.
