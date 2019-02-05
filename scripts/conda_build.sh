#! /bin/bash

echo -e "Version \"$1\""
echo -e "Git Revision \"$2\""
echo -e "Conda Channel \"$3\""

echo -e "\nUpdating meta.yaml"

sed -i "s/\(.*version:\).*/\1 \"$1\"/" ../meta.yaml

sed -i "s/\(.*git_rev:\).*/\1 $2/" ../meta.yaml

echo -e "Building conda package"

conda build ../ &> build.log

if [[ $? -ne 0 ]]
then
	echo "Error building conda package, check build.log"

	exit
fi

echo -e "Uploading conda package"

upload=$(cat build.log | grep 'anaconda upload.*')

$upload -u $3 -f
