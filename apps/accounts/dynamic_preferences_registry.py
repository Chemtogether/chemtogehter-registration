from dynamic_preferences.types import BooleanPreference, StringPreference
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry


general = Section('general')
account_creation = Section('account_creation')


@global_preferences_registry.register
class SiteTitle(StringPreference):
    section = general
    name = 'site_title'
    default = 'My site'
    verbose_name = 'Site title'
    help_text = 'Title of this site used in templates.'

@global_preferences_registry.register
class MaintenanceMode(BooleanPreference):
    section = general
    name = 'maintenance_mode'
    default = False
    verbose_name = 'Maintenance mode'
    help_text = 'Shuts down this site and shows a maintenance page instead.'



@global_preferences_registry.register
class AccountCreation(BooleanPreference):
    section = account_creation
    name = 'account_creation_open'
    default = True
    verbose_name = 'Account creation open'
    help_text = 'Enable the creation of accounts via the signup form.'

@global_preferences_registry.register
class StaffAccountCreation(BooleanPreference):
    section = account_creation
    name = 'staff_account_domain_enabled'
    default = False
    verbose_name = 'Domain-enabled staff account creation'
    help_text = 'Automatically promote users to staff based on the domain of their email.'

@global_preferences_registry.register
class StaffAccountDomain(StringPreference):
    section = account_creation
    name = 'staff_account_domain'
    default = 'example.com'
    verbose_name = 'Domain for domain-enabled staff account creation'
    help_text = 'Domain for the email accounts to be promoted to staff.'
