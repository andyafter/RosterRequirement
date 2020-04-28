The Basic Roster System

The basic roster system should contain necessary database, model and APIs for the processing of a roster schedule. For the very initial version, the following:
- A User class which is the model for users. 
- A Sector class which is the model for the time sector of a user. A user can have many sectors. However the sectors must not contain overlap. 
- A Request class which is the object created when a user send requests to the system, such as add/remove schedule. 

For the logic part we need to have the following basic functions:
- CRUDs for all the classes(create, read, update, delete)
- A planner service which provide API for querying the schedules of a specific time slot
- The planner service should also provide API for querying the schedules of a specific employee
- A scheduler(could be a different service), scans all the request, then either periodically or manually, make changes to the final roster schedule