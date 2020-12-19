from aiohttp_requests import requests

from patreon.utils import user_agent_string


class OAuth(object):
    def __init__(self, client_id, client_secret):
        super(OAuth, self).__init__()
        self.client_id = client_id
        self.client_secret = client_secret

    async def get_tokens(self, code, redirect_uri):
        return await self.__update_token({
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": redirect_uri
        })

    async def refresh_token(self, refresh_token, redirect_uri=None):
        return await self.__update_token({
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        })

    @staticmethod
    async def __update_token(params):
        response = await requests.post(
            "https://www.patreon.com/api/oauth2/token",
            params=params,
            headers={
                'User-Agent': user_agent_string(),
            }
        )
        return await response.json()
