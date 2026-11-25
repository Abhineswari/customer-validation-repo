from customer_validation import validate_customer
def test_valid_csutomer():
  customer = {
    "name": "John",
    "age": 25,
    "email": "john@email.com"
  }
  assert validate_customer(customer) ==  True
