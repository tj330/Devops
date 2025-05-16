# File & Directory Permissions

Create /devops_workspace and a file project_notes.txt.
    
    mkdir devops_workspace
    cd devops_workspace
    touch project_notes.txt
Set permissions:
Owner can edit, group can read, others have no access.

    chmod 640 project_notes.txt

Use ls -l to verify permissions.

    ls -l
    total 0
    -rw-r----- 1 devops_user devops_team 0 May 17 07:32 project_notes.txt
