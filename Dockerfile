FROM the-box-base:latest

WORKDIR /app

COPY src src
COPY .env.exemple .env

EXPOSE 5002

CMD ["-m", "src.main"]
ENTRYPOINT ["python3"]