Row = 20
i = 0
total_grade = 0.0  # 수강학점 * 성적 누계
total_credits = 0.0  # 수강학점 누계
while i < Row:
    # 과목별 성적 정보를 입력받음
    subject, credits, grade = input().split()  # 과목, 학점, 성적

    # 입력된 정보의 유효성을 검사하고, 유효하지 않은 경우 반복문을 탈출함
    if not subject or not credits or not grade:
        break
    if credits not in ['0.0', '1.0', '2.0', '3.0', '4.0']:
        break
    if grade not in ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F', 'P']:
        break
    if len(subject) > 50:
        break

    # Pass한 과목이 아닌 경우에 대해서만 학점 계산
    if grade != 'P':
        grade_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
                      'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}  # 성적을 {key, value}로 정의
        total_grade += grade_dict[grade] * float(credits)  # 학점 * 과목 성적
        total_credits += float(credits)

    # 다음 입력을 위해 i값을 업데이트함
    i += 1

if total_credits == 0:
    print('0.000000')
else:
    # 연산 종료 후 전공 평점을 계산 (학점 * 과목 평점) / (학점 총합)
    total = float(total_grade) / float(total_credits)
    print('{:.6f}'.format(total))