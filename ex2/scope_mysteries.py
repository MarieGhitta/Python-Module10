from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counting() -> int:
        nonlocal count
        count += 1
        return count
    return counting


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def adding(power: int) -> int:
        nonlocal total
        total += power
        return total
    return adding


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: str) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        if key in memory:
            return memory[key]
        else:
            return "Memory not found"
    return {
        "store": store,
        "recall": recall
    }


if __name__ == '__main__':
    print("==================================================\n")
    print("Testing mage counter...")
    counter = mage_counter()

    print(counter())
    print(counter())
    print(counter())
    print("\nTesting spell accumulator...")
    acc = spell_accumulator(10)

    print("After adding 5:", acc(5))
    print("After adding 3:", acc(3))
    print("After adding 10:", acc(10))
    print("\nTesting enchantment factory")
    flame = enchantment_factory("Flaming")
    ice = enchantment_factory("Frozen")

    print(flame("Sword"))
    print(ice("Shield"))
    print("\nTesting memory vault...")
    vault = memory_vault()

    vault["store"]("dragon", "Ancient red dragon")
    vault["store"]("spell", "Fireball")

    print(vault["recall"]("dragon"))
    print(vault["recall"]("spell"))
    print(vault["recall"]("unknown"))
    print("\n==================================================")
