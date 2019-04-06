from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from napalm import get_network_driver
from netmiko import ConnectHandler

from .models import Device

def index(request: HttpRequest) -> HttpResponse:
    devices = Device.objects.all()
    context = {
        'title': 'Hello Stream!',
        'name': 'Paul',
        'devices': devices,
    }
    return render(request, 'base.html', context)

def get_device_stats (request: HttpRequest, device_id) -> HttpResponse:
    device = Device.objects.get(pk=device_id)
    if request.method =='GET':
        driver = get_network_driver(device.napalm_driver)
        with driver(device.host, device.username, device.password, optional_args={'port': 2022}) as device_conn:
            interfaces = device_conn.get_interfaces()
        context = {
            'device': device,
            'interfaces': interfaces,
        }
        #print device.get_interfaces_counters()
        return render(request, 'device.html', context)
    elif request.method == 'POST':
        interface_name = request.POST.get("interface_name")
        enable_interface = request.POST.get("enable")
        config_commands = ['interface '+ str(interface_name)]
        if enable_interface == 'False':
            config_commands.append(' shutdown')
        else:
            config_commands.append(' no shutdown')
        conn_params = {
            'ip': device.host,
            'username': device.username,
            'password': device.password,
            'port': 2022,
            'device_type': device.netmiko_device_type,
        }
        with ConnectHandler(**conn_params) as device_conn:
            device_conn.send_config_set(config_commands)
        return redirect('/device/'+str(device_id))