from django.test import TestCase
from cards.models import Card

# Create your tests here.

class CardTestCase(TestCase):
    def setUp(self):
        Card.objects.create(
            card_name="Emrakul, the World Anew",
            img_url="https://cards.scryfall.io/large/front/b/9/b914bfd9-5be3-4459-a68a-9b3ea2747bbc.jpg?1717011239",
            mana_cost="12",
            text="When you cast this spell, gain control of all creatures target player controls. Flying, protection from spells and from permanents that were cast this turn. When Emrakul, the World Anew leaves the battlefield, sacrifice all creatures you control. Madness—Pay six Colorless.",
            rarity="Mythic",
            card_set="Modern Horizons 3"
                            
            )
        
    def test_card_to_dict(self):
        card = Card.objects.get(card_name="Emrakul, the World Anew")
        self.assertEqual(card.to_dict(), {
            "id": 1,
            "name": "Emrakul, the World Anew",
            "img_url": "https://cards.scryfall.io/large/front/b/9/b914bfd9-5be3-4459-a68a-9b3ea2747bbc.jpg?1717011239",
            "mana": "12",
            "card_text": "When you cast this spell, gain control of all creatures target player controls. Flying, protection from spells and from permanents that were cast this turn. When Emrakul, the World Anew leaves the battlefield, sacrifice all creatures you control. Madness—Pay six Colorless.",
            "rarity": "Mythic",
            "set": "Modern Horizons 3"
        })
        