from barcode import EAN13
from barcode.writer import ImageWriter

RA = {
    "Yahan": "000112235013",
    "Rubens": "000111723903",
    "Ariel": "000108380199",
    "Sofia": "000110323364",
    "Miguel": "000111770556",
    "Mariane": "000113273823",
    "Heloisa": "000110379048"
}

for name, cod in RA.items():
    cod = cod[:12]
    codigo_de_barra = EAN13(cod, writer=ImageWriter())
    codigo_de_barra.save(f"Codigo_RA_{name}")
