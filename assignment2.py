import winsound
import time

def sort_merge(data):
    if len(data) > 1:
        center = len(data) // 2
        Left = data[:center]
        Right = data[center:]

        sort_merge(Left)
        sort_merge(Right)

        a = b = c = 0

        while a < len(Left) and b < len(Right):
            if Left[a] < Right[b]:
                data[c] = Left[a]
                a += 1
            else:
                data[c] = Right[b]
                b += 1
            c += 1
            print("Swap occurred:", data)
            winsound.Beep(1050, 600)  # Beep at 1050 hz
            time.sleep(0.5)  # Pause for half a second to visualize the sorting process

        while a < len(Left):
            data[c] = Left[a]
            a += 1
            c += 1

        while b < len(Right):
            data[c] = Right[b]
            b += 1
            c += 1

def primary():
    data = input("Enter the array elements (Seperate with Space): ").split()
    data = [int(x) for x in data]  # Convert input strings to ints
    print("Given array is:", data)
    sort_merge(data)
    print("Sorted array is:", data)

if __name__ == "__main__":
    primary()
