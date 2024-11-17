# myexceptions\AssetNotFoundException.py

class AssetNotFoundException(Exception):
    def __init__(self, asset_id):
        super().__init__(f"Custom Exception: Asset with ID {asset_id} not found in the db.")
