#!/bin/bash

( cd src/server && docker build -t addressbook-server . )

cd src/client && docker build -t addressbook-client .
