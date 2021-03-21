import unittest

# from Testing.testing_lab.cat.cat import Cat


class CatTests(unittest.TestCase):
    # Cat's size is increased after eating
    def test_catEat_CatSizeIncreaseAfterEating(self):
        name = "Tommy"
        cat = Cat(name)
        cat.eat()
        self.assertEqual(1, cat.size)

    # Cat is fed after eating
    def test_catEat_CatFedIsTrueAfterEating(self):
        name = "Tommy"
        cat = Cat(name)
        cat.eat()
        self.assertTrue(cat.fed)

    # Cat cannot eat if already fed, raises an error
    def test_catEat_RaiseErrorIfCatFedIsTrue(self):
        name = "Tommy"
        cat = Cat(name)
        cat.eat()
        with self.assertRaises(Exception) as context:
            cat.eat()
        self.assertIsNotNone(context.exception)

    # Cat cannot fall asleep if not fed, raises an error
    def test_catSleep_RaiseErrorIfCatFedIsFalse(self):
        name = "Tommy"
        cat = Cat(name)
        with self.assertRaises(Exception) as context:
            cat.sleep()
        self.assertIsNotNone(context.exception)

    # Cat is not sleepy after sleeping
    def test_catEatSleep_CatIsNotSleepyAfterSleeping(self):
        name = "Tommy"
        cat = Cat(name)
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    unittest.main()
