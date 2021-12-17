# Project Purple Cow

## Structure
The application relies on Docker to run within containers. The application itself is withint the `application` directory.

## Running Project
Execute the following commands
``` bash
docker build -t purplecow .
docker run -d --name purplecow_c -p 3000:3000 purplecow
```
This will build the image defined in `Dockerfile`, create a new container `purplecow_c`, and run at `localhost:3000`

### Available endpoints

| endpoint |  action | params  | returns  | description  |
|---|---|---|---|---|
|  /items |  GET | None  | Items in storage  | Returns all items in storage  |
|  /items/{id} |  GET | id  | Item in storage  | Returns item in storage with passed id |
|   /items  |  POST | JSON Body ex: `[{"id": 1, "name": "Test"}]`  |  Added items | Adds new items to the storage  |
|    /items |  DELETE |  None | null  |  Removes all items from storage |

### Documentation

Generated documentation is available at `http://localhost:3000/docs`

## Future Considerations

### Security
- Currently there is no user authorization needed to set and delete items in storage which is a high concern
- As an expansion, the applications sketched out using sqllite in an insecure configuration. A password and user authorization should be put in place to prevent unauthorized access to restricted actions (put, delete). Docker secrets may be used to hold database access information.

### Application Structure
The file structure should be divided to better define the different application roles between the API services, databases and later security and Docker secret configurations.

### Database Configuration
- Currently, a simple data storage is used to handle items, convert to using DB
    - The simple storage is limited in being a list so duplicates are easy to apply, future iteration should include duplication checking and deeper schema validation
    - The current data structure is severly limited in search and relational capabilities and raises space concerns
- Future database should either exist on it's own infrastructure or, at the very least, in a docker environment to allow for independent scaling and resource allocation
    - Consider using Alembic along with SQLAlchemy to initialize the DB
    - Having a tool for DB initilization will also help with any migration needed and handle new deployments
- The current implementation assumes that the client will provide item IDs, these should be handled via the data storage to ensure uniqueness and consistency
  - Need to further refine requirements to determine if the items will require additional attributes which would influence which DB solution we will want to pursue

### Configuration
- Currently the port information is hard coded into the Dockerfile
  - Ideally we will update to accept arguments to set the port based on start up parameters
  - These parameters may originate from either the command line or from a container manager such as K8, DockerSwarm/Compose

### Feature Expansion
- API
    - CRUD Parameter validation
    - Allow to CRUD operations based upon Item Id
    - Expand on FastAPIs pydantic models and define a return model for each endpoint
- Security
    - Protect CRUD operations by user authentication and authorization
- Scalability and Reliability
    - Use Docker Compose or K8 to allow for more reliability by providing container health checks, restarts
    - Addition of extensive unit and integration testing for functions added
- Usability/User Experience
    - Addition of documentation landing page for browser users
    - Additional of UI to allow for CRUD applications through browser
