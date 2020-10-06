# CortexResponder_DuoUserAccount
Rep. for Cortex Responder (TheHive project - https://github.com/TheHive-Project/CortexDocs)
to Lock/Unlock User Accounts in the Duo Admin Portal (Cisco Security)


There are two Responder available in order to change the status of a User in Duo Security via the AdminAPI (https://duo.com/docs/adminapi)

DuoLockUserAccount -> changes the "status" to “disabled” - The user will not be able to log in.
DuoUnlockUserAccount ->  changes the "status" to “active” - The user must complete secondary authentication.

The Responder is looking for a "username" as input and queries the Duo Admin API, to receive the associated UserID.
The UserID is used to change the "status" of the particular user.

## How to install:
  * Install Responder via git clone into the Responder folder from your Cortex installation.
  * Restart Cortex to initialize the new Responder "systemctl restart cortex"
  * Add the ResponderConfig 
  * ![ResponderConfig](/ResponderConfig.jpg)
  * Enable the Responder Actions
  * ![Responders](/Responders.jpg)
 
## **Add Observable type in TheHive**
  * Per default TheHive has no "username" Observable type, so we have to add this in the Admin settings
  * ![AddObservableType](/AddObservableType.jpg)

