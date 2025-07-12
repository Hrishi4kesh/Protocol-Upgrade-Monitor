# src/utils.py

from web3 import Web3
from web3._utils.events import get_event_data
from web3.exceptions import MismatchedABI


def load_contract(web3, abi, address):
    return web3.eth.contract(address=address, abi=abi)


def decode_logs(logs, contract, web3):
    decoded_events = []

    for log in logs:
        for attr in dir(contract.events):
            if attr.startswith("_"):  # skip internal keys
                continue
            try:
                event_cls = getattr(contract.events, attr)
                abi = event_cls._get_event_abi()
                data = get_event_data(web3.codec, abi, log)
                decoded_events.append(data)
                break  # stop after first successful decode
            except (MismatchedABI, ValueError, AttributeError):
                continue

    return decoded_events
