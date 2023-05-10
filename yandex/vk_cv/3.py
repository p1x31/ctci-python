form_data = {'name': 'Masha'}

try:
    name = from_data["name"]
except KeyError:
    print("error")
    raise
finally:
    print("finally")