import GFE

def model_1_drop_columns():
    drop_columns = [[3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 16, 17, 18, 19, 20, 21, 22, 23, 27, 28, 29, 30,
     31, 32, 33, 34, 35, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 54, 55, 56, 60, 61, 62, 63, 64,
      65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 84, 85, 86, 90, 91, 92, 93, 94, 95,
       96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
        117, 118, 119, 123, 124, 125, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 147, 148,
         149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 165, 166, 167, 168, 169, 170, 171,
          172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191,
           192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211,
            212, 213, 214, 215, 216, 217, 218, 222, 223, 224, 225, 226, 227, 228, 229, 230, 234, 235, 236, 237,
             238, 239, 240, 241, 242, 243, 244, 245, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
              261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280,
               281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299]]
    return drop_columns

def model_2_drop_columns():
    drop_columns = [0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 28, 29, 30,
     31, 36, 37, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 55, 56, 57, 62, 63, 64, 65, 66, 67, 68, 69,
      70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 82, 83, 88, 89, 90, 91, 92, 93, 94, 95, 98, 99, 100, 101,
       104, 105, 106, 107, 110, 111, 112, 113, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127,
        128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147,
         148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
         168, 169, 170, 171, 172, 173, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191,
          192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211,
           212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231,
           232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251,
            252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271,
             272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291,
             292, 293, 294, 295, 296, 297, 298, 299]
    return drop_columns


def main():

    list1 = [['a_affirmative_datapoints', 'a_affirmative_targets'],
             ['a_conditional_datapoints', 'a_conditional_targets'],
             ['a_doubt_question_datapoints', 'a_doubts_question_targets'],
             ['a_emphasis_datapoints', 'a_emphasis_targets'],
             ['a_negative_datapoints', 'a_negative_targets'], ['a_relative_datapoints', 'a_relative_targets'],
             ['a_topics_datapoints', 'a_topics_targets'], ['a_wh_question_datapoints', 'a_wh_question_targets'],
             ['a_yn_question_datapoints', 'a_yn_question_targets'],['b_affirmative_datapoints', 'b_affirmative_targets'],
             ['b_conditional_datapoints', 'b_conditional_targets'],
             ['b_doubt_question_datapoints', 'b_doubt_question_targets'],
             ['b_emphasis_datapoints', 'b_emphasis_targets'],
             ['b_negative_datapoints', 'b_negative_targets'], ['b_relative_datapoints', 'b_relative_targets'],
             ['b_topics_datapoints', 'b_topics_targets'], ['b_wh_question_datapoints', 'b_wh_question_targets'],
             ['b_yn_question_datapoints', 'b_yn_question_targets']]

    serial = 1
    for i in list1:
        if serial in range(1,10):
            print("\n\n\t\t{}) User:A - file name: {} \n".format(serial, i[0]))
        else:
            print("\n\n\t\t{}) User:B - file name: {} \n".format((serial-9), i[0]))
        
        data, target = GFE.load_data(i)
        drop_columns_model1 = self.model_1_drop_columns()
        
        # for performing same on model 2
        #drop_columns_model2 = self.model_2_drop_columns()

        input_data_with_sel_features = data.drop(data.columns[drop_columns_model1], axis=1)
        GFE.perform_modelling(input_data_with_sel_features, target, 10)
        serial += 1

    GFE.comparison()

if __name__ == '__main__':
    main()