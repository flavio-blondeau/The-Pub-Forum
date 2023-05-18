from django.contrib.auth.mixins import UserPassesTestMixin


class StaffMixin(UserPassesTestMixin):
    """
    This mixin is created to ensure that only staff users can create a new section
    """
    def test_func(self):
        return self.request.user.is_staff