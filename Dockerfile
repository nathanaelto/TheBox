FROM the-box-base:latest

WORKDIR /app

COPY src src
COPY .env.exemple .env

EXPOSE 443

CMD ["-m", "src.main"]
ENTRYPOINT ["python3"]