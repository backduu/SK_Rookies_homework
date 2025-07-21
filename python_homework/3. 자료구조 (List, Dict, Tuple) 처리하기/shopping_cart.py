cart = {
    "사과" : (2, 1000),
    "바나나" : (3, 800),
    "오렌지" : (1, 1500)
}

print("쇼핑 카트:")
total_price = 0

for item, (quantity, price_per_unit) in cart.items():
    item_total = quantity * price_per_unit
    total_price += item_total
    print(f"{item}: {quantity}개 (개당 {price_per_unit}원) = {item_total}원")


print(f"총 가격: {total_price}원")
