
from product import product_details

def test_product_details():
    result = product_details("P101", "Laptop", 2, 50000.0)

    expected = (
        "Product ID: P101\n"
        "Product Name: Laptop\n"
        "Quantity: 2\n"
        "Price: 50000.0"
    )

    assert result == expected


def test_product_details_second():
    result = product_details("P102", "Mouse", 5, 500.0)

    expected = (
        "Product ID: P102\n"
        "Product Name: Mouse\n"
        "Quantity: 5\n"
        "Price: 500.0"
    )

    assert result == expected
