# src/utils.py

from web3._utils.events import get_event_data
from web3.exceptions import MismatchedABI
from src.logger import logger

def decode_logs(logs, contract, web3):
    decoded = []
    # Iterate over all defined event classes in the contract
    for log in logs:
        matched = False
        for event_cls in contract.events.__dict__.values():
            if not hasattr(event_cls, 'abi'):
                continue
            try:
                event_data = get_event_data(web3.codec, event_cls.abi, log)
                decoded.append(event_data)
                matched = True
                break
            except MismatchedABI:
                continue
            except Exception as e:
                logger.warning(f"Failed to decode log with {event_cls.__name__}: {e}")
                continue
        if not matched:
            logger.warning("No matching event found for log.")
    logger.info(f"Decoded {len(decoded)} governance events")
    return decoded
