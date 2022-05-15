from fastapi import APIRouter
from api import UserApi
from api import DepartmentAPI, DoctorAPI, PatientAPI, RoomAPI, MedicationAPI, PaymentAPI, AppointmentAPI, PrescriptionAPI
router = APIRouter()

router.include_router(UserApi.router, tags=["user"], prefix="/users")   
router.include_router(DepartmentAPI.router, tags=["department"], prefix="/departments")
router.include_router(DoctorAPI.router, tags=["doctor"], prefix="/doctors")
router.include_router(PatientAPI.router, tags=["patient"], prefix="/patients")
router.include_router(RoomAPI.router, tags=["room"], prefix="/rooms")
router.include_router(MedicationAPI.router, tags=["medication"], prefix="/medications")
router.include_router(AppointmentAPI.router, tags=["appointment"], prefix="/appointments")
router.include_router(PaymentAPI.router, tags=["payment"], prefix="/payments")
router.include_router(PrescriptionAPI.router, tags=["prescription"], prefix="/prescriptions")