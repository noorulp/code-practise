class TimeMap:

    def __init__(self):
        self.keyMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.keyMap.get(key) is None:
            self.keyMap[key] = []
        self.keyMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if self.keyMap.get(key) is None:
            return ""
        keyList = self.keyMap[key]
        if timestamp < keyList[0][0]:
            return ""
        if timestamp > keyList[-1][0]:
            return keyList[-1][1]
        left = 0
        right = len(keyList) - 1
        mid = (left + right)//2
        while left <= right:
            mid = (left + right) // 2
            time, st = keyList[mid]
            if time == timestamp:
                return st
            elif time > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        time, st = keyList[mid]
        if time < timestamp:
            return st
        return keyList[mid - 1][1]

if __name__ == '__main__':
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 5)  #// store the key "foo" and value "bar" along with timestamp = 1.
    print(timeMap.get("foo", 1))       #// return "bar"
    print(timeMap.get("foo", 3))
    timeMap.set("foo", "bar10", 10) #// store the key "foo" and value "bar2" along with timestamp = 4.
    timeMap.set("foo", "bar13", 13)
    timeMap.set("foo", "bar15", 15)
    timeMap.set("foo", "bar16", 16)
    timeMap.set("foo", "bar18", 18)

    print(timeMap.get("foo", 6))        #// return ""
    print(timeMap.get("foo", 5))         #// return "bar"
    print(timeMap.get("foo", 17))