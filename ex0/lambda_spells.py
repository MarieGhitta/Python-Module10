def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact['power'],
        reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(
        lambda mage: mage['power'] >= min_power,
        mages
    ))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(
        lambda name: "* " + name + " *",
        spells
    ))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda mage: mage['power'])['power'],
        "min_power": min(mages, key=lambda mage: mage['power'])['power'],
        "avg_power": sum(map(lambda mage: mage['power'], mages))/len(mages)
    }


if __name__ == '__main__':
    artifacts = [{'name': 'Fire Staff', 'power': 78, 'type': 'accessory'},
                 {'name': 'Storm Crown', 'power': 111, 'type': 'weapon'},
                 {'name': 'Earth Shield', 'power': 101, 'type': 'accessory'},
                 {'name': 'Ice Wand', 'power': 82, 'type': 'relic'}]
    mages = [{'name': 'Kai', 'power': 69, 'element': 'earth'},
             {'name': 'Alex', 'power': 90, 'element': 'ice'},
             {'name': 'Morgan', 'power': 74, 'element': 'fire'},
             {'name': 'River', 'power': 75, 'element': 'wind'},
             {'name': 'Phoenix', 'power': 78, 'element': 'light'}]
    spells = ['earthquake', 'freeze', 'meteor', 'heal']
    print("==================================================\n")
    print("Testing artifact sorter...")
    print(artifact_sorter(artifacts))
    print("\nTesting mage filter...")
    print(power_filter(mages, 80))
    print("\nTesting spell transformer...")
    print(spell_transformer(spells))
    print("\nTesting mage stats...")
    print(mage_stats(mages))
    print("\n==================================================")
