# A class has two sections: Section A roll numbers and Section B roll numbers. Find students who are common in both sections.

sectionA=set({'TA1','TA2','TA3','TA7','TA9','TA11'})
sectionB=set({'TA2','TA3','TA8','TA19','TA14'})

common_student_in_both_sections=sectionA.intersection(sectionB)
print(common_student_in_both_sections)

#{'TA2', 'TA3'}