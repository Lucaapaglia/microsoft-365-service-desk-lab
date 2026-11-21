# Using the checks in a real environment

Reference procedures reviewed 21 November 2026. The demo reads local JSON. None of these tenant or endpoint checks was executed against a real organization.

| Question | Who can check and what to record |
| --- | --- |
| Did the relevant sign-in succeed? | With the appropriate Entra licensing and a role such as Reports Reader, locate the specific attempt by user, time and application. Record the result and correlation ID in the internal ticket. [Entra sign-in troubleshooting](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-troubleshoot-sign-in-errors) |
| Is the required app enabled? | Ask the authorized licensing owner to inspect the product and individual app plan for the intended account. License changes require appropriate approval and a role such as License Administrator. An enabled plan alone does not prove provisioning is complete. [Microsoft 365 licensing](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/assign-licenses-to-users?view=o365-worldwide) |
| Does the device meet the access requirements? | The employee can check the enrolled work device in Company Portal. The endpoint team can compare its latest status with the relevant sign-in event using its delegated access. [Check device access](https://learn.microsoft.com/en-us/intune/user-help/compliance/validate-device-access-windows) |
| Does an advisory match the workload, symptom and time? | A tenant role with service-health access, such as Service Support Administrator, can check the admin center. Record the affected workload and advisory status. [Microsoft 365 service health](https://learn.microsoft.com/en-us/microsoft-365/enterprise/view-service-health?view=o365-worldwide) |
| Which microphone is Teams using? | The employee can view the selected microphone in the desktop app and test the result with a colleague. [Teams device settings](https://support.microsoft.com/en-us/teams/notifications-settings/manage-your-device-settings-in-microsoft-teams) |
