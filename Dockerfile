FROM the-box-base:latest

WORKDIR /app

COPY src src
COPY .env.exemple .env

VOLUME /etc/letsencrypt:/etc/letsencrypt

EXPOSE 5002

CMD ["-m", "src.main", "gunicorn", "-w", "4", "-b", "0.0.0.0:5002", "--certfile", "/etc/letsencrypt/live/thebox.nathabox.fr/fullchain.pem", "--keyfile", "/etc/letsencrypt/live/thebox.nathabox.fr/privkey.pem", "--timeout", "120"]
ENTRYPOINT ["python3"]