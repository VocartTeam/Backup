from backup_copy import make_copy_new_version
from backup_replace import iteration_through_locations_with_backup_replace
from backup_update import backup_of_subfolders_update



print('\n \nSTART OF BACKUP. \n \n')


make_copy_new_version()
print('\n *** New backup copy was created. *** \n')

iteration_through_locations_with_backup_replace()
print('\n *** Backup files were replaced by new ones. *** \n')

backup_of_subfolders_update()
print('\n *** Backup files and subfolders were checked and updated. *** \n')


print('\n \nBACKUP COMPLETED. \n \n')
