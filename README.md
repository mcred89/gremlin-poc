# gremlin-poc

A few simple flask microservices used to play with Gremlin

## Install Instructions

This is meant to be run on 2 seperate Ubuntu VMs. Run the below commands on both servers, then move on to the app specific sections.

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
apt-cache policy docker-ce
sudo apt-get install docker-ce
apt-get install git-core
git clone git://github.com/mcred89/gremlin-poc.git
echo "deb https://deb.gremlin.com/ release non-free" | sudo tee /etc/apt/sources.list.d/gremlin.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C81FC2F43A48B25808F9583BDFF170F324D41134 9CDB294B29A5B1E2E00C24C022E8EF3461A50EF6
sudo apt-get update && sudo apt-get install -y gremlin gremlind
```

### frontend

- Passes your IP to the backend and uses the response to render a webpage with the time based on your IP's timezone.
- If it doesn't get a response within 0.01 it times out and uses "Hammer Time" as the current time.

Build commands:

```bash
cd gremlin-poc/frontend
docker build -t gremlin-poc-front:latest .
docker run -d -p 80:80 gremlin-poc-front:latest
export GREMLIN_IDENTIFIER=gremlin-poc-front
gremlin init
```

### ip-by-geo

- Call with /{ip-seperated-with-dashes} as your path.
- Returns `{time: "HH:MM:SS"}` with your local time, based on your IP's TZ.

Build commands:

```bash
cd gremlin-poc/ip-by-geo
docker build -t gremlin-poc-ip:latest .
docker run -d -p 80:80 gremlin-poc-ip:latest
export GREMLIN_IDENTIFIER=gremlin-poc-ip
gremlin init
```
