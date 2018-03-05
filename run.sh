#!/bin/sh

while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    --csvpath)
    CSVPATH="$2"
    shift # past argument
    shift # past value
    ;;
    -i|--interactive)
    INTERACTIVE="-i"
    shift # past argument
    shift # past value
    ;;
	*)    # search term
    SEARCHTERM="$1"
    shift # past argument
    ;;
esac
done

if [ "$SEARCHTERM" = "" ] && [ "$INTERACTIVE" = "" ]
then
	echo "usage: run.sh [-i | --interactive] [--csvpath <path>] [<searchterm>]"
	echo "if run in interactive mode <searchterm> is ignored"
	echo "if not in interactive mode then <searchterm> is required"
	echo "csvpath defaults to data/address_book.csv if omitted"
	exit 1
fi

CSVPATH="${CSVPATH:-$(pwd)/data/address_book.csv}"

docker run -d -p 4000:80 --mount type=bind,source="$CSVPATH",target=/app/address_book.csv addressbook-server
docker run -it -e interactive="$INTERACTIVE" -e searchterm="$SEARCHTERM" addressbook-client
