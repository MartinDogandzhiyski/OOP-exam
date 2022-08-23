from project.pet_shop import PetShop
from unittest import TestCase, main

class PetShopTests(TestCase):
    def test_init(self):
        pet_shop = PetShop("Test")
        self.assertEqual("Test", pet_shop.name)
        self.assertEqual([], pet_shop.pets)
        self.assertEqual({}, pet_shop.food)

    def test_add_food_method_if_raises_error(self):
        pet_shop = PetShop("Test")
        with self.assertRaises(ValueError) as ex:
            pet_shop.add_food('aa', -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_method_with_correct_data(self):
        pet_shop = PetShop("Test")
        result = pet_shop.add_food('aa', 50.5000)
        self.assertEqual({'aa': 50.5000}, pet_shop.food)
        self.assertEqual(f"Successfully added 50.50 grams of aa.", result)
        result = pet_shop.add_food('aa', 30)
        self.assertEqual({'aa': 80.5000}, pet_shop.food)
        self.assertEqual("Successfully added 30.00 grams of aa.", result)

    def test_add_pet_if_raises_correct(self):
        pet_shop = PetShop("Test")
        pet_shop.pets = ['nurko']
        with self.assertRaises(Exception) as ex:
            pet_shop.add_pet('nurko')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_with_correct_data(self):
        pet_shop = PetShop("Test")
        pet_shop.pets = ['nurko']
        result = pet_shop.add_pet('nurko2')
        self.assertEqual(f"Successfully added nurko2.", result)
        self.assertEqual(['nurko', 'nurko2'], pet_shop.pets)

    def test_feed_pet_if_raises_correctly(self):
        pet_shop = PetShop("Test")
        pet_shop.pets = ['nurko']
        with self.assertRaises(Exception) as ex:
            pet_shop.feed_pet('aa', 'aa')
        self.assertEqual(f"Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_not_existing_food(self):
        pet_shop = PetShop("Test")
        pet_shop.pets = ['nurko']
        pet_shop.food = {'aa': 50}
        result = pet_shop.feed_pet('ad', 'nurko' )
        self.assertEqual(f'You do not have ad', result)

    def test_feed_pet_with_existing_food(self):
        pet_shop = PetShop("Test")
        pet_shop.pets = ['nurko']
        pet_shop.food = {'aa': 50}
        result = pet_shop.feed_pet('aa', 'nurko' )
        self.assertEqual("Adding food...", result)
        self.assertEqual({'aa': 1050.00}, pet_shop.food)
        pet_shop.food = {'aa': 101}
        result = pet_shop.feed_pet('aa', 'nurko')
        self.assertEqual({'aa': 1}, pet_shop.food)
        self.assertEqual(f"nurko was successfully fed", result)

    def test_repr_method_if_returns_correctly_string(self):
        pet_shop = PetShop("Test")
        pet_shop.pets = ['nurko', 'nurko2']
        pet_shop.food = {'aa': 50}
        expected_result = f"Shop Test:\n" + f"Pets: nurko, nurko2"
        self.assertEqual(expected_result, pet_shop.__repr__())




if __name__ == '__main__':
    main()
