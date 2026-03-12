import functools
import operator
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        ft = operator.add
    elif operation == "multiply":
        ft = operator.mul
    elif operation == "max":
        ft = max
    elif operation == "min":
        ft = min
    return functools.reduce(ft, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchant = functools.partial(base_enchantment, 50, "fire")
    ice_enchant = functools.partial(base_enchantment, 50, "ice")
    lightning_enchant = functools.partial(base_enchantment, 50, "lightning")
    return {
        "fire_enchant": fire_enchant,
        "ice_enchant": ice_enchant,
        "lightning_enchant": lightning_enchant
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def spell(value) -> str:
        return "unknown spell type"

    @spell.register(int)
    def _(value: int) -> str:
        return "damage spell"

    @spell.register(str)
    def _(value: str) -> str:
        return "enchantment"

    @spell.register(list)
    def _(value: list) -> str:
        return "multi-cast"
    return spell


if __name__ == '__main__':
    print("==================================================\n")
    spells = [10, 20, 30, 40]

    print("Testing spell reducer...")

    print("Add:", spell_reducer(spells, "add"))
    print("Multiply:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))

    print("\nTesting spell enchanter...")

    def base_enchantment(power, element, target):
        return f"{element} enchantment with power {power} on {target}"

    enchants = partial_enchanter(base_enchantment)

    print(enchants["fire_enchant"]("Dragon"))
    print(enchants["ice_enchant"]("Sword"))
    print(enchants["lightning_enchant"]("Staff"))

    print("\nTesting memoized fibonacci")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(10))
    print(dispatcher("fire"))
    print(dispatcher([1, 2, 3]))

    print("\n==================================================")
