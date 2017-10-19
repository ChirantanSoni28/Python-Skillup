#STEP 1 convert scores to numbers
def convert_to_numeric(score):
    score = float(score)
    return score
    #STEP 2 and STEP 3 find the average of the middle three scores

def sum_of_middle_three(s1,s2,s3,s4,s5):
    x = [s1,s2,s3,s4,s5]
    score1 = x[0]
    #print(score1)
    score2 = x[4]
    #print(score2)
    total = sum(x) - (score1 + score2)
    return total

    #STEP 4 turn average score into a rating

def score_to_rating_string(av_score):
    #rating = None
    if av_score < 1:
        rating = "Terrible"
    elif av_score < 2:
        rating = "Bad"
    elif av_score < 3:
        rating = "OK"
    elif av_score < 4:
        rating = "Good"
    elif av_score < 5:
        rating = "Excellent"
    else:
        return "No ratings found!"
    return rating

def score_to_rating(s1,s2,s3,s4,s5):

    """" #Step 1: Take Scores and convert them to float """
    s1 = convert_to_numeric(s1)
    s2 = convert_to_numeric(s2)
    s3 = convert_to_numeric(s3)
    s4 = convert_to_numeric(s4)
    s5 = convert_to_numeric(s5)
    print(s1,s2,s3,s4,s5)
    """" #Step 2: Take average of the sums of the middle 3 """
    average = sum_of_middle_three(s1,s2,s3,s4,s5)/3
    print(average)
    """" #Step 3: map average scores to ratings """

    rating = score_to_rating_string(average)

    return rating


print(score_to_rating(4,"5","3",2.5,5))
