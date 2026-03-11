def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combine(value):
        return (spell1(value), spell2(value))
    return combine


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def mega_fireball(value):
        return base_spell(value) * multiplier
    return mega_fireball


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(x):
        if condition(x):
            return spell(x)
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sort_spell(value):
        for spell in spells:
            value = spell(value)
        return value
    return sort_spell


if __name__ == '__main__':
    print("==================================================\n")
    print("Testing spell combiner...")

    def add2(x):
        return x + 2

    def multiply3(x):
        return x * 3

    combo = spell_combiner(add2, multiply3)
    print(combo(5))
    print("\nTesting power amplifier...")

    def fireball(x):
        return x * 10

    mega_fireball = power_amplifier(fireball, 3)

    result = mega_fireball(2)

    print("Result:", result)
    print("\nTesting conditional caster...")

    def is_even(x):
        return x % 2 == 0

    def double(x):
        return x * 2

    spell = conditional_caster(is_even, double)

    print("Test avec 4 :", spell(4))  # devrait lancer le sort
    print("Test avec 5 :", spell(5))  # devrait échouer
    print("\nTesting spell sequence...")

    def add2(x):
        return x + 2

    def multiply3(x):
        return x * 3

    def minus1(x):
        return x - 1
    spells = [add2, multiply3, minus1]
    sequence = spell_sequence(spells)

    print("Result:", sequence(5))
    print("\n==================================================")
