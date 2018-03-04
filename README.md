docker build -t addressbook .

docker run -it --mount type=bind,source="$(pwd)/data/address_book.csv",target=/app/address_book.csv addressbook
