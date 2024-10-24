stock = { 
    "팥붕어빵" : 10,
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5
}

prices = {
    "팥붕어빵" : 1000,
    "슈크림붕어빵" : 1200,
    "초코붕어빵" : 1500
}

sales = {
    "팥붕어빵": 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}

while True:
    mode = input("원하는 모드를 선택해주세요(주문, 관리자, 종료): ")
    if mode == "종료":
        break

    if mode == "주문":
        while True:
            order = {}
            bread_type = input("주문할 붕어빵 종류를 입려하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵 중 한가지를 골라주세요)종료를 원하는 경우 '종료'를 입력해주세요: ")
            if bread_type == "종료":
                break
            bread_count = int(input("주문할 붕어빵 개수를 입력하세요: "))

            if stock[bread_type] >= bread_count :
                stock[bread_type] -= bread_count
                sales[bread_type] += bread_count
                print(f"{bread_type} {bread_count}개를 판매했습니다.")
            else:
                result = bread_count - stock[bread_type]
                print(f"죄송합니다. {bread_type} 재고가 {result}개 부족합니다.")
            
            print("-------------------------------------------")
            #len(stock) : 함수   stock.items()
            for bread, quantity in stock.items():
                print(f"{bread} : {quantity}")

    if mode == "관리자":
        while True:
            bread_type = input("추가할 붕어빵 종류를 입려하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵 중 한가지를 골라주세요)종료를 원하는 경우 '종료'를 입력해주세요: ")
            if bread_type == "종료":
                break
            bread_count = int(input("추가할 붕어빵 개수를 입력하세요: ")) 
            stock[bread_type] += bread_count
            print(f"{bread_type}의 재고가 {bread_count}개 추가되어, 현재 총 {stock[bread_type]}개 입니다.")

print("영업을 종료합니다.")
total_sales = sum(sales[bread] * prices[bread] for bread in sales) #컴프리핸션 작동되는 원리
print(f"총 매출 : {total_sales}원")

