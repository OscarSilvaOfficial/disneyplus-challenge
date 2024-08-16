# Disney Plus API Challenge

[Challenge description](./CHALLENGE.md)

## System Design

### High level system architecture

My architecture design is based on microservices, and based in disney size, we would have a squad per service.

- All the services is using EC2 instance.
- The services execution is inside a Docker contâiner.
- Kubernets is responsable for horizontal auto-scaling and load balancing.
- All services are connected on API Gateway.

![High level system architecture](./high%20level%20diagram.drawio.png)
