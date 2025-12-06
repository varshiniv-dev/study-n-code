import speedtest


def Speed_test():
    test = speedtest.Speedtest()

    down = test.download() / 1_000_000
    up = test.upload() / 1_000_000
    ping = test.results.ping

    print("Download Speed:", round(down, 2), "Mbps")
    print("Upload Speed:", round(up, 2), "Mbps")
    print("Ping:", ping)


Speed_test()
