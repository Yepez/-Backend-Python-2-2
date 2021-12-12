import json
import unittest

from handler import get_negocios


class TestHandler(unittest.TestCase):
    """Tests handler methods"""

    def test_get_negocios(self):
        """Tests get_negocios"""
        event = {}
        event["pathParameters"] = {}
        event["pathParameters"]["condicion"] = "restaurantes"
        event["pathParameters"]["entidad"] = "todos"
        res = get_negocios(event, None)

        self.assertEqual(200, res["statusCode"])

        negocio = json.loads(res["body"])
        self.assertEqual("09002722513004564000037878S7", negocio[0]["CLEE"], msg=None)
        self.assertEqual("8332181", negocio[0]["Id"])
        self.assertEqual(" LA CASA DE TOÑO", negocio[0]["Nombre"])
        self.assertEqual("GRUPO RESTAURANTERO GR2 SA DE CV", negocio[0]["Razon_social"])


if __name__ == "__main__":
    unittest.main()
