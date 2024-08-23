# Deploying the Project

## docker-compose up

1. **Миграции накатываются, суперюзер admin/admin создается**
2. **Заходим в контейнер: docker exec -it app bash**
3. **Запускаем команду: ./manage.py parse_log /app/log_storage/nginx_json_logs.txt**
4. **API - /api**
5. **Swagger - /docs**

