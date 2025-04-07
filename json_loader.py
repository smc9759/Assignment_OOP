import json
from Stat import 스탯

def load_role_stats(file_path="role_stat_config.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    role_stat_dict = dict()
    for role, values in data.items():
        role_stat_dict[role] = 스탯(**values)  # hp, mp, dmg 키워드 전달
    return role_stat_dict

ROLE_STAT_CONFIG = load_role_stats()