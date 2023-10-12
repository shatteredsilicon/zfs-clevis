#!/bin/bash

(
echo "##### Unlocking ZFS encrypted volumes"

while read -u 3 ds enc key
do
	if [ "${enc}" != "off" -a "${key}" != "-" ]
	then
		echo "Loading key for ${ds}"
		if (echo -n "${key}" | clevis decrypt | zfs load-key -L prompt "${ds}")
		then
			echo "Dataset ${ds} unlocked"
		else
			echo "FAILED TO UNLOCK ${ds}"
		fi
	fi
done 3< <(zfs list -H -o name,encryption,zfs-clevis:key)
) 1>&2
