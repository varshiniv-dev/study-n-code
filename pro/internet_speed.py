import speedtest


def Speed_test():
    test = speedtest.Speedtest()   # correct class name

    # Download speed
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print("Download speed in Mbps:", down_speed)

    # Upload speed
    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print("Upload speed in Mbps:", up_speed)

    # Ping
    ping = test.results.ping
    print("Ping:", ping)


Speed_test()
