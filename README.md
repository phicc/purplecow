# Project Purple Cow
## Proof of Concept for Public Health/Social Justice Initiatives

## Overview
A proof of concept application for public health and social justice initiatives.

## Infrastructure
Consists of a simple CRUD REST API relying on a basic data structure to store items.

## Running Application
Docker is required to run the application.

Execute the following commands
``` bash
docker build -t purplecow .
docker run -d --name purplecow_c -p 3000:3000 purplecow
```

See `solution.md` for further details
