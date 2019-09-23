num_dict = {'0':'zero','1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
            '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen',
            '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '30':'thirty', '40':'forty','50':'fifty','60':'sixty','70':'seventy','80':'eighty','90':'ninety','100':'one hundred','200':'two hundred','300':'three hundred','400':'four hundred','500':'five hundred','600':'six hundred','700':'seven hundred','800':'eight hundred','900':'nine hundred'
            }


def checkio(nums):
    nums_list = []
    for i in str(nums):
        nums_list.append(i)
    if len(nums_list)==3 and nums_list[1]!='0':
        nums_list[0]=nums_list[0]+'00'
        nums_list[1]=nums_list[1]+'0'
        if nums_list[1] == '10':
            nums_list[1] = '1'+nums_list[2]
            res_one = num_dict[nums_list[0]]+' '+num_dict[nums_list[1]]
            return res_one
        if nums_list[2] == '0':
            res = num_dict[nums_list[0]] + ' ' + num_dict[nums_list[1]]
        else:
            res = num_dict[nums_list[0]] + ' ' + num_dict[nums_list[1]] + ' ' + num_dict[nums_list[2]]
        return res
    elif len(nums_list)==3 and nums_list[1]=='0':
        if nums_list[2] == '0':
            nums_list[0] = nums_list[0] + '00'
            res = num_dict[nums_list[0]]
        else:
            nums_list[0] = nums_list[0] + '00'
            res = num_dict[nums_list[0]] +' ' + num_dict[nums_list[2]]
        return res
    elif len(nums_list)==2:
        nums_list[0]=nums_list[0]+'0'
        if nums_list[1] == '0':
            res = num_dict[nums_list[0]]
        elif nums_list[0] == '10':
            nums_list[0] = '1'+nums_list[1]
            res = num_dict[nums_list[0]]
        else:
            res = num_dict[nums_list[0]] + ' ' + num_dict[nums_list[1]]
        return res
    elif len(nums_list) == 1:
        res = num_dict[nums_list[0]]
        return res



if __name__ == '__main__':
    checkio(101)
