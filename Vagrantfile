Vagrant.configure("2") do |config|
  
  config.vm.box = "generic/ubuntu1804"
  config.vm.network "forwarded_port", guest: 8000, host: 8001 #Django
  config.vm.network "forwarded_port", guest: 3000, host: 3000 #React
  config.vm.synced_folder ".", "/vagrant"
  config.vm.provision "shell", path: "install.sh"
  config.vm.provision "shell", path: "run-django-env.sh", run: 'always' #???
  
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 2
  end
end
