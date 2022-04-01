class InterimGradeLetter:
    def __init__(self, assignment1, assignment2, assignment3):
        self.assignment1 = assignment1
        self.assignment2 = assignment2
        self.assignment3 = assignment3

    # checks if the student has failed or not
    def check_for_fail(self):
        return 0 in [self.assignment1, self.assignment2, self.assignment3] or \
               self.assignment1 < 50 and self.assignment2 < 50 or \
               self.assignment1 < 50 and self.assignment3 < 50 or \
               self.assignment3 < 50 and self.assignment2 < 50

    # get the weighted score based on the weightage provided in the table
    def get_weighted_assignment_scores(self):
        return self.assignment1 * 0.2 + self.assignment2 * 0.4 + self.assignment3 * 0.4

    # get grades based on the criteria provided
    def get_grades(self):
        final_marks = self.get_weighted_assignment_scores()
        if final_marks >= 85:
            return 'HD'
        elif final_marks >= 75:
            return 'D'
        elif final_marks >= 65:
            return 'C'
        elif final_marks >= 50:
            return 'P'
        elif final_marks >= 45:
            if self.check_for_fail():
                return 'F'
            elif self.assignment1 < 50 or self.assignment2 < 50:
                return 'SA'
            else:
                return 'SE'
        else:
            if self.check_for_fail():
                return 'F'
            else:
                return 'AF'


# running the code
if __name__ == '__main__':
    grades = list(map(float, input('Enter a student\'s assessment marks (separated by comma): ')
                      .split(',')))
    print(InterimGradeLetter(*grades).get_grades())