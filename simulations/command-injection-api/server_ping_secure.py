# CORRIGIDO - simulação de diagnóstico de rede seguro
# O comando ping é executado SEM shell e a entrada é estritamente validada.
# Gerado via revisão de código com DIO Agent (Hermes).

import ipaddress
import subprocess
import sys

def validar_alvo(target):
    """Aceita IPv4, IPv6 ou hostname restrito (sem metacharacteres)."""
    if not target or len(target) > 253:
        raise ValueError("Alvo inválido ou muito longo")

    try:
        ipaddress.ip_address(target)  # verifica IPv4 ou IPv6
        return target
    except ValueError:
        pass

    # Hostname: somente letras, dígitos, hífen e ponto
    if target.startswith("-") or target.endswith("."):
        raise ValueError("Hostname inválido")

    for parte in target.split("."):
        if not parte or len(parte) > 63:
            raise ValueError("Hostname inválido")
        if parte.startswith("-") or parte.endswith("-"):
            raise ValueError("Hostname inválido")
        if not all(c.isalnum() or c == "-" for c in parte):
            raise ValueError("Caracteres inválidos no hostname")

    return target


def ping_host(target_ip):
    try:
        alvo = validar_alvo(target_ip)
    except ValueError as exc:
        print(f"[!] Alvo inválido: {exc}")
        return

    print(f"[*] Iniciando diagnóstico de rede para o host: {alvo}")

    try:
        resultado = subprocess.run(
            ["ping", "-c", "2", alvo],
            check=False,
            capture_output=True,
            timeout=10,
            text=True,
            shell=False,   # seguro: nenhum shell é invocado
        )
    except subprocess.TimeoutExpired:
        print("[!] Resposta lenta demais. Timeout de 10s atingido.")
        return
    except FileNotFoundError:
        print("[!] O comando 'ping' não está disponível neste sistema.")
        return

    print(resultado.stdout)
    if resultado.stderr:
        print(resultado.stderr, file=sys.stderr)

    if resultado.returncode != 0:
        print(f"[!] Ping terminou com código de saída {resultado.returncode}")


if __name__ == "__main__":
    host = input("Digite o IP ou hostname para ping: ")
    ping_host(host)
