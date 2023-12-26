from typing import Optional
from ThamesThrive.domain.sign_up_data import SignUpRecord
from ThamesThrive.service.storage.factory import storage_manager


async def read_pro_service_endpoint() -> Optional[SignUpRecord]:
    return SignUpRecord.create(await storage_manager("ThamesThrive-pro").load(id="0"))


async def save_pro_service_endpoint(sign_up_record: SignUpRecord):
    sign_up_record.id = '0'
    return await storage_manager("ThamesThrive-pro").upsert(sign_up_record)


async def delete_pro_service_endpoint():
    sm = storage_manager("ThamesThrive-pro")
    return await sm.delete(id="0", index=sm.get_single_storage_index())


async def refresh():
    return await storage_manager('ThamesThrive-pro').refresh()
