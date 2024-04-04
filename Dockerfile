# Используйте официальный Python runtime как родительский образ
FROM python:3.8.10

# Установите рабочую директорию в /app
WORKDIR /MLSP

ENV VIRTUAL_ENV=/MLSP/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Скопируйте содержимое текущей директории в контейнер в /app
COPY . /MLSP
COPY survey_results_public.csv /MLSP/survey_results_public.csv

# Установите Poetry
RUN pip install poetry

# Скопируйте pyproject.toml и poetry.lock в /app
COPY pyproject.toml poetry.lock /MLSP/

# Установите зависимости
RUN poetry install --no-dev

# Откройте порт 8501
EXPOSE 8501

# Запустите Streamlit при запуске контейнера
ENTRYPOINT [".venv/bin/python", "-m", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
