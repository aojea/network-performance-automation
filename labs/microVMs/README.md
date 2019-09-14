Obtain rootfs

wget
https://download.opensuse.org/repositories/Cloud:/Images:/Leap_15.1/images/openSUSE-Leap-15.1-OpenStack-rootfs.x86_64-0.0.4-Build7.44.tar.xz

Obtain kernel image

https://download.opensuse.org/repositories/Kernel:/


https://github.com/firecracker-microvm/firecracker/blob/master/docs/rootfs-and-kernel-setup.md

Use firecracker

https://github.com/firecracker-microvm/firecracker/blob/master/docs/getting-started.md


Set up the network

sudo ip tuntap add tap0 mode tap
sudo ip tuntap add tap1 mode tap

firectl --kernel=hello-vmlinux.bin --root-drive=alpine.ext4
--firecracker-binary=./firecracker --tap-device=tap0/aa:bb:11:22:33:44
--tap-device=tap1/aa:bb:11:22:33:11


