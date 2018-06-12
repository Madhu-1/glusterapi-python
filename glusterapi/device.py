import json

from common import BaseAPI
from exceptions import GlusterApiInvalidInputs


class DeviceApis(BaseAPI):
    def device_add(self, host, device=""):
        """
        Gluster Peer add

        :param host: (string) Host UUID
        :param metadata: (dict) host metadata
        :param zone: (string) zone id
        :raises: GlusterApiError on failure
        """
        device = device.strip()
        if len(device) == 0:
            raise GlusterApiInvalidInputs("Invalid device specified")
        req = {
            "device": device
        }
        return self._handle_request(self._post, 201, "/v1/peers/%s" % host, json.dumps(req))

    def peer_remove(self, peerid):
        """
        Gluster Peer remove

        :param peerid: (string) peerid returned from peer_add
        :raises: GlusterApiError on failure
        """
        url = "/v1/peers/" + peerid
        return self._handle_request(self._delete, 204, url, None)

    def peer_status(self):
        """
        Gluster Peer Status

        :raises: GlusterApiError on failure
        """
        return self._handle_request(self._get, 200, "/v1/peers")
