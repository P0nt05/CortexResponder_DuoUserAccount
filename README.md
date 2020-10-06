# CortexResponder_DuoUserAccount
Rep. for Cortex Responder (TheHive project - https://github.com/TheHive-Project/CortexDocs)
to Lock/Unlock User Accounts in the Duo Admin Portal (Cisco Security)


There are two Responder available in order to change the status of a User in Duo Security via the AdminAPI (https://duo.com/docs/adminapi)

DuoLockUserAccount -> changes the "status" to “disabled” - The user will not be able to log in.
DuoUnlockUserAccount ->  changes the "status" to “active” - The user must complete secondary authentication.

How to install:
- Install Responder via git clone into the Responder folder from your Cortex installation.
- Restart Cortex to initialize the new Responder "systemctl restart cortex"
- Add the ResponderConfig 

- Enable the Repsonder Actions
