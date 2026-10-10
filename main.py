fuerza = 0
movimiento = 0
observacion_local = 0
inicio_observacion = 0

# Tiempo de vigencia de la observación humana
# 10000 ms = 10 segundos
TIEMPO_OBSERVACION = 10000


def on_button_pressed_a():
    global observacion_local

    # La persona local informa:
    # "Sin observación relevante"
    observacion_local = 0

    basic.show_string("OK")

    serial.write_value("observacion", observacion_local)


input.on_button_pressed(Button.A, on_button_pressed_a)


def on_button_pressed_b():
    global observacion_local
    global inicio_observacion

    # La persona local informa:
    # "Hay una observación relevante"
    observacion_local = 1

    # Guardamos el momento en que comenzó
    # la observación humana
    inicio_observacion = input.running_time()

    basic.show_string("H")

    serial.write_value("observacion", observacion_local)


input.on_button_pressed(Button.B, on_button_pressed_b)


def on_forever():
    global fuerza
    global movimiento
    global observacion_local

    # CAPA SENSOR
    fuerza = input.acceleration(Dimension.STRENGTH)

    # Diferencia respecto del valor aproximado
    # de reposo por gravedad
    movimiento = abs(fuerza - 1000)

    # CONTROL TEMPORAL DE LA OBSERVACIÓN HUMANA
    if observacion_local == 1:

        tiempo_transcurrido = input.running_time() - inicio_observacion

        if tiempo_transcurrido > TIEMPO_OBSERVACION:

            observacion_local = 0

            serial.write_value("observacion_vencida", 1)

    # REGISTRO SERIAL
    serial.write_value("movimiento", movimiento)
    serial.write_value("observacion", observacion_local)

    # INTERPRETACIÓN DEL SISTEMA

    # Sensor + observación humana
    if movimiento > 150 and observacion_local == 1:

        basic.show_icon(IconNames.YES)

    # Solo sensor
    elif movimiento > 150:

        basic.show_icon(IconNames.DIAMOND)

    # Solo observación humana activa
    elif observacion_local == 1:

        basic.show_icon(IconNames.SQUARE)

    # Estado normal
    else:

        basic.show_icon(IconNames.SMALL_DIAMOND)

    basic.pause(500)


basic.forever(on_forever)