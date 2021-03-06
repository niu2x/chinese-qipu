#!/bin/bash
echo "workdir is $1"
pushd .
cd $1

find . -maxdepth 1 -type f|while read item; do

echo ${item}

filename=$(basename ${item})
subdir=${filename:0:2}
if ! [ -d ${subdir} ]; then
	mkdir ${subdir};
fi

mv $item ${subdir}/


done

popd
