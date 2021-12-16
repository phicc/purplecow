# Project Purple Cow

## Structure
The application relies on Docker to run within containers. The application itself is withint the `application` directory.

## Running Project
Execute the following command
``` bash
docker
```

## Future Considerations

### Security
Currently, the applications uses sqllite in an unsecure configuration. A password and user authorization should be put in place to prevent unauthorized access to restricted actions (put, delete). Docker secretes may be used to hold database access information.

### Application Structure
The file structure should be divided to better define the different application roles between the API services, databases and later security and Docker secret configurations.

### Database Configuration
- Consider using Alembic along with SQLAlchemy to initialize the DB
- Having a tool for DB initilization will also help with any migration needed and handle new deployments

### Configuration
- Currently the port information is hard coded into the Dockerfile
  - Ideally we will update to accept arguments to set the port based on start up parameters
  - These parameters may originate from either the command line or from a container manager such as K8, DockerSwarm/Compose

### Feature Expansion
- Allow to CRUD operations based upon Item Id
- Protect CRUD operations by user authentication and authorization
- Use Docker Compose or K8 to allow for more reliability by providing container health checks, restarts
- Addition of extensive unit and integration testing for functions added
- Addition of documentation landing page for browser users
- Additional of UI to allow for CRUD applications through browser