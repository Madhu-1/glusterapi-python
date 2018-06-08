import ConfigParser

import pytest

from glusterapi import Client


class PeerInfo(object):
    peerID = ''
    host = ''

    @classmethod
    def set_host(cls, host):
        cls.host = host

    @classmethod
    def set_peer_id(cls, peerid):
        cls.peerID = peerid

    @property
    def get_peer_id(self):
        return self.peerID

    @property
    def get_host(self):
        return self.host


Peer = PeerInfo()


@pytest.fixture(scope='module')
def gd2client():
    config = ConfigParser.ConfigParser()
    config.read("../config.ini")
    endpoint = config.get('glusterd2', 'endpoint')
    user = config.get('glusterd2', 'user')
    secret = config.get('glusterd2', 'secret')
    verify = config.getboolean('glusterd2', 'verify')
    host = config.get('peer', 'host')
    # store host in PeerInfo
    Peer.set_host(host)

    return Client(endpoint=endpoint, user=user,
                  secret=secret, verify=verify)


def test_peer_add(gd2client):
    status, resp = gd2client.peer_add(host=Peer.get_host)
    # store  peerID in class variable
    Peer.set_peer_id(resp['id'])
    assert status == 201


def test_peer_status(gd2client):
    status, resp = gd2client.peer_status()
    assert resp[0]['id'] == Peer.get_peer_id
    assert status == 200


def test_peer_remove(gd2client):
    status, resp = gd2client.peer_remove(peerid=Peer.get_peer_id)
    assert status == 204
