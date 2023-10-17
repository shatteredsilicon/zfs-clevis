#!/usr/bin/bash

check() {
	return 0
}

depends() {
	return 0
}

install() {
	inst_multiple $(rpm -ql --noartifact clevis-pin-tpm2 clevis jose tpm2-tss | grep -v '^/usr/share')

	# Install our hook before the standard ZFS one to unlock what we can
	inst_hook pre-mount 85 "${moddir}/fetch-keys.sh"
}
