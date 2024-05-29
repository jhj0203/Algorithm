def solution(str1, str2):
    answer = ''
    list1 = list(str1)
    list2 = list(str2)
    answerList = []
    for i in range(0,len(str1)):
        answerList.append(list1[i])
        answerList.append(list2[i])
            
    answer = ('').join(answerList)
    print(answer)
    return answer