# gremlin-poc

A few simple flask microservices used to play with Gremlin

## frontend

- Passes your IP to the backend and uses the response to render a webpage with the time based on your IP's timezone.
- If it doesn't get a response within 0.01 it times out and uses "Hammer Time" as the current time.

Build commands:

```bash
cd frontend
sudo docker build -t gremlin-poc-front:latest .
sudo docker run -d -p 80:80 gremlin-poc-front:latest
```

## ip-by-geo

- Takes /{ip-seperated-with-dashes}
- Returns `{time: "HH:MM:SS"}` with your local times, based on your IP's TZ.

Build commands:

```bash
cd ip-by-geo
sudo docker build -t gremlin-poc-ip:latest .
sudo docker run -d -p 80:80 gremlin-poc-ip:latest
```
