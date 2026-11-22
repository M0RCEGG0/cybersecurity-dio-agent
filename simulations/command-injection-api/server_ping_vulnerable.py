# WARNING: Arquivo com falhas intencionais de segurança para simulação educacional.
# NÃO UTILIZE EM PRODUÇÃO!

import os

# FALHA 1 (OWASP A07 - Falhas de Autenticação / Exposição de Credenciais):
# Segredos e tokens nunca devem estar hardcoded no código-fonte.
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def ping_host(target_ip):
    print(f"[*] Iniciando diagnóstico de rede para o host: {target_ip}")
    
    # FALHA 2 (OWASP A03 - Injection / MITRE T1059 Command Injection):
    # O comando é concatenado diretamente como string no shell do sistema operacional.
    # Se o usuário passar: "8.8.8.8; cat /etc/passwd" ou "127.0.0.1 & dir",
    # o segundo comando será executado com os privilégios da aplicação!
    command = f"ping -c 2 {target_ip}"
    
    os.system(command)

if __name__ == "__main__":
    host = input("Digite o IP ou hostname para ping: ")
    ping_host(host)
