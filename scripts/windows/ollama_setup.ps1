# Ollama + Modelle (Windows)
if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) { Write-Host "Bitte Ollama für Windows installieren: https://ollama.com"; exit 1 }
ollama pull llama3.2:3b-instruct
ollama pull qwen2.5:7b-instruct-q5_K_M
ollama pull phi3:mini
ollama pull tinyllama:1.1b
curl http://localhost:11434/api/generate -d "{`"model`":`"tinyllama:1.1b`",`"prompt`":`"Hallo`"}"