# fixNetboxVirtualChassisInterfaces
NetBox doesn't provide a convenient way to update interface names for a virtual chassis.   This fixes that for Cisco gear.  I'll look at updating it for other types of network devices, but since I don't have access to any other switches or routers, this only works for Cisco for now.

NetBox is an open source DCIM that provides a very useful way of managing a large data center as well as a campus environment. 
More information can be found at https://netbox.readthedocs.io/en/stable/

This script uses the pynetbox python module provided by NetBox to update interface names of a virtual chasis.  When creating a virtual chassis from a set of devices, the interface names are typically the exact same on all the devices.  This is because the device template for each device will have a standard set of interfaces created from the device template.  
