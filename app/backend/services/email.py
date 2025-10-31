from typing import Iterable, List, Optional, Tuple, Union
from flask_mail import Mail, Message
from flask import current_app
import mimetypes
import os
import threading

# Extensão Flask-Mail (inicializada no app)
mail = Mail()

Attachment = Union[str, Tuple[str, str, bytes]]  # caminho do arquivo OU (filename, mimetype, bytes)

class EmailService:
    """
    Serviço de envio de e-mails.
    - Usa Flask-Mail e configurações em current_app.config (MAIL_*)
    - Suporta corpo em texto/HTML e anexos.
    - Pode enviar de forma assíncrona via thread.
    """

    def __init__(self, default_sender: Optional[str] = None) -> None:
        self.default_sender = default_sender

    def _build_message(
        self,
        to: Union[str, Iterable[str]],
        subject: str,
        body_text: Optional[str] = None,
        body_html: Optional[str] = None,
        cc: Optional[Iterable[str]] = None,
        bcc: Optional[Iterable[str]] = None,
        sender: Optional[str] = None,
    ) -> Message:
        recipients = [to] if isinstance(to, str) else list(to)
        msg = Message(
            subject=subject,
            recipients=recipients,
            cc=list(cc) if cc else None,
            bcc=list(bcc) if bcc else None,
            sender=sender or self.default_sender or current_app.config.get("MAIL_DEFAULT_SENDER"),
        )
        if body_text:
            msg.body = body_text
        if body_html:
            msg.html = body_html
        return msg

    def _attach(self, msg: Message, attachments: Optional[Iterable[Attachment]]) -> None:
        if not attachments:
            return
        for item in attachments:
            if isinstance(item, str):
                path = item
                if not os.path.isfile(path):
                    continue
                filename = os.path.basename(path)
                ctype, _ = mimetypes.guess_type(filename)
                ctype = ctype or "application/octet-stream"
                with open(path, "rb") as f:
                    msg.attach(filename, ctype, f.read())
            else:
                filename, mimetype, data = item
                msg.attach(filename, mimetype or "application/octet-stream", data)

    def send(
        self,
        to: Union[str, Iterable[str]],
        subject: str,
        body_text: Optional[str] = None,
        body_html: Optional[str] = None,
        cc: Optional[Iterable[str]] = None,
        bcc: Optional[Iterable[str]] = None,
        attachments: Optional[Iterable[Attachment]] = None,
        sender: Optional[str] = None,
        async_send: bool = False,
    ) -> dict:
        if not (body_text or body_html):
            raise ValueError("Informe body_text ou body_html")
        msg = self._build_message(to, subject, body_text, body_html, cc, bcc, sender)
        self._attach(msg, attachments)

        def _send():
            mail.send(msg)

        if async_send:
            t = threading.Thread(target=_send, daemon=True)
            t.start()
            return {"ok": True, "async": True}
        _send()
        return {"ok": True}

# Instância pronta para uso
email_service = EmailService()
