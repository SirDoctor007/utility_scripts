import time


class Search:
    def __init__(self, json_data):
        self.json_data = json_data
        self.region = json_data["regions"][0]
        self.device_name = ""
        self.start = (int(time.time()) - 604800) * 1000
        self.end = int(time.time()) * 1000

    def select_region(self):
        options = {}
        for pos, region in enumerate(self.json_data["regions"], 1):
            options[pos] = region

        while True:
            for position in options:
                print(f"{position}) {options[position]}")
            try:
                ans = int(input("Select a region: "))
                if ans not in options.keys():
                    raise ValueError
                else:
                    break
            except ValueError:
                print("That is not a valid answer.")

        self.region = options[ans]
        return 0

    def set_start_datetime(self):
        pass

    def set_end_datetime(self):
        pass

    def get_device_name(self):
        while True:
            device_name = input("Enter the device's name: ")
            while True:
                try:
                    ans = int(input(f"Is this correct '{device_name}'?\n1) Yes\n2) No\n--> "))
                    if ans not in [1, 2]:
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print("That is not a valid answer.")
            if ans == 1:
                break

        self.device_name = device_name
        return 0

    def list_urls(self):
        urls = dict()
        urls["network"] = self.json_data["searches"]["network"]["url"].replace("[REGION]", self.region)\
            .replace("[START_TIME_EPOCH_MILLISEC]", str(self.start)).replace("[END_TIME_EPOCH_MILLISEC]", str(self.end))\
            .replace("[MACHINE_NAME]", self.device_name)
        urls["process"] = ""

        for search in urls:
            print(f"{search}: {urls[search]}")


if __name__ == "__main__":

    url_data = {
              "searches": {
                  "network": {
                      "url": ""
                  },
                  "process": {
                      "url": ""
                  }
              },
              "regions": [""]
            }

    s = Search(url_data)
    s.get_device_name()
    s.list_urls()
