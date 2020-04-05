# Digital library project
![](https://www.meme-arsenal.com/memes/580d12ebd24e434175efd82087f1a1b3.jpg)


##  The goal
- Provide access to electronic materials (books, videos, papers, presentations, etc.) on each course

##  Technical constraints
- Have to be the WEB app
- There should be roles for: Administrator, User
- Authorised access only

## Authentication

 Postgres:
```angular2
docker run --name=postgres_swp -d -v $(pwd)/postgres_data:/var/lib/postgresql/data -p 5433:5432 -e POSTGRES_HOST_AUTH_METHOD=trust postgres
docker exec -it postgres_swp bash
psql -U postgres
CREATE DATABASE db;

host: localhost
port: 5433
login: postgres
database name: db
```

Admin panel:
```angular2
Username: admin
Token: 02c7928250a336bae475482b93b0a1ca05fe625e
Email address: admin@example.com
Password: 12345678
```
