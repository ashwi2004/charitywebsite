from django.contrib import admin
from .models import User, Cause,Donation

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'points')
    search_fields = ('name', 'phone')

class CauseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'goal_amount', 'amount_raised', 'start_date', 'end_date')
    search_fields = ('name', 'description')
    list_filter = ('start_date', 'end_date')

class DonationAdmin(admin.ModelAdmin):
    list_display = ('user', 'cause', 'amount', 'date')
    search_fields = ('user__name', 'cause__name')
    list_filter = ('date', 'cause')

# Register models with the default admin site
admin.site.register(User, UserAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Cause, CauseAdmin)

# Custom admin site configuration
class CustomAdminSite(admin.AdminSite):
    site_header = "Custom Admin Dashboard"

custom_admin_site = CustomAdminSite(name='custom_admin')

# Register models with the custom admin site
custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(Donation, DonationAdmin)
custom_admin_site.register(Cause, CauseAdmin)
