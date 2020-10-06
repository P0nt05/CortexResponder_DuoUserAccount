#!/usr/bin/env python3
# encoding: utf-8

from cortexutils.responder import Responder
import requests
import duo_client
from datetime import datetime

class DuoUnlockUserAccount(Responder):
    def __init__(self):
        Responder.__init__(self)
        self.API_hostname = self.get_param('config.API_hostname', None, "API hostname is missing")
        self.iKey = self.get_param('config.iKey', None, "Integration Key is missing")
        self.sKey = self.get_param('config.sKey', None, "Secret Key is  missing")

    def run(self):
        Responder.run(self)

        if self.get_param('data.dataType') == 'username':

            str_username = self.get_param('data.data', None, 'No artifacts available')

            admin_api = duo_client.Admin(self.iKey, self.sKey, self.API_hostname)

            response = admin_api.get_users_by_name(username=str_username)

#            print(response)

            user_id=response[0]["user_id"]

#            print("user_id:",user_id)

            r = admin_api.update_user(user_id=user_id,status='active')

#            print("response:",r)

            if r.get('status') == 'active':
                self.report({'message': 'User is unlocked in Duo Security. The user must complete secondary authentication.'})
            else:
                self.error('Failed to unlock User Account in Duo.')
        else:
            self.error('Incorrect dataType. "username" expected.')

    def operations(self, raw):
        return [self.build_operation('AddTagToArtifact', tag='Duo User: reactivated')]

if __name__ == '__main__':
        DuoUnlockUserAccount().run()
