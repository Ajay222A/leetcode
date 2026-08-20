class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        le=len(students)
        c=0
        while students:
            if students[0]==sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                c=0
            else:
                d=students.pop(0)
                students.append(d)
                c+=1
            if c==le:
                break                
        return len(students)
                