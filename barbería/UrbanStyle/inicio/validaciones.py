from datetime import date, time, datetime
#valida fecha actual vs fecha de reserva (si es una fecha valida o no)
def validar_fecha_reserva(fecha_reserva):
    fecha_actual = date.today()
    if fecha_reserva < fecha_actual:
        return False
    return True

#compara hora de inicio y hora de fin de la reserva
def validar_horario_reserva(hora_inicio, hora_fin):
    if hora_inicio >= hora_fin:
        return False
    return True
#para la duracion, hora no < hora de reserva
def validar_duracion_reserva(hora_inicio, hora_fin, duracion_minima=60):
    if hora_inicio >= hora_fin:
        return False
    inicio = datetime.combine(date.today(), hora_inicio)
    fin = datetime.combine(date.today(), hora_fin)
    duracion = fin - inicio
    minutos = duracion.total_seconds() / 60
    if minutos < duracion_minima:
        return False
    return True
