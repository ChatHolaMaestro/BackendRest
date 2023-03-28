from .shared_permissions import (
    BasePermission,
    IsAuthenticated,
    IsStaffUser,
    IsSuperUser,
    IsAdminRole,
    IsTeacherRole,
    IsSchoolManagerRole,
    IsSameUser,
    IsNotSameUser,
)

from .or_permission import OrPermission
