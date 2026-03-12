from app.battle_knight.knight_for_battle import KnightForBattle


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict
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
            name=knight_dict["name"],
            power=knight_dict["power"],
            hp=knight_dict["hp"],
            armour=knight_dict["armour"],
            weapon=knight_dict["weapon"],
            potion=knight_dict["potion"]
        )

    def apply_armour(self) -> None:
        for part in self.armour:
            self.protection += part["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            self.hp += self.potion.get("effect").get("hp", 0)
            self.power += self.potion.get("effect").get("power", 0)
            self.protection += self.potion.get("effect").get("protection", 0)

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
