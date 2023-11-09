from ipaddress import ip_address
import pytest

def filter_subnet(ips: list[ip_address]) -> list[ip_address]:
    valid_ip_addresses = []
    for ip in ips:
        ip_string = format(ip)
        if len(ip_string.split('.')) !=  4:
            raise ValueError('Improper formatted Ip Address in list.')
        if ip_string.split('.')[2] == '60':
            valid_ip_addresses.append(ip)

    return valid_ip_addresses

def test_filter_subnet__no_valid_ipaddresses__return_empty_list():
    assert filter_subnet(['192.168.80.20']) == []


def test_filter_subnet__invalid_ipaddresses__return_empty_list():
    with pytest.raises(ValueError):
        filter_subnet(['192.168.80.20.50']) == []


def test_filter_subnet__given_list__return_expected_list():
    given_data_list = ['192.168.80.20', '192.168.60.1', '192.168.91.23',
                       '192.168.60.43', '192.168.60.22', '192.168.61.5',
                       '192.168.60.98', '192.168.1.24', '192.168.60.13',
                       '192.168.60.47']
    expected_filtered_result = ['192.168.60.1','192.168.60.43', '192.168.60.22', 
                       '192.168.60.98', '192.168.60.13','192.168.60.47']
    assert filter_subnet(given_data_list) == expected_filtered_result