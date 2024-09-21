def calcular_descuento(monto_total, descuento=10):

  descuento_decimal = descuento / 100
  monto_descuento = monto_total * descuento_decimal
  return monto_descuento

precio_original_1 = 9624
descuento_aplicado_1 = calcular_descuento(precio_original_1)
precio_final_1 = precio_original_1 - descuento_aplicado_1

print("Monto total:", precio_original_1)
print("El descuento es:", descuento_aplicado_1)
print("El precio final es:", precio_final_1)

print ()

precio_original_2= float(input("Ingrese un Monto: "))
descuento_2 = int(input("Ingrese un porcentaje de Descuento: "))
precio_descuento_2 = calcular_descuento(precio_original_2 , descuento_2)
precio_2 = precio_original_2 - precio_descuento_2

print("Monto total:", precio_original_2)
print("El descuento es:", precio_descuento_2)
print("El precio final es:", precio_2)
