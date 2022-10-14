def calcular_total_pago(pago_sin_impuesto,impuesto):
    pago_total=pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

pago_sin_impuesto = float(input('ingrese el valor de la compra: '))
impuesto= float(input('valor del impuesto: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'pago con impuesto: {pago_con_impuesto}')
