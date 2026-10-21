# To test: from root folder:
# python -c "from src.logsgenerator.beaconing.beaconing import generate; print(*generate(3), sep='\n')"
# in generate(), you can use 2 arguments, not only one, example: "[...]; print(*generate(10, 30), sep='\n')"

from datetime import datetime, timedelta

def generate(count=5, interval=10):
    lines = []
    start = datetime.now() - timedelta(seconds=(count - 1) * interval)
    for i in range(count):
        moment = start + timedelta(seconds=i * interval)
        stamp = moment.strftime("%Y-%m-%d %H:%M:%S")
        lines.append(
            f"timestamp={stamp} event=network_connect "
            f"src_ip=192.168.1.50 dst_ip=203.0.113.77 dst_port=443 protocol=tcp"
        )
    return lines