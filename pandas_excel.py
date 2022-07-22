# Import Excel file via Pandas

import pandas as pd
data = pd.ExcelFile(
    "https://video.ittensive.com/python-advanced/website.load.timings.xlsx"
    ).parse(
        sheet_name=0,
        names=["Date","DOM time","Load time"],
        converters={"Date": pd.to_datetime,
                    "DOM time": int,
                    "Load time": int}
    )
# data = data.parse(sheet_names=0) use when we have diff sheets
print(data.head())
