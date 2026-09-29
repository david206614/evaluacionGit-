def validar_estado_afiliado(tipo_afiliacion, estado):
    if estado.lower() == "activo":
        return f"Afiliado con régimen {tipo_afiliacion} habilitado para citas."
    return "Afiliado suspendido o retirado."

print(validar_estado_afiliado("Contributivo", "Activo"))
