import pandas as pd
import finpy_tse as fpy

start_date = '1399-10-12' # 2021-01-01
end_date = '1401-10-10'   # 2022-12-30

# overall_dataset = fpy.Get_CWI_History(
#     start_date=start_date,
#     end_date=end_date,
#     ignore_date=False,
#     just_adj_close=False,
#     show_weekday=False,
#     double_date=True)

# overall_dataset.to_csv("D:\\Univercity\\Statistical Machine Learning\\Project\\SML-Project\\Dataset\\Overall.csv")

# usd_dataset = fpy.Get_USD_RIAL(
#     start_date=start_date,
#     end_date=end_date,
#     ignore_date=False,
#     show_weekday=False,
#     double_date=True)

# usd_dataset.to_csv("D:\\Univercity\\Statistical Machine Learning\\Project\\SML-Project\\Dataset\\Dollar.csv")

gold_dataset = fpy.Get_Price_History(
    stock='طلا',
    start_date=start_date,
    end_date=end_date,
    ignore_date=False,
    adjust_price=False,
    show_weekday=False,
    double_date=True)

gold_dataset.to_csv("D:\\Univercity\\Statistical Machine Learning\\Project\\SML-Project\\Dataset\\Gold.csv")