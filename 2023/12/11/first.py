def solution(consume, cards):
    # 모든 카드에 대한 할인 금액이 0일때 -1 return ->  모든 할인 금액이 0일때 is_discount 는 False로 유지된다.
    is_discount = False # 이걸 global로 지정할지는 좀 생각해보자
    answer = -1

    discount_amount_list = return_discount_amount_to_list(consume, cards)

    max_discount = -1
    idx_max_discount = list()
    
    for card_idx, discount_amount in enumerate(discount_amount_list):
        if discount_amount > 0 :
            is_discount = True
        if discount_amount > max_discount :
            idx_max_discount.clear() # idx_max_discount 리스트를 비운다. -> 가장 할인율이 높고 이와 같은게 아직 없으니까
            idx_max_discount.append(card_idx)
            max_discount = discount_amount
        elif discount_amount == max_discount :
            idx_max_discount.append(card_idx)
    
    if is_discount :
        answer = min(idx_max_discount) + 1

    return answer


def return_discount_amount_to_list(consume, cards) : # return 타입은 List[int]이다

    #카테고리별 사용 금액 정리
    category_per_amount_dict = dict()
    for data in consume :
        category, amount = split_consume(data)
        #category_per_amount_dict에 category가 있으면 amount를 더하고 없으면 새로 만든다.
        if category in category_per_amount_dict :
            category_per_amount_dict[category] += amount
        else :
            category_per_amount_dict[category] = amount
    
    #카드별 할인 금액 리스트에 정리
    discount_per_card_list = list()
    for card_disount in cards :
        discount_amount = discount_amount_by_card(card_disount,category_per_amount_dict) #discount_amount의 타입은 int이다.
        discount_per_card_list.append(discount_amount)

    return discount_per_card_list


def split_consume(consume_data) :
    # 뛰어쓰기를 기점으로 split 한다.
    consume_list = consume_data.split(" ")
    category = consume_list[0]
    amount = int(consume_list[1])
    return category, amount

def split_card_data(card) :
    card_list = card.split(" ")

    category = card_list[0]
    percent = card_list[1] # 할인율인데 이걸 그냥 처음부터 float로 내놔서 바로 곱하기 가능하게 할까?
    maximum_discount = card_list[2]

    return category, percent, maximum_discount

def discount_amount_by_card(card_disount_datas,category_per_amount_dict) :#여기서 card_disount_datas 하나의 카드에 대한 할인 정보 들릐 list를 의미한다.
    #할인된게 없을때 그냥 0으로 return
    discount_amount = 0

    for card_disount in card_disount_datas :

        category, percent, maximum_discount = split_card_data(card_disount)

        #category_per_amount_dict에 category가 있으면 할인 계산 시작한다.
        if category in category_per_amount_dict :
            amount = category_per_amount_dict[category]
            discount_amount_for_category = amount * float(percent) / 100
            discount_amount_for_category = int(discount_amount_for_category)
            if discount_amount_for_category > int(maximum_discount) :
                discount_amount_for_category = int(maximum_discount)
            discount_amount += discount_amount_for_category

    return discount_amount




if __name__ == '__main__':
    print('Hello World!')
    # consume = ["public_transport 10000","public_transport 10000","taxi 20000","shopping 377000", "food 16000","public_transport 2000"]
    # cards = [["food 5 30000","convenience_store 20 10000", "public_transport 15 2000"], ["food 5 30000", "shopping 10 15000", "movie 7 5000"]]
    consume = ["movie 10000"]
    cards = [["movie 100 5000"], ["movie 50 5000"], ["movie 10 5000"]]
    answer = solution(consume, cards)
    print(answer)
    