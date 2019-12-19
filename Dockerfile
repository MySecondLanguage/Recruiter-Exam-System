FROM python:3

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir -p /app
RUN cd /app
WORKDIR /app


COPY entrypoint.sh ./
RUN chmod +x ./entrypoint.sh

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY backend ./backend/
COPY coretemplates ./coretemplates/
COPY static ./static/
