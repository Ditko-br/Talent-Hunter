from typing import Iterable, List, Optional
from flask import current_app
from .email import email_service

class NotificationService:
    """Camada de notificação do sistema (por enquanto via e-mail).
    Pode ser estendida para SMS, Push, etc.
    """

    def __init__(self, sender: Optional[str] = None) -> None:
        self.sender = sender or current_app.config.get("MAIL_DEFAULT_SENDER")

    # --- Usuário -------------------------------------------------------------------------
    def send_welcome(self, to_email: str, username: str) -> dict:
        subject = "Bem-vindo ao Talent Hunter"
        body_html = f"""
        <h2>Olá, {username}!</h2>
        <p>Seu cadastro foi realizado com sucesso.</p>
        <p>Boas buscas e bons matches! 🚀</p>
        """
        return email_service.send(to=to_email, subject=subject, body_html=body_html, sender=self.sender)

    def send_password_reset(self, to_email: str, reset_url: str) -> dict:
        subject = "Redefinição de senha"
        body_html = f"""
        <p>Recebemos uma solicitação para redefinir sua senha.</p>
        <p>Clique no link abaixo para continuar. Se você não solicitou, ignore este e-mail.</p>
        <p><a href=\"{reset_url}\">Redefinir senha</a></p>
        """
        return email_service.send(to=to_email, subject=subject, body_html=body_html, sender=self.sender)

    def send_2fa_secret(self, to_email: str, secret: str, issuer: str = "TalentHunter", account_label: Optional[str] = None) -> dict:
        # O frontend pode converter em QR Code usando o otpauth URI abaixo
        account = account_label or to_email
        otpauth = f"otpauth://totp/{issuer}:{account}?secret={secret}&issuer={issuer}&algorithm=SHA1&digits=6&period=30"
        subject = "Ativação de 2FA"
        body_html = f"""
        <p>2FA ativado. Use este segredo no seu autenticador:</p>
        <p><b>{secret}</b></p>
        <p>URI (para QR Code): <code>{otpauth}</code></p>
        """
        return email_service.send(to=to_email, subject=subject, body_html=body_html, sender=self.sender)

    # --- Jobs ----------------------------------------------------------------------------
    def send_job_alert(self, to_email: str, jobs: List[dict], title: str = "Alerta de vagas") -> dict:
        if not jobs:
            return {"ok": True, "skipped": True}
        items = []
        for j in jobs:
            title_ = j.get("title", "Vaga")
            company = j.get("company", "")
            url = j.get("url", "#")
            loc = j.get("location") or j.get("country") or "Remoto"
            items.append(f"<li><a href=\"{url}\" target=\"_blank\">{title_}</a> — {company} — {loc}</li>")
        body_html = f"""
        <h3>{title}</h3>
        <ul>
            {''.join(items)}
        </ul>
        <p>Boas oportunidades!</p>
        """
        return email_service.send(to=to_email, subject=title, body_html=body_html, sender=self.sender)

# Instância pronta
notification_service = NotificationService()
