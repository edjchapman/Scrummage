import subprocess

container_service_name = 'log_machine_backend_'
proxy_container = 'log_machine_proxy_1'


def exists_on_upstream(container):
    """
    Check if container is already in the config
    """
    with open('nginx/nginx.conf') as f:
        if container in f.read():
            return True
        return False


def discover_upstream():
    """
    find a better way
    @return:
    """
    existing_upstream = []
    for i in range(1, 1000):
        container = 'server ' + container_service_name + str(i) + ':8000;'
        if exists_on_upstream(container):
            existing_upstream.append(container_service_name + str(i))
    return existing_upstream


def add_nginx_upstream(container):
    """
    Modify nginx upstream
    @type container: object
    """
    with open('nginx/nginx.conf', 'r+') as f:
        data = f.read()
        f.seek(0)
        if not exists_on_upstream(container):
            print('add_nginx_upstream', container)
            data = data.replace('# server_placeholder', '# server_placeholder \n\tserver ' + container + ':8000;')
        f.write(data)


def remove_nginx_upstream(container):
    """
    Modify nginx upstream
    """
    to_remove = 'server ' + container + ':8000;'
    with open('nginx/nginx.conf', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if line.strip("\n").strip("\t").strip() == to_remove:
                continue
            else:
                f.write(line)
        f.truncate()


def get_containers():
    cmd = ["docker", "ps", "--format", '"{{.Names}}"', "--filter", "name=" + container_service_name]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    out, err = p.communicate()
    nodes = out.decode("utf-8")
    nodes = nodes.replace('"', '').split()
    return nodes


if __name__ == '__main__':
    existing_nodes = discover_upstream()
    restart = False
    # while True:
    containers = get_containers()
    for container in containers:
        if container not in existing_nodes:
            print('adding', container)
            add_nginx_upstream(container)
            existing_nodes.append(container)
            restart = True

    for container in existing_nodes:
        if container not in containers:
            print('removing', container)
            remove_nginx_upstream(container)
            existing_nodes.remove(container)
            restart = True

    if restart:
        print('restarting ngix')
        cmd = ["docker", "exec", "-t", proxy_container, "nginx", "-s", "reload"]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out, err = p.communicate()
        print(out, err)
        restart = False
