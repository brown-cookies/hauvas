#!/bin/sh

if [ -n "$WINDIR" ]; then
    # This environment variable is typically present on Windows
    
    echo "Loading data from dump (OS = WINDOWS)"

    py manage.py loaddata dump/user.json
    py manage.py loaddata dump/permission.json
    py manage.py loaddata dump/group.json
    py manage.py loaddata dump/contenttypes.json

    py manage.py loaddata dump/main/semester.json
    py manage.py loaddata dump/main/department.json
    py manage.py loaddata dump/main/block.json
    py manage.py loaddata dump/main/profile.json

    py manage.py loaddata dump/dashboard/professor.json
    py manage.py loaddata dump/dashboard/student.json
    py manage.py loaddata dump/dashboard/course.json
    py manage.py loaddata dump/dashboard/enrollment.json
    py manage.py loaddata dump/dashboard/modulelist.json
    py manage.py loaddata dump/dashboard/moduleitem.json

elif [ "$(uname)" = "Darwin" ]; then
    # macOS

    echo "Loading data from dump (OS = MACOS)"

    python manage.py loaddata dump/user.json
    python manage.py loaddata dump/permission.json
    python manage.py loaddata dump/group.json
    python manage.py loaddata dump/contenttypes.json

    python manage.py loaddata dump/main/semester.json
    python manage.py loaddata dump/main/department.json
    python manage.py loaddata dump/main/block.json
    python manage.py loaddata dump/main/profile.json

    python manage.py loaddata dump/dashboard/professor.json
    python manage.py loaddata dump/dashboard/student.json
    python manage.py loaddata dump/dashboard/course.json
    python manage.py loaddata dump/dashboard/enrollment.json
    python manage.py loaddata dump/dashboard/modulelist.json
    python manage.py loaddata dump/dashboard/moduleitem.json
    
elif [ "$(uname)" = "Linux" ]; then
    # Linux

    echo "Loading data from dump (OS = LINUX)"

    python manage.py loaddata dump/user.json
    python manage.py loaddata dump/permission.json
    python manage.py loaddata dump/group.json
    python manage.py loaddata dump/contenttypes.json

    python manage.py loaddata dump/main/semester.json
    python manage.py loaddata dump/main/department.json
    python manage.py loaddata dump/main/block.json
    python manage.py loaddata dump/main/profile.json

    python manage.py loaddata dump/dashboard/professor.json
    python manage.py loaddata dump/dashboard/student.json
    python manage.py loaddata dump/dashboard/course.json
    python manage.py loaddata dump/dashboard/enrollment.json
    python manage.py loaddata dump/dashboard/modulelist.json
    python manage.py loaddata dump/dashboard/moduleitem.json

else
    echo "Unknown OS"
fi
