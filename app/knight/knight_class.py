from app.battle_knight.knight_for_battle import KnightForBattle


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @classmethod
    def new_knight(cls, knight_dict: dict) -> Knight:
        return cls(
            **knight_dict
        )

    def apply_armour(self) -> None:
        for part in self.armour:
            self.protection += part["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion.get("effect")
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def prepare_for_battle(self) -> KnightForBattle:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

        return KnightForBattle(
            self.name,
            self.hp,
            self.power,
            self.protection,
        )
