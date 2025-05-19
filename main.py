from src.cf_api import CFConnect
from src.tools import Tools
import argparse
import time



def run(config, update, force = False):

    ## CloudFlare
    name = config["domain"]
    cf = CFConnect(name, config["token"])

    current_ip = tools.getIp(config["get_ip_from"])
    last_ip = update['last_ip']

    if current_ip != last_ip or force:
        print(f"[Update IP] {last_ip} => {current_ip}")

        # get All records
        records = cf.getRecords().filter(name=name, type='A')
        records_id = [record.get("id") for record in records]

        data = {
            "content" : f"{current_ip}",
        }
        # update domain zone
        for rid in records_id:
            cf.updateRecord(rid, data)
        # update file update.yaml
        tools.setYaml(update_filename, "last_ip", current_ip)
        tools.setYaml(update_filename, "last_update", int(time.time()))

    else:
        print(f"[OK] Current IP: {current_ip}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()

    tools = Tools()
    config_filename = "config.yaml"
    update_filename = "update.yaml"

    run(tools.getYaml(config_filename), tools.getYaml(update_filename), args.force)



