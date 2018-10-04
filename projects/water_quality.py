import os




#####################################################################
# Given that the files are already downloaded.
#####################################################################

def get_downloaded_shellfish_filenames(data_dir_path
    , phytoplankton_start_str, e_coli_start_str, biotoxin_start_str):

    def list_of_files_starting_with(startswith, filesnames):
        return [f for f in filesnames if f.startswith(startswith)]
    
    filesnames_all = os.listdir(data_dir_path)
    filesnames_shellfish = list_of_files_starting_with('Shellfish', filesnames_all)
    
    filenames_shellfish_phytoplankton = list_of_files_starting_with(phytoplankton_start_str, filesnames_shellfish)    
    filenames_shellfish_e_coli = list_of_files_starting_with(e_coli_start_str, filesnames_shellfish)
    filenames_shellfish_biotoxin = list_of_files_starting_with(biotoxin_start_str, filesnames_shellfish)
    
    return filenames_shellfish_phytoplankton, filenames_shellfish_e_coli, filenames_shellfish_biotoxin

def run_assert_the_downloaded_files_are_the_same(filenames_shellfish_e_coli
    , filenames_shellfish_phytoplankton, filenames_shellfish_biotoxin):

    # These were the files as they were first downloaded.

    assert filenames_shellfish_e_coli == [
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_April_27_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_January_19_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_July_06_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_March_16_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_April_06_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_March_02_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_June_15_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_February_16_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_August_03_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_June_29_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_August_10_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_May_25_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_August_17_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_March_23_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_January_12_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_January_26_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_April_13_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_May_11_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_April_20_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_February_23_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_July_13_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_May_18_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_June_01_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_March_09_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_July_27_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_June_22_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_July_20_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_June_08_.xls',
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_March_30_.xls']

    assert filenames_shellfish_phytoplankton == [
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_March_30.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_May_18.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_July_20.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_June_22.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_January_12.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_May_25.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_January_19.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_March_16.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_March_02.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_January_26.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_April_27.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_April_06.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_August_10.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_June_01.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_July_13.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_April_13.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_March_09.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_February_16.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_April_20.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_May_11.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_June_29.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_February_23.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_August_03.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_March_23.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_August_17.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_June_08.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_July_27.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_July_06.xlsx',
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_June_15.xlsx']

    assert filenames_shellfish_biotoxin == [
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_January_12.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_February_16.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_July_13.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_March_09.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_June_08.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_January_19.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_August_17.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_May_18.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_July_27.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_June_22.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_April_13.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_March_16.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_January_26.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_April_27.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_May_11.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_June_29.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_June_01.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_May_25.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_February_23.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_March_23.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_March_30.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_August_10.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_March_02.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_April_06.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_July_20.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_April_20.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_June_15.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_July_06.xls',
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_August_03.xls']
    
