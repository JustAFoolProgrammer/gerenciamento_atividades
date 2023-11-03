ARG PYTHON_VERSION=3.8-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

ENV SECRET_KEY = 'django-insecure-4w!c=ue*=nz6z(4f)=l+@2z69kxmn+1113wbkxitq+z_mn27x7'

EXPOSE 8000
CMD ['python', 'manage.py', 'collectstatic', '--noinput']
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "gerenciamento_atividades.wsgi"]
