# Read credentials from file option

read -p "Project Name: " NAME
read -p "Project Base Directory: " BASE_DIR
TEMPLATE_DIR=$PWD"/../flask_boilerplate"

cp -r $TEMPLATE_DIR $BASE_DIR"/"$NAME
# Rename all "project"'s with lowercase name

# Create git repo and push to github

cd $BASE_DIR
git init
hub create $NAME
git add .
git commit -m "Initial commit."
git push -u origin master