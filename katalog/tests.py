from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from katalog.models import CatalogItem

class KatalogTests(TestCase):
    def test_create_catalog_item(self):
        item = CatalogItem.objects.create(
            item_name = "ASUS ROG Zephyrus G15", 
            item_price = 26149000, 
            item_stock = 1, 
            description = "Ryzen 6800HS & RTX 3060", 
            rating = 5, 
            item_url = "https://www.tokopedia.com/nvidiageforcelt/asus-rog-zephyrus-g15-ga503rm-geforce-rtx-3060-ryzen-7-6800hs-unit"
        )
        self.assertEquals(item.item_name, "ASUS ROG Zephyrus G15")
        self.assertEquals(item.item_price, 26149000)
        self.assertEquals(item.item_stock, 1)
        self.assertEquals(item.description, "Ryzen 6800HS & RTX 3060")
        self.assertEquals(item.rating, 5)
        self.assertEquals(item.item_url, "https://www.tokopedia.com/nvidiageforcelt/asus-rog-zephyrus-g15-ga503rm-geforce-rtx-3060-ryzen-7-6800hs-unit")


# class Tugas2UnitTesting(TestCase):
#     def test_hello_is_exist(self):
#         response = Client().get('/katalog/')
#         self.assertEqual(response.status_code,200)