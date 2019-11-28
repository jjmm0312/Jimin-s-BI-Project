import similarity
import random
from operator import itemgetter
import collections, functools, operator
import copy

TOTAL_INPUT_NEWS_COUNT = 10
TOTAL_RETURN_NEWS_COUNT = 11

def e_recommend(priority, data): #explicit recommend
    weight = [4,3,2,1]
    result = []

    # select random news in the selected category by user
    for i in range (3):
        print(priority[i])
        candidate_items = []
        for item in data:
            if item['category'] == priority[i]['category']:
                candidate_items.append(item)
        #print(candidate_items[0])
        candidate_items_len = len(candidate_items)
        print(candidate_items_len)
        selected_item = random.sample(candidate_items, weight[i])
        print(len(selected_item))
        print(selected_item)
        print('\n\n\n')
        result.extend(selected_item)

    # select random news from other categories
    candidate_items = []

    for item in data:
        if item['category'] != priority[0]['category'] and item['category'] != priority[1]['category'] and item['category'] != priority[2]['category']:
            candidate_items.append(item)
    #print(candidate_items[0])
    candidate_items_len = len(candidate_items)
    selected_item = random.sample(candidate_items, weight[3]+1)
    result.extend(selected_item)

    print('e_recommend finish\n')

    print('-----------------------------\n')

    print(len(result))

    return result # 30 news recommended by algorithm

def i_recommend(history, data): #implicit recommended

    result = []
    my_news = history
    my_news_count = []
    sorted_my_news_count = []

    # my_news => my_news_count
    for i in range (TOTAL_INPUT_NEWS_COUNT):
        current_category = history[i]['category']

        # there is no element in the list => insert
        if len(my_news_count) == 0 :
            tmp = {}
            tmp['key'] = current_category
            tmp['value'] = 1
            my_news_count.append(tmp)
            continue

        # there are some elements in the list.
        isExist = False

        for j in range (len(my_news_count)) :
            if (my_news_count[j]['key'] == current_category) :
                my_news_count[j]['value'] = my_news_count[j]['value']+1
                isExist = True
                break # they already have that category, then just count up.

        # if they don't have the category, add category.
        if isExist == False :
            tmp = {}
            tmp['key'] = current_category
            tmp['value'] = 1
            my_news_count.append(tmp)


    #print(my_news_count)

    # my_news_count => sorted_my_news_count
    sorted_my_news_count = sorted(my_news_count, key=itemgetter('value'),reverse=True)

    priority = []
    for i in range(len(sorted_my_news_count)):
        priority.append(sorted_my_news_count[i]['key'])

    #print(priority)
    ######################################################################################finish

    #print(sorted_my_news_count)

    # recommend largest 3 category
    # In each category set
    # calculate similarity with every news in their set.
    # add every news' similarity in same categoryItem_count
    # sort and select news which have highest similarity

    print('-----------------------------')
    print('similarity part in\n\n')

    totalSim = []
    smallTotalSim = []

    if(len(sorted_my_news_count) <3):
        priLen = len(sorted_my_news_count)
    else:
        priLen = 3



    for pri in range (priLen):
        smallTotalSim = []
        for i in range (TOTAL_INPUT_NEWS_COUNT):
            if(my_news[i]['category'] == priority[pri]):
                print('category : ' + my_news[i]['category'])
                print('my_index : ' + str(my_news[i]['index']))
                currentSim = similarity.similarity(my_news[i]['category'], my_news[i]['index'])

                if(smallTotalSim == []):
                    smallTotalSim = copy.deepcopy(currentSim)
                    totalItemCount = len(smallTotalSim)
                    totalSim.append(smallTotalSim)

                else:
                    for j in range (totalItemCount):
                        totalSim[pri][j]['similarity'] = float(totalSim[pri][j]['similarity']) + float(currentSim[j]['similarity'])

    #print(len(totalSim))
    print('==============================================\n')

    # sort total similarity to search highest similarity
    # if the selected news is not in the history, insert to the result list
    for pri in range (priLen):
        sorted_totalSim = []
        sorted_totalSim = sorted(totalSim[pri], key=itemgetter('similarity'),reverse=True)


        resultCount = 0
        currentCount = 0 # instead of for loop

        isContinue = False
        while (resultCount != sorted_my_news_count[pri]['value']):
            #print(currentCount)
            currentIndex = sorted_totalSim[currentCount]['j_index']

            # remove duplication
            for i in range (TOTAL_INPUT_NEWS_COUNT):
                 #if the news is in the history, continue
                 if(my_news[i]['index'] == currentIndex):

                     currentCount = currentCount+1
                     isContinue = True
                     break

            if(isContinue == True):
                isContinue = False
                continue


            # push to the result list.
            resultCount = resultCount+1
            #print('++++++++++++++++++++++++++++++++++++++')
            result.append(data[int(currentIndex)])
            currentCount = currentCount+1

        # Delete my_news element if I push output
        print("result count : " + str(resultCount))

#######################################################################largest 3 category finish
    print("**********************************************")
    print('current result length : ' + str(len(result)))

    # make rest_of_my_news
    totalSim = []
    rest_of_my_news = []
    for i in range(TOTAL_INPUT_NEWS_COUNT):
        if my_news[i]['category'] != sorted_my_news_count[0]['key'] and my_news[i]['category'] != sorted_my_news_count[1]['key'] and my_news[i]['category'] != sorted_my_news_count[2]['key']:
            rest_of_my_news.append(my_news[i])

    print('rest of my news count : ')
    print(len(rest_of_my_news))

    # select the most similar news
    for i in range(len(rest_of_my_news)):
        totalSim = similarity.similarity( rest_of_my_news[i]['category'], rest_of_my_news[i]['index'])

        sorted_totalSim = []
        sorted_totalSim = sorted(totalSim, key=itemgetter('similarity'),reverse=True)

        currentCount = 0 # instead of for loop
        fin = False

        while(fin == False):
            currentIndex = sorted_totalSim[currentCount]['j_index']

            # remove duplication
            for i in range (len(rest_of_my_news)):
                 #if the news is in the history, continue
                 if(rest_of_my_news[i]['index'] == currentIndex):

                     currentCount = currentCount+1
                     isContinue = True
                     break

            if(isContinue == True):
                isContinue = False
                continue

            # push to the result list.

            result.append(data[int(currentIndex)])
            fin = True

    print('##########################################\n')

    candidate_items = []
    for item in data:
        for category in range(len(sorted_my_news_count)):
            if item['category'] == sorted_my_news_count[category]['key']:
                continue
        candidate_items.append(item)
    #print(candidate_items[0])
    candidate_items_len = len(candidate_items)
    selected_item = random.sample(candidate_items, 1)
    result.extend(selected_item)

    print('result list length : ' + str(len(result)))
    print('i_recommend finish')
    return result
