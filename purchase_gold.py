import api
import threading


def double_boost():
    for i in range(1000):
        thr = threading.Thread(target=send_purchase)
        thr.start()


def send_purchase():
    while True:
        try:
            api.purchase_gold("UWiWZDxK4ToqDS1uILqs1w", "5vI/elrvv80MV8arcW9g2j86zMbpXoEXSDzXYhycZX5G12IByO+u5LqVPitTJasZaAvfjiVO0ov8MTxRVJz2YFd1nfrUZwnajz3Q9U+pQEYBHJ1pi2hQlsZSL6NzBQ86VibRndT42u/iMrGcwVQ+j6pylT/L4MHWQKsBhB00Vx46o7y0MOXKZ59K7fy+pmTCKdLLZLZGg2ngsiB64N1YA9QRUvCAUCZl+POqJ2vaHTwA3loVLp7WtUux69avK+69+bTs9k29j3dzXhIxFigMR9/Fw+LghRRZkUnWa/4GyWFR8kUYyfhGDbAisVXhwcJmCaEg768LUHCnHoh77m2FZQ==", "%7B%22orderId%22%3A%22GPA.3336-4632-3035-04640%22%2C%22packageName%22%3A%22com.pennypop.monsters.live%22%2C%22productId%22%3A%22gold1%22%2C%22purchaseTime%22%3A1725991541846%2C%22purchaseState%22%3A0%2C%22purchaseToken%22%3A%22hlapgngoaghdkkgeiolmmopk.AO-J1OzC305eQi7NNV0MI7Uxo7gyUi1sdAGlfKb6cpkzWyWXs7nd4Ke3Nq3v0uP4aYC2Rvk1oItS8t5sYCLXrECawieqFg_zcP-KeJ3T3skED9Bquc06bro%22%2C%22quantity%22%3A1%2C%22acknowledged%22%3Afalse%7D", "Set10_Set12_9999_p9_peace_grabs")
            print(1)
        except:
            pass


for i in range(1):
    thr = threading.Thread(target=double_boost)
    thr.start()