import yaml, sys, os, re
def die(msg): print(msg); sys.exit(1)
p = yaml.safe_load(open("OPS/registry/ports.yaml"))
seen={}
for name,port in p.items():
    if port in seen: die(f"Konflikt: Port {port} doppelt ({seen[port]} vs {name})")
    seen[port]=name
# einfache ENV-Checkliste
required_env = [
 "POSTGRES_USER","POSTGRES_PASSWORD","POSTGRES_DB",
 "N8N_ENCRYPTION_KEY","IMAP_HOST","IMAP_USER","IMAP_PASSWORD",
 "SMTP_HOST","SMTP_USER","SMTP_PASSWORD","TELEGRAM_BOT_TOKEN","TELEGRAM_CHAT_ID"
]
if os.path.exists(".env"):
    vals = dict(line.strip().split("=",1) for line in open(".env") if "=" in line and not line.strip().startswith("#"))
    missing=[k for k in required_env if not vals.get(k)]
    if missing: die(f"Fehlende ENV Variablen in .env: {', '.join(missing)}")
print("OK: Ports eindeutig & ENV plausibel (Basis).")