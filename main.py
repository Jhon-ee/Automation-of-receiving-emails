from imap_tools import MailBox, AND
import os

user = "SEU EMAIL"
password = "SENHA"
my_email = MailBox("IMAP DO SEU EMAIL").login(user,password)

list_emails = my_email.fetch(AND(from_="EMAIL REMETENTE"), limit=1, reverse=True)
for email in list_emails:
    for anexo in email.attachments:
        if "Fatura" in anexo.filename:
            info_anexo = anexo.payload
            if os.path.exists("E:/"): # Se existir o disco E
                with open("E:/1 FATURA.pdf", "wb") as file: # Irá criar ou sobrescrever o arquivo
                    file.write(info_anexo)
                    print("Arquivo adicionado com sucesso!")
            else:
                print("Diretório não encontrado!")
