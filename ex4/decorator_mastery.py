import functools
from typing import Callable, Any
import time
import random


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if args[2] < min_power:
                raise ValueError("Insufficient power for this spell")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    continue
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name) >= 3 and
                all(char.isalpha() or char == " "
                for char in name))

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


if __name__ == '__main__':
    print("==================================================\n")
    print("\nTesting spell timer...")

    @spell_timer
    def fireball(target, power):
        return "Fireball cast!"

    result = fireball("Dragon", 10)
    print("Returned value:", result)

    print("\nTesting power validator...")
    guild = MageGuild()

    @power_validator(10)
    def cast_spell(power):
        print(f"Spell cast with power {power}")
        return power * 2

    print("=== Strong spell ===")
    print(guild.cast_spell("Fireball", 15))

    print("\n=== Weak spell ===")
    try:
        print(guild.cast_spell("Spark", 5))
    except ValueError as e:
        print("Error:", e)

    print("\nTesting retry spell...")

    @retry_spell(3)
    def unstable_spell():
        print("Casting spell")
        if random.random() < 0.7:
            raise ValueError("Spell failed!")
        return "Spell succeeded!"

    result = unstable_spell()
    print("Result:", result)

    print("\nTesting MageGuild")

    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al28"))

    print(guild.cast_spell("Fireball", 15))
    try:
        print(guild.cast_spell("Spark", 5))
    except ValueError as e:
        print("Error:", e)
    print("\n==================================================")
