import vk


class VkAuth:
    def __init__(self, token):
        self.token = token
        self.api = None

    def get_api_session(self):
        print(self.token)
        session = vk.Session(access_token=self.token)
        self.api = vk.API(session)

        return self.api
