def converter(original_unit, coefficient=0.3048):
    return original_unit * coefficient

print(converter(10))
