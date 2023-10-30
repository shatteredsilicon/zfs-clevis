#!/bin/bash

(
command -v zfs > /dev/null|| exit -1
command -v clevis > /dev/null || exit -1

echo "##### Unlocking ZFS encrypted volumes"

while read -u 3 ds enc keystatus encroot key
do
	if [ "${ds}" = "${encroot}" ]
	then
		if [ "${enc}" != "off" -a "${key}" != "-" ]
		then
			if [ "${keystatus}" = "available" ]
			then
				echo "Dataset ${ds} already unlocked"
			else
				echo "Loading key for ${ds}"
				if (echo -n "${key}" | clevis decrypt | zfs load-key -L prompt "${ds}")
				then
					echo "Dataset ${ds} unlocked"
				else
					echo "FAILED TO UNLOCK ${ds}"
				fi
			fi
		fi
	fi
	# Do not quote ${1} in the zfs list, it needs to not be expanded if not supplied
done 3< <(zfs list -H -o name,encryption,keystatus,encryptionroot,zfs-clevis:key ${1})
) 1>&2
