#Input information

hour_exam = int(input()) *60
minutes_exam = int(input())
exam_time = hour_exam + minutes_exam
arrival_hour = int(input()) *60
arrival_minutes = int(input())
arrival_time = arrival_minutes + arrival_hour
arriving = ''
difference = 0
hour = 0
minutes = 0

#Logic
if arrival_time > exam_time:
    arriving = 'Late'

elif exam_time - 30 <= arrival_time <= exam_time:
    arriving = 'On time'

elif exam_time - 30 >= arrival_time:
    arriving = 'Early'

print(arriving)

difference = abs(exam_time - arrival_time)
hour = difference //60
minutes = difference % 60

if exam_time - 60 < arrival_time < exam_time:
    print(f'{minutes} minutes before the start')
elif arrival_time <= exam_time - 60:
    print(f'{hour}:{minutes:02d} hours before the start')
elif exam_time <= arrival_time < exam_time + 60:
    print(f'{minutes} minutes after the start')
elif arrival_time >= exam_time + 60:
    print(f'{hour}:{minutes:02d} hours after the start')