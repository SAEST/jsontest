import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_correo():
    # Configuración del servidor SMTP de Gmail
    smtp_host = "gw-correo.ife.org.mx"
    smtp_port = 25
    remitente = "pruebas.dest@ine.mx"

    # Información del build de Jenkins
    build_name = os.getenv('JOB_NAME', 'Desconocido')
    build_result = sys.argv[1] if len(sys.argv) > 1 else 'Desconocido'
    build_duration = sys.argv[2] if len(sys.argv) > 2 else 'Desconocido'
    build_number = os.getenv('BUILD_NUMBER', 'Desconocido')
    build_url = os.getenv('BUILD_URL', 'Desconocido')
    blue_ocean_url = f"{os.getenv('JENKINS_URL')}blue/organizations/jenkins/{build_name}/detail/{build_name}/{build_number}/pipeline"
    log = f"{build_url}execution/node/3/ws/registro_actualizaciones.txt"
    url_dist = f"http://10.35.16.10:8086/publicacion/nacional/base-datos"
    url_json = f"http://10.35.16.10:8086/publicacion/nacional/assets/configuracion.json"
 
    # Configuración del mensaje
    destinatarios = ["eric.ruiz@ine.mx"]#, "georgina.cuadriello@ine.mx", "jessica.trejo@ine.mx", "cristhian.tellez@outlook.com"]
    subject = f"[DEST][Jenkins] Resultado de ejecución de Pipeline: {build_name} Número: {build_number}"
     
    body = f"""
        <h2 style="color: #2E86C1;"> Resultado de Ejecución de Actualización de Json</h2>
        <p>Estimado equipo.</p>
        <p>El pipeline <strong>{build_name}</strong> ha finalizado. Aquí está el resumen:</p>
        <table style="width: 50%; border: 1px solid #ddd; border-collapse: collapse;">
            <tr>
                <td style="padding: 8px; border: 1px solid #ddd;">Build Number</td>
                <td style="padding: 8px; border: 1px solid #ddd;">{build_number}</td>
            </tr>
            <tr>
                <td style="padding: 8px; border: 1px solid #ddd;">Estado</td>
                <td style="padding: 8px; border: 1px solid #ddd;">{build_result}</td>
            </tr>
            <tr>
                <td style="padding: 8px; border: 1px solid #ddd;">Duración</td>
                <td style="padding: 8px; border: 1px solid #ddd;">{build_duration}</td>
            </tr>
        </table>
        <p>Revisa más detalles, es necesario conexion VPN para redINE:</p>
        <p>Usuario: invitado Contraseña: DEST-QA</p>
        <a href="{blue_ocean_url}" style="display: inline-block; padding: 10px 20px; color: #fff; background-color: #5bc0de; text-decoration: none;">Pipeline Blue Ocean</a>
        <a href="{build_url}" style="display: inline-block; padding: 10px 20px; color: #fff; background-color: #5bc0de; text-decoration: none;">Pipeline Jenkins</a>
        <a href="{log}" style="display: inline-block; padding: 10px 20px; color: #fff; background-color: #5bc0de; text-decoration: none;">Log</a>
        <a href="{url_dist}" style="display: inline-block; padding: 10px 20px; color: #fff; background-color: #5bc0de; text-decoration: none;">URL Dist</a>
        <a href="{url_json}" style="display: inline-block; padding: 10px 20px; color: #fff; background-color: #5bc0de; text-decoration: none;">URL Json</a>
        <p>Atentamente.<br>Equipo de QA - Automotion</p>
    """

    # Crear el mensaje MIME
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = subject
    mensaje.attach(MIMEText(body, 'html'))

    # Conectar al servidor y enviar el correo
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.set_debuglevel(True)
            server.sendmail(remitente, destinatarios, mensaje.as_string())
            print("Correo enviado con éxito")
            print(f"Destinatarios: {destinatarios}")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# Llamada a la función para enviar el correo
if __name__ == "__main__":
    enviar_correo()
