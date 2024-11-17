# myexceptions\AssetNotMaintainException.py

class AssetNotMaintainException(Exception):
    def __init__(self, asset_id):
        super().__init__(f"Asset with ID {asset_id} has not been maintained for over 2 years and cannot be used.")
