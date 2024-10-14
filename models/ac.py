from pydantic import BaseModel
from typing import List


class EouStation(BaseModel):
    md: float
    inc: float
    az: float
    ns: float
    ew: float
    tvd: float
    dls: float
    snn: float
    see: float
    svv: float
    sne: float
    snv: float
    sev: float


class EouTrajectory(BaseModel):
    stations: List[EouStation]