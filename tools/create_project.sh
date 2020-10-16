# Read credentials from file option

read -p "Project Name: " NAME
read -p "Project Base Directory: " BASE_DIR
PROJECT_DIR=$PWD"/../flask_boilerplate"

cp -r $PROJECT_DIR $BASE_DIR"/"$NAME
# Rename all "project"'s with lowercase name
# Create git repo and push to github