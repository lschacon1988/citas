from django_cron import CronJobBase, Schedule
from datetime import datetime, timedelta
from .models import Meet

format_hours = "%H:%M"
class VerificarMeetCronJob(CronJobBase):
    RUN_EVERY_MINS = 3  # Intervalo de tiempo para ejecutar la tarea (15 minutos en este caso)
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'app.meet.verificar_Meet_cron_job'  # Código único para el cron job

    def do(self):
        ahora = datetime.now()
        tiempo_limite = ahora - timedelta(minutes=3)
        
        

        Meet_pendientes = Meet.objects.filter(date=ahora.date(), start_time__lt= tiempo_limite.strftime(format_hours), status='scheduled')
        
        print('/*/*/*/*/',Meet_pendientes)
        
        Meet_pendientes.update(status='canceled')
