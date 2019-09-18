Obtain rootfs

wget
https://download.opensuse.org/repositories/Cloud:/Images:/Leap_15.1/images/openSUSE-Leap-15.1-OpenStack-rootfs.x86_64-0.0.4-Build7.44.tar.xz

Obtain kernel image

https://download.opensuse.org/repositories/Kernel:/

 1050  wget
 https://download.opensuse.org/repositories/Kernel:/HEAD/standard/x86_64/kernel-kvmsmall-5.3.rc8-2.1.gd6f0b71.x86_64.rpm
  1051  rpm2cpio kernel-kvmsmall-5.3.rc8-2.1.gd6f0b71.x86_64.rpm | cpio -id
   1052  cd boot/
    1053  s
     1054  ls
      1055  ls -altrh
       1056  file vmlinux-5.3.0-rc8-2.gd6f0b71-kvmsmall.gz
        1057  gunzip vmlinux-5.3.0-rc8-2.gd6f0b71-kvmsmall.gz
         1058  ls
          1059  file vmlinux-5.3.0-rc8-2.gd6f0b71-kvmsmall
           1060  mv vmlinux-5.3.0-rc8-2.gd6f0b71-kvmsmall vmlinux


https://github.com/firecracker-microvm/firecracker/blob/master/docs/rootfs-and-kernel-setup.md

Use firecracker

https://github.com/firecracker-microvm/firecracker/blob/master/docs/getting-started.md


Set up the network

sudo ip tuntap add tap0 mode tap
sudo ip tuntap add tap1 mode tap

firectl --kernel=hello-vmlinux.bin --root-drive=alpine.ext4
--firecracker-binary=./firecracker --tap-device=tap0/aa:bb:11:22:33:44
--tap-device=tap1/aa:bb:11:22:33:11

Configure network insside the VM with trex networks and enabale forward

sysctl net.ipv4.conf.all.forwarding=1
sysctl net.ipv6.conf.all.forwarding=1

ip link set eth0 up
ip link set eth1 up
ip addr add 1.1.1.1/24 dev eth0
ip addr add 2.2.2.1/24 dev eth1

ip route add 16.0.0.0/12 via 1.1.1.10
ip route add 48.0.0.0/12 via 2.2.2.20
