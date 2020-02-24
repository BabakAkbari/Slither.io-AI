from RemoteEnv import RemoteEnv

remote_env =RemoteEnv(tcp_ip='0.0.0.0', tcp_port=5005, buffer_size=20)
while True:
    remote_env.env_cmd()