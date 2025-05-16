from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
import uuid
from typing import Optional


class VehiclePartsLink(SQLModel, table=True):
    vehicletype_id: uuid.UUID | None = Field(default=None, foreign_key="vehicletype.id", primary_key=True)
    part_id: uuid.UUID | None = Field(default=None, foreign_key="parts.id", primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=True)

class VehiclePartsLinkCreate(SQLModel):
    vehicletype_id: uuid.UUID 
    part_id: uuid.UUID
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "vehicletype_id": "123e4567-e89b-12d3-a456-426614174000",
                    "part_id": "123e4567-e89b-12d3-a456-426614174000",
                }
            ]
        }
    }

class VehiclePartsLinkRead(SQLModel):
    vehicletype_id: uuid.UUID
    part_id: uuid.UUID
    created_at: datetime
    updated_at: Optional[datetime] = None
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "vehicletype_id": "123e4567-e89b-12d3-a456-426614174000",
                    "part_id": "123e4567-e89b-12d3-a456-426614174000",
                    "created_at": "2023-10-01T12:00:00Z",
                    "updated_at": "2023-10-01T12:00:00Z",
                }
            ]
        }
    }




VehiclePartsLink.model_rebuild()