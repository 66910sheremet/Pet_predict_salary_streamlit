FROM python:3.8.10

WORKDIR /MLSP

ENV VIRTUAL_ENV=/MLSP/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . /MLSP
COPY survey_results_public.csv /MLSP/survey_results_public.csv

RUN pip install poetry

COPY pyproject.toml poetry.lock /MLSP/

RUN poetry install --no-dev

EXPOSE 8501

ENTRYPOINT [".venv/bin/python", "-m", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
