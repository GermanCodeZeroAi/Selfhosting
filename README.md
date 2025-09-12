## Croff – Lokales, kostenloses Automatisierungs-Toolkit (Selfhosting)

Erstelle, plane und beobachte Automations-Jobs komplett offline auf deinem eigenen Rechner. Keine Cloud, keine Gebühren, keine Telemetrie – alles lokal und kostenlos.

### Funktionsüberblick

- Aufgaben als Skripte (Bash, Python, Node.js) ausführbar
- Zeitgesteuerte Ausführung über `cron` oder `systemd`-Timer
- Ereignis-Trigger (Dateiänderungen) mit `entr` oder `inotifywait` (optional)
- Mehrstufige Workflows über einfache Shell-Skripte
- Datei-Logging für Nachvollziehbarkeit und Audits
- 100% lokal: funktioniert komplett ohne Internet

### Voraussetzungen

- Linux mit `bash`
- Entweder `cron` (Standard unter Linux) oder `systemd`-Timer
- Optional: `python3`, `node` (falls du solche Tasks schreiben möchtest)
- Optional: `entr` (`sudo apt install entr`) oder `inotify-tools` (`sudo apt install inotify-tools`) für ereignisgesteuerte Jobs
- Optional: `git` für Versionierung

### Empfohlene Projektstruktur

```text
.
├─ tasks/            # Einfache Einzelskripte (Bash/Python/Node)
├─ workflows/        # Mehrstufige Abläufe, die mehrere tasks kombinieren
├─ logs/             # Lauf- und Fehlerprotokolle
├─ .env.example      # Beispiel für lokale Secrets/Konfiguration
└─ .gitignore        # Ignoriert z. B. logs/ und .env
```

### Installation

1) Repository lokal ablegen (klonen oder als ZIP entpacken)
2) Ordner anlegen: `tasks`, `workflows`, `logs`
3) Optional: Helfer installieren
   - `sudo apt update && sudo apt install -y entr inotify-tools shellcheck`

### Schnellstart (ohne Docker)

1) Erstes Task-Skript anlegen: `tasks/hello.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail
mkdir -p logs
echo "$(date -Is) [hello] Hallo von deinem lokalen Automatisierungs-Toolkit" | tee -a logs/hello.log
```

Danach ausführbar machen und testen:

```bash
chmod +x tasks/hello.sh
./tasks/hello.sh
```

2) Zeitgesteuert ausführen mit `cron`

Öffne die Cron-Tabelle:

```bash
crontab -e
```

Füge einen Eintrag hinzu (alle 5 Minuten):

```cron
*/5 * * * * /bin/bash -lc 'cd /ABSOLUT/PFAD/ZUM/REPO && ./tasks/hello.sh >> logs/hello.log 2>&1'
```

Hinweis: Ersetze `/ABSOLUT/PFAD/ZUM/REPO` durch deinen tatsächlichen Pfad.

### Ereignisgesteuerte Jobs (optional)

- Mit `entr` (führt aus, sobald sich `watched.txt` ändert):

```bash
echo watched.txt | entr -r ./tasks/hello.sh
```

- Mit `inotifywait` (aus `inotify-tools`):

```bash
while inotifywait -e modify watched.txt; do ./tasks/hello.sh; done
```

### Mehrstufige Workflows

Lege ein Workflow-Skript an: `workflows/sample_backup.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail
repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
log_dir="$repo_dir/logs"
mkdir -p "$log_dir"
log_file="$log_dir/backup.$(date +%F).log"
{
  echo "$(date -Is) [workflow] Start backup"
  "$repo_dir/tasks/backup_db.sh"
  "$repo_dir/tasks/pack_files.sh"
  echo "$(date -Is) [workflow] Done"
} | tee -a "$log_file"
```

Plane den Workflow täglich um 02:00 Uhr:

```cron
0 2 * * * /bin/bash -lc 'cd /ABSOLUT/PFAD/ZUM/REPO && ./workflows/sample_backup.sh >> logs/workflow.log 2>&1'
```

### Konfiguration und Secrets

Lege eine `.env` im Projektwurzelverzeichnis an (nicht einchecken!):

```env
DB_URL=postgres://user:pass@localhost:5432/db
API_TOKEN=dein_token
```

Binde die Variablen in Skripten ein:

```bash
set -a; [ -f .env ] && . ./.env; set +a
```

Empfohlene `.gitignore`-Einträge:

```gitignore
.env
logs/
```

### Qualität und Tests (optional)

- Shell-Skripte prüfen: `shellcheck tasks/*.sh workflows/*.sh`
- Trockenlauf: Skripte ohne Nebenwirkungen mit `--dry-run`-Flags bauen (falls vorgesehen)

### Fehlerbehebung

- Cron läuft nicht? `systemctl status cron` (oder `crond`) prüfen.
- Keine Ausführungsrechte? `chmod +x <skript>` setzen.
- Pfadprobleme in Cron? Immer absolute Pfade verwenden und `cd` ins Repo.
- Logs leer? Prüfe, ob das Skript `stdout/stderr` korrekt umleitet und `logs/` existiert.

### Sicherheit

- Skripte als normaler Benutzer ausführen, nicht als `root`.
- Secrets ausschließlich lokal in `.env` oder im System-Secret-Store halten.
- Backups von Logs/Artefakten regelmäßig rotieren/archivieren.

### Lizenz

Lege eine passende Lizenz fest (z. B. MIT) und füge eine `LICENSE`-Datei hinzu.

### Mitmachen

Vorschläge, Verbesserungen und Bugreports sind willkommen. Dieses Toolkit versteht sich als einfache, lokale Basis, die du nach Bedarf erweitern kannst.
