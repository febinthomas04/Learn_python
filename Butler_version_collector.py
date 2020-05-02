from config import TOWER_IP
import subprocess
import network
import struct
import os
import json
import requests
import time
from logging_settings import ServerLogger

butler_id = int(os.popen('hostname').read().rstrip().split('-')[1])


def is_valid_version(version):
    return '_' in str(version)


def get_butler_version(retry=1, max_retries=1):
    '''Get Butler Version number'''

    ServerLogger.info("Version_collector: get_butler_version called at %s", time.strftime("%a, %d %b %Y %H:%M:%S"))
    if retry > max_retries:
        return None

    hdr = "$S"
    bytes = bytearray()
    bytes.extend(hdr)
    bytes.append(0)
    bytes.append(5)
    # print ("\nSending header bytes to safety system to recieve butler_version\n")

    net = network.network()
    net.send("safety_system", bytes)
    msg = net.receive("safety_system")
    net.close()

    if msg != None:
        try:
            unpack_str = "ccBBB" + str(ord(msg[4])) + "s"
            # print("unpack_str: ", unpack_str)
            butler_version_ss = struct.unpack(unpack_str, msg)[5][1:-1]
            ServerLogger.info('Version_collector: Butler Version received from SS: %s', butler_version_ss)
            return butler_version_ss
        except Exception as e:
            ServerLogger.info("Version_collector: Error in Decoding msg..!! Sleeping for 30 sec !! %s", e)
            time.sleep(30)
    else:
        ServerLogger.info("Version_collector: Error in communication with Safety System..!! Sleeping for 30 sec !!")
        time.sleep(30)
    return get_butler_version(retry + 1, max_retries)


def get_ss_version(retry=1, max_retries=1):
    '''Get safety version number'''

    ServerLogger.info("Version_collector: get_ss_version called at %s", time.strftime("%a, %d %b %Y %H:%M:%S"))

    if retry > max_retries:
        return None

    hdr = "$S"
    bytes = bytearray()
    bytes.extend(hdr)
    bytes.append(0)
    bytes.append(1)
    # print ("\nSending header bytes to safety system to recieve ss_bin_version\n")
    net = network.network()
    net.send("safety_system", bytes)
    msg = net.receive("safety_system")
    net.close()

    if msg != None:
        # print("msg: ", msg)
        try:
            unpack_str = "ccBBB" + str(ord(msg[4])) + "s"
            # print("unpack_str: ", unpack_str)
            butler_safety_version = struct.unpack(unpack_str, msg)[5][1:-1]
            ServerLogger.info('Version_collector: Butler Safety Version received from SS: %s', butler_safety_version)

            if is_valid_version(butler_safety_version):
                return butler_safety_version
        except Exception as e:
            ServerLogger.info("Version_collector: Error Decoding get_ss_version msg..!! Sleeping for 30 sec !! %s", e)
    else:
        ServerLogger.info("Version_collector: Error in communication with Safety System..!! Sleeping for 30 sec !!")
    time.sleep(30)
    return get_ss_version(retry + 1, max_retries)


def get_ods_front_version(retry=1, max_retries=1):
    '''Get ODS Front version number'''

    ServerLogger.info("Version_collector: get_ods_front_version called at %s", time.strftime("%a, %d %b %Y %H:%M:%S"))
    if retry > max_retries:
        return None

    hdr = "$O"
    bytes = bytearray()
    bytes.extend(hdr)
    bytes.append(0)
    bytes.append(1)
    # print ("\nSending header bytes to safety system to recieve ods_bin_version\n")
    net = network.network()
    net.send("safety_system", bytes)
    msg = net.receive("safety_system")
    net.close()

    if msg != None:
        # print("msg: ", msg)
        try:
            unpack_str = "ccBBB" + str(ord(msg[4])) + "s"
            # print("unpack_str: ", unpack_str)
            butler_odsf_version = struct.unpack(unpack_str, msg)[5][1:-1]
            ServerLogger.info('Version_collector: Butler ODS Front Version received from SS: %s', butler_odsf_version)

            if is_valid_version(butler_odsf_version):
                return butler_odsf_version

        except Exception as e:
            ServerLogger.info(
                "Version_collector: Error in Decoding get_ods_front_version msg..!! Sleeping for 30 sec !! %s", e)
    else:
        ServerLogger.info("Version_collector: Error in communication with Safety System..!! Sleeping for 30 sec !!")
    time.sleep(30)
    return get_ods_front_version(retry + 1, max_retries)


def get_ods_back_version(retry=1, max_retries=1):
    '''Get ODS Back version number'''

    ServerLogger.info("Version_collector: get_ods_back_version called at %s", time.strftime("%a, %d %b %Y %H:%M:%S"))

    if retry > max_retries:
        return None

    hdr = "$O"
    bytes = bytearray()
    bytes.extend(hdr)
    bytes.append(0)
    bytes.append(1)
    # print ("\nSending header bytes to safety system to recieve ods_bin_version\n")
    net = network.network()
    net.send("safety_system", bytes)
    msg = net.receive("safety_system")
    net.close()

    if msg != None:
        try:
            # print("msg: ", msg)
            unpack_str = "ccBBB" + str(ord(msg[4])) + "s"
            # print("unpack_str: ", unpack_str)
            butler_odsb_version = struct.unpack(unpack_str, msg)[5][1:-1]
            ServerLogger.info('Version_collector: Butler ODS Back Version received from SS: %s', butler_odsb_version)

            if is_valid_version(butler_odsb_version):
                return butler_odsb_version

        except Exception as e:
            ServerLogger.info(
                "Version_collector: Error in Decoding get_ods_back_version msg..!! Sleeping for 30 sec !! %s", e)
    else:
        ServerLogger.info("Version_collector: Error in communication with Safety System..!! Sleeping for 30 sec !!")
    time.sleep(30)
    return get_ods_front_version(retry + 1, max_retries)

def get_bms_version_from_log():
    '''Get BMS version number'''

    ServerLogger.info("Version_collector: get_bms_version_from_log called at %s",
                      time.strftime("%a, %d %b %Y %H:%M:%S"))

    try:
        command = "awk '/Code_Version BMS/ {print}' /data/fw/log/ss/SSlog_*|awk '{print $7}'|tail -1"
        return subprocess.check_output(command, shell=True).split('\n')[0].split(':')[1]
    except Exception as e:
        ServerLogger.info("Version_collector: get_bms_version_from_log error %s", e)
    return None


def get_bms_version(retry=1, max_retries=1):
    '''Get BMS version number'''

    ServerLogger.info(" get_bms_version called at %s ", time.strftime("%a, %d %b %Y %H:%M:%S"))
    if retry > max_retries:
        return get_bms_version_from_log()

    hdr = "$B"
    bytes = bytearray()
    bytes.extend(hdr)
    bytes.append(0)
    bytes.append(1)
    # print ("\nSending header bytes to safety system to recieve bms_bin_version\n")
    net = network.network()
    net.send("safety_system", bytes)
    msg = net.receive("safety_system")
    net.close()

    if msg != None:
        # print("msg: ", msg)
        try:
            unpack_str = "ccBBB" + str(ord(msg[4])) + "s"
            # print("unpack_str: ", unpack_str)
            butler_bms_version = struct.unpack(unpack_str, msg)[5][1:-1]
            ServerLogger.info('Version_collector: get_bms_version res from SS: %s', butler_bms_version)
            if is_valid_version(butler_bms_version):
                return butler_bms_version

        except Exception as e:
            ServerLogger.info(
                "Version_collector: Error in Decoding get_bms_version msg..!! Sleeping for 30 sec !! %s", e)
    else:
        ServerLogger.info(
            "Version_collector: get_bms_version Error in communication with Safety System..!! Sleeping for 30 sec !!")
    time.sleep(30)
    return get_bms_version(retry + 1, max_retries)


def get_nav_version(retry=1, max_retries=1):
    '''Get Nav version number'''

    ServerLogger.info("Version_collector: get_nav_version called at %s", time.strftime("%a, %d %b %Y %H:%M:%S"))

    if retry > max_retries:
        return None

    hdr = "$N"
    bytes = bytearray()
    bytes.extend(hdr)
    bytes.append(0)
    bytes.append(1)
    # print ("\nSending header bytes to safety system to recieve bms_bin_version\n")

    net = network.network()
    net.send("navigation_system", bytes)
    msg = net.receive("navigation_system")
    net.close()

    if msg != None:
        try:
            # print("msg: ", msg)
            unpack_str = "ccBBB" + str(ord(msg[4])) + "s"
            # print("unpack_str: ", unpack_str)
            butler_nav_version = struct.unpack(unpack_str, msg)[5][1:-1]
            ServerLogger.info('Version_collector: Butler Nav Version received from BBB: %s', butler_nav_version)
            if is_valid_version(butler_nav_version):
                return butler_nav_version
        except Exception as e:
            ServerLogger.info("Version_collector: Error in Decoding msg..!! Sleeping for 30 sec !! %s", e)
    else:
        ServerLogger.info("Version_collector: Error in communication with Beaglebone..!! Sleeping for 30 sec !!")
    time.sleep(30)
    return get_nav_version(retry + 1, max_retries)


def get_lmd_version(retry=1, max_retries=1):
    '''Get Lift version number'''

    ServerLogger.info("Version_collector: get_lmd_version called at %s", time.strftime("%a, %d %b %Y %H:%M:%S"))

    if retry > max_retries:
        return None

    hdr = "$L"
    bytes = bytearray()
    bytes.extend(hdr)
    bytes.append(0)
    bytes.append(2)
    # print ("\nSending header bytes to safety system to recieve bms_bin_version\n")

    net = network.network()
    net.send("navigation_system", bytes)
    msg = net.receive("navigation_system")
    net.close()

    if msg != None:
        ServerLogger.info("get_lmd_version msg: %s", msg)
        try:
            unpack_str = "ccBBB" + str(ord(msg[4])) + "s"
            # print("unpack_str: ", unpack_str)
            butler_lmd_version = struct.unpack(unpack_str, msg)[5][1:-1]
            ServerLogger.info('Version_collector: get_lmd_version res from BBB: %s', butler_lmd_version)
            if is_valid_version(butler_lmd_version):
                return butler_lmd_version
        except Exception as e:
            ServerLogger.info("Version_collector: Error in Decoding get_lmd_version msg..!! Sleeping for 30 sec !! %s",
                              e)
    else:
        ServerLogger.info(
            "Version_collector: get_lmd_version Error in communication with Beaglebone..!! Sleeping for 30 sec !!")
    time.sleep(30)
    return get_lmd_version(retry + 1, max_retries)


def get_wmd_version(retry=1, max_retries=1):
    '''Get Wheel version number'''

    ServerLogger.info("Version_collector: get_wmd_version called at %s", time.strftime("%a, %d %b %Y %H:%M:%S"))

    if retry > max_retries:
        return None

    hdr = "$W"
    bytes = bytearray()
    bytes.extend(hdr)
    bytes.append(0)
    bytes.append(2)
    # print ("\nSending header bytes to safety system to recieve bms_bin_version\n")
    net = network.network()
    net.send("navigation_system", bytes)
    msg = net.receive("navigation_system")
    net.close()

    if msg != None:
        try:
            ServerLogger.info("get_wmd_version msg: %s", msg)
            unpack_str = "ccBBB" + str(ord(msg[4])) + "s"
            # print("unpack_str: ", unpack_str)
            butler_wmd_version = struct.unpack(unpack_str, msg)[5][1:-1]
            ServerLogger.info('Version_collector: get_wmd_version res: %s', butler_wmd_version)
            if is_valid_version(butler_wmd_version):
                return butler_wmd_version

        except Exception as e:
            ServerLogger.info("Version_collector: Error in Decoding get_wmd_version msg..!! Sleeping for 30 sec !! %s",
                              e)
    else:
        ServerLogger.info(
            "Version_collector: get_wmd_version Error in communication with Beaglebone..!! Sleeping for 30 sec !!")
    time.sleep(30)
    return get_wmd_version(retry + 1, max_retries)


def get_ipu_version(retry=1, max_retries=1):
    '''Get IPU version number'''

    ServerLogger.info("Version_collector: get_ipu_version called at %s", time.strftime("%a, %d %b %Y %H:%M:%S"))

    if retry > max_retries:
        return None

    hdr = "$I"
    bytes = bytearray()
    bytes.extend(hdr)
    bytes.append(0)
    bytes.append(1)
    # print ("\nSending header bytes to safety system to recieve bms_bin_version\n")
    net = network.network()
    net.send("ipu", bytes)
    msg = net.receive("ipu")
    net.close()

    if msg != None:
        try:
            ServerLogger.info("get_ipu_version msg: %s", msg)
            unpack_str = "ccBBB" + str(ord(msg[4])) + "s"
            # print("unpack_str: ", unpack_str)
            butler_ipu_version = struct.unpack(unpack_str, msg)[5][1:-1]
            ServerLogger.info('Version_collector: get_ipu_version res: %s', butler_ipu_version)
            if True or is_valid_version(butler_ipu_version):
                return butler_ipu_version

        except Exception as e:
            ServerLogger.info("Version_collector: Error in Decoding get_ipu_version msg..!! Sleeping for 30 sec !! %s",
                              e)
    else:
        ServerLogger.info(
            "Version_collector: get_ipu_version Error in communication..!! Sleeping for 30 sec !!")
    time.sleep(30)
    return get_ipu_version(retry + 1, max_retries)


def get_ipu_version_from_log():
    '''Get IPU version number'''

    ServerLogger.info("Version_collector: get_ipu_version_from_log called at %s",
                      time.strftime("%a, %d %b %Y %H:%M:%S"))

    try:
        command = "awk '/Version/ {print}' /data/fw/log/ButlerIPUServer* |awk '{print $9}'|tail -1 ; "
        return subprocess.check_output(command, shell=True).split('\n')[0]
    except Exception as e:
        ServerLogger.info("Version_collector: get_ipu_version_from_log error %s", e)
    return None


def get_butler_remote_version():
    ServerLogger.info("Version_collector: get_butler_remote_version called at %s",
                      time.strftime("%a, %d %b %Y %H:%M:%S"))

    try:
        command = "ls /opt/butler_remote/releases | head -n 1"
        return subprocess.check_output(command, shell=True).split('\n')[0]
    except Exception as e:
        ServerLogger.info("Version_collector: get_butler_remote_version error %s", e)
    return None


def get_subsystem_json(subsystem_name, subsystem_version):
    return {
        "version_number": subsystem_version,
        "subsystem": subsystem_name
    }


def get_all_versions(max_retries=1):
    ServerLogger.info("Version_collector: get_all_versions called")
    ip = os.popen(
        "ip route get 8.8.8.8 | awk 'NR==1 {print $NF}'").read().rstrip()

    butler_subsystems = []

    bot_version = get_butler_version(retry=1, max_retries=max_retries)
    ods0 = get_ods_front_version(retry=1, max_retries=max_retries)
    ods1 = get_ods_back_version(retry=1, max_retries=max_retries)
    ss = get_ss_version(retry=1, max_retries=max_retries)
    bms = get_bms_version(retry=1, max_retries=max_retries)
    wmd = get_wmd_version(retry=1, max_retries=max_retries)
    lmd = get_lmd_version(retry=1, max_retries=max_retries)
    ipu = get_ipu_version_from_log()
    nav = get_nav_version(retry=1, max_retries=max_retries)
    butler_remote = get_butler_remote_version()

    if ods0:
        butler_subsystems.append(get_subsystem_json('ods0', ods0))

    if ods1:
        butler_subsystems.append(get_subsystem_json('ods1', ods1))

    if ss:
        butler_subsystems.append(get_subsystem_json('ss', ss))

    if bms:
        butler_subsystems.append(get_subsystem_json('bms', bms))

    if ipu:
        butler_subsystems.append(get_subsystem_json('ipu', ipu))

    if nav:
        butler_subsystems.append(get_subsystem_json('nav', nav))

    if butler_remote:
        butler_subsystems.append(get_subsystem_json('butler_remote', butler_remote))

    if wmd:
        butler_subsystems.append(get_subsystem_json('wmd', butler_remote))

    if lmd:
        butler_subsystems.append(get_subsystem_json('lmd', butler_remote))

    all_versions = {
        "butler_id": butler_id,
        "butler_version": bot_version,
        "ip": ip,
        "butler_subsystem_relations": butler_subsystems
    }
    return all_versions


def update_butler_status(status):
    payload = {
        "butler_id": butler_id,
        "status": status
    }
    endpoint = "http://" + TOWER_IP + "/api/v1/dm/butler_status/"
    headers = {'Content-type': 'application/json'}
    r = requests.post(url=endpoint, data=json.dumps(payload), headers=headers)
    return r


def is_any_version_invalid(all_versions):
    if all_versions['butler_id'] is None:
        return True

    for butler_subsystem_relation in all_versions['butler_subsystem_relations']:
        if butler_subsystem_relation['version_number'] is None:
            return True
    return False


def send_all_versions(max_retries=1):
    all_versions = get_all_versions(max_retries)

    ServerLogger.info("Version_collector: all_version_json: %s", all_versions)

    # don't make API call to tower
    if is_any_version_invalid(all_versions):
        return {
            'all_versions': all_versions,
            'sent': False
        }

    endpoint = "http://" + TOWER_IP + "/api/v1/dm/butlers/"
    r_sc = 0
    retries = 0
    while (retries < 10 and r_sc != 201):
        retries += 1
        headers = {'Content-type': 'application/json'}
        r = requests.post(url=endpoint, data=json.dumps(all_versions), headers=headers)
        r_sc = r.status_code
        ServerLogger.info("Version_collector: Response code for version update: %s", r.status_code)

    return {
        'all_versions': all_versions,
        'sent': (retries < 10)
    }


if __name__ == "__main__":
    ServerLogger.info("Version_collector: Started version collector from main")
    resp = send_all_versions(max_retries=5)
    if resp['sent']:
        r1 = update_butler_status("Default")
        ServerLogger.info("Version_collector: Response code for status update: %s", r1.status_code)