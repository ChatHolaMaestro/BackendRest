from .shared_permissions import (
    AllowAny,
    BasePermission,
    IsAuthenticated,
    IsStaffUser,
    IsSuperUser,
    IsAdminRole,
    IsTeacherRole,
    IsSchoolManagerRole,
    IsSameUser,
)

from .or_permission import OrPermission
