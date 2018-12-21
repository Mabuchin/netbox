# -*- mode: ruby -*-
# vi: set ft=ruby :

# Set VirtualBox as default provider
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'virtualbox'

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/bionic64"
  config.ssh.username = 'vagrant'
  config.ssh.forward_agent = true
  config.vm.box_check_update = true

  vboxname = "netbox-dev"
  config.vm.define vboxname
  config.vm.provider :virtualbox do |vbox|
    vbox.name = vboxname
  end


  # Access to funnels-server from the host
  config.vm.network :forwarded_port, guest: 6379, host: 6379

  # Access to funnels-server from the host
  config.vm.network :forwarded_port, guest: 8000, host: 8000


  # Share folder to the guest VM
  config.vm.synced_folder "./", "/usr/local/src/netbox"

  # VirtualBox configuration
  config.vm.provider "virtualbox" do |vb|
    vb.cpus = 2
    vb.memory =2048
  end

  config.vm.hostname = "netbox-dev"
end