class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]
    return sum

class list_D2(list):
    def __init__(self,arr):
        
        ### YOUR CODE HERE ###
        if len(arr)==0 :
            raise not2DError()
        else:
            for ist in arr:
                if type(ist) != list :
                    raise not2DError()
                elif len(ist) != 0 and type(ist[0]) == list :
                    raise not2DError()

        fst_len = len(arr[0])
        for lst in arr:
            if len(lst) != fst_len:
                raise unevenListError()
        ###

        self.extend(arr)

    def __str__(self):

        ### YOUR CODE HERE ###
        
        x = len(self)
        y = 0
        if x != 0:
            y = len(self[0])
        ret = "list_2D: "+str(x)+"*"+str(y)
        return ret

        ######

    def transpose(self):

        ### YOUR CODE HERE ###
        #(1,2),(3,4),(5,6) -> (1,3,5),(2,4,6)

        newlist = []
        len_x = len(self)
        len_y = 0
        if len_x != 0:
            len_y = len(self[0])

        #열 길이만큼 빈 리스트 삽입해두기
        for i in range(len_y):
            newlist.append([])

        #리스트 채우기
        for x in self:
            for j,y in enumerate(x):
                newlist[j].append(y)
                
        return list_D2(newlist)
        
        ######


    def __matmul__(self, others):
        
        ### YOUR CODE HERE ###

        others = others.transpose()

        if len(self)==0 and len(others)==0:
            return self
        if len(self)==0 or len(others)==0:
            raise improperMatrixError()
        if len(self[0]) != len(others[0]):
            raise improperMatrixError()

        result = []
        for i in self:
            sub_result = []
            for j in others:
                sub_result.append(mul1d(i,j))
            result.append(sub_result)
        
        return list_D2(result)

        ######

    def avg(self):

        ### YOUR CODE HERE ###

        list_sum = 0
        count=0
        for x in self:
            for y in x:
                list_sum += y
                count += 1
        return list_sum/count

        ######
