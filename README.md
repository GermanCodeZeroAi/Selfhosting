# GermanCodeZeroAI (GCZA)
Lokales, autonomes Automatisierungs-System (n8n + lokale KI, Telegram-Steuerung, MCP-ready).
Neuer Agent? Lies diese Datei → öffne `DOCS/` und lies ALLES. Danach arbeiten.

## Quickstart
1) `.env` aus `.env.example` kopieren und füllen.
2) `make validate && make up`
3) n8n öffnen: http://localhost:5678 → Workflow `workflows/mailops_v1.json` importieren.

## Pflichten (jeder Agent)
Nach JEDER Aufgabe Report in `AGENTS/reports/`:
- Agent/Modell • Datum/Uhrzeit • Aufgabe • Datei(en) • Pfad • Zweck • Ergebnis.