import time

from cpppo.server import enip
from cpppo.server.enip import client


def get_lk_g5000_measurement(
        connection,
        debug=False
):
    with connection:
        req = connection.service_code(
            code=0x4b,
            path=f'@0x71/0x01/0x00',  # path=@class/instance/attribute
            data=[ord(c) for c in 'MS,01'] + [0]  # 这个指令详见rs232串口说明书
        )
        if debug:
            print(f'req={enip.enip_format(req)}')
        assert connection.readable(timeout=10.0)  # receive reply
        rpy = next(connection)
        if debug:
            print(f'data={enip.enip_format(rpy)}')
        data = rpy.enip.CIP.send_data.CPF.item[
            1].connection_data.request.service_code.data
        z = float(''.join([chr(x) for x in data[6:6 + 8]]), )
        if debug:
            print(f'Z={z}mm')
    return z


def init_lk_g5000_connection(host):
    return client.implicit(host=host, timeout=15, )


if __name__ == '__main__':
    host = '192.168.6.2'
    conn = init_lk_g5000_connection(host=host)
    for i in range(10):
        print(get_lk_g5000_measurement(conn, debug=True))
        time.sleep(0.01)
