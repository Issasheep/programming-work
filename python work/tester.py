
class common: 
    item_stat_multiplyer = 1
    possable_reroll = 0
    
class rare:
    item_stat_multiplyer = 1.4
    possable_reroll = 2

class epic: 
    item_stat_multiplyer = 1.8
    possable_reroll = 4

class legendary:
    item_stat_multiplyer = 2.5
    possable_reroll = 7



class spear:
    weapon_type: str = "melee"
    base_range: float = 4.5 
    crit_chance: float = 1
    crit_damage: float = 2.5

class cross_bow:
    weapon_type: str = "ranged"
    base_range: float = 9
    crit_chance: float = 0.5
    crit_damage: float = 1.5

class sword:
    weapon_type: str = "melee"
    base_range: float = 3.5
    crit_chance: float = 5
    crit_chance: float = 3.5


print (cross_bow.weapon_type)




