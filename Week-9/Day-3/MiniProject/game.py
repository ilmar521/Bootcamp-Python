from characters import Druid
from characters import Warrior
from characters import Mage

war_viks = Warrior('Viks', 100, 20)
dr_mike = Druid('Mike', 150, 10)
mage_briar = Mage('Briar', 80, 15)

print(war_viks, dr_mike, mage_briar)

war_viks.brawl(dr_mike)
dr_mike.meditate()
dr_mike.animal_help()
dr_mike.fight(war_viks)
mage_briar.curse(war_viks)
mage_briar.summon()
mage_briar.cast_spell(war_viks)
war_viks.train()
war_viks.roar(dr_mike)
war_viks.basic_attack(dr_mike)
war_viks.brawl(mage_briar)
war_viks.train()

print(war_viks, dr_mike, mage_briar)
