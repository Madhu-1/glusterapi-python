import json

from common import BaseAPI


class PeerApis(BaseAPI):
    def peer_add(self, host, metadata=None, zone=""):
        """
        Gluster Peer add

        :param host: (string) Hostname or IP
        :param metadata: (dict) host metadata
        :param zone: (string) zone id
        :raises: GlusterApiError on failure
        """
        req = dict()
        req['addresses'] = []
        req['addresses'].append(host)
        if metadata is None:
            metadata = dict()
        req['metadata'] = metadata
        req['zone'] = zone
        return self._handle_request(self._post, 201, "/v1/peers", json.dumps(req))

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
