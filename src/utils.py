# src/utils.py

from web3._utils.events import get_event_data
from web3.exceptions import MismatchedABI
from src.logger import logger

def decode_logs(logs, contract, web3):
    decoded = []
    for log in logs:
        matched = False
        for event_cls in contract.events.__dict__.values():
            if not hasattr(event_cls, 'abi'):
                continue
            try:
                event_data = get_event_data(web3.codec, event_cls.abi, log)
                if event_data is not None:
                    decoded.append(event_data)
                    matched = True
                    break
            except MismatchedABI:
                continue
            except Exception as e:
                logger.warning(f"Failed to decode log with {getattr(event_cls, '__name__', str(event_cls))}: {e}")
                logger.debug(f"Raw log: {log}")
                continue
        if not matched:
            logger.warning("No matching event found for log.")
    logger.info(f"Decoded {len(decoded)} governance events")
    return decoded
