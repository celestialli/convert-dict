#!/bin/bash

echo "-- Running: ruff format"
ruff format

echo "-- Running: ruff check --select I --fix"
ruff check --select I --fix