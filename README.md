# FastAPI Starter
My first attempt at creating a FastAPI starter project.

## Getting started
- Run `docker-compose up`
- SSH into API container `docker exec -it fastapi bash`
- Run `migri init` to create sample **message** table

## Testing
- Run `docker-compose up` or `docker-compose up db` to start database
- Run `nox -e test`
