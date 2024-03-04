from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def diff_hours(time_str):
    # Convertendo o objeto datetime.time em uma string no formato 'HH:MM'
    time_str = time_str.strftime('%H:%M')
    
    current_time = datetime.now().replace(second=0, microsecond=0)
    given_time = datetime.strptime(time_str, '%H:%M')
    time_diff = current_time - given_time

    hours = abs(time_diff.seconds) // 3600
    minutes = (abs(time_diff.seconds) // 60) % 60

    return f'{hours} horas e {minutes} minutos atrás'
