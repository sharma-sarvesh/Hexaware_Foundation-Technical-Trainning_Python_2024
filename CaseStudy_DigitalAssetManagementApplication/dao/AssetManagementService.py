# dao/AssetManagementService.py

from abc import ABC, abstractmethod
from entity.Asset import Asset
from myexceptions.AssetNotFoundException import AssetNotFoundException
from myexceptions.AssetNotMaintainException import AssetNotMaintainException

class AssetManagementService(ABC):
    
    @abstractmethod
    def add_new_asset(self, asset: Asset) -> bool:     #* Type Hinting
        pass                                #it tells what types of values are expected for the parameters 
                                            # and what type the function will return

    @abstractmethod
    def update_the_asset(self, asset: Asset) -> bool:
        pass

    @abstractmethod
    def get_asset_by_id(self, asset_id: int) -> Asset:
        pass

    @abstractmethod
    def deleteing_asset(self, asset_id: int) -> bool:
        pass

    @abstractmethod
    def allocating_asset(self, asset_id: int, employee_id: int, allocation_date: str) -> bool:
        pass

    @abstractmethod
    def deallocating_asset(self, asset_id: int, employee_id: int, return_date: str) -> bool:
        pass

    @abstractmethod
    def performing_maintenance(self, asset_id: int, maintenance_date: str, description: str, cost: float) -> bool:
        pass

    @abstractmethod
    def reserving_asset(self, asset_id: int, employee_id: int, reservation_date: str, start_date: str, end_date: str) -> bool:
        pass

    @abstractmethod
    def withdrawing_reservation(self, reservation_id: int) -> bool:
        pass
