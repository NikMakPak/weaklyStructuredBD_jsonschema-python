import json
from jsonschema import validate, ValidationError

with open('schema.json', 'r') as f:
    schema = json.load(f)

# Функция для проверки объекта на соответствие схеме
def validate_object(obj):
    try:
        validate(instance=obj, schema=schema)
        print("Данные корректны.")
    except ValidationError as e:
        print(f"Ошибка валидации: {e.message}")

with open('data.json', 'r') as f:
    data = json.load(f)
    validate_object(data)

with open('error_data.json', 'r') as f:
    data = json.load(f)
    validate_object(data)
