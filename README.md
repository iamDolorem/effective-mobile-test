# Effective Mobile test (nginx -> backend)

Минимальный проект из двух контейнеров:

- **backend** (Python) слушает **8080** и отвечает на `/` строкой:  
  `Hello from Effective Mobile!`
- **nginx** слушает **80** и проксирует `/` на backend внутри docker-сети.

## Архитектура

Host (localhost:80) -> nginx container (80) - > backend container (8080)
                                 (docker network DNS: "backend")

**Важно:**
- наружу проброшен **только порт 80** (nginx)
- backend **не публикуется** на хост, доступен только внутри docker-сети по имени `backend`


## Запуск

Требуется: Docker + Docker Compose

```bash
docker compose up --build -d
docker compose ps
curl.exe http://localhost
docker compose down - остановить
docker compose stop/docker compose start - пауза/старт
