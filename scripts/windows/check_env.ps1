Write-Host "== GCZA Windows Check =="
$node = node -v 2>$null; if(!$node){Write-Host "Node fehlt. Installiere Node 20 LTS."}
$py = python --version 2>$null; if(!$py){Write-Host "Python fehlt. Installiere Python 3.11."}
docker --version
wsl.exe --status