"""
 Initializing some default parameters for api routes
"""

from fastapi import APIRouter  # pylint: disable=E0401

from api.endpoints.tests import tests_router

router = APIRouter()

router.include_router(tests_router, prefix="/tests")
