from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


class ManagerAccessMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser 

class StaffAccessMixin(LoginRequiredMixin,UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role=="Staff"

class CustomerAccessMixin(LoginRequiredMixin,UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role=="Customer"


class AccessMixin(LoginRequiredMixin,UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.role == "Staff":
            return True
        elif self.request.user.is_authenticated and self.request.user.is_superuser:
            return True
        else:
            return False