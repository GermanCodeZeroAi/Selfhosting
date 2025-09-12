# Externe Downloads und Ressourcen

## Tools und Software

### Ollama (Windows)
- Download: https://ollama.com/download/windows
- GitHub: https://github.com/ollama/ollama

### n8n Community Nodes
- n8n Community Nodes: https://www.npmjs.com/search?q=keywords:n8n-community-node

### Whisper (Optional für Voice)
- OpenAI Whisper: https://github.com/openai/whisper
- Whisper.cpp (schneller): https://github.com/ggerganov/whisper.cpp

### Stable Diffusion (Optional für Bildgenerierung)
- AUTOMATIC1111 WebUI: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- ComfyUI: https://github.com/comfyanonymous/ComfyUI

### Voice Cloning (Optional)
- RVC WebUI: https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI
- OpenVoice: https://github.com/myshell-ai/OpenVoice

## Modelle

### Ollama Modelle
```bash
# Bereits im ollama_setup.ps1 enthalten:
ollama pull llama3.2:3b-instruct
ollama pull qwen2.5:7b-instruct-q5_K_M
ollama pull phi3:mini
ollama pull tinyllama:1.1b

# Weitere empfohlene Modelle:
ollama pull mistral:7b-instruct
ollama pull gemma2:2b
ollama pull llava:7b  # Multimodal
```

### Hugging Face Modelle (Optional)
- Sentence Transformers (für Embeddings): https://huggingface.co/sentence-transformers
- BERT German: https://huggingface.co/bert-base-german-cased

## Docker Images (werden automatisch gezogen)
- traefik:v2.10
- postgres:15
- redis:7
- qdrant/qdrant:v1.8.4
- n8nio/n8n:1.71.1
- grafana/grafana:10.4.2
- prom/prometheus:v2.51.2
- grafana/loki:2.9.3

## Dokumentation
- n8n Docs: https://docs.n8n.io/
- FastAPI: https://fastapi.tiangolo.com/
- Docker Compose: https://docs.docker.com/compose/
- Traefik: https://doc.traefik.io/traefik/

## Weitere Ressourcen
- MCP (Model Context Protocol): https://github.com/anthropics/model-context-protocol
- LangChain: https://github.com/langchain-ai/langchain
- AutoGPT: https://github.com/Significant-Gravitas/AutoGPT