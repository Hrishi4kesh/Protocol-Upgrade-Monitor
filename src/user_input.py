# src/user_input.py

def get_user_inputs(
    network,
    contract_address,
    from_block,
    to_block,
    risk_tolerance,
    upgrade_type,
    time_horizon,
    asset_pairs
):
    return {
        "network": network,
        "contract_address": contract_address,
        "from_block": from_block,
        "to_block": to_block,
        "risk_tolerance": risk_tolerance,
        "upgrade_type": upgrade_type,
        "time_horizon": time_horizon,
        "asset_pairs": asset_pairs,
    }
