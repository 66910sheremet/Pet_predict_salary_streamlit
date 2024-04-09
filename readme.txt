Запуск из контейнера:
docker run -p 8501:8501 salary_prediction

Открыть браузер по адресу http://localhost:8501

Запуск программы:
poetry run streamlit run app.py     


Или запуск контейнера из CLI:

# Запуск контейнера Docker в фоновом режиме
Start-Process -NoNewWindow -FilePath "docker" -ArgumentList "run", "-d", "-p", "8501:8501", salary_prediction

# Проверка доступности порта 8501
$serverAvailable = $false
for ($i = 0; $i -lt 30; $i++) {
    $connection = Test-NetConnection -ComputerName localhost -Port 8501
    if ($connection.TcpTestSucceeded) {
        $serverAvailable = $true
        break
    }
    Start-Sleep -Seconds 1
}

# Если сервер доступен, открыть браузер
if ($serverAvailable) {
    Start-Process "http://localhost:8501"
}


Инструкция для сборки контейнера:
docker build -t salary_prediction .

