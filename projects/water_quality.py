import os
import datetime
import pandas as pd


my_months = ['January'
     , 'February'
     ,'March'
     , 'April'
     , 'May'
     , 'June'
     , 'July'
     , 'August'
     , 'September'
     , 'October'
     , 'November'
     , 'December'
    ]

def get_header(filepath):

    return pd.read_excel(filepath, sheet_name='Report').columns.values

def read_e_coli(file_dir, file_name):
    file_path = os.path.join(file_dir, file_name)

    if file_name == 'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_May_25_.xls':
        dat_df = pd.read_excel(file_path, sheet_name='Report', skiprows=[0])
    else:
        dat_df = pd.read_excel(file_path, sheet_name='Report')

    dat_df = dat_df[['Ecoli/100g', 'Collection Date', 'Production Area']]
    dat_df['Collection Date'] = pd.to_datetime(dat_df['Collection Date'])
    dat_df = dat_df.set_index('Collection Date')
    dat_df['Ecoli/100g'] = dat_df['Ecoli/100g'].astype(str).str.strip('<').str.strip('>').astype('float')

    return dat_df

def read_e_coli_as_df():
    e_coli_list = []
    for f in filenames_shellfish_e_coli:
        df = read_e_coli(file_dir=data_dir_path, file_name=f)
        e_coli_list.append(df)
    return pd.concat(e_coli_list)

def e_coli_select_area(e_coli):
    return e_coli[e_coli['Production Area'] == 'Loch na Cille']


def create_e_coli_fig_file_path(str_):
    fn = 'e_coli_' + str_.lower().replace(' ', '_') + '.png'
    e_coli_fig_file_path = os.path.join('figs', fn)
    return e_coli_fig_file_path
   

def read_pyhtoplankton(data_dir_path):

    pyhtoplankton_list = []
    for f in filenames_shellfish_phytoplankton:

        phytoplankton_period = pd.read_excel(
            os.path.join(data_dir_path, f), skiprows=[0, 1, 2, 3], header=None)

        pyhtoplankton_list.append(phytoplankton_period)

    return pd.concat(pyhtoplankton_list)

def preprocess_pyhtoplankton(pyhtoplankton):

    pyhtoplankton.columns = header
    pyhtoplankton['Region'] = pyhtoplankton.Region.fillna(method='ffill')
    pyhtoplankton['Collected'] = pd.to_datetime(pyhtoplankton['Collected'])

    return pyhtoplankton

def select_area(area, pyhtoplankton):

    pyhtoplankton_area = pyhtoplankton[pyhtoplankton['Area']==area]
    pyhtoplankton_area = pyhtoplankton_area.set_index('Collected')

    return pyhtoplankton_area


def list_of_areas(pyhtoplankton):
    return pyhtoplankton.Area.unique()

#pyhtoplankton_ct = select_area('Campbeltown Loch', pyhtoplankton)

def create_phytoplankton_metadata():

    header = ['Region'
         , 'Area'
         , 'Site'
         , 'Origin of Sample'
         , 'NGR'
         , 'SIN'
         , 'Sample'
         , 'Collected'
         , 'Received'
         , 'Analyzed'
         , 'Pseudo-nitzschia'
         , 'Alexandrium'
         , 'Dinophysis'
         , 'prorocentrum_lima'
         , 'prorocentrum_cordatum'
         , 'Lingulodinium'
         , 'Protoceratium']

    header_pyhtoplanktons = header[10:]
    header_pyhtoplanktons_trig = header[10:-3]
    header_pyhtoplanktons_no_trig = header[-3:]

    phytoplankton_metadata={'header':header
                           , 'header_pyhtoplanktons':header[10:]
                           , 'header_pyhtoplanktons_trig':header[10:-3]
                           , 'header_pyhtoplanktons_no_trig':header[-3:]
                           , 'triggers':[50000, 40, 100, 100]}

    return phytoplankton_metadata

def download_save_from_list(list_of_filenames):

    def download_save(url, path):

        r = requests.get(url, stream=True)

        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)

    for filename in list_of_filenames:

        #url = 'http://www.foodstandards.gov.scot/downloads/' + filename
        url =  url(filename)
        path = filepath(filename)
        #if os.path.exists(path):
        #    continue

        download_save(url, path)

        print('.', end='')

def run_get_list_of_data_files():
    """Create lists of the downloaded data files."""

    data_dir_path = get_data_dir_path()

    list_of_data_files = pd.DataFrame(os.listdir(data_dir_path), columns=['files'])
    list_of_data_files_phytoplankton = list_of_data_files[list_of_data_files.files.str.startswith(file_start_string['phytoplankton_start_str'])].copy()
    list_of_data_files_e_coli = list_of_data_files[list_of_data_files.files.str.startswith(file_start_string['e_coli_start_str'])].copy()
    list_of_data_files_biotoxin = list_of_data_files[list_of_data_files.files.str.startswith(file_start_string['biotoxin_start_str'])].copy()


    def year(x):
        return int(x.split('.')[0].split('_')[-4])
    def month(x):
        my_months_to_int = dict(zip(my_months, range(1,13)))
        return my_months_to_int[x.split('.')[0].split('_')[-2]]
    def day(x):
        return int(x.split('.')[0].split('_')[-1])
    def to_date(x):
        return datetime.date(year=year(x), month=month(x), day=day(x))

    list_of_data_files_phytoplankton['date'] = list_of_data_files_phytoplankton['files'].apply(to_date)
    list_of_data_files_biotoxin['date'] = list_of_data_files_biotoxin['files'].apply(to_date)


    def year(x):
        return int(x.split('_')[-5])
    def month(x):
        my_months_to_int = dict(zip(my_months, range(1,13)))
        return my_months_to_int[x.split('_')[-3]]
    def day(x):
        return int(x.split('_')[-2])
    def to_date(x):
        return datetime.date(year=year(x), month=month(x), day=day(x))

    list_of_data_files_e_coli['date'] = list_of_data_files_e_coli['files'].apply(to_date)

    return (list_of_data_files_phytoplankton
        , list_of_data_files_e_coli
        , list_of_data_files_biotoxin)


# Used to create format string
# And, find a list of files
file_start_string = {
    'phytoplankton_start_str':'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report'
    , 'biotoxin_start_str':'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report'
    , 'e_coli_start_str':'Shellfish_-_E._coli_-_Weekly_Result_Report'}

# Format string used for creating filenames for downloading.
format_str = {
    'format_str_phytoplankton': file_start_string['phytoplankton_start_str'] + '_-_{}_-_{}_{}.xlsx'
    , 'format_str_e_coli': file_start_string['biotoxin_start_str'] + '_-_{}_-_{}_{}_.xls'
    , 'format_str_biotoxin':file_start_string['e_coli_start_str'] + '_-_{}_-_{}_{}.xls'}


def get_data_dir_path():
    return os.path.join(os.path.expanduser('~'), 'Downloads/data')

def run_get_downloaded_shellfish_filenames():

    (filenames_shellfish_phytoplankton
    , filenames_shellfish_e_coli
    , filenames_shellfish_biotoxin) = get_downloaded_shellfish_filenames(
                                       data_dir_path=get_data_dir_path()
                                       , phytoplankton_start_str=file_start_string['phytoplankton_start_str']
                                       , e_coli_start_str=file_start_string['e_coli_start_str']
                                       , biotoxin_start_str=file_start_string['biotoxin_start_str'])

    run_assert_the_downloaded_files_are_the_same(
        filenames_shellfish_e_coli=filenames_shellfish_e_coli
        , filenames_shellfish_phytoplankton=filenames_shellfish_phytoplankton
        , filenames_shellfish_biotoxin=filenames_shellfish_biotoxin)

    return filenames_shellfish_phytoplankton, filenames_shellfish_e_coli, filenames_shellfish_biotoxin

def url(filename):
    return 'http://www.foodstandards.gov.scot/downloads/' + filename

def filepath(filename):
    return os.path.join(data_dir_path, filename)

def filter_out_exiting_filesnames(list_of_filenames):
    """Remove from list if the file exists locally."""
    new_filenames = []
    for filename in list_of_filenames:
        if os.path.exists(path):
            continue
        new_filenames.append(filename)

def create_list_of_potential_filenames(format_string):
    """Create strings that could have been used."""



    list_of_filenames = []

    t = datetime.datetime(year=2018, month=1, day=1)
    for i in range(365):

        day = t.strftime('%d')
        month = my_months[t.month-1]
        year = t.year
        list_of_filenames.append(format_string.format(year, month, day))
        t = t + datetime.timedelta(days=1)
    return list_of_filenames


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

def run_assert_the_downloaded_files_are_the_same(
    filenames_shellfish_e_coli
    , filenames_shellfish_phytoplankton
    , filenames_shellfish_biotoxin):

    # These were the files as they were first downloaded.

    assert filenames_shellfish_e_coli.sort() == [
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
     'Shellfish_-_E._coli_-_Weekly_Result_Report_-_2018_-_March_30_.xls'].sort()

    assert filenames_shellfish_phytoplankton.sort() == [
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
     'Shellfish_-_Phytoplankton_-_4_Weekly_Result_Report_-_2018_-_June_15.xlsx'].sort()

    assert filenames_shellfish_biotoxin.sort() == [
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
     'Shellfish_-_Biotoxin_-_4_Weekly_Result_Report_-_2018_-_August_03.xls'].sort()
