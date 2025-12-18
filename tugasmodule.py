import platform
devices_info = {
    'os detail': platform.platform(),
    'os name': platform.system(),
    'CPU': platform.processor(),
    'architecture': platform.machine(),
}
print(f'os detail : {devices_info['os detail']}')
print(f'os name : {devices_info['os name']}')
print(f'os CPU : {devices_info['CPU']}')
print(f'os architecture : {devices_info['architecture']}')
for key, value in devices_info.items():
    print(key, ":",value)